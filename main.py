from app.config import config
from plugins import active_plugin_callbacks

if __name__ == "__main__":
    print(f"Configured database: {config.database.host}:{config.database.port}...")
    for callback in active_plugin_callbacks:
        callback()
