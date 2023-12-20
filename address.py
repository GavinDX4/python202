# Get User Input
last_name = input("Enter Last Name: ")
first_name = input("Enter First Name: ")
street_number = input("Enter Street Number: ")
street_name = input("Enter Street Name: ")
po_box = input("Enter PO Box or Apartment Number (if applicable): ")
city = input("Enter City: ")
state = input("Enter State (Abbreviation): ")
zip_code = input("Enter Zip Code (5 digits only): ")

# Store Data in Tuple
address = (last_name, first_name, street_number, street_name, po_box, city, state, zip_code)

# Format the address
formatted_address = f"{address[0].title()}, {address[1].title()}\n{address[2]} {address[3].title()}\n"

# Check if the Apartment Value is Given
if po_box:
    formatted_address += f"PO BOX {address[4].upper()}\n"
formatted_address += f"{address[5].title()}, {address[6].upper()} {address[7]}"

# Print the formatted address
print(formatted_address)