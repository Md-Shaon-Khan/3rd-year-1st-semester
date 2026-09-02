import socket
import threading
import time
import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title='Socket Chat', page_icon='💬', layout='centered')

if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'sock' not in st.session_state:
    st.session_state.sock = None
if 'connected' not in st.session_state:
    st.session_state.connected = False
if 'username' not in st.session_state:
    st.session_state.username = ''


def receive_loop(sock, message_list, lock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                message_list.append('* Disconnected from server *')
                break
            with lock:
                message_list.append(data.decode('utf-8'))
        except OSError:
            break


if 'lock' not in st.session_state:
    st.session_state.lock = threading.Lock()


def connect(host, port, username):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    prompt = sock.recv(1024)
    sock.sendall(username.encode('utf-8'))
    st.session_state.sock = sock
    st.session_state.connected = True
    st.session_state.username = username
    thread = threading.Thread(
        target=receive_loop,
        args=(sock, st.session_state.messages, st.session_state.lock),
        daemon=True,
    )
    thread.start()


def disconnect():
    if st.session_state.sock:
        try:
            st.session_state.sock.sendall('/quit'.encode('utf-8'))
            st.session_state.sock.close()
        except OSError:
            pass
    st.session_state.sock = None
    st.session_state.connected = False


def send_message(text):
    if st.session_state.sock and text:
        try:
            st.session_state.sock.sendall(text.encode('utf-8'))
        except OSError:
            st.session_state.connected = False


st.title('💬 Socket Chat')

with st.sidebar:
    st.header('Connection')
    host = st.text_input('Host', value='127.0.0.1', disabled=st.session_state.connected)
    port = st.number_input('Port', value=5555, step=1, disabled=st.session_state.connected)
    username = st.text_input('Username', value=st.session_state.username, disabled=st.session_state.connected)

    if not st.session_state.connected:
        if st.button('Connect', use_container_width=True):
            if username.strip():
                connect(host, int(port), username.strip())
                st.rerun()
            else:
                st.warning('Enter a username first.')
    else:
        st.success(f'Connected as {st.session_state.username}')
        if st.button('Disconnect', use_container_width=True):
            disconnect()
            st.rerun()

if st.session_state.connected:
    st_autorefresh(interval=1000, key='chat_refresh')

chat_container = st.container(height=420)
with chat_container:
    with st.session_state.lock:
        for msg in st.session_state.messages:
            if msg.startswith(f'{st.session_state.username}:'):
                with st.chat_message('user'):
                    st.write(msg)
            elif msg.startswith('Server:'):
                with st.chat_message('assistant'):
                    st.write(msg)
            else:
                with st.chat_message('assistant', avatar='👥'):
                    st.write(msg)

if st.session_state.connected:
    user_input = st.chat_input('Type a message...')
    if user_input:
        send_message(user_input)
        st.session_state.messages.append(f'{st.session_state.username}: {user_input}')
        st.rerun()
else:
    st.info('Connect to a server from the sidebar to start chatting.')