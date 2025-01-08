import time

# Define all activities as functions
def activity1():
    print("Activity no.1")
    print("Hello World")

def activity2():
    print("Activity no. 2")
    name = input("Input your name: ")
    age = input("Input your age: ")
    add = input("Input your email address: ")
    print(f"Hi {name}, {age} years of age, \n{add}")

def activity3():
    print("Activity no.3")
    name = input("Input your name: ")
    add = input("Input your address: ")
    age = input("Input your age: ")
    print(f"Hi {name}, from {add}, age of {age}")

def activity4():
    f = eval(input("Enter the temperature in Fahrenheit: "))
    c = ((f - 32) * 5) / 9
    print(f"{f} degrees in Fahrenheit converted to Celsius is {round(c, 2)}")

def activity5():
    x = 10
    print(x)
    x = x + 10
    print(x)
    
    x += 10
    print(x)
    x *= 3
    print(x)

def activity6():
    password = "lotie"
    my_pw = input("Enter your password: ")
    if my_pw.lower() == password:
        print("Access Granted. Enjoy.")
    elif my_pw.lower() == "jaoming":
        print("Tumpak!")
    else:
        print("Access Denied.")

def activity7():
    print("# SCHOLARSHIP GRANT APPLICATION SYSTEM")
    name = input("Enter your name: ")
    isEnrolled = input("Are you currently enrolled in DLL? (yes/no): ")
    if isEnrolled.lower() == "yes":
        print(f"Hi, {name}! Welcome to the DLL Scholarship Grant System.")
        age = int(input("How old are you right now? "))
        if 18 <= age <= 35:
            print("Your age complies with the age requirement.")
            grades = eval(input("What was your last GWA? "))
            if 86 <= grades <= 100:
                print("Your grades pass the requirements.")
                print("Congratulations! You are now granted a scholarship.")
            else:
                print("You are not qualified for the scholarship grant.")
                is4ps = input("Is your family currently enrolled/subscribed in 4Ps program? ")
                if is4ps.lower() == "yes":
                    print("Congratulations! You are now granted a scholarship.")
                else:
                    print("Sorry, only for 4Ps members.")
        else:
            print("Sorry, you are not qualified for the scholarship grant.")
    else:
        print("Thank you for using the system.")

def activity8():
    for ikot in range(1, 21):
        print("Happy Anniversary Dalubhasaan ng Lungsod ng Lucena")

def activity9():
    num = eval(input("Enter a starting count: "))
    factorial = 1
    for x in range(num, 0, -1):
        factorial *= x
    print(f"The factorial of {num} is {factorial}")

def activity10():
    for loop in range(1, 7):
        for x in range(7 - loop):
            print(" ", end=" ")
        for y in range(loop):
            print(loop, end=" ")
        for z in range(loop - 1):
            print(loop, end=" ")
        print()

def activity11():
    for x in range(1, 11):
        print(f"{x}", end=" ")
        for y in range(1, 11):
            print("*", end=" ")
        print()

def activity12():
    for x in range(1, 6):
        for y in range(1, x + 1):
            print(".", end=" ")
        for z in range(6, x, -1):
            print("*", end=" ")
        for a in range(6, x, -1):
            print("^", end=" ")
        print()

def activity13():
    for x in range(1, 11):
        print(f"{x} x 1 = {x * 1}")

def activity14():
    num = eval(input("Enter the number of triangles: "))

    for x in range(1, 6):
        for y in range(1, num + 1):
            for z in range(1, x + 1):
                print("x", end=" ")
            for a in range(6, x, -1):
                print(" ", end=" ")
            print(end=" ")
        print()

def activity15():
    isReapet = True

    while isReapet:
        name = input("Enter a name: ")
        print(f"Hi, {name}!")
        if name.lower() == "rodelyn":
            print("LOOP TERMINATED")
            isReapet = False
            break

def activity16():
    tuloy = True
    sum = 0
    while tuloy:
        num = eval(input("Enter any number --->  "))

        if num == 0:
            print("LOOP STOPPED")
            print(f"The sum of all the numbers given is {sum}")
            break
        else:
            sum += num
            continue

def activity17():
    def greet_Someone():
        print("Hi , hoped your having a delightful Tuesday afternoon.")

    def greet_Person(name):
        print(f"Hi {name}, hoped your having a delightful Tuesday afternoon.")

    def right_Triangle():
        for x in range(1, 6):
            for y in range(1, x + 1):
                print("*", end=" ")
            for z in range(6, x, -1):
                print(" ", end=" ")
            print()

    def get_info(name, age):
        print(f"Hi {name}, with age {age} yrs old.")

    def factorial(number):
        fact = 1
        for x in range(number, 0, -1):
            fact *= x
        print(f"The factorial of {number} is {fact}")

    greet_Someone()
    greet_Person("Student")
    right_Triangle()
    get_info("Rodelyn", 22)
    factorial(4)

