customer_heights_inches = []

while True:
    try:
        num_of_customers = int(input("Enter the number of customers: "))
        if num_of_customers > 0:
            break
        else:
            print("Invalid input. Please enter a positive number of customers.")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

for i in range(1, num_of_customers + 1):
    while True:
        try:
            height_inches = float(input("Enter height in inches for customer {}: ".format(i)))
            customer_heights_inches.append(height_inches)
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for height.")

heights_in_centimeters = [height * 2.54 for height in customer_heights_inches]

print("Heights in centimeters:", heights_in_centimeters)