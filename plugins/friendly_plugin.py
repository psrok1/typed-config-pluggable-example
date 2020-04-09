from typedconfig import Config, section, group_key, key

from app.config import ApplicationConfig, config


@section("friendly_plugin")
class WhatToSayConfig(Config):
    """
    Additional section with plugin-specific configuration
    """
    what_to_say = key(cast=str)


class FriendlyPluginConfig(ApplicationConfig):
    """
    Main configuration object extended by plugin-specific sections
    """
    friendly_plugin = group_key(WhatToSayConfig)


# Use common provider with app configuration
config = FriendlyPluginConfig(provider=config.provider)


def execute():
    # Usage of plugin-specific values
    print(f"Friendly Plugin says {config.friendly_plugin.what_to_say}")
    # Usage of application-wide values
    print(f"Let's pretend that we're connecting to {config.database.host}:{config.database.port}...")
