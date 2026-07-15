fruits = ("banana", "pear", "mango")
fruitsToCheck = ("banana", "mango", "orange", "apple", "onion", "pear")
for fruit in fruitsToCheck:    
    if fruit in fruits:
        print(f"You like {fruit}!")
    else:print(f"{fruit.title()} is not your favorite")