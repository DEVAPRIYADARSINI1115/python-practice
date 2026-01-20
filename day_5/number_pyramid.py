#TO PRINT A NUMBER PYRAMID PATTERN BY TAKING INPUT FROM THE USER
def print_number_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(' ', end=' ')
        # Print numbers
        for k in range(1, i + 1):
            print(k, end=' ')
        print()
# Example usage        
n = int(input("Enter the number of rows for the number pyramid: "))
print_number_pyramid(n)
# Output for n = 5:
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5