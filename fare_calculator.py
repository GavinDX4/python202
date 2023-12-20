# Define the base fare as a constant
base_fare = 4.00

def fare_calculator(distance_km):
    """
    Calculate the total taxi fare based on the distance.
        1) Calculates rate per meter 
        2) Calculates total Fare 
        3) Formats the final answer
    """
    #Calculates Rate Per Meter
    rate_per_meter = 0.25 / 140

    #Calculates Total Fare and Formats it for 2 decimal points
    total_fare = base_fare + (float(distance_km) * rate_per_meter * 1000)
    formatted_fare = f"${total_fare:.2f}"

    return formatted_fare

#Defines distance_km and prints the answer
fare = fare_calculator(3.4)
print(fare)