from curses.ascii import isupper
from unittest import result


school =" AkiraChix"
print(str(school))
x=len(school)//2
output=""
for i in range(len(school)):
    if i>=x:
        output+=school[i].upper()
    else:
        output +=school[i]
        
print(str(output))


colors=["Red","Green","Yellow","Marron","Violet","Blue"]
for color in range(len(colors)):
    print( color,colors[color])
    new_list=enumerate(colors)
    print(new_list)
    


my_homeplace="I come from Laikipia county"
print(my_homeplace.replace("Laikipia","Nyeri"))
print(my_homeplace.swapcase())
print("from" in my_homeplace)
print(my_homeplace.find("come"))

for word in my_homeplace:
    print(word.isdigit())
    break


full_name = "Lucy Karimi"
y=len(full_name)//2
name=""
# x1=0
# x2=0
# for x in full_name:
#     if (x1.isLower()):
#         print(x.count())
#     elif(i.isupper()):
#         print(x.count())
for i in enumerate(full_name):
    print(i)
students={"Lucy":22,"Ian":25,"Jebitok":33,"Alex":12,"Annita":24}
for i in enumerate(students):
    print(i)
schools=["Co-operative","AkiraChix","Nairobi Uni","Kenyatta","Maseno"]
courses=["Business management","Information technology","computer science","Acturial science","Business information technology"]
for x,y in zip(schools,courses):
    print(x,y)
characters=["r","t","y","q","d","s","J","v","n"]
new_chars=characters[:]
print(new_chars)
characters[1:5] =[]
print()


# write a program that takes in a string and counts the number of vowels in the string

name="Lucy Karimi"
def vowels(string):
    new_name=""
    for i in name:
        if i=="a"or i=="e"or i=="e"or i=="o"or i=="u"  in name:
            new_name+=i
            print(name.count(i))
vowels("Lucy")
            
            
# write a program to find common characters in 2 strings

            
        