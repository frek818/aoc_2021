

def solution(movements):
    horizontal, vertical = 0, 0
    for move in movements:
        direction, magnitude = move.split(' ')
        if direction == "forward":
            horizontal += int(magnitude)
        elif direction == "down":
            vertical += int(magnitude)
        elif direction == "up":
            vertical -= int(magnitude)

    return horizontal * vertical

def solution2(movements):
    horizontal, vertical, aim = 0, 0, 0
    for move in movements:
        direction, magnitude = move.split(' ')
        magnitude = int(magnitude)
        if direction == "forward":
            horizontal += magnitude
            vertical += (aim * magnitude) 
        elif direction == "down":
            aim += int(magnitude)
        elif direction == "up":
            aim -= int(magnitude)

    return horizontal * vertical

assert 150 == solution(["forward 5","down 5","forward 8","up 3","down 8","forward 2"])
assert 900 == solution2(["forward 5","down 5","forward 8","up 3","down 8","forward 2"])

def main():
    with open('input.txt', 'r') as inp:
        input_data = inp.readlines()
    result1 = solution(input_data)
    print(f"Part 1 answer: {result1}")

    result2 = solution2(input_data)
    print(f"Part 2 answer: {result2}")

main()
