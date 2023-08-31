print("To-Do-List Application\n\n")
A_Task = None
ToDo_List = []
TaskAmountCounting = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','1th','12th','13th','14th','15th','16th','17th','18th','19th','20th']
moreCount = 0
completedTask = list()

def addingList():

   count = 0
   print("How many task would you like to input:")
   TaskAmount = int(input())

   while TaskAmount > count :# Looping for writing out the task as soon as possible.
        A_Task = input("{} Task\n>" .format(TaskAmountCounting[count]))
        ToDo_List.append(A_Task)
        count += 1

   print("Would you like to add more to your task list")
   answer = input(">")

   if answer.startswith("y"):
     TaskAmount = int(input("How many more:\n>"))
     while TaskAmount > count:
      A_Task = input("{} Task\n>" .format(TaskAmountCounting[count]))
      ToDo_List.append(A_Task)
      count += 1

   else:
     print("Okay")

   return ToDo_List


def markingList():
  print("Which of the task below, would you like to mark as done")
  answer = int(input(">"))

  for count, Task in enumerate(ToDo_List, start = 1):
    print(count,':\t ', Task)

  answer = answer - 1
  removedTask = ToDo_List.pop(answer)
  completedTask.append(removedTask)
      
  print("These are the remaining task")
  for count, Task in enumerate(ToDo_List, start = 1):
    print(count,':\t ', Task)


  while True:
    print('Do you still wanna mark any task as done again(Yes / No)')
    answer = input(">").lower()

    if answer.startswith("y") :
      print("These are the reamaining task list")
    for count, Task in enumerate(ToDo_List, start = 1):
      print(count,':\t ', Task)
    answer = input('Which of the task above would you like to remove:')
           
    answer = answer - 1
    removedTask = ToDo_List.pop(answer)
    completedTask.append(removedTask)

    print("These are the remaining task")
    for count, Task in enumerate(ToDo_List, start = 1):
     print(count,':\t ', Task)

     return ToDo_List

