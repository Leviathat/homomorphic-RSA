from helper import ch
import socket

def main():
    HOST = '127.0.0.1'
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            data = int(input("CLIENT: ENTER INT ->"))
            s.sendall(data.to_bytes())

            encrypted_result = s.recv(1024).decode()
            print("CLIENT: RECEIVED -> {}\n".format(encrypted_result))

            result = ch.decrypt(int(encrypted_result))
            print("CLIENT: DECRYPTED -> {}".format(result))

if __name__ == "__main__":
    main()
