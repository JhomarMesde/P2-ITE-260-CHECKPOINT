def average(a, b, c):
‎    return (a + b + c) / 3
‎
‎students = int(input("How many students? "))
‎
‎for i in range(students):
‎    name = input("Enter name: ")
‎    a = float(input("Activity 1: "))
‎    b = float(input("Activity 2: "))
‎    c = float(input("Activity 3: "))
‎
‎    avg = average(a, b, c)
‎
‎    if avg >= 90:
‎        status = "Excellent"
‎    elif avg >= 80:
‎        status = "Very Good"
‎    elif avg >= 75:
‎        status = "Passed"
‎    else:
‎        status = "Failed"
‎
‎    print("Name:", name)
‎    print("Activity 1:", a)
‎    print("Activity 2:", b)
‎    print("Activity 3:", c)
‎    print("Average:", round(avg, 2))
‎    print("Status:", status)