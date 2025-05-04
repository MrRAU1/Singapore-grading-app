print("Singapore Grading System")

while True:
    # Input
    subject = input("\nEnter subject name (or type 'exit' to quit): ")
    if subject.lower() == "exit":
        print("Thanks for using the grading system. Goodbye!")
        break

    try:
        max_score = int(input("Enter maximum score for that subject: "))
        got_score = int(input("Enter score you got for that subject: "))
    except ValueError:
        print("Please enter valid numbers for the scores.")
        continue

    # Calculate percentage
    percentage = (got_score / max_score) * 100

    # Determine AL grade
    if percentage >= 90:
        grade = "AL1"
    elif percentage >= 85:
        grade = "AL2"
    elif percentage >= 80:
        grade = "AL3"
    elif percentage >= 75:
        grade = "AL4"
    elif percentage >= 65:
        grade = "AL5"
    elif percentage >= 45:
        grade = "AL6"
    elif percentage >= 20:
        grade = "AL7"
    else:
        grade = "AL8"

    # Final result message
    print(f"\nYou got {got_score} over {max_score}, which is {percentage:.2f}% — and in Singapore grading terms, that is {grade}.")

    # Friendly feedback
    if grade in ["AL1", "AL2", "AL3"]:
        print("Excellent job! You're among the top performers!")
    elif grade in ["AL4", "AL5", "AL6"]:
        print("OKOK lah...can do better...you not considered good accordinng to asian law study harder.")
    else:
        print("YOU SUCH A FAILURE ...NO WONDER WHY YOUR PARENTS SAY YOU DISGRACE... YOU MAKE A 1-YEAR-OLD LOOK SMART...AT THIS RATE YOUR JOB IS A CLEANER!!!")
