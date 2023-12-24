import os
i = 1
class todo_class:
    def __init__(self):
        self.todo = None 
        self.todo_file = "todos.txt"
        self.donetodos = "done_todos.txt"
        

        # Überprüfe die Existenz der Dateien und erstelle sie, wenn sie nicht vorhanden sind
    
        # Überprüfe die Zugriffsrechte auf die Datei 'todos.txt'
        if not os.access(self.todo_file, os.R_OK | os.W_OK):
           print("Keine Berechtigung auf die Datei 'todos.txt' zum Lesen und Schreiben.")
           exit(1)

    def is_file_not_empty(self,file_path):
       return os.path.exists(file_path) and os.path.getsize(file_path) > 0


    def add_todo(self,todo):

        with open(self.todo_file, "+a") as f:
            f.write(f".{todo}\n")
            print(f"{todo} is been Added")

    def all_todos(self):
        if self.is_file_not_empty(self.todo_file):
            print("Todos:")
            with open(self.todo_file, '+r') as f:
                print(f.read())
                    
        else:
            print("File is empty")

    def all_removes(self):
        if self.is_file_not_empty(self.donetodos):
            with open(self.donetodos, '+r') as f:
                print("Removed Todos:")
                print(f.read())
        else:
            print("File is empty")

    def remove_todo(self, numb_of_todo):
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
            print("File is empty")
            
    def remove_all(self,user_input):
        if user_input=="y":
            with open(self.todo_file, "+r") as f:
                lines = f.readlines()
                with open(self.donetodos, "+a") as f:
                    f.writelines(lines)
            with open(self.todo_file, 'w') as f:
                f.write("")
            print("All Todos got cleared")

MC = todo_class()#const for my class(todo)
done = False
while not done:
    print("""1. Enter dodo
2. see todos
3. remove todo
4. remove all todos
5. see the removed todos
Q. quit""")
    user_order = input("What do u want tu do: ") 
    if user_order == "1":
        todo = input("Enter Todo: ")
        MC.add_todo(todo=todo)
    elif user_order == "2":
        MC.all_todos()
    elif user_order == "3":
        user_input = int(input("Witch todo want you to remove?(Number of Line) "))
        MC.remove_todo(user_input-1)
    elif user_order == "4":
        user_input = input("Are you sure?(for yes enter 'y' for no enter something else) ")
        MC.remove_all(user_input=user_input)
    elif user_order == "5":
        MC.all_removes()
    elif user_order == "Q":
        print("Programm End")
        done = True
    else:
        print("INVAILD")