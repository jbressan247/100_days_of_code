from random import choice
from high_low_data import data

correct_times = 0
current_choice = ""
runner_up_choice = ""


def check_followers():
    global correct_times
    if current_choice["follower_count"] == runner_up_choice["follower_count"]:
        correct_times += 1
        print(f"Their equal! Streak: {correct_times}")
        return True
    elif current_choice["follower_count"] > runner_up_choice["follower_count"]:
        correct_times += 1
        print(f"{current_choice["name"]} has a bigger follower count. Nice job! Streak: {correct_times}")
        return True
    else:
        print(f"{runner_up_choice["name"]} has a bigger follower count. Try again :( Streak: {correct_times}")
        return False


correct = True

random_a = choice(data)
random_b = choice(data)

print(
    f"Compare A: {random_a["name"]}, a {random_a["description"]}, from {random_a["country"]}: {random_a["follower_count"]}")
print(
    f"Compare B: {random_b["name"]}, a {random_b["description"]}, from {random_b["country"]}: {random_b["follower_count"]}")

while correct:
    user_choice = input("Who has more followers: 'A' or 'B'").upper()
    if user_choice == "A":
        current_choice = random_a
        runner_up_choice = random_b

    elif user_choice == "B":
        current_choice = random_b
        runner_up_choice = random_a

    old_choice = current_choice

    if correct == check_followers():
        random_a = old_choice
        random_b = choice(data)
        print(
            f"Compare A: {random_a["name"]}, a {random_a["description"]}, from {random_a["country"]}: {random_a["follower_count"]}")
        print(
            f"Compare B: {random_b["name"]}, a {random_b["description"]}, from {random_b["country"]}: {random_b["follower_count"]}")
    else:
        quit()

