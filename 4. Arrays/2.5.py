# 2.4 - Cinema seats analysis
cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
    return len(seats) * len(seats[0])

def seats_available(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == 'A':
                count += 1
    return count

def seats_booked(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == 'B':
                count += 1
    return count

def seat_status(seats, row, place):
    return "Available" if seats[row-1][place-1] == 'A' else "Booked"

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))
