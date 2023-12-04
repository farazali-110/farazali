def hollow_inverted_half_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            if j == 1 or j == i or i == rows:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example: To print a hollow inverted half pyramid with 6 rows
hollow_inverted_half_pyramid(6)
