import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_item=len(names)

random_choice =random.randint(0 , num_item - 1)
Person_who_will_pay=names[random_choice]
print(Person_who_will_pay + " is going to buy the meal today.")
