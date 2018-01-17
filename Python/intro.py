# known_people = ["Ahmed", "Mohamed", "Osman"]
# person = input("Enter the person you know: ")
#
# if person in known_people:
#     print("You know {}".format(person))
# else:
#     print("You dont know {}".format(person))

def who_do_you_know():
    # Ask the user for a list of people they know
    # Split the string into a list
    # Return that list
    people = input("Enter the names of people you know, seperated by commas: ")
    normalised_people = [person.strip().lower() for person in people.split(",")]
    return normalised_people


def ask_user():
    # Ask user for a name
    # See if their name is in the list of people they know
    # Print out that they know the person
    person = input("Enter a name of someone you know: ")
    if person in who_do_you_know():
        print("You know {}".format(person))

ask_user()
