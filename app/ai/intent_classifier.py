class IntentClassifier:

    def classify(self, command: str):

        command = command.lower()

        if "chrome" in command:
            return "open_chrome"

        elif "calculator" in command or "calc" in command:
            return "open_calculator"

        elif "vs code" in command or "vscode" in command or "code" in command:
            return "open_vscode"

        elif "notepad" in command:
            return "open_notepad"

        else:
            return "unknown"