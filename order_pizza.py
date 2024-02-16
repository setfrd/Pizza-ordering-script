
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")  # Get input from the user for pizza size
add_pepperoni = input("Do you want pepperoni? Y or N: ")  # Get input from the user for pepperoni preference
extra_cheese = input("Do you want extra cheese? Y or N: ")  # Get input from the user for extra cheese preference

price = {"S": 15, "M": 20, "L": 25}

# Adding pepperoni and extra cheese costs
if size in price:
    if add_pepperoni == "Y":
        if size == "S":
            price[size] += 2
        else:
            price[size] += 3
    if extra_cheese == "Y":
        price[size] += 1

print(f"Your final bill is: ${price[size]}.")
