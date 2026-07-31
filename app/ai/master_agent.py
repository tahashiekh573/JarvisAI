from app.ai.tool_router import ToolRouter
from app.ai.browser_planner import BrowserPlanner
from app.ai.browser_executor import BrowserExecutor
from app.ai.desktop_planner import DesktopPlanner
from app.ai.desktop_executor import DesktopExecutor


class MasterAgent:

    def __init__(self):

        self.router = ToolRouter()

        self.browser_planner = BrowserPlanner()
        self.browser_executor = BrowserExecutor()

        self.desktop_planner = DesktopPlanner()
        self.desktop_executor = DesktopExecutor()

    def execute(self, command):

        planner = self.router.route(command)

        print(f"\n[SELECTED PLANNER] {planner}\n")

        if planner == "browser":

            plan = self.browser_planner.create_plan(command)

            print(plan)

            self.browser_executor.execute(plan)

        elif planner == "desktop":

            plan = self.desktop_planner.create_plan(command)

            print(plan)

            self.desktop_executor.execute(plan)

        else:

            print(f"[ERROR] Planner '{planner}' not implemented.")