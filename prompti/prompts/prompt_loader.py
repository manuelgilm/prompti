from typing import Union
from pathlib import Path
import pickle


def pickle_loader(path: Union[str, Path]):
    """
    Load the prompt from the path

    :param path: The path to load the prompt from
    :return: The prompt object
    """

    if isinstance(path, str):
        path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Path {path} does not exist")
    with open(path.as_posix(), "rb") as f:
        prompt_obj = pickle.load(f)
    return prompt_obj


def prompt_loader(path: Union[str, Path]):
    """
    Load the prompt from the path

    :param path: The path to load the prompt from
    :return: The prompt object
    """
    # Load the prompt
    if isinstance(path, str):
        path = Path(path)

    with open(path.as_posix(), "rb") as f:
        prompt_obj = pickle.load(f)
    return prompt_obj
