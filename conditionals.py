from random import random


phone_balance = 3
bank_balance = 10

print(phone_balance,bank_balance)
if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10
    
print(phone_balance,bank_balance)


class Solution:
    def fizzBuzz(self, n):
       
        ans = []

        for num in range(1,n+1):

            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)

            if divisible_by_3 and divisible_by_5:
                # Divides by both 3 and 5, add FizzBuzz
                ans.append("FizzBuzz")
            elif divisible_by_3:
                # Divides by 3, add Fizz
                ans.append("Fizz")
            elif divisible_by_5:
                # Divides by 5, add Buzz
                ans.append("Buzz")
            else:
                # Not divisible by 3 or 5, add the number
                ans.append(str(num))

        return ans
Solution()
# class season():
#     if season == 'spring':
#         print('plant the garden!')
#     elif season == 'summer':
#         print('water the garden!')
#     elif season == 'fall':
#         print('harvest the garden!')
#     elif season == 'winter':
#         print('stay indoors!')
#     else:
#         print('unrecognized season')
# season()
number = 145
if number %2==0:
    print("Number" + str(number) + "is even")
else:
    print("Number"+str(number)+ " is odd")
    
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65
age =67
concession_ticket = 1.25
adult_ticket = 2.50
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)

points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)
# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 100
guess = 22

if guess<answer:
    result = "Oops!  Your guess was too low."
elif guess>answer:
    result = "Oops!  Your guess was too high."
elif answer==guess:
    result = "Nice!  Your guess matched the answer!"

print(result)

#Create a program, 
# which, given a 5 character string as a target word, 
# and a 5 character string as a guess, return a 5 character string where:
#‘2’ = this letter is in this position
#‘1’ = this letter is in the target word but not this position
#‘0’ = this letter is either not in the target word, or is not in the target word as many times as it is in the guess

def worldle():
    name= str(input("Enter a word:"))
    names = ["Janeffer","Smith","Scott","Marvin","John","Greg","Justin","Rittah","Joannah","Hariet","Christine"]
    word = random.choice(name)
    print("Guess the characters")
    guesses =""
    turns +=1
    while turns>0:
        failed =0
        for char in word:
            if char in guesses:
                print(char,end="")
            else:
                print("")
                print(char,end="")
                failed+=1
                
        if failed==0:
            print("You won!")
            print("The word is: ",word)
            break
        print()
        guess= input("Guess a character:")
        guesses+=guess
        if guesses  not in word:
            turns-+1
            print("wrong")
            print("You have ,"+ turns),"more guesses"
            if turns==0:
                print("You loose")
                
worldle()
            
                