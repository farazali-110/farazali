def hollow_full_pyramid(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end=" ")
        
        # Print asterisks or spaces for the pyramid
        for k in range(2 * i - 1):
            if k == 0 or k == 2 * i - 2 or i == rows:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        
        # Move to the next line after each row
        print()

# Example: To print a hollow full pyramid with 5 rows
hollow_full_pyramid(5)
