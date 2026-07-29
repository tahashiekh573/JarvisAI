from app.ai.ai_engine import AIEngine


class IntentClassifier:

    def __init__(self):
        self.ai = AIEngine()

    def classify(self, command):

        intent = self.ai.get_intent(command)

        return intent