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