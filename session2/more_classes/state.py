config = {
    "theme": {"value": "light", "allowed_values": ["light", "dark", "rainbow"]},
    "language": {"value": "en", "allowed_values": ["en", "de"]},
    "notifications": {"value": True, "allowed_values": [True, False]}
}

def set_config(key, value):
    global config

    if key not in config:
        raise LookupError("Key not in config")

    if value not in config[key]["allowed_values"]:
        raise ValueError("Value for config item is not in allowed values")


    config[key]["value"] = value
    print(f"Config updated: {key} = {value}")

def get_config(key):
    global config

    if key not in config:
        raise LookupError("Key not in config")

    return config[key]["value"]

# TODO: remove the code above and implement the same functionality in the ConfigManager class
class ConfigManager:
    ...
    # TODO your code goes here





# TODO Bonus task: Alter your ConfigManager s.t. it implements the Singleton pattern