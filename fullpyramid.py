def full_pyramid(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end=" ")
        
        # Print asterisks
        for k in range(2 * i - 1):
            print("*", end=" ")
        
        # Move to the next line after each row
        print()

# Example: To print a full pyramid with 5 rows
full_pyramid(5)
