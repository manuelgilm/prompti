from typing import Dict


def replace_variables_in_prompt(prompt: str, variables: Dict[str, str]) -> str:
    """
    Replace the variables in the prompt.

    :param prompt: The prompt to replace the variables in
    :param variables: The variables to replace
    :return: The prompt with the variables replaced
    """
    for variable, value in variables.items():
        prompt = prompt.replace(f"{{{{{variable}}}}}", value)
    return prompt
