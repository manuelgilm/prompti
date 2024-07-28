from typing import List
from typing import Union
from typing import Optional
from pathlib import Path
from prompti.prompts.base import Prompt
import pickle


def prompt_loader(path: Union[str, Path]) -> Prompt:
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
