import matplotlib.pyplot as plt

# Data for the strategies
threads =  ['10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K', '90K', '100K']

buddy_system_times = [1.41, 2.50, 2.81, 4.38, 5.47, 6.72, 8.59, 11.09, 11.91, 13.45]
tree_based_buddy_times = [1.41, 2.19, 2.66, 6.98, 15.16, 24.06, 29.06, 36.41, 38.75, 39.95]
multi_list_buddy_times = [1.56, 7.81, 7.97, 14.38, 19.69, 25.31, 28.44, 29.84, 33.84, 45.75]
non_blocking_buddy_times = [1.56, 2.19, 5.88, 6.09, 9.06, 16.56, 20.94, 27.5, 31.41, 34.98]
optimized_non_blocking_buddy_times = [1.41, 3.44, 3.34, 6.09, 17.34, 20.03, 20.47, 21.09, 23.59, 24.54]

# Create the plot
plt.figure(figsize=(10, 6))

# Plot for each strategy
plt.plot(threads, buddy_system_times, label='MLVPBS', marker='o', color='blue')
plt.plot(threads, tree_based_buddy_times, label='TreeBasedBuddy', marker='v', color='green')
plt.plot(threads, multi_list_buddy_times, label='MultiListBuddy', marker='^', color='red')
plt.plot(threads, non_blocking_buddy_times, label='NonBlockingBuddy', marker='<', color='purple')
plt.plot(threads, optimized_non_blocking_buddy_times, label='OptimizedNonBlockingBuddy', marker='>', color='orange')

# Add labels and title
plt.xlabel('Number of Allocations')
plt.ylabel('Total Time (ms)')
plt.title('Total Memory Allocation Time vs Number of Allocations')

# Set custom x-ticks
plt.xticks(threads)

# Display the legend
plt.legend(fontsize=16)

# Show the plot

plt.tight_layout()
plt.show()
