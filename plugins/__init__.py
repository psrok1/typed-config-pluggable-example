from .friendly_plugin import execute as friendly_plugin_entrypoint

active_plugin_callbacks = [
    friendly_plugin_entrypoint
]
