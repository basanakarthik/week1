# ---------------------------------------------------------
# Personal Information Manager
# Author: Basana Venkata Karthik
# Description: Updated version with graceful KeyboardInterrupt handling
# ---------------------------------------------------------

print("=" * 45)
print("         PERSONAL INFORMATION MANAGER")
print("=" * 45)
print()

name = "Basana Venkata Karthik"
age = 22
city = "Vizianagaram"
hobby = "Learning Python"

print("Please provide the following details:")
print("-" * 45)

try:
    favorite_food = input("Enter your favorite food: ").strip()
    while favorite_food == "":
        print("❗ Input cannot be empty.")
        favorite_food = input("Enter your favorite food: ").strip()

    favorite_color = input("Enter your favorite color: ").strip()
    while favorite_color == "":
        print("❗ Input cannot be empty.")
        favorite_color = input("Enter your favorite color: ").strip()

except KeyboardInterrupt:
    print("\nProcess interrupted by user. Exiting gracefully.")
    exit(0)

age_in_months = age * 12

print()
print("=" * 45)
print("              YOUR INFORMATION")
print("=" * 45)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print()

print("=" * 45)
print("Thank you for using this program!")
print("=" * 45)
