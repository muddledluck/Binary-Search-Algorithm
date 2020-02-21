print("It will search(or return) the index of number from shorted list by using Binary Search Algorithm\nUser can enter a list in form of '1 33 5 2 52 3 5 3'\n")

user_input = input("Enter a list/array: ").strip()
user_find = input("Enter a number to find the index: ").strip()
try:
    user_find = int(user_find)
    user_input = user_input.split()
    user_input = [int(i) for i in user_input]
    user_input.sort()
    mid = int(len(user_input)/2)
    for i in range(len(user_input)):
        if user_input[mid] == user_find:
            print(f"The index of the {user_find} is {mid}")
            break
        elif user_input[mid] < user_find:
            mid = int((mid + user_input.index(user_input[-1]))/2)    
        else:
            mid = int((mid + user_input.index(user_input[0]))/2)
except TypeError:
    print("Enter a numeric values!!!!")