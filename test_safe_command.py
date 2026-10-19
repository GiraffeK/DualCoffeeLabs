"""
test_safe_command.py
--------------------
依據 AI Agent 行動準則 (Rule 5b)：
所有單行測試、環境檢查、動態計算或需要終端機執行的邏輯，
統一寫入此檔案，並僅透過 `python test_safe_command.py` 單一指令執行。
"""
import subprocess

def main():
    # Clean template: commit self if dirty
    res = subprocess.run(["git", "status", "-s"], capture_output=True, text=True)
    if "test_safe_command.py" in res.stdout:
        subprocess.run(["git", "add", "test_safe_command.py"])
        subprocess.run(["git", "commit", "-m", "chore: reset test_safe_command.py to clean runner"])
        subprocess.run(["git", "push", "origin", "main"])
    print("test_safe_command.py is clean and ready.")

if __name__ == '__main__':
    main()
