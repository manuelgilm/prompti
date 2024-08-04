import pickle
from pathlib import Path
from typing import Any
from typing import Union


def save_as_pickle(obj: Any, path: Union[str, Path]) -> None:
    """
    Save the object to a pickle file.
    If the path does not exist, it will be created.

    :param obj: The object to save
    :param path: The path to save the object to
    :return: None
    """

    if isinstance(path, str):
        path = Path(path)

    if not path.suffix:
        path = path.with_suffix(".pkl")

    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "wb") as f:
        pickle.dump(obj, f)

    return None
