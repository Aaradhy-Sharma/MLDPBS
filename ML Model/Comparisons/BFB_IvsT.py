import matplotlib.pyplot as plt
import numpy as np

# Data for the strategies and block sizes
block_sizes = ['10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K', '90K', '100K']
strategies = ['FirstFit', 'MLVPBS', 'BestFit']

# Total times for each strategy and block size
total_times = [
    [10.0, 10.0, 5070.0],  # Allocation: 10K
    [10.0, 10.0, 39910.0],  # Allocation: 20K
    [20.0, 10.0, 90890.0],  # Allocation: 30K
    [40, 10, 108735],       # Allocation: 40K
    [30, 15, 126781],       # Allocation: 50K
    [30, 20, 149687],       # Allocation: 60K
    [30, 20, 155562],       # Allocation: 70K
    [60, 25, 186823],       # Allocation: 80K
    [30, 30, 210713],       # Allocation: 90K
    [30, 20, 264979]        # Allocation: 100K
]

# Convert block sizes to x-axis values (numeric values)
x = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])

# Plot total times for each strategy using a line plot
plt.plot(x, [i[0] for i in total_times], label='FirstFit', marker='o', color='blue')
plt.plot(x, [i[1] for i in total_times], label='MLVPBS', marker='o', color='green')
plt.plot(x, [i[2] for i in total_times], label='BestFit', marker='o', color='red')

# Add labels and title
plt.xlabel('Allocations')
plt.ylabel('Total Time (ms)')
plt.title('Total Memory Allocation Time by Number of Allocations')

# Set y-axis to log scale for better readability
plt.yscale('log')

# Set custom x-ticks with corresponding allocation sizes
plt.xticks(x, block_sizes)

# Add a legend
plt.legend()

# Display the plot with a tight layout
plt.tight_layout()
plt.show()
