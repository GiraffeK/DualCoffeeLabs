import subprocess

def main():
    print("Executing git status...")
    subprocess.run(["git", "status", "-s"], check=True)
    print("\nAdding files...")
    subprocess.run(["git", "add", ".antigravityrules", "Bulletin.json", "development-log.md", "test_safe_command.py"], check=True)
    print("\nCommitting...")
    subprocess.run(["git", "commit", "-m", "chore: setup AI Agent operating rules, development log, bulletin and safe test runner"], check=True)
    print("\nPushing to remote...")
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("Done!")

if __name__ == '__main__':
    main()
