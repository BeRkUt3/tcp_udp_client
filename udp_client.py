import socket
target_host = input("Enter target host (Ex.:127.0.0.1):")
while len(target_host) == 0:
	target_host = input("Empty input. Enter target host (Ex.:127.0.0.1):")
target_port = input("Enter target port (default 9997):")

target_port = int(target_port) if len(target_port) > 0 else 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
	message = input("Enter message to send: ")
	client.sendto(message.encode('utf-8'), (target_host, target_port))
	data, addr = client.recvfrom(4096)
	print(data.decode())
except:
	print("Error. Check your input and try again.")
client.close()
