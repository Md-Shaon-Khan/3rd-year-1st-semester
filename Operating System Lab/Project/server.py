import socket
import threading
import datetime

HOST = '0.0.0.0'
PORT = 5555
LOG_FILE = 'chat_log.txt'

clients = {}
clients_lock = threading.Lock()

def log_message(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f'[{timestamp}] {message}'
    print(entry)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(entry + '\n')

def broadcast(message, sender_socket=None):
    with clients_lock:
        for sock, name in list(clients.items()):
            if sock != sender_socket:
                try:
                    sock.sendall(message.encode('utf-8'))
                except OSError:
                    remove_client(sock)

def remove_client(sock):
    with clients_lock:
        name = clients.pop(sock, None)
    if name:
        log_message(f'{name} disconnected.')
        broadcast(f'* {name} has left the chat *')
    try:
        sock.close()
    except OSError:
        pass

def handle_client(sock, addr):
    try:
        sock.sendall('Enter your username: '.encode('utf-8'))
        username = sock.recv(1024).decode('utf-8').strip()
        if not username:
            username = f'{addr[0]}:{addr[1]}'

        with clients_lock:
            clients[sock] = username

        log_message(f'{username} connected from {addr[0]}:{addr[1]}')
        broadcast(f'* {username} has joined the chat *', sender_socket=sock)

        while True:
            data = sock.recv(1024)
            if not data:
                break
            message = data.decode('utf-8').strip()
            if not message:
                continue
            if message == '/quit':
                break
            log_message(f'{username}: {message}')
            broadcast(f'{username}: {message}', sender_socket=sock)

    except (ConnectionResetError, OSError):
        pass
    finally:
        remove_client(sock)

def server_console_loop():
    while True:
        try:
            message = input()
        except (EOFError, KeyboardInterrupt):
            break
        if not message:
            continue
        if message == '/quit':
            break
        log_message(f'Server: {message}')
        broadcast(f'Server: {message}')

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    log_message(f'Server listening on {HOST}:{PORT}')

    console_thread = threading.Thread(target=server_console_loop, daemon=True)
    console_thread.start()

    try:
        while True:
            client_socket, addr = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True)
            thread.start()
    except KeyboardInterrupt:
        log_message('Server shutting down.')
    finally:
        server_socket.close()

if __name__ == '__main__':
    main()