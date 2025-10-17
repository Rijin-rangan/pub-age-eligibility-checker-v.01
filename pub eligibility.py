
print("**************Check if youre eligible to enter pub**************")
minimum_age = 18

while True:
    try:
        name = str(input())
        age = int(input("enter the age: "))
    except ValueError:
        print("Invalid input for age. Please enter a numeric value.")
        continue

    combined = f"Name: {name} \n Age: {age}"
    print(combined)
    break

if age >= minimum_age:
    print("you are old enough to enter the pub")
else:
    print("you are not old enough to enter the pub")

while True:
        if age >= minimum_age:
            print("Do you want to proceed? \n Choose your option!")
            print("0-->Exit")
            print("1-->Proceed")

            try:
                input_value = int(input())
                if input_value == 1:
                    print("Proceeding")
                    print("Thank You!!!")
                    break
                elif input_value == 0:
                    print("Exiting")
                    print("See you next time!!!")
                    break
                else:
                    print("Invalid input, please enter 0 or 1.")
                    continue
            except ValueError:
                print("Invalid input, please enter 0 or 1.")
                continue
        else:
            new_age = minimum_age - age
            print(f"See you after {new_age} years")
            break


print("****************************end****************************")
