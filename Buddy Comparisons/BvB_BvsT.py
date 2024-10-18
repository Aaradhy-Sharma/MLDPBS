import matplotlib.pyplot as plt
import numpy as np

# Data for the block sizes and times for each strategy
block_sizes = [6, 360, 482]

buddy_system_times = [20.550, 24.20, 31.00]
tree_based_buddy_times = [22.650, 28.80, 35.80]
multi_list_buddy_times = [26.690, 29.00, 37.20]
non_blocking_buddy_times = [24.80, 27.00, 35.20]
optimized_non_blocking_buddy_times = [22.00, 25.20, 34.00]

# Plot each strategy as a separate line
plt.plot(block_sizes, buddy_system_times, label='MLVPBS', marker='o', color='blue')
plt.plot(block_sizes, tree_based_buddy_times, label='TreeBasedBuddy', marker='v', color='green')
plt.plot(block_sizes, multi_list_buddy_times, label='MultiListBuddy', marker='^', color='red')
plt.plot(block_sizes, non_blocking_buddy_times, label='NonBlockingBuddy', marker='<', color='purple')
plt.plot(block_sizes, optimized_non_blocking_buddy_times, label='OptimizedNonBlockingBuddy', marker='>', color='orange')

# Add labels and title
plt.xlabel('Block Size (bytes)')
plt.ylabel('Total Time (ms)')
plt.title('Total Memory Allocation Time vs Block Size')

# Set custom x-ticks
plt.xticks(block_sizes)

# Add a legend
plt.legend(fontsize=10)

# Display the plot without grids
plt.tight_layout()
plt.show()
