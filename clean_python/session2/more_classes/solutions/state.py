

class ConfigManager:

    def __init__(self):
        self._values = {}
        self._allowed_values = {}

    def set_config_value(self, key, value):
        if key not in self._values:
            raise LookupError("Key not in config")
        if value not in self._allowed_values[key]:
            raise ValueError("Value for config item is not in allowed values")
        self._values[key]["value"] = value
        print(f"Config updated: {key} = {value}")

    def get_config_value(self, key):
        if key not in self._values:
            raise LookupError("Key not in config")
        return self._values[key]

    def add_new_config_value(self, key, value, allowed_values):
        if key in self._values:
            raise ValueError("Key already in config.")

        self._values[key] = value
        self._allowed_values[key] = allowed_values


config = ConfigManager()
config.add_new_config_value("theme", "light", ["light", "dark", "rainbow"])
config.add_new_config_value("language", "en", ["en", "de"])
config.add_new_config_value("notifications", "True", [True, False])

print(f"Theme: {config.get_config_value("theme")}")


# TODO Bonus task: Alter your ConfigManager s.t. it implements the Singleton pattern


class ConfigManager:

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(ConfigManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._values = {}
        self._allowed_values = {}

    def set_config_value(self, key, value):
        if key not in self._values:
            raise LookupError("Key not in config")
        if value not in self._allowed_values[key]:
            raise ValueError("Value for config item is not in allowed values")
        self._values[key]["value"] = value
        print(f"Config updated: {key} = {value}")

    def get_config_value(self, key):
        if key not in self._values:
            raise LookupError("Key not in config")
        return self._values[key]

    def add_new_config_value(self, key, value, allowed_values):
        if key in self._values:
            raise ValueError("Key already in config.")

        self._values[key] = value
        self._allowed_values[key] = allowed_values

config1 = ConfigManager()
config2 = ConfigManager()

assert config1 is config2

config1.add_new_config_value("foo", "bar", ["bar", "baz"])

assert config2.get_config_value("foo") == "bar"