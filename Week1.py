class PersonalInformationManager:
    def __init__(self, name, age, city, hobbies):
        self.name = name
        self.age = age
        self.city = city
        self.hobbies = hobbies  # List of hobbies

    def display(self):
        print("=" * 30)
        print("  Personal Information Manager  ")
        print("=" * 30)
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"City   : {self.city}")
        print("Hobbies:")
        for idx, hobby in enumerate(self.hobbies, 1):
            print(f"  {idx}. {hobby}")
        print("=" * 30)

# Example use
if __name__ == "__main__":
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    hobbies = input("Enter your hobbies:").split(',')

    # Remove leading/trailing whitespace from hobbies
    hobbies = [hobby.strip() for hobby in hobbies]

    pim = PersonalInformationManager(name, age, city, hobbies)
    pim.display()