pizzas = ["pepperoni", "cheese", "meat lover's"]
for pizza in pizzas:
    print(f"A type of pizza that I like is {pizza}.")
print("Pizza is a food that I like.")
friend_pizzas = pizzas[:]
friend_pizzas.append("pineaple")
for friend_pizza in friend_pizzas:
    print(f"A type of pizza that my friend likes is {friend_pizza}.")
print("My friend likes pizza more than me.")