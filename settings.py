from pathlib import Path

class Settings:
    def __init__(self, path):
        self.path = Path(path)
        if Path(path).exists():
            self.exists = True
            self.server = self.get_server()
            self.port = self.get_port()
            self.token = self.get_token()
            self.nickname = self.get_nickname()
            self.channel = self.get_channel()
        else:
            self.exists = False

    def get_server(self):
        with open(self.path, 'r') as file:
            return file.readlines()[1].split('= ')[-1].rstrip()

    def get_port(self):
        with open(self.path, 'r') as file:
            return int(file.readlines()[2].split('= ')[-1].rstrip())

    def get_token(self):
        with open(self.path, 'r') as file:
            return file.readlines()[3].split('= ')[-1].rstrip()

    def get_nickname(self):
        with open(self.path, 'r') as file:
            return file.readlines()[4].split('= ')[-1].rstrip()

    def get_channel(self):
        with open(self.path, 'r') as file:
            return '#' + file.readlines()[5].split('= ')[-1].rstrip()