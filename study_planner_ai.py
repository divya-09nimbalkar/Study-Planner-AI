import json
from pathlib import Path

DATA_FILE = Path("tasks.json")

def load_tasks():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []

def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2))

def add_task(subject, hours):
    tasks = load_tasks()
    task = {"subject": subject, "hours": hours, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Added task: {subject} ({hours} hrs)")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return
    for i, t in enumerate(tasks, 1):
        status = "✔️" if t["completed"] else "⏳"
        print(f"{i}. {t['subject']} - {t['hours']} hrs {status}")

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print(f"🎉 Task {index+1} marked complete!")
    else:
        print("Invalid task index.")

def main():
    print("📚 AI Study Planner")
    print("Commands: add, list, done, quit")

    while True:
        cmd = input("\nEnter command: ").strip().lower()
        if cmd == "add":
            subject = input("Subject: ")
            hours = int(input("Hours: "))
            add_task(subject, hours)
        elif cmd == "list":
            list_tasks()
        elif cmd == "done":
            idx = int(input("Task number: ")) - 1
            complete_task(idx)
        elif cmd == "quit":
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
