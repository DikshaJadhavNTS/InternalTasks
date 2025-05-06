def basic_form():
    print("Please fill out this form:")

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    print("\n--- Form Submitted ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")

if __name__ == "__main__":
    basic_form()