import keyring
import yaml

def get_api_key(key_name: str) -> str:
    """
    Get the API key from the Keyring.
    """
    api_key = keyring.get_password("system", key_name)
    if api_key is None:
        raise ValueError("API key not found in Keyring!")
    return api_key


def read_yaml(path: str) -> dict:
    """
    Get dict from a yaml file
    """
    with open(path, "r") as f:
        return yaml.safe_load(f)
