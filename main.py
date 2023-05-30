from robotics import Robot


SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Quandrinaut")


def main():
    """Main function to run the robot."""
    try:
        # Introduce the robot
        robot.introduce()

        # Get scientists' information from Wikipedia
        robot.get_scientist_info(SCIENTISTS)

        # Write scientists' information to an Excel file
        robot.write_to_excel()
        
        # Write scientists' information to a destinated database
        robot.write_to_database()

    except Exception as e:
        # If an exception occurs, log the error and notify via email
        robot.handle_exceptions_with_notify_email(f"An error occurred when starting the robot: {str(e)}. Please contact the administrator.")
        
        # shut down the application
        return

# Entry point of the script
if __name__ == "__main__":
    main()
