total_chores=4
original_count=total_chores
print(f"you have {original_count} chores to finish today")
completed_count=0
chore_num=1

while chore_num <= total_chores:
    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore ="feed the pet"
    elif chore_num == 3: next_chore ="take out the trash"
    else next_chore ="feed the pet"
answer = input(f"Have you finished: {next_chore}? (yes/no)")

if answer == "yes":
    completed_count += 1
    chore_num += 1
    print("Great job! chore completed")
else:
    print("okay, finish it and check again!")

print("chores remaining:" total_chores-completed_count)
print()
print("======= All chores completed =======")
print("Great work finishing your checklist today!")

test_value = 0
safety_counter = 0
while test_value>=0:
    print("This condition never changes. so, it would run forever.")
    safety_counter =+ 1
    if safety_counter == 3:
        print("(Stopping here on purpose. a real invinite loop never stops on its own!)")
        break

print("===== CHORE CHECKLIST SUMMARY=====")