def activity18():
    def factorial(number):
        """This function is for calculating factorial. Just put the number inside the parenthesis."""
        fact = 1
        for x in range(number, 0, -1):
            fact *= x
        return fact

    print(f"The factorial of 5 is {factorial(5)}")

def activity19():
    from __main__ import activity18

    def factorial(number):
        # return act18.factorial(number)

        print(f"The factorial of 7 is {factorial(7)}")

# Code Challenges
def code_challenge1():
    print("\t\t\t * \n\t\t        *** \n\t\t       ***** \n\t\t\t*** \n\t\t\t *")

def code_challenge2():
    name = input("What is your name? ")
    print("\t\t\t\t\t\t\t\t * \n\t\t\t\t\t\t\t        *** \n\t\t\t\t\t\t\t       ***** \n\t\t\t\t\t\t             *Hi " +name+"* \n\t\t\t\t\t\t\t       ***** \n\t\t\t\t\t\t\t        *** \n\t\t\t\t\t\t\t\t *")

def code_challenge3():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))

    sum = int(x) + int(y)
    print("The sum of 10 and 2 is", sum)

    x = 10
    y = 2
    diff = int(x) - (y)
    print("The difference of 10 and 2 is", diff)

    x = 10 
    y = 2
    prod = int(x) * int(y)
    print("The product of 10 and 2 is", prod)

    x = 10
    y = 2
    quotient = int(x) / int(y)
    print("The quotient of 10 and 2 is", quotient)

    x = 10
    y = 2 
    exp = int(x) ** (y)
    print("The exponent of 10 and 2 is", exp)

    x = 10
    y = 2 
    rem = int(x) % int(y)
    print("The remainder of 10 and 2 is", rem)

    x = 10
    y = 2 
    fldiv =  int(x) // int(y)
    print("The floor division of 10 and 2 is", fldiv)

def code_challenge4():
    name = input("enter your name: ")
    maneh1 = eval(input("Enter your deposit: ")) 
    print("Hi!",name, " your deposit amount breakdown in PH denominator is as follow")

    maneh2 = maneh1 // 1000 
    maneh3 =  maneh1 % 1000
    print(maneh2, "1000")

    maneh4 = maneh3 // 500 
    maneh5 = maneh3 % 500
    print(maneh4, "500")

    maneh6 = maneh5 // 200
    maneh7 = maneh5 % 200
    print (maneh6, "200")

    maneh8 = maneh7 // 100 
    maneh9 = maneh7 % 100

    maneh10 = maneh9 // 50
    maneh11 = maneh9 % 50
    print(maneh8, 100)
    print(maneh10, "50")

    maneh12 = maneh11 // 20 
    maneh13 = maneh11 % 20

    maneh14 = maneh13 // 10 
    maneh15 = maneh13 % 10   
 
    maneh16 = maneh15 //5
    maneh17 = maneh15 % 5

    maneh18 = maneh17 // 1 
    maneh19 = maneh17 % 1
    print(maneh12, "20") 
    print(maneh14, "10") 
    print(maneh16, "5")
    print(maneh18, "1")

def code_challenge5():
    #Grading decision

    name = input("Please enter your name: ")
    grade = float(input("Please input your grade: "))

    os = 90 - 100
    vs = 85 - 89
    s = 80 - 84
    o = 75-79
    f = 74 

    #passed = 75
    #failed = 74 

    if grade > 75:
        print("Good job! You passed!")

    else:
        print("You failed. Better luck next time!")

def code_challenge6():
    age = int(input("Enter your age: "))

    if age < 0:
            category = "Invalid age"
    elif age <= 8:
        category = "Toddler"
    elif age <= 14:
        category = "Preteen"
    elif age <= 18:
        category = "Teenager"
    elif age <= 27:
        category = "Early Adult"
    elif age <= 44:
        category = "Middle Adult"
    elif age <= 59:
        category = "Past Adult"   
    else:
        category = "Senior"

    print(f"You are a {category}.")

def code_challenge7():
    name = input("Please enter your name: ")
    print(f"Hi {name}! Welcome to our store!")

    print(" **MEAT** \n pork = 300 \n chicken = 220 \n beef = 450")
    print(" **DRY GOODS** \n cereal = 120 \n coffee = 70 \n sugar = 70 \n instant noodles = 30")

    pur = input("Did you purchased a grocery today? (yes/no): ")
    yes = "proceed"
    order = input("What did you purchased? ")
    if pur == yes: 
        print("Okay, thank you! Let's proceed!")
    else: 
        print("Thank you for visiting our store! :)")


