numbers = [10, 20, 30, 40, 50]
new_number = float(input("Enter a number: "))
closest = numbers[0]
for num in numbers:
    if abs(num - new_number) < abs(closest - new_number):
        closest = num

print("Closest number is:", closest)
