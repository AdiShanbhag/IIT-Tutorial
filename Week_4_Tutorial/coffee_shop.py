print("Welcome to the Python Coffee Shop")

customer_name = input("What is your name?")
print("Hello " + customer_name + "! Let's order some coffee")

price_coffee = 5.00
price_latte = 10.00
price_mocha = 15.00

print("Coffee: $" + str(price_coffee))
print("Latte: $" + str(price_latte))
print("Mocha: $" + str(price_mocha))

repeat_order_choice = "yes"
final_cost = 0

while repeat_order_choice == "yes":
    while True:

        choice = input("What would you like to order? (coffee/latte/mocha): ")
        if choice == "coffee":
            cost = price_coffee
        elif choice == "latte":
            cost = price_latte
        elif choice == "mocha":
            cost = price_mocha
        else:
            print("Sorry, we do not have that.")
            cost = 0

        quantity = int(input("How many cups would you like? "))

        total_cost = cost * quantity

        final_cost = final_cost + total_cost

        anything_else = input("Would you like to have anything else: ")

        if anything_else == "yes":
            continue
        else:
            break
        
    is_a_student = input("Are you a student at the University?")

    if is_a_student == "yes":
        final_cost = final_cost - final_cost * 0.10
    
    print("Your total is: $" + str(final_cost))
    print("Thank you, " + customer_name + "!")

    repeat_order_choice_input = input("Would you like to order again?")

    if repeat_order_choice_input == "yes":
        repeat_order_choice = repeat_order_choice_input
    else:
        print("Thank you for visiting, Enjoy your day")
        repeat_order_choice = "no"