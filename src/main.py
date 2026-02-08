# In-memory store for the todos
todos = []
next_id = 1

def add_todo():
    global next_id
    title = input("Enter todo title: ")
    description = input("Enter todo description: ")
    todo = {
        "id": next_id,
        "title": title,
        "description": description,
        "completed": False
    }
    todos.append(todo)
    next_id += 1
    print("Todo added successfully.")

def view_todos():
    if not todos:
        print("No todos found.")
    else:
        for todo in todos:
            status = "Completed" if todo["completed"] else "Pending"
            print(f"ID: {todo['id']}, Title: {todo['title']}, Status: {status}")

def update_todo():
    try:
        todo_id = int(input("Enter todo ID to update: "))
        for todo in todos:
            if todo["id"] == todo_id:
                new_title = input(f"Enter new title (current: {todo['title']}): ")
                new_description = input(f"Enter new description (current: {todo['description']}): ")
                todo["title"] = new_title
                todo["description"] = new_description
                print("Todo updated successfully.")
                return
        print("Todo ID not found.")
    except ValueError:
        print("Invalid input. Please enter a number for the ID.")

def delete_todo():
    try:
        todo_id = int(input("Enter todo ID to delete: "))
        for i, todo in enumerate(todos):
            if todo["id"] == todo_id:
                del todos[i]
                print("Todo deleted successfully.")
                return
        print("Todo ID not found.")
    except ValueError:
        print("Invalid input. Please enter a number for the ID.")

def toggle_complete():
    try:
        todo_id = int(input("Enter todo ID to toggle completion status: "))
        for todo in todos:
            if todo["id"] == todo_id:
                todo["completed"] = not todo["completed"]
                status = "Completed" if todo["completed"] else "Pending"
                print(f"Todo status changed to {status}.")
                return
        print("Todo ID not found.")
    except ValueError:
        print("Invalid input. Please enter a number for the ID.")

def main_menu():
    while True:
        print("\n--- Todo Menu ---")
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Mark Complete / Incomplete")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_todo()
        elif choice == "2":
            view_todos()
        elif choice == "3":
            update_todo()
        elif choice == "4":
            delete_todo()
        elif choice == "5":
            toggle_complete()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
