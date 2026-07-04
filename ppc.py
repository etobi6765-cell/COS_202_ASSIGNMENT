def calculate_cgpa():
    print("=" * 45)
    print("      PERSONAL POCKET CGPA CALCULATOR (PPC)    ")
    print("=" * 45)

    try:
        num_courses = int(input("Enter the number of courses taken: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    total_credit_units = 0
    total_quality_points = 0

    # Loop through each course to collect data
    for i in range(1, num_courses + 1):
        print(f"\n--- Course {i} ---")
        
        try:
            credit_unit = int(input(f"Enter credit unit for Course {i}: "))
            score = float(input(f"Enter score obtained (0 - 100) for Course {i}: "))
        except ValueError:
            print("Invalid input numerical values required. Skipping this course.")
            continue

        # Selection Control Statements to determine Grade Point based on Score
        if score >= 70:
            grade = 'A'
            grade_point = 5
        elif score >= 60:
            grade = 'B'
            grade_point = 4
        elif score >= 50:
            grade = 'C'
            grade_point = 3
        elif score >= 45:
            grade = 'D'
            grade_point = 2
        elif score >= 40:
            grade = 'E'
            grade_point = 1
        else:
            grade = 'F'
            grade_point = 0

        # Calculate quality points for the course
        course_quality_point = credit_unit * grade_point
        
        # Accumulate totals
        total_credit_units += credit_unit
        total_quality_points += course_quality_point

        print(f"Result: Grade {grade} | Grade Point: {grade_point} | Quality Point: {course_quality_point}")

    # Final CGPA evaluation using conditional safety checks
    print("\n" + "=" * 45)
    if total_credit_units > 0:
        cgpa = total_quality_points / total_credit_units
        print(f"TOTAL CREDIT UNITS: {total_credit_units}")
        print(f"TOTAL QUALITY POINTS: {total_quality_points}")
        print(f"YOUR CALCULATED CGPA IS: {cgpa:.2f}")
        
        # Classification system using selection control statements
        if cgpa >= 4.50:
            print("Classification: First Class Honours! 🌟")
        elif cgpa >= 3.50:
            print("Classification: Second Class Upper Division (2:1) 👍")
        elif cgpa >= 2.40:
            print("Classification: Second Class Lower Division (2:2)")
        elif cgpa >= 1.50:
            print("Classification: Third Class Pass")
        else:
            print("Classification: Pass / Probationary")
    else:
        print("No valid course details were provided. CGPA cannot be calculated.")
    print("=" * 45)

# Execute the pocket calculator program
if __name__ == "__main__":
    calculate_cgpa()
