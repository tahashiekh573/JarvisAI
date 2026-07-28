from app.ai.intent_classifier import IntentClassifier
from app.ai.planner import Planner
from app.ai.router import Router


class CommandParser:

    def __init__(self):

        self.classifier = IntentClassifier()
        self.planner = Planner()
        self.router = Router()

    def execute(self, command):

        intent = self.classifier.classify(command)

        print(f"[INTENT] {intent}")

        plan = self.planner.create_plan(intent)

        print(f"[PLAN] {plan}")

        self.router.execute(plan)