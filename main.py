total_chores = 4
original_count = total_chores
print(f"You have {total_chores} chores to complete today.")

complete_count = 0
chore_num = 1

while chore_num <= total_chores:

    if chore_num == 1: next_chore = "make your bed"
    elif chore_num == 2: next_chore = "Feed the cat"
    elif chore_num == 3: next_chore = "take out the trash"
    elif chore_num == 4: next_chore = "do the dishes"

    answer = input(f"Have you completed chore {next_chore}? (yes/no) ")
    if answer == "yes":
        complete_count += 1
        chore_num += 1
    else:
        print("Okay, finish it and check again!")
    print("Chores remaining: ", total_chores - complete_count)
    print()

print("===== ALL CHORES COMPLETED =====")
print("Great work completing all your chores today!")

print("Now lets peek an infinite loop...")
test_value = 0
safe_counter = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter += 1
    if safety_counter > 3:
        print("(Stopping here on purpose - in real infinite loops never stops by its own!)")
        break

print("\n===== CHORE CHECKLIST SUMMURY =====")
print("Chores Assigned Today: ", original_count)
print("Chores Completed Today: ", complete_count)
print("Chores Remaining Today: ", total_chores - complete_count)
print("====================================")