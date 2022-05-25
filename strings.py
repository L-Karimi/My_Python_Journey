ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford_quote)
ford_quote = "Whether you think you can, or you think you can't--you're right."
print(ford_quote)
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username +" accessed the site "  + url + " at " + timestamp +".")

#Use string concatenation and the len() function to find the length of a certain movie star's actual full name. Store that length in the name_length variable. Don't forget that there are spaces in between the different parts of a name!
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name)+len(middle_names)+len(family_name)
#todo: calculate how long this name is

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
#VCalculate and print the total sales for the week from the data provided. Print out a string of the form "This week's total sales: xxx", where xxx will be the actual total of all the numbers. You’ll need to change the type of the input data in order to calculate that total.
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
total_sales = int("121")+int("105")+int("110")+int("98")+int("95")
print(total_sales)
# print("This week's total sales:" + total_sales)


animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))


course="software development"
print(course.capitalize())
print(course.casefold())
print(course.expandtabs())
print(course.endswith('f'))