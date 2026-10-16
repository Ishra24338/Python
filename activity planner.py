# Part 1
homework=int(input("Enter your homework time in minutes: "))
# Part 2
if homework>60:
    plan="start homework now"
    print("That is a long homework session")
else:
    plan="finish homework quickly"
    print("That is a short homework session")

# Part 3
freetime=input("Is there free time after the homework?(yes/no):")
if freetime==yes:
    print("Reminder:pick up a hobby for your free time")

# Part 4
print("=======DAILY PLANNER=======")
print("Homework minutes:",homework)
print("Plan:",plan)
print("Free time:",freetime)


