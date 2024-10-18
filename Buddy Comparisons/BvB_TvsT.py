import matplotlib.pyplot as plt

# Data for the strategies
threads = [2, 4, 8, 16, 32, 64]

buddy_system_times = [6.09, 6.10, 5.60, 4.70, 3.20, 1.00]
tree_based_buddy_times = [24.53, 17.88, 14.38, 10.98, 7.69, 5.90]
multi_list_buddy_times = [7.97, 7.38, 6.990, 5.25, 5.05, 4.05]
non_blocking_buddy_times = [12.83, 12.81, 11.62, 10.75, 8.75, 3.75]
optimized_non_blocking_buddy_times = [35.94, 32.19, 13.00, 7.34, 5.14, 3.14]

# Create the plot
plt.figure(figsize=(10, 6))

# Plot for each strategy
plt.plot(threads, buddy_system_times, label='MLVPBS', marker='o', color='blue')
plt.plot(threads, tree_based_buddy_times, label='TreeBasedBuddy', marker='v', color='green')
plt.plot(threads, multi_list_buddy_times, label='MultiListBuddy', marker='^', color='red')
plt.plot(threads, non_blocking_buddy_times, label='NonBlockingBuddy', marker='<', color='purple')
plt.plot(threads, optimized_non_blocking_buddy_times, label='OptimizedNonBlockingBuddy', marker='>', color='orange')

# Add labels and title
plt.xlabel('Number of Threads')
plt.ylabel('Total Time (ms)')
plt.title('Total Memory Allocation Time vs Number of Threads')

# Set custom x-ticks
plt.xticks(threads)

# Display the legend
plt.legend(fontsize=16)  # Yo

# Show the grid and plot

plt.tight_layout()
plt.show()
