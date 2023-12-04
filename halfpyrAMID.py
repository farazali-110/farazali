def half_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

# Example: To print a half pyramid with 6 rows
half_pyramid(6)





