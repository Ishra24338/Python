#PART 1
import keyword

#PART 2
name = input ("Enter your name:")
goal = input ("Enter your the skill you want to get better at :")
target_month = input ("Enter your the month you want to reach it by :")

#PART3
daily_minutes=30

#PART 4
print("\n MY PERSONAL GOAL PLAN\n")

#PART 5
print("Name:",name)
print("Goal:",goal)
print("Target month:",target_month )
print("Daily practise:",daily_minutes, "minutes")

#PART 6
print( "\n status:", end=" ")
print ("not started")
print("Reminder:", end="-")
print("Practise every day!\n")

#PART 7
print("In one sentence:")
print(name, "wants to work on",goal,"for", daily_minutes,"minutes everyday until",target_month)
print("\n Words Python has reserved for itself:")
print(keyword.kwlist)

