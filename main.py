# This program will make it so you are able to add, remove, and view tasks. This will also serve as practice for how to use classes (Object Oriented Programming)
# October 3, 2024
# Python 3.12
# MacOS Sonoma

# A class named Todolist is created.
class Todolist:
    # __init__ function was defined with a self parameter inside.
    def __init__(self):
        self.tasks = []

    # A function named add_task was defined, the purpose of this function is to prompt the user to add a task to their list.
    def add_task(self,task):
        # Adds the task to their list.
        self.tasks.append(task)
        # Outputs that the task has been added successful.
        print("Task has been successfully added ✅\n" + task)

    # A function named remove_task is defined, the purpose is to remove a task from the task list.
    def remove_task(self, task):
        # If the task is in the task list, remove the task. 
        if task in self.tasks:
            self.tasks.remove(task)
            # Output that the program has successfully removed the task.
            print("\nYour task has been removed successfully! ✅")
        # If the task is not found in the task list, the program will display this message.
        else: 
            print("\nThere is no such task, please try again. ❌")
    # A function named view_tasks that allows the user to view tasks that they have added. 
    def view_tasks(self):
        # If a user has tasks, they will be displayed.
        if self.tasks:
            # If a user has a task, it will be displayed on the console. 
            print("Here are your tasks:")
            # This indicates that the index will start at 1 instead of the default of 0. 
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')
        # If the user has no tasks, it will display that they don't have any tasks.
        else: 
            print("\nYou have no tasks.")

    # The main module is defined.
    def main(self):
        # Users will be given the option to choose a number 1-4 and it will determine whether they want to add, remove, or view a task or if they would like to quit the program all together.
        while True:
            print("\n1. Add Task")
            print("2. Remove Task")
            print("3. View Tasks")
            print("4. Quit Program")
            # Program prompts user to input their number. 
            user = input("Pick a number based on what you would like to do.")

            # If the user inputs 1, they will be able to add a task. 
            if user == "1":
                # Prompts user to enter the task that they would like to complete. 
                choice = input("Please enter a task that you would like to add.")
                # Calls function.
                todo_list.add_task(choice)
            # If the user inputs 2, they will be able to remove a task.
            elif user == "2":
                # Prompts user to enter the task they would like to remove.
                choice = input("Enter task you would like to remove.")
                # Calls function. 
                todo_list.remove_task(choice)
            # If the user inputs 3, they will be able to view their tasks. 
            elif user == "3":
                # Calls function. 
                todo_list.view_tasks()
            # If the user inputs 4, the program will stop.
            elif user == "4":
                print("Thank you for using our program.")
                break
            # If the user doesn't input any of the valid values, it will say that the input is invalid.
            else:
                print("This is not a valid choice, try again.")


if __name__ == "__main__":
    todo_list = Todolist()  
    todo_list.main()
