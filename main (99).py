import datetime

def track_periods():
    cycle_length = int(input("Enter your average menstrual cycle length in days: "))
    period_length = int(input("Enter your average period length in days: "))

    current_date = datetime.date.today()

    last_period_start = current_date
    next_period_start = current_date + datetime.timedelta(days=cycle_length)

    while True:
        print("\nMenu:")
        print("1. Log period start")
        print("2. Predict next period start")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            last_period_start = current_date
            print("Period start logged successfully.")

        elif choice == "2":
            days_until_next_period = (next_period_start - current_date).days
            print(f"Next period is predicted to start in {days_until_next_period} days.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

        current_date = datetime.date.today()

        if current_date >= next_period_start:
            last_period_start = next_period_start
            next_period_start = last_period_start + datetime.timedelta(days=cycle_length)

            print("Period completed. New period start predicted.")

# Run the program
track_periods()

