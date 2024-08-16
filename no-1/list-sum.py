#LIST SUM
# Define the list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Iterate over the list and perform the addition
for i in range(int(len(lst)**(1/2))):
    for j in range(0, len(lst) - 1, 2):
        lst[j] = lst[j] + lst[j+1]
    lst = lst[::2]

    # Print the list after each iteration
    print(f"After iteration {i+1}: {lst}")

# Print the final sum of the list
print(f"\nFinal sum: {lst[0]}")