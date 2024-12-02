reports = input("Enter the reports: ")
reports_list = reports.split('\n')
safety = 0

for report in reports_list:
    mistakes = 0
    direction = 0
    prev_direction = 0
    counter = 1
    report = report.split()
    prev_value = int(report[0])
    for level in report[1:]:
        value = int(level)
        if prev_value == int(report[0]):
            if prev_value > value:
                prev_direction = -1
            elif prev_value < value:
                prev_direction = 1
        if value > prev_value:
            direction = 1
        if value < prev_value:
            direction = -1
        if 1 > abs(prev_value - value) or 3 < abs(prev_value - value) or prev_direction != direction:
            mistakes = mistakes + 1
            if mistakes >= 2:
                break
        prev_direction = direction
        prev_value = value
        print("counted")
        counter = counter + 1
    if counter == len(report):
        safety = safety + 1
print(safety)

