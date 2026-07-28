import subprocess
import os


def open_notepad():
    """
    Open Windows Notepad
    """
    try:
        subprocess.Popen(["notepad.exe"])
        print("[SUCCESS] Notepad Opened")
    except Exception as e:
        print(f"[ERROR] Failed to open Notepad: {e}")


def open_calculator():
    """
    Open Windows Calculator
    """
    try:
        subprocess.Popen(["calc.exe"])
        print("[SUCCESS] Calculator Opened")
    except Exception as e:
        print(f"[ERROR] Failed to open Calculator: {e}")


def open_chrome():
    """
    Open Google Chrome
    """

    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(
            r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
        ),
    ]

    for path in chrome_paths:
        if os.path.exists(path):
            try:
                subprocess.Popen([path])
                print("[SUCCESS] Chrome Opened")
                return
            except Exception as e:
                print(f"[ERROR] {e}")
                return

    print("[ERROR] Chrome not found.")


def open_vscode():
    """
    Open Visual Studio Code
    """

    vscode_paths = [
        os.path.expandvars(
            r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"
        ),
        r"C:\Program Files\Microsoft VS Code\Code.exe",
    ]

    for path in vscode_paths:
        if os.path.exists(path):
            try:
                subprocess.Popen([path])
                print("[SUCCESS] VS Code Opened")
                return
            except Exception as e:
                print(f"[ERROR] {e}")
                return

    print("[ERROR] VS Code not found.")