# # Todo List Application

class Todo_list:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the list.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted successfully.")
        else:
            print("Invalid task number.")

    def mark_as_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task '{self.tasks[task_number - 1]['task']}' marked as completed.")
        else:
            print("Invalid task number.")

    def mark_as_not_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = False
            print(f"Task '{self.tasks[task_number - 1]['task']}' marked as not completed.")
        else:
            print("Invalid task number.")

    def delete_all_tasks(self):
        if not self.tasks:
            print("No tasks to delete.")
        else:
            self.tasks.clear()
            print("All tasks deleted successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nTask List:")
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{i}. {task['task']} - {status}")


def main():
    print("Welcome to the Todo List!")
    todo_list = Todo_list()
    while True:
        print("\nTODO List APP")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Done")
        print("4. Mark Task as Not Done")
        print("5. Clear All Tasks")
        print("6. List Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as Done: "))
            todo_list.mark_as_done(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to mark as Not Done: "))
            todo_list.mark_as_not_done(task_number)
        elif choice == "5":
            todo_list.delete_all_tasks()
        elif choice == "6":
            todo_list.list_tasks()
        elif choice == "7":
            print("Exiting the TODO List App. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()


