from abc import ABC
from typing import Dict
from typing import Any
from typing import List
from typing import Union
from typing import Optional

from pathlib import Path
from ruamel.yaml.representer import RoundTripRepresenter
from ruamel.yaml import YAML
import re
import pickle 

class Prompt:
    def __init__(self):
        """
        Initialize the prompt class
        """
        self.metadata = {}

    def create_prompt(
        self,
        name: str,
        prompt: str,
        model_name: Optional[str],
        temperature: Optional[float],
        max_tokens: Optional[int],
    ):
        """
        Create a prompt

        :param prompt: The prompt to create
        :param name: The name of the prompt
        :param model_name: The model name
        :param temperature: The temperature
        :param max_tokens: The maximum tokens
        :return: None
        """
        self.raw_prompt = prompt
        self.prompt_name = name
        self.prompt_variables = self.__get_variables_from_prompt()
        self.metadata["prompt_name"] = self.prompt_name
        self.metadata["prompt"] = self.raw_prompt
        self.metadata["variables"] = self.prompt_variables
        self.metadata["parameters"] = {
            "model_name": model_name,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

    def __get_variables_from_prompt(self) -> List[str]:
        """
        Get the variables from the prompt
        """
        variable_list = re.findall(r"\{{(.*?)\}}", self.raw_prompt)
        return variable_list

    def save(self, path:Union[str, Path]):
        """
        Save the prompt to a file.

        :param path: The path to save the prompt to
        """
        if isinstance(path, str):
            path = Path(path)        
        path.mkdir(parents=True, exist_ok=True)

        with open(path / f"{self.prompt_name}.pkl", "wb") as f:
            pickle.dump(self, f)
        
    def repr_str(self, dumper: RoundTripRepresenter, data: str):
        if '\n' in data:
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
        return dumper.represent_scalar('tag:yaml.org,2002:str', data)





        