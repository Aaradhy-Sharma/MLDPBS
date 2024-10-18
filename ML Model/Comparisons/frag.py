import matplotlib.pyplot as plt

# Data for memory utilization percentages
systems = ['MLVPBS', 'Best Fit', 'First Fit']
memory_utilization = [90.32, 79.31, 70.77]

# Create the bar plot
plt.bar(systems, memory_utilization, color=['blue', 'yellow', 'green'])

# Add title and labels
plt.title('Memory Utilization Percentage by System')
plt.xlabel('Memory Allocation Systems')
plt.ylabel('Memory Utilization (%)')

# Display the percentage values above the bars
for i, value in enumerate(memory_utilization):
    plt.text(i, value + 1, f'{value}%', ha='center')

# Show the plot
plt.show()
