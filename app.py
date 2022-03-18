from settings import Settings
import socket

settings = Settings('config.cfg')

if not settings.exists:
    raise FileExistsError(f"File {settings.path} not exists")

socket = socket.socket()
socket.connect((settings.server, settings.port)) # Connects with twitch IRC server

socket.send(f"PASS {settings.token}\n".encode('utf-8')) # Passes token to socket
socket.send(f"NICK {settings.nickname}\n".encode('utf-8')) # Passes nickname to socket
socket.send(f"JOIN {settings.channel}\n".encode('utf-8')) # Passes channel name to socket

message = socket.recv(4096).decode('utf-8')
print(message)