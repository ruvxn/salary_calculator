import time


class SalaryCalculator:

    def __init__(self, hourly_rate):

        self.hourly_rate = hourly_rate  # Set the hourly pay rate
        self.pay_per_second = hourly_rate / 3600  # Convert hourly rate to pay per second
        self.start_time = None  # Initialize the start time
        self.earned_salary = 0.0  # Initialize the total earned salary
        self.is_running = False  # Flag to indicate if the shift is active

    def start_shift(self):

        if not self.is_running:  # Ensure the shift is not already running
            self.start_time = time.time()  # Record the current time
            self.is_running = True  # Mark the shift as active
            print("Shift started.")
        else:
            print("Shift is already running.")  # Prevent multiple starts

    def stop_shift(self):

        if self.is_running:  # Ensure the shift is running
            elapsed_time = time.time() - self.start_time  # Calculate elapsed time
            self.earned_salary += elapsed_time * self.pay_per_second  # Add to total earned salary
            self.start_time = None  # Reset the start time
            self.is_running = False  # Mark the shift as inactive
            print(f"Shift stopped. Total earned: ${self.earned_salary:.2f}")
        else:
            print("Shift is not running.")  # Prevent stopping if not running

    def get_earned_salary(self):

        if self.is_running:  # If the shift is running
            elapsed_time = time.time() - self.start_time  # Calculate elapsed time
            current_salary = self.earned_salary + (elapsed_time * self.pay_per_second)
            return current_salary  # Include the real-time salary
        return self.earned_salary  # Return the total earned if not running

    def reset(self):

        self.start_time = None  # Clear the start time
        self.earned_salary = 0.0  # Reset the total earned salary
        self.is_running = False  # Mark the shift as inactive
        print("Calculator reset.")


def main():

    hourly_rate = float(input("Enter your hourly rate: "))
    calculator = SalaryCalculator(hourly_rate)

    while True:
        # Display menu options
        print("\nOptions:")
        print("1. Start Shift")
        print("2. Stop Shift")
        print("3. Check Earned Salary")
        print("4. Reset")
        print("5. Exit")

        choice = input("Select an option: ")  # Get user choice
        if choice == "1":
            calculator.start_shift()  # Start the shift
        elif choice == "2":
            calculator.stop_shift()  # Stop the shift
        elif choice == "3":
            current_salary = calculator.get_earned_salary()  # Get the earned salary
            print(f"Current earned salary: ${current_salary:.2f}")
        elif choice == "4":
            calculator.reset()  # Reset the calculator
        elif choice == "5":
            print("Exiting...")
            break  # Exit the loop
        else:
            print("Invalid option. Please try again.")  # Handle invalid input

if __name__ == "__main__":
    main()
