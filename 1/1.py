ans = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        digits = []
        for c in line:
            if c.isdigit():
                digits.append(c)
                
        if digits:
            score = int(digits[0] + digits[-1])
            ans += score
            