while True:
    count = 0
    print("Making your day a purposeful one with valuables goal and task for today\n")
    print("So ... what would you like to do for today:\n")
    print("1 . Add a new task to the list\n\n2. List out the tasks\n\n3. Mark a Task being Done\n\n4. Display list of completed tasks\n\n5. Quit\n\n")
    optionAns = input("Type out the number of your choice here:\n>")

    if optionAns == '1': #for Adding tasks to the list
     while True:
      print("How many task would you like to type")
      TaskAmount = input()

      try:
       TaskAmount = int(TaskAmount)
       if TaskAmount > 0 and TaskAmount < 100:
         print("You are good to go")
         break
       else:
         print("Please ... make sure the number you type in is greater than 0 and lesser than 0.")
      except:
       print("Please ... put in an integer number")
   


      #After task input validation, then we write the task through repeated loops and iteration.  
     while TaskAmount > count :# Looping for writing out the task as soon as possible.
       
      A_Task = input("{} Task:\n" .format(TaskAmountCounting[count]))
      ToDo_List.append(A_Task)
      count += 1

     answer = input("Would you like to:\n1.)add more to the task list\n2.)Go back to the main page\n>")
     if answer == "1":
           
         print("Okay\nHow many more task would you like to input:")
         askAmount = int(input())

         while askAmount > moreCount:# Another chance; Looping for writing out the task as soon as possible.
          
          A_Task = input("{} Task\n>" .format(TaskAmountCounting[count]))
          ToDo_List.append(A_Task)
          moreCount += 1 
          count += 1
         print('Now taking you to the main page\n\n')

     else:
       print("Now taking you to the main page\n\n")
       

    elif  optionAns == '2':  #for listing out the task.
         if len(ToDo_List) == 0:
          
          print("Task List Empty")
          print('Would you like to add task to the list')
          answer = input(">")
          if answer.startswith('y'):
             print("Okay")
             addedList = addingList()
             print("This is your new task list.")
             print(ToDo_List)
             print("Taking you to main page\n\n")
          else:
           print("Taking you to the main page\n\n")
           break
          
         else:
           while True:
            for indexCounting, Task in enumerate(ToDo_List, start = 1):
             print(indexCounting, ":\t" , Task)
        
            answer = input("Back to main Page\n(Yes \ No)\n\n").lower()
            if answer.startswith("y"):
             print("Moving back to next page\n\n")
             break

           #if answer.startswith("y"):
           # print("Okay\nMoving to the main page\n\n")
            
         
    elif optionAns == '3': #for removing and marking any task that is done between them.

      if len(ToDo_List) == 0:
       
       answer = input("The Task list is empty\nYou won't be able to mark anything as done\nWould you like to add to task list")

       if answer.startswith("y"):
         addingList()
         print("This is the list of your task.")
         for indexCounting, Task in enumerate(ToDo_List, start = 1):
           print(indexCounting, ":\t", Task)
         answer = input("Now, would you like to mark any task as done\n>").lower()
         if answer.startswith("y"):
           markingList()
         else:
          print("OKay\nTaking you to main page\n\n")
          break
       else:
         print("OKay\nTaking you to main page\n\n")
         break
       

      else:
        print("Which of the task below, would you like to mark as done")
        answer = input(">")

        for count, Task in enumerate(ToDo_List, start = 1):
          print(count,':\t ', Task)

        answer = answer - 1
        removedTask = ToDo_List.pop(answer)
        completedTask.append(removedTask)
      
        print("These are the remaining task")
        for count, Task in enumerate(ToDo_List, start = 1):
         print(count,':\t ', Task)


        while True:
          print('Do you still wanna mark any task as done again(Yes / No)')
          answer = input(">").lower()

          if answer.startswith("y") :
          
            print("These are the reamaining task list")
            for count, Task in enumerate(ToDo_List, start = 1):
             print(count,':\t ', Task)
            answer = int(input('Which of the task above would you like to remove:'))
           
            answer = answer - 1
            removedTask = ToDo_List.pop(answer)
            completedTask.append(removedTask)

            print("These are the remaining task")
            for count, Task in enumerate(ToDo_List, start = 1):
              print(count,':\t ', Task)
              break
          else:
            print("Taking you to the main Page.")
            break

    elif  optionAns == '4': #for displaying list of completed task.
      if len(completedTask) == 0:
        print("You haven't accomplished any task for today")
        print("It will either be for two reasons\n 1.) Maybe you haven't completed a task from the task list\n2.) Or you don't have any task on the task list\n\n\n")
        print("So what would you like to work on firstly")
        print("1.)Display\check your list to see if you have any Task on it\n\n2.)Or if you have, you would like to mark some task as done\n")
        # while True:

        answer = int(input("Type option 1 0r 2 >"))
        if answer == 1:
          if len(ToDo_List) == 0:
            print("You have an empty list")
            print("Would you like to add some task to your Task list (Yes / No)")
            answer = input(">").lower()
            if answer.startswith("y"):
              addedList = addingList()
              print("This are now the new task within the list:\n"," ", addedList)
              print("On the main page\tClick on Option 3 to mark the completed task you have worked on")
              print("Moving to the main page ........ moving ... moving ....")
            else:
             print("Since, you don't have any written task, you won't be able to mark any task you have done")
             print("Okay\nTaking you to the main page\n\n\n")
          else:
            print("Your task list is not empty")
            print(ToDo_List)
            print("\n\nSo ...\n")
            #Which task would you like to mark as done
            print("Of which task, would you like to clear out and mark as done from the task list")  
            answer = input("Pick the task number\n")

            for indexcounting, Task in enumerate(ToDo_List, start = 1):
             print("Option.", indexcounting,")"," ", Task)
            answer = answer - 1
            removedTask = ToDo_List.pop(answer)
            completedTask.append(removedTask)

            option = input("Would you like to include any task again as done(Yes / No)")
            if option == 'Yes':
             count = 0
             number = int(input("How many more would you like to add"))
             while number > count:
               print("Of which task, would you like to clear out from the task list")  
               answer = input("Pick the task number\n")

               for indexcounting, Task in enumerate(ToDo_List, start = 1):
                print("Option.", indexcounting,")"," ", Task)
               answer = answer - 1
               removedTask = ToDo_List.pop(answer)
               completedTask.append(removedTask)

               count = count + 1
             print("Okay\n Meet you at the main page.\n\n\n")

        elif answer == 2:
          if len(ToDo_List) != 0:
           print("Of which task, would you like to clear out and mark as done from the task list")  
           answer = input("Pick the task number\n")

           for indexcounting, Task in enumerate(ToDo_List, start = 1):
             print("Option.", indexcounting,")"," ", Task)
           answer = answer - 1
           removedTask = ToDo_List.pop(answer)
           completedTask.append(removedTask)

           option = input("Would you like to include any task again as done(Yes / No)")
           if option == 'Yes':
             count = 0
             number = int(input("How many more would you like to add"))
             while number > count:
               print("Of which task, would you like to clear out from the task list")  
               answer = input("Pick the task number\n")

               for indexcounting, Task in enumerate(ToDo_List, start = 1):
                print("Option.", indexcounting,")"," ", Task)
               answer = answer - 1
               removedTask = ToDo_List.pop(answer)
               completedTask.append(removedTask)

               count = count + 1
             print("Okay\n Meet you at the main page.\n\n\n")

            
          else:
            print("You have don't have any task list written down yet\nType on Option (2) to write it all up.")
            print("Moving you to the main page ... To write the task up.")
          
            

        
      else:
       print("These are the list of completed tasks you have accomplished")
       for indexCounting , completeTask in enumerate(completedTask, start = 1):
        print(indexCounting,':\t', completeTask)
      
#stopped at optionAns == '4' finish up marking task as done
    else:
      quit()

#Debug(Test) out option three, four and five for the appplication functionality.
