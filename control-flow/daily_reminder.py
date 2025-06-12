# Prompt for task description
task = input("Enter your task: ")

# Prompt for priority level
priority = input("Priority (high/medium/low): ").lower()

# Prompt for time sensitivity
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case for priority
match priority:
    case "high":
        priority_label = "high priority"
    case "medium":
        priority_label = "medium priority"
    case "low":
        priority_label = "low priority"
    case _:
        priority_label = "unknown priority"

# Form reminder based on time sensitivity
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_label} task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {priority_label} task. Consider completing it when you have free time.")