import matplotlib.pyplot as plt

#Example
x_values = [1,2,3,4]
y_values = [1,2,3,4]
plt.plot(x_values, y_values)
plt.ylabel('Numbers')
plt.xlabel('Numbers')
plt.title('Simple Plot')
plt.show()

#While Loop Example

#Declare Variables
x_values = []
y_values = []
x = 0

#Adds numbers to the variables in a list
while x <= 10:
    x_values.append(x)
    y_values.append(x)
    x += 1

#Elements for the plot and run
plt.plot(x_values, y_values)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('While Plot')
plt.show()

#If Statement Example

#Declare Variables
x_plot_1 = [1, 2, 3, 4, 5]
y_plot_1 = [2, 4, 8, 16, 64]

x_plot_2 = [1, 2, 3, 4, 5]
y_plot_2 = [1, 3, 9, 27, 81]

# Define a condition
condition_met = False

# Plot different data based on the condition
if condition_met:
    plt.plot(x_plot_1, y_plot_1, label='Geometric Sequence by 2')
else:
    plt.plot(x_plot_2, y_plot_2, label='Geometric Sequence by 3')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Conditional Plot')
plt.legend()

# Show the plot
plt.show()