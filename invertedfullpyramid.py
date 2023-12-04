def inverted_full_pyramid(rows):
    for i in range(rows, 0, -1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end=" ")
        
        # Print asterisks
        for k in range(2 * i - 1):
            print("*", end=" ")
        
        # Move to the next line after each row
        print()

# Example: To print an inverted full pyramid with 5 rows
inverted_full_pyramid(5)
