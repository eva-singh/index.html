import random
computer_list=['stone','paper','scissor']
computer=[0]
you=[0]
name=input('Enter your name here: ')
print("Hi",name,", welcome to the game of stone,paper,scissors!")
hel_p=input("Would you like to know how to play?(yes/no): ").lower()
if hel_p=="yes":
    print("\'STONE\' is greater than \'SCISSOR\' \n\'PAPER\' is greater than \'STONE\' \n\'SCISSOR\' is greater than \'PAPER\'")
else:
    print("Alright!")
number=int(input("How many rounds would you like to play ?(enter digits): "))
for i in range(0,number):
    object = input('Please type any one object from \'Stone\',\'Paper\' and \'Scissor\' here: ').lower()
    if object == 'stone':
        computer_output = random.choice(computer_list)
        print("The computer has chosen","\'", '\u300E', computer_output.upper(), '\u300F',"\'")
        if computer_output == 'paper':
            print("As \'paper\' is greater than \'stone\',")
            print("\u3014 The computer \u3015 has won this round \u2755")
            for value in computer:
                value+=1
            print("The computer's points are" ,value)
            computer.append(value)
        elif computer_output=='scissor':
            print('As \'stone\' is greater than \'scissor\',\n \u3014 You \u3015 have won this round u2755')
            for point in you:
                point+=1
            print("Your points are",point)
            you.append(point)
        else:
            print("As both have chosen \'stone\', it's a tie for this round.")
    if object!="stone" and object!="scissor" and object!="paper":
        print("Please enter only the required objects (stone/paper/scissor). Kindly restart the game" ) 
        break
    elif object == 'paper':
        computer_output = random.choice(computer_list)
        print("The computer has chosen","\'", '\u300E', computer_output.upper(), '\u300F', "\'")
        if computer_output == 'scissor':
            print('As \'scissor\' is greater than \'paper\',')
            print('\u3014 The computer \u3015 has won this round \u2755')
            for value in computer:
                value+=1
            print("The computer's points are",value)
            computer.append(value)
        elif computer_output=="stone":
            print('As \'paper\' is greater than \'stone\',\n \u3014 You \u3015 have won this round \u2755')
            for point in you:
                point+=1
            print("Your points are",point)
            you.append(point)
        else:
            print("As both have chosen \'paper\', it's a tie for this round.")
        if object!="stone" and object!="scissor" and object!="paper":
            print("Please enter only the required objects (stone/paper/scissor). Kindly restart the game." ) 
            break
    elif object == 'scissor' :
        computer_output = random.choice(computer_list)
        print("The computer has chosen","\'", '\u300E', computer_output.upper(), '\u300F', "\'")
        if computer_output == 'stone':
            print('As \'stone\' is greater than \'scissor\',')
            print('\u3014 The computer \u3015 has won this round \u2755')
            for value in computer:
                value+=1
            print("The computer's points are" ,value)
            computer.append(value)
        elif computer_output=="paper":
            print('As \'scissor\' is greater than \'paper\', \n \u3014 You \u3015 have won this round \u2755')
            for point in you:
                point+=1
            print("Your points are", point)
            you.append(point)
        else:
            print("As both have chosen \'scissor\', it's a tie for this round.")
        if object!="stone" and object!="scissor" and object!="paper":
            print("Please enter only the required objects (stone/paper/scissor). Kindly restart the game" ) 
            break
if object=="stone" or object=="paper" or object=="scissor":       
    final_point=0
    if len(computer)>len(you):
        print("As the computer has", len(computer)-len(you), "more point(s) than you, it has won the game! " "\nThank you for playing!")
    elif len(you)>len(computer):
        print("As you have", len(you)-len(computer), "more point(s) than the computer, you have won the game!" "\nThank you for playing!")
    else:
        print("It's a tie!" "\nThank you for playing the game!")
