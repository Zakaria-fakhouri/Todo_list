import os

class TodoClass:
    def __init__(self):
        """
        Initialize the TodoClass with default values and check file permissions.
        """
        self.todo = None 
        self.todo_file = "todos.txt"
        self.donetodos = "done_todos.txt"

        # Check the existence of files and create them if not present
        # Check the read and write permissions on the 'todos.txt' file
        if not os.access(self.todo_file, os.R_OK | os.W_OK):
            print("No permission to read and write to the 'todos.txt' file.")
            exit(1)

    def is_file_not_empty(self, file_path):
        """
        Check if a file exists and is not empty.

        Args:
            file_path (str): The path to the file.

        Returns:
            bool: True if the file exists and is not empty, False otherwise.
        """
        return os.path.exists(file_path) and os.path.getsize(file_path) > 0

    def add_todo(self, todo):
        """
        Add a todo to the 'todos.txt' file.

        Args:
            todo (str): The todo to be added.
        """
        with open(self.todo_file, "+a") as f:
            f.write(f".{todo}\n")
            print(f"{todo} has been added.")

    def all_todos(self):
        """
        Display all todos from the 'todos.txt' file.
        """
        if self.is_file_not_empty(self.todo_file):
            print("Todos:")
            with open(self.todo_file, '+r') as f:
                print(f.read())
        else:
            print("File is empty.")

    def all_removes(self):
        """
        Display all removed todos from the 'done_todos.txt' file.
        """
        if self.is_file_not_empty(self.donetodos):
            with open(self.donetodos, '+r') as f:
                print("Removed Todos:")
                print(f.read())
        else:
            print("File is empty.")

    def remove_todo(self, numb_of_todo):
        """
        Remove a todo from the 'todos.txt' file and move it to 'done_todos.txt'.

        Args:
            numb_of_todo (int): The index of the todo to be removed.
        """
        if self.is_file_not_empty(self.todo_file):
            with open(self.todo_file, '+r') as f:
                lines = f.readlines()
                done_todo = lines[numb_of_todo]
                lines.pop(numb_of_todo)
                with open(self.donetodos, "+a") as f:
                    f.write(done_todo)
                with open(self.todo_file, 'w') as f:
                    f.writelines(lines)
        else:
            print("File is empty.")

    def remove_all(self, user_input):
        """
        Remove all todos from 'todos.txt' and move them to 'done_todos.txt' if the user confirms.

        Args:
            user_input (str): User input to confirm removal ('y' for yes, anything else for no).
        """
        if user_input.lower() == "y":
            with open(self.todo_file, "+r") as f:
                lines = f.readlines()
                with open(self.donetodos, "+a") as f:
                    f.writelines(lines)
            with open(self.todo_file, 'w') as f:
                f.write("")
            print("All Todos have been cleared.")

# Main program execution
if __name__ == "__main__":
    # Instantiate the TodoClass
    todo_manager = TodoClass()

    done = False
    while not done:
        # Display menu options to the user
        print("""1. Enter todo
2. See todos
3. Remove todo
4. Remove all todos
5. See removed todos
Q. Quit""")
        
        user_order = input("What do you want to do: ")
        if user_order == "1":
            todo = input("Enter Todo: ")
            todo_manager.add_todo(todo=todo)
        elif user_order == "2":
            todo_manager.all_todos()
        elif user_order == "3":
            try:
                user_input = int(input("Which todo do you want to remove? (Enter the number): "))
                todo_manager.remove_todo(user_input - 1)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif user_order == "4":
            user_input = input("Are you sure? (Enter 'y' for yes, anything else for no): ")
            todo_manager.remove_all(user_input=user_input)
        elif user_order == "5":
            todo_manager.all_removes()
        elif user_order.upper() == "Q":
            print("Program End")
            done = True
        else:
            print("INVALID")
