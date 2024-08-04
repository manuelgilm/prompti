class BasePromptExample:

    def __init__(self, prompti):
        self.prompti = prompti

    def run(self):
        print("Running example prompt")
        self.prompti.prompt("What is your name?")

        name = self.prompti.get_input()
        print(f"Hello {name}!")
