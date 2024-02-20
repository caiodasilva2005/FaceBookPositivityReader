# Add new tasks.
# View all tasks.
# Mark tasks as completed.
# Delete tasks

#task class
class Task:
    def __init__(self, taskName, description, time, priority, isCompleted):
        self.taskName = taskName
        self.description = description
        self.time = time
        self.priority = priority
        self.isCompleted = isCompleted
    
    def markAsCompleted(self):
        self.isCompleted = True
    
    def toString(self):
        return "Task: {}\nDescription: {}\nTime To Complete: {}\nPriority: {} \nCompleted: {} \n".format(self.taskName, self.description, self.time, self.priority, self.isCompleted)
        
def main():

    print("hi")
    taskList = []   

    def viewTasks(taskList):
        if (len(taskList) == 0):
            print("No Tasks Available")
            return
        for i in range(0, len(taskList)):
            print("{}. {}".format(i+1, taskList[i].toString()))

    def findTaskByName(taskList, taskName):
        for i in range(0, len(taskList)):
            if taskList[i].taskName == taskName:
                print("{}. {}".format(i+1, taskList[i].toString()))
                return True
        return False

    def addTask(taskList, task):
        
        added = False
        
        if len(taskList) == 0:
            taskList.append(task)
            added = True

        if added == False:
            for i in range(0,len(taskList)):
                if taskList[i].priority <= task.priority:
                    taskList.insert(i, task)
                    added = True
        
        if added ==  False:
            taskList.append(task)
            added = True
        
        if added == True:
            print("Added Task.")
    
    def deleteTask(taskList, taskNumber):
        taskList.pop(taskNumber)
        print("Deleted Task.")
    
    def completeTask(taskList, taskNumber):
        taskList[taskNumber-1].markAsCompleted()
    
    def clearCompletedTasks(taskList):
        for i in range(len(taskList) - 1, -1, -1):
            if taskList[i].isCompleted == True:
                taskList.remove(taskList[i])

    print('===========TO-DO LIST============')
    print("OPTIONS")
    print("[v]: View All Tasks")
    print("[s]: Search For Task")
    print("[a]: Add a Task")
    print("[d]: Delete a Task")
    print("[c]: Mark Task As Completed")
    print("[cc]: Clear Completed Task")
    print("[q]: To Quit To-Do List")

    userInput = ""
    while userInput != "q":
        userInput = input("Enter An Option: ")
        if userInput == "v":
            viewTasks(taskList)
        elif userInput == "s":
            taskName = input("Enter A Task Name: ")
            while taskName != "q" and findTaskByName(taskList, taskName) == False:
                taskName = input("Task Not Found. Search again or [q] to quit: ")
        elif userInput == "a":
            name = input("Enter The Task Name: ")
            description = input("Enter A Description: ")
            time = input("Enter The Time To Complete: ")
            priority = int(input("Enter Priority Level: "))
            addTask(taskList, Task(name, description, time, priority, False))
        elif userInput == "d": 
            taskNumber = int(input("Enter The Task Number To Delete:"))
            deleteTask(taskList, taskNumber-1)
        elif userInput == "c": 
            taskNumber = int(input("Enter The Task Number of The Completed Task: "))
            completeTask(taskList, taskNumber)
        elif userInput == "cc":
            clearCompletedTasks(taskList)
            print("Completed Tasks Have Been Cleared.")
        else:
            print("Invalid Input.")
    
    print("Exiting To-DO-List...")

main()


    

