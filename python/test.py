import matplotlib.pyplot as plt
import numpy as np
import time

def bubble_sort(arr):
    n = len(arr)
    steps = []
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            # Capture the current state of the array
            steps.append(arr.copy())
    return steps

# Example array to sort
array_to_sort = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2]

# Sorting and capturing steps
steps = bubble_sort(array_to_sort)

# Visualization of sorting process
fig, ax = plt.subplots()

def update_plot(step):
    ax.clear()
    ax.bar(range(len(steps[step])), steps[step], color='blue')
    ax.set_title(f'Step {step + 1}/{len(steps)}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_xticks(range(len(steps[step])))
    ax.set_xticklabels(range(len(steps[step])))

# Animate the sorting process
for i in range(len(steps)):
    update_plot(i)
    plt.pause(0.3)  # Pause to show each step
    plt.draw()

plt.show()
