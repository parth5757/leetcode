def min_moves_to_seats(seats, students):
    # Sort both arrays to align the students with seats in minimal move configuration
    seats.sort()
    students.sort()
    print(zip(seats, students))
    # Calculate the total number of moves required
    total_moves = 0
    for seat, student in zip(seats, students):
        total_moves += abs(seat - student)
    
    return total_moves

# Example usage
seats1 = [3, 1, 5]
students1 = [2, 7, 4]
print(min_moves_to_seats(seats1, students1))  # Output: 4

seats2 = [4, 1, 5, 9]
students2 = [1, 3, 2, 6]
print(min_moves_to_seats(seats2, students2))  # Output: 7

seats3 = [2, 2, 6, 6]
students3 = [1, 3, 2, 6]
print(min_moves_to_seats(seats3, students3))  # Output: 4
