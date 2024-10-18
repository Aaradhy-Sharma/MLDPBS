import matplotlib.pyplot as plt
import numpy as np

# Data for the strategies and block sizes
block_sizes = ['2,4,6,8,16', '', '', '', '', '32', '64', '128', '256', '360', '482', '512']
strategies = ['FirstFit', 'MLVPBS', 'BestFit']

# Total times for each strategy and block size
total_times = [
    # Times for different block sizes and strategies
    [50, 20, 8967], [50, 25, 9034], [55.0, 30.0, 9589.0], [50, 30, 9989], 
    [60, 30, 10445], [60, 40, 11009], [60, 40, 12506], [50, 30, 13587], 
    [50, 30, 14099], [60.0, 50.0, 6991.0], [70.0, 50.0, 15070.0], [77, 55, 16289]
]

# Convert block sizes to x-axis values (numeric values)
x = np.array([2, 4, 6, 8, 16, 32, 64, 128, 256, 360, 482, 512])

# Plot total times for each strategy using a line plot
plt.plot(x, [i[0] for i in total_times], label='FirstFit', marker='o', color='blue')
plt.plot(x, [i[1] for i in total_times], label='MLVPBS', marker='o', color='green')
plt.plot(x, [i[2] for i in total_times], label='BestFit', marker='o', color='red')

# Add labels and title
plt.xlabel('Block Sizes (bytes)')
plt.ylabel('Total Time (ms)')
plt.title('Total Memory Allocation Time by Block Size ')

# Set y-axis to log scale for better readability
plt.yscale('log')

# Set custom x-ticks with corresponding block sizes
plt.xticks(x, block_sizes, rotation=315)

# Add a legend
plt.legend()

# Display the plot with a tight layout
plt.tight_layout()
plt.show()
