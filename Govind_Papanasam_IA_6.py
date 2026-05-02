# Daily Steps Tracker
# Author: YourName YourLastName
# This program tracks daily steps for a week and evaluates performance against a goal

# main function to control program flow
def main():
    # Function to set the user's daily step goal
    def set_steps_goal():
        # Prompt user for daily steps goal
        print("Set your daily steps goal")
        goal = int(input("Enter your daily steps goal: "))
        return goal
    # Function to record steps for 7 days
    def record_daily_steps():
        total_steps = 0 # Initialize variables
        day_index = 0
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Loop for 7 days
        while day_index < 7:
            # Ask user for steps for the current day
            steps = int(input(f"Enter steps for day {days[day_index]}: "))

            # Add to total steps
            total_steps = total_steps +  steps

            # Move to next day
            day_index = day_index + 1

        return total_steps # Return total steps after 7 days

    # Function to evaluate weekly performance
    def evaluate_weekly_performance(total_steps, goal):
        # Calculate average steps
        average = total_steps / 7

        # Display average steps
        print("\nWeekly Steps Summary")
        print(f"Total steps: {total_steps}")
        print(f"your average daily steps: {average:.2f}")

        # Compare average with goal
        if average > goal:
            print(f"You exceeded your daily step goal! Great job! Keep it up!")
        elif average == goal:
            print(f"You met your daily steps goal! Very good performance!")
        else:
            print(f"You did not meet your daily steps goal. Don't worry, we'll try harder next time!")
    # ---- Program Executive Starts Here -----
    print("Welcome to the Daily Step Tracker!")  # Create a friendly starter message
    goal = set_steps_goal() # Get user's goal
    total_steps = record_daily_steps() # Record steps for the week
    evaluate_weekly_performance(total_steps, goal) # Show evaluated performance summary

# Call the main function to run the program
main()

