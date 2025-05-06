
USERNAME = {
    "Diksha": "1234",
    "Amit": "amit@123",
    "Admin": "admin123",
    "vendor": "123",
}

attempts = 3

while attempts > 0:
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")

    if input_username in USERNAME and USERNAME[input_username] == input_password:
        print("Login successful..!! ")
        break
    else:
        attempts -= 1
        print("Incorrect Login Details. ")
        print(f"You left only {attempts} attempts")

if attempts == 0:
    print("You reached maximum attemps for login. Exiting from inventory.")


products = {
    1: ("T-shirt", 599),
    2: ("Jeans", 1299),
    3: ("Sneakers", 2499),
    4: ("Jacket", 1999),
    5: ("Sunglasses", 799),
    6: ("Backpack", 1499),
    7: ("Dress", 1899),
    8: ("Wristwatch", 2999),
    9: ("Sandals", 1099),
    10: ("Cap", 499),
    11: ("Formal Shirt", 999),
    12: ("Trousers", 1199),
    13: ("Heels", 2299),
    14: ("Belt", 699),
    15: ("Sweatshirt", 1399),
}

cart = []


print("--- Welcome to Myntra ---")
for num in products.keys():
    name, price = products[num]
    print(f"{num}. {name} - ₹{price}")

while True:
    choice = input("\nEnter product number to what you want purchase "
                 "(or Press 'buy' to get bill): ")
    if choice.lower() == 'buy':
        break
    choice = int(choice)
    if choice in products:
        cart.append(products[choice])
        print(f"{products[choice][0]} added to cart.")

print("--- Your Bill ---")
total = 0
for item, price in cart:
    print(f"{item} - ₹{price}")
    total += price
print(f"Total Amount: ₹{total}")
print("Thank you for shopping!")            

