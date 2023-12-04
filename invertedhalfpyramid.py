def inverted_half_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

# Example: To print an inverted half pyramid with 6 rows
inverted_half_pyramid(6)
