class Planner:
    """
    Planner converts user commands into executable tools.
    """

    def __init__(self):

        self.command_map = {

            "open chrome": "open_chrome",
            "chrome kholo": "open_chrome",

            "open vscode": "open_vscode",
            "open vs code": "open_vscode",
            "vs code kholo": "open_vscode",

            "open calculator": "open_calculator",
            "calculator kholo": "open_calculator",

            "open notepad": "open_notepad",
            "notepad kholo": "open_notepad",
        }

    def plan(self, command: str):

        command = command.lower().strip()

        tool = self.command_map.get(command)

        if tool:
            return {
                "status": True,
                "tool": tool
            }

        return {
            "status": False,
            "message": "Command Not Supported"
        }