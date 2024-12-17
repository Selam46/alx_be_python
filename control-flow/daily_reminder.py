
# Prompt the user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Match case statement to react based on priority
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"'{task}' is a low priority task"
    case _:
        print("Invalid priority. Please enter high, medium, or low.")
        exit()

# Check if the task is time-bound and modify the reminder message
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
elif time_bound == "no":
    reminder_message += ". Consider completing it when you have free time."
else:
    print("Invalid input for time-bound. Please enter yes or no.")
    exit()

# Print the customized reminder
print(f"Reminder: {reminder_message}")
