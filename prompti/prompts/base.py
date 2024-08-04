from abc import ABC
from abc import abstractmethod

from typing import List
from typing import Union


from pathlib import Path
import re
import pickle

from prompti.utils.save import save_as_pickle
from prompti.prompts.prompt_loader import pickle_loader
from prompti.utils.string_utils import replace_variables_in_prompt


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

    @property
    def prompt(self):
        return self.raw_prompt


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
        save_as_pickle(self, path)

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
        prompt = replace_variables_in_prompt(self.raw_prompt, variable_values)
        return prompt

    @classmethod
    def load(cls, path: Union[str, Path]):
        """
        Load the prompt from the path

        :param path: The path to load the prompt from
        :return: The prompt object
        """
        prompt_obj = pickle_loader(path)
        return prompt_obj


class ZeroShotPrompt(BasePrompt):

    def __init__(
        self, prompt: str, model_name: str, temperature: float, max_tokens: int
    ):
        self.raw_prompt = prompt
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
