from typedconfig import Config, key, group_key, section
from typedconfig.source import IniFileConfigSource, EnvironmentConfigSource


@section('database')
class DatabaseConfig(Config):
    """
    Database configuration
    """
    host = key(cast=str)
    port = key(cast=int)
    timeout = key(cast=float)


class ApplicationConfig(Config):
    """
    Main configuration object
    """
    database = group_key(DatabaseConfig)


config = ApplicationConfig(sources=[
    EnvironmentConfigSource(),
    IniFileConfigSource("config.ini")
])
