#Intializze Starting Variables
total = 0
count = 0

#Run the function by getting input from the user
while True:
    user_selection = input("Give me a number [q to quit]: ")

    #Add an option to quit
    if user_selection == 'q':
        break
    
    #Add the inputed numbers to both variables
    total += float(user_selection) 
    count += 1

#Print the answers
if count > 0:
    Average = total / count
    print(f"The sum of the numbers entered is: {total}")
    print(f"The count of the numbers entered: {count}")
    print(f"The average of the numbers entered is: {Average}")
    
#Give an option incase no numbers were entered
else:
    print("No numbers were entered.")