#def item_catgorized(name, price, quantity):


def code_challenge8():
    sum = 0
    for lotie in range(1,11):
        num = eval(input(f"Input #{lotie}: "))
        sum += num
    print(f"The sum of all the numbers given/provided is {sum}")

def code_challenge9(): 
    for x in range(1,6):
        for b in range(1, x + 1):
            print(" ",end=" ")
        for c in range (6, x, -1):
            print("*",end=" ")
        print()

def code_challenge10():
    x = 5  

    # Upper part of the diamond
    for f in range(1, x + 1):
        print(" " * (x - f), end="")  
        print("* " * f)               

    # Lower part of the diamond
    for s in range(x - 1, 0, -1):
        print(" " * (x - s), end="") 
        print("* " * s)              

def code_challenge11():
# Arrow Heads Up
    for x in range(1,6):
        for y in range(5, x, -1):
            print(" ",end=" ")
        for z in range(1, 2 * x):
            print("*",end=" ")
        print()

# Arrow Heads Down
    for x in range(4, 0, -1):
        for y in range(5, x, -1):
            print(" ",end=" ")
        for z in range(1, 2 * x):
            print("*",end=" ")
        print()

def code_challenge12():
#Arrow Up

    for x in range(1,6):
        for y in range(6, x, -1):
            print(" ",end=" ")
        for z in range(1, x + 1):
            print("*",end=" ")
        for a in range(1, x + 1):
            print("*",end=" ")
        print()

#Arrow Down 
    for x in range(1,6):
        for y in range(1,6):
            print(" ",end=" ")
        for z in range(1,3):
            print("*",end=" ")
        print()


def code_challenge13():
    for x in range(1,7):
        for y in range(6, x,-1):
            print(" ",end=" ")
        for z in range(x, 1, -1):
            print(z,end = " ")
        for a in range(1, x + 1):
            print(a, end =" ")
        print()
    for x in range(5, 0, -1):
        for y in range(6, x, -1):
            print(" ",end=" ")
        for z in range(x, 1, -1):
            print(z,end = " ")
        for a in range(1, x + 1):
            print(a, end =" ")
        print()



# Map activities to their respective functions
activities = {
    "1": activity1,
    "2": activity2,
    "3": activity3,
    "4": activity4,
    "5": activity5,
    "6": activity6,
    "7": activity7,
    "8": activity8,
    "9": activity9,
    "10": activity10,
    "11": activity11,
    "12": activity12,
    "13": activity13,
    "14": activity14,
    "15": activity15,
    "16": activity16,
    "17": activity17,
    "18": activity18,
    "19": activity19,
}

# Map code challenges to their respective functions
code_challenges = {
    "1": code_challenge1,
    "2": code_challenge2,
    "3": code_challenge3,
    "4": code_challenge4,
    "5": code_challenge5,
    "6": code_challenge6,
    "7": code_challenge7,
    "8": code_challenge8,
    "9": code_challenge9,
    "10": code_challenge10,
    "11": code_challenge11,
    "12": code_challenge12,
    "13": code_challenge13,
}

# Menu Compilation System
print("WELCOME TO MY CODE COMPILATION FOR FIRST SEMESTER!")
time.sleep(1)

proceed = input("Would you like to continue? yes or no: ").lower()
if proceed != "yes":
    print("Thank you for visiting!")
else:
    while True:
        print("\n[1] Activity List")
        print("[2] Code Challenge List")
        print("[0] Exit the program")
        user_input = input("Enter the number of the option you want to execute: ")
        time.sleep(1)
        
        if user_input == "1":
            print("\nActivities:")
            for key in activities.keys():
                print(f"[{key}] Activity {key}")
            activity_choice = input("Please input the number of the activity you want to execute: ")
            if activity_choice in activities:
                print(f"Executing Activity {activity_choice}...\n")
                activities[activity_choice]()  # Call the corresponding function
            else:
                print("Invalid activity number.")
        elif user_input == "2":
            print("\nCode Challenges:")
            for key in code_challenges.keys():
                print(f"[{key}] Code Challenge {key}")
            challenge_choice = input("Please input the number of the code challenge you want to execute: ")
            if challenge_choice in code_challenges:
                print(f"Executing Code Challenge {challenge_choice}...\n")
                code_challenges[challenge_choice]()  # Call the corresponding function
            else:
                print("Invalid code challenge number.")
        elif user_input == "0":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid option. Please try again.")
