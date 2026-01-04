
print("This is 99 Bottles of Beer on the Wall.")

bottles = 99

for bottles_of_beer in range(bottles, 0, -1):

    if bottles == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")

    elif bottles == 1:
        print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
        bottles -= 1
        print(f"Take one down and pass it around, no more bottles of beer on the wall.")

    elif bottles == 2:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1
        print(f"Take one down and pass it around, {bottles} bottle of beer on the wall.")

    else:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1
        print(f"Take one down and pass it around, {bottles} bottles of beer on the wall.")

# Test Comment for Git Repo.

print("Hello, this is a first test for setting up Git, and getting VSCode connected to GitHub.")

print("I'm trying to create a new branch.")