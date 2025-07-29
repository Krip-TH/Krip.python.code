# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Krip", 20, "Phuket", "Thailand")  # name, age, city, country
    hobbies = []

    while True:

        choice = input("What do you want to do ?(1: Display 2: Add Hobby ,3:Remove Hobby , 4: Edit Age ,5:Exit):")

        # Your code here
        if choice == "1":
            print(f"Name: {person[0]}")
            print(f"Age : {person[1]}")
            print(f"City : {person[2]}")
            print(f"Country : {person[3]}")
            print(f"Hobbies : {hobbies}")

        elif choice == "2":
            # append hobby
            hobby = input("What is your favorite hobbies :")
            hobbies.append(hobby)

        elif choice == "3":
            # remove hobby
            if hobbies:
                hobbies.pop()
            else:
                print("No hobbies to remove.")

        elif choice == "4":
            # edit age
            person_list = list(person)  # ("Krip", 20, "Phuket", "Thailand")
            age = input("How old are you? :")
            person_list[1] = age
            person = tuple(person_list)

        elif choice == "5":
            break

if __name__ == "__main__":
    personal_info_manager()