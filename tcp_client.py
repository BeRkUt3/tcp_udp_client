import socket
target_host = input("[*] Enter target host (Ex.:www.google.com):")
while len(target_host) == 0:
	target_host = input("[*] Empty input. Enter target host (Ex.:www.google.com):")
target_port = input("[*] Enter target port (default 80):")

target_port = int(target_port) if len(target_port) > 0 else 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	message = input("[*] Enter message to send: ")
	client.connect((target_host, target_port))
	client.send(message.encode('utf-8'))
	response = client.recv(4096)
	print(response.decode())
except:
	print("[!] Error. Check your input and try again.")
client.close()
