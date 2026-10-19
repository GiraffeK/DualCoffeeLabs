"""
test_safe_command.py
--------------------
依據 AI Agent 行動準則 (Rule 5b)：
所有單行測試、環境檢查、動態計算或需要終端機執行的邏輯，
統一寫入此檔案，並僅透過 `python test_safe_command.py` 單一指令執行。
"""
import subprocess

def main():
    print("Executing git status...")
    subprocess.run(["git", "status", "-s"], check=True)
    subprocess.run(["git", "add", "AI-Agent-must-read-at-beginning.txt", "test_safe_command.py"], check=True)
    subprocess.run(["git", "commit", "-m", "chore: clean AI-Agent-must-read-at-beginning.txt and update runner"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("Git sync complete.")

if __name__ == '__main__':
    main()
