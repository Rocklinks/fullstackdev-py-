import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8080))
data = client_socket.recv(1024)
print("Received:", data.decode())
client_socket.close()