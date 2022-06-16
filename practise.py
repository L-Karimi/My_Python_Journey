from datetime import datetime

now = datetime.now()

hour = now.hour
name="Lucy"
if hour >= 20 or hour < 6:
    print(f"Buenas noches {name}!")
elif hour >= 20 or hour<= 12:
    print(f" ¡Buenos días {name}")
else:
    print(f" ¡Buenas tardes {name}")

age = int(input("Enter your age:"))
if int(age)>=18:
    print("You are eligible to vote")
    print("Go out and vote")
    
    
empty_tuple=()
brothers=("Paul","Kefa","Jeremy","Shadrack")
sisters=("Beatrice","Hannah")
siblings= brothers.union(sisters)
print(siblings)

squares= [2,4,6,8,10,12,14]
new_values =[]
for i in squares:
    new_values.append(1*i)
    print(new_values)
    
sentense="I will soon buy myself a car and build a house"
vowels= [ i for i in sentense if i is  'aeiou']
print(vowels)