# Handling hours input
while True:
    try:
        hours = int(input("Enter the number of hours studied: "))

        if hours < 0:
            print(
                "Error: Hours cannot be negative. "
                "Please enter a valid number."
            )
            continue

        break

    except ValueError:
        print(
            "Error: Invalid input. "
            "Please enter a whole number for hours."
        )


# Handling minutes input
while True:
    try:
        minutes = int(input("Enter the number of minutes studied: "))

        if minutes < 0:
            print(
                "Error: Minutes cannot be negative. "
                "Please enter a valid number."
            )
            continue

        break

    except ValueError:
        print(
            "Error: Invalid input. "
            "Please enter a whole number for minutes."
        )


# Calculate total study time
total_minutes = (hours * 60) + minutes

# Convert total minutes into hours and remaining minutes
display_hours = total_minutes // 60
display_minutes = total_minutes % 60

# Display results
print(f"\nYou entered: {hours} hour(s) and {minutes} minute(s)")

if minutes >= 60:
    print(
        f"Normalized time: {display_hours} hour(s) "
        f"and {display_minutes} minute(s)"
    )

print(f"Total study time: {total_minutes} minutes")
