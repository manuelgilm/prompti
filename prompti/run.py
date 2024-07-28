from prompti.prompts.base import Prompt
from prompti.prompts.prompt_loader import prompt_loader
from pprint import pprint

from typing import Dict
from typing import Any

import textstat


def main():
    prompt = Prompt()
    prompt.create_prompt(
        prompt="""
        This is a prompt with a {{variable}} and this is another variable {{variable2}}
        Now we can add some more text here
        and here.
        """,
        name="testing_prompt",
    )
    prompt.save("custom_prompts/testing_prompts")

    # # load the prompt
    my_prompt = Prompt().load("custom_prompts/testing_prompts/testing_prompt.pkl")
    print(type(my_prompt))
    print(my_prompt.prompt_name)
    print(my_prompt.raw_prompt)
    print("--predict--")
    print(my_prompt.predict(variable="var1", variable2="var2"))


def main2():
    text = """
    Love encompasses a range of strong and positive emotional and mental states, 
    from the most sublime virtue or good habit, the deepest interpersonal affection,
    to the simplest pleasure.[1] An example of this range of meanings is that the love 
    of a mother differs from the love of a spouse, which differs from the love for food.
    Most commonly, love refers to a feeling of strong attraction and emotional attachment.[2]

    Love is considered to be both positive and negative, with its virtue representing human kindness,
    compassion, and affection—"the unselfish, loyal, and benevolent concern for the good of another"—and 
    its vice representing a human moral flaw akin to vanity, selfishness, amour-propre, and egotism.
    It may also describe compassionate and affectionate actions towards other humans, oneself, 
    or animals.[3] In its various forms, love acts as a major facilitator of interpersonal relationships and, 
    owing to its central psychological importance, is one of the most common themes in the creative arts.
    [4][5] Love has been postulated to be a function that keeps human beings together against menaces 
    and to facilitate the continuation of the species.[6]
    """
    metrics = get_text_stats(text)
    pprint(metrics)


def get_text_stats(text: str) -> Dict[str, Any]:
    """
    Get the text metrics from the text

    :param text: The text to get the metrics from
    :return: The metrics
    """
    return {
        "flesch_reading_ease": textstat.flesch_reading_ease(text),
        "flesch_kincaid_grade": textstat.flesch_kincaid_grade(text),
        "smog_index": textstat.smog_index(text),
        "coleman_liau_index": textstat.coleman_liau_index(text),
        "automated_readability_index": textstat.automated_readability_index(text),
        "dale_chall_readability_score": textstat.dale_chall_readability_score(text),
        "difficult_words": textstat.difficult_words(text),
        "linsear_write_formula": textstat.linsear_write_formula(text),
        "gunning_fog": textstat.gunning_fog(text),
        "text_standard": textstat.text_standard(text),
        "fernandez_huerta": textstat.fernandez_huerta(text),
        "szigriszt_pazos": textstat.szigriszt_pazos(text),
        "gutierrez_polini": textstat.gutierrez_polini(text),
        "crawford": textstat.crawford(text),
        "gulpease_index": textstat.gulpease_index(text),
        "osman": textstat.osman(text),
    }
