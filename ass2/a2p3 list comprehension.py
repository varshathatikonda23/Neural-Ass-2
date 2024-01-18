def convert_to_centimeters(height_inches):
    return height_inches * 2.54
while True:
    try:
        num_clients = int(input("Enter the number of clients: "))
        if num_clients <= 0:
            raise ValueError("Please enter a positive integer for the number of clients.")
        break
    except ValueError as error_msg:
        print(f"Error: {error_msg}")
heights_inches_list = []
for i in range(num_clients):
    while True:
        try:
            client_height = float(input(f"Enter height in inches for client {i + 1}: "))
            if client_height <= 0:
                raise ValueError("Please enter a positive number for height.")
            heights_inches_list.append(client_height)
            break
        except ValueError as error_msg:
            print(f"Error: {error_msg}")
heights_centimeters_list = [convert_to_centimeters(height) for height in heights_inches_list]
average_height_inches = sum(heights_inches_list) / num_clients
average_height_centimeters = sum(heights_centimeters_list) / num_clients
print("\nHeights in inches_list)ches:", heights_inches_list)
print("Heights in centimeters:", heights_centimeters_list)
print(f"\nAverage Height (in inches): {average_height_inches:.2f} inches")
print(f"Average Height (in centimeters): {average_height_centimeters:.2f} cm")