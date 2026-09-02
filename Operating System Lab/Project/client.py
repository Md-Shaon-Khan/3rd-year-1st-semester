import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 5555

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print('\nDisconnected from server.')
                break
            print('\r' + data.decode('utf-8'))
            print('> ', end='', flush=True)
        except OSError:
            break
    sock.close()
    sys.exit(0)

def main():
    host = sys.argv[1] if len(sys.argv) > 1 else HOST
    port = int(sys.argv[2]) if len(sys.argv) > 2 else PORT

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    prompt = sock.recv(1024).decode('utf-8')
    username = input(prompt)
    sock.sendall(username.encode('utf-8'))

    thread = threading.Thread(target=receive_messages, args=(sock,), daemon=True)
    thread.start()

    print("Connected. Type your messages below ('/quit' to exit).")
    while True:
        try:
            message = input('> ')
        except (EOFError, KeyboardInterrupt):
            message = '/quit'
        if message == '/quit':
            sock.sendall(message.encode('utf-8'))
            break
        sock.sendall(message.encode('utf-8'))

    sock.close()

if __name__ == '__main__':
    main()