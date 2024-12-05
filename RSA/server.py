from helper import ch
import socket


def main():
    HOST = '127.0.0.1'
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        print("SERVER: LISTENING")

        conn, addr = s.accept()
        with conn:

            while True:
                data = conn.recv(1024)
                message = int.from_bytes(data)

                print("SERVER: RECEIVED -> {}".format(message))

                encrypted_data = ch.encrypt(message)
                conn.sendall(str(encrypted_data).encode())

if __name__ == "__main__":
    main()