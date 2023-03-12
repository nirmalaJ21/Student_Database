#===========================================================================
# Nirmala Joshi 9th March
#Student Database
#==================================================================================
print('Student Database'.upper())
print('*'* 50)
#==============================================================================
import re
# Three lists defined
student_Name = ["Nirmala Joshi", "Romana Choudhuary", "Chitra Chaudhari", "Andrew Jeffers", "Andre Hoffman",
                "Joesph Merten", "David Wolverton",
                "Steven Fredrick", "Dionta Jones", "Jason Zeng"]
student_Hometown = ["Novi", "Livonia", "Grandrapid", "Detriot", "Lansing", "Farminton Hills", "Troy", "Norhtville",
                    "Rochester Hills", "Canton"]
student_FavFood = ["Fruit Salad", "Pizza", "Donut", "pritzzel", "bread", "sandwiches", "Spanish food", "pizza",
                   "burger", "Chess roll"]
# Function defined to see list of students
def all_student(studentname):
    global strlen
    i = 0
    for item in studentname:
       i = i +1
       print(f'Student {i} is {item}')
# Function defined to search student by name
def search_Student_By_Name(studentname,studentcity,favfood):

    while True :
        option1 = input('Welcome ! Which student would you like to learn more about ?Enter full  name ')
        # check for proper capitalization
        if option1.islower():
            option1 = option1.title()

        # check for extra spaces
        option1 = ' '.join(option1.split())
        # Only character name allowed
        if  option1.isdigit():
            print('Please enter alphabetic characters only. Try again.')
            continue
            #Name has to be atlease 2 charater long
        if len(option1) < 2:
            print('Please enter a name with at least 2 characters. Try again.')
            continue
        # First name and last name validation
        name = option1.split()
        if len(name) != 2:
            print('Please enter a first name and last name separated by a space. Try again.')
            continue
            #To check if student is present in list given
        if option1 not in studentname:
            print('Sorry, we do not have information about that student. Please try again with full name.')
            continue




#Logic to ask for town or food of student  and print correct msg.
        for item in studentname:
                    if item == option1:
                        i = studentname.index(option1)
                        while True:
                            print(f'Student  is {item}. what would you like to know? ')
                            town_Or_Food = input('Enter: '"Hometown" ' ' 'or' ' '"Favorite Food"'')
                            if town_Or_Food == 'hometown' or town_Or_Food == 'town' or town_Or_Food == 'Hometown':
                                print(f'{item}  is from {studentcity[i]}')
                                break
                            elif town_Or_Food == 'Favorite Food' or town_Or_Food== 'Food' or town_Or_Food == 'food':
                                 print(f'{item}\'s favourite food is  {favfood[i]}')
                                 break
                            else:
                                print('Ops! ,Please enter valid data')
                                continue
#Option to itreate thorugh the choice again in case you want to see another student's information
                        while True:
                            choice = input('\t\n\twould you like to learn about another student (y/n)?')
                            if choice == 'y':
                                print("Continue...")
                                break
                            elif choice == 'n':
                                print("Good bye...")
                                return
                            else:
                                 print('Please enter valid choice')
                                 continue

#Function to serch student by index number
def student_chekc_by_index(studentname,studenttown,studentfood):
   while True:
    # Loop to check valid entry of data within range 1 to lenght of list
    while True:
        # Loop to check integer data in option else keep continuing
        while True:
            try:
                option = int(input('Welcome ! Which student would you like to learn more about ?Enter a number 1- 10 '))
                break  # break out of the inner while loop if user provided number is integer
            except ValueError:
                print("oops! That was not a valid integer.Please try again...")
                continue
        strlen = len(student_Name)
        if option > strlen or option <= 0:
            print(f'Invalid option selected,enter number in the range 1  to {strlen}')
            continue
        else:
            option = option - 1
            while True :
                print(f'Student {option + 1} is {studentname[option]}. what would you like to know? ')
                if option >= 0 and option < strlen:
                    town_Or_Food = input('Enter: '"Hometown" ' ' 'or' ' '"Favorite Food"'')
                    if town_Or_Food == 'hometown' or town_Or_Food  == 'town' or town_Or_Food == 'Hometown':
                        print(f'{student_Name[option]}  is from {studenttown[option]}')
                        break
                    elif town_Or_Food == 'Favorite Food' or town_Or_Food== 'Food' or town_Or_Food == 'food'  :
                        print(f'{studentname[option]}\'s favourite food is  {studentfood[option]}')
                        break
                    else :
                        print('Ops! ,Please enter valid data')
                        continue
        while True:
            choice = input('\t\n\twould you like to learn about another student (y/n)?')
            if choice == 'y':
                print("Continue...")
                break
            elif choice == 'n':
                        # print("Good bye...")
                        # break
                return
            else:
                print("Please enter valid choice...")
                continue
#main loop to exit code/program
while True :
        while True:
         opt1 =input("\n1.Would you like to search student by number?\n2.Do you want to see a list of all students ? \n3.Would you like to search student by name?")
         if opt1 =='1':
             student_chekc_by_index(student_Name,student_Hometown,student_FavFood)
             break
         elif opt1 == '2':
             all_student(student_Name)
             break
         elif opt1 == '3':
             search_Student_By_Name(student_Name, student_Hometown, student_FavFood)
             break
         else :
              print('Please enter valid choice 1,2,3')
              continue
        while True:
            choice = input('\t\n\twould like to continue (y/n)?')
            if choice == 'y':
                print("Continue...")
                break
            elif choice == 'n':
                print("Good bye...")
                exit()
            else:
                print("Please enter valid choice...")
                continue




