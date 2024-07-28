from abc import ABC
from abc import abstractmethod

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


class BasePrompt(ABC):

    @abstractmethod
    def create_prompt(self, **kwargs):
        """
        Create a prompt
        """
        return

    @abstractmethod
    def save(self, path: Union[str, Path]):
        """
        Save the prompt to a file.
        """
        return
    
    @abstractmethod
    def predict(self, **kwargs):
        """
        Predict the output from the prompt
        """
        return
    
    @classmethod
    def load(cls, path: Union[str, Path]):
        """
        Load the prompt from the path
        """
        return

class Prompt(BasePrompt):


    def create_prompt(self, name: str, prompt: str):
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
        self.prompt_variables = self.__get_variables_from_prompt(self.raw_prompt)

    def __get_variables_from_prompt(self, prompt) -> List[str]:
        """
        Get the variables from the prompt
        """
        variable_list = re.findall(r"\{{(.*?)\}}", prompt)
        return variable_list


    def save(self, path: Union[str, Path]):
        """
        Save the prompt to a file.

        :param path: The path to save the prompt to
        """
        if isinstance(path, str):
            path = Path(path)
        path.mkdir(parents=True, exist_ok=True)

        with open(path / f"{self.prompt_name}.pkl", "wb") as f:
            pickle.dump(self, f)

    def predict(self, **kwargs):
        """
        Predict the output from the prompt
        """
        # Get the variables from the prompt
        variables = self.prompt_variables
        
        # Get the variables from the kwargs
        variable_values = {}
        for variable in variables:
            if variable not in kwargs:
                raise ValueError(f"Variable {variable} is missing from the kwargs")
            variable_values[variable] = kwargs[variable]

        # Replace the variables in the prompt
        prompt = self.raw_prompt
        for variable, value in variable_values.items():
            prompt = prompt.replace(f"{{{{{variable}}}}}", value)

        return prompt
        
    @classmethod
    def load(cls, path: Union[str, Path]):
        """
        Load the prompt from the path

        :param path: The path to load the prompt from
        :return: The prompt object
        """
        if isinstance(path, str):
            path = Path(path)

        with open(path.as_posix(), "rb") as f:
            prompt_obj = pickle.load(f)
        return prompt_obj