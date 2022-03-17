from settings import Settings

settings = Settings('config.cfg')

if not settings.exists:
    raise FileExistsError(f"File {settings.path} not exists")

print(settings.server, settings.port, settings.token, settings.nickname, settings.channel, sep='\n')