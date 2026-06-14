invite_list = ["archimedes", "jim parsons", "ari gibson"]
print(f"You are invited to dinner at my house, {invite_list[0].title()}.")
print(f"You are invited to dinner at my house, {invite_list[1].title()}.")
print(f"You are invited to dinner at my house, {invite_list[2].title()}.")

print(f"{invite_list[2].title()} can't make it!")

del invite_list[2]
invite_list.insert(2, "keanu reeves")

print(f"You are invited to dinner at my house, {invite_list[0].title()}.")
print(f"You are invited to dinner at my house, {invite_list[1].title()}.")
print(f"You are invited to dinner at my house, {invite_list[2].title()}.")

