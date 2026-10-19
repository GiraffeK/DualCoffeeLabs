"""
test_safe_command.py
--------------------
依據 AI Agent 行動準則 (Rule 5b)：
所有單行測試、環境檢查、動態計算或需要終端機執行的邏輯，
統一寫入此檔案，並僅透過 `python test_safe_command.py` 單一指令執行。
"""
import subprocess

def main():
    print("--- Git Status ---")
    status = subprocess.run(["git", "status", "-s"], capture_output=True, text=True, check=True)
    print(status.stdout or "Working tree is clean.")
    
    if status.stdout.strip():
        print("--- Adding all modified and untracked files ---")
        subprocess.run(["git", "add", "."], check=True)
        print("--- Committing ---")
        subprocess.run(["git", "commit", "-m", "chore: sync development log and latest workspace updates"], check=True)
    
    print("--- Pushing to remote origin main ---")
    push = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True, check=True)
    print(push.stdout or push.stderr or "Push complete.")
    print("--- Done ---")

if __name__ == '__main__':
    main()
