import time
import matplotlib.pyplot as plt
import numpy as np
import math
from timeit import default_timer as timer

# O(1) - Constant Time
def constant_time(arr):
    """Access first element of an array - O(1)"""
    if len(arr) > 0:
        return arr[0]
    return None

# O(log n) - Logarithmic Time
def binary_search(arr, target):
    """Binary search algorithm - O(log n)"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# O(n) - Linear Time
def linear_search(arr, target):
    """Linear search algorithm - O(n)"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# O(n log n) - Log-linear Time
def merge_sort(arr):
    """Merge sort algorithm - O(n log n)"""
    if len(arr) <= 1:
        return arr
    
    # Create a copy to avoid modifying the original array
    arr_copy = arr.copy()
    mid = len(arr_copy) // 2
    left = merge_sort(arr_copy[:mid])
    right = merge_sort(arr_copy[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# O(n²) - Quadratic Time
def bubble_sort(arr):
    """Bubble sort algorithm - O(n²)"""
    # Create a copy to avoid modifying the original array
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy

# O(2^n) - Exponential Time
def fibonacci_recursive(n):
    """Recursive Fibonacci - O(2^n)"""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# O(n!) - Factorial Time
def permutations(arr, l, r, count=None):
    """Generate all permutations - O(n!)"""
    # Create a copy to avoid modifying the original array
    arr_copy = arr.copy()
    if count is None:
        count = [0]
    
    if l == r:
        count[0] += 1
    else:
        for i in range(l, r + 1):
            arr_copy[l], arr_copy[i] = arr_copy[i], arr_copy[l]
            permutations(arr_copy, l + 1, r, count)
            # No need to backtrack with a copied array
    
    return count[0]

# Generate test data with appropriate sizes
def generate_test_data():
    sizes = {
        'small': [10, 50, 100, 200, 300, 400, 500],  # For most algorithms
        'very_small': [4, 5, 6, 7, 8]  # For factorial/exponential algorithms
    }
    
    data = {
        'constant': [list(range(size)) for size in sizes['small']],
        'logarithmic': [list(range(size)) for size in sizes['small']],
        'linear': [list(range(size)) for size in sizes['small']],
        'loglinear': [list(range(size)) for size in sizes['small'][:4]],  # Smaller for nlogn
        'quadratic': [list(range(size)) for size in sizes['small'][:3]],  # Smaller for n²
        'exponential': list(range(10, 25)),  # Small inputs for O(2^n)
        'factorial': list(range(3, 9))  # Very small inputs for O(n!)
    }
    
    return data

# Measure and plot time complexities
def plot_time_complexities():
    # Generate test data
    test_data = generate_test_data()
    
    # Results dictionary
    results = {}
    
    # Measure O(1) - Constant time
    sizes, times = [], []
    for arr in test_data['constant']:
        start = timer()
        constant_time(arr)
        end = timer()
        sizes.append(len(arr))
        times.append(end - start)
    results['O(1)'] = (sizes, times)
    
    # Measure O(log n) - Logarithmic time
    sizes, times = [], []
    for arr in test_data['logarithmic']:
        start = timer()
        binary_search(arr, -1)  # Search for a non-existent element
        end = timer()
        sizes.append(len(arr))
        times.append(end - start)
    results['O(log n)'] = (sizes, times)
    
    # Measure O(n) - Linear time
    sizes, times = [], []
    for arr in test_data['linear']:
        start = timer()
        linear_search(arr, -1)  # Search for a non-existent element
        end = timer()
        sizes.append(len(arr))
        times.append(end - start)
    results['O(n)'] = (sizes, times)
    
    # Measure O(n log n) - Log-linear time
    sizes, times = [], []
    for arr in test_data['loglinear']:
        reversed_arr = list(reversed(arr))  # Worst case for sorting
        start = timer()
        merge_sort(reversed_arr)
        end = timer()
        sizes.append(len(arr))
        times.append(end - start)
    results['O(n log n)'] = (sizes, times)
    
    # Measure O(n²) - Quadratic time
    sizes, times = [], []
    for arr in test_data['quadratic']:
        reversed_arr = list(reversed(arr))  # Worst case for bubble sort
        start = timer()
        bubble_sort(reversed_arr)
        end = timer()
        sizes.append(len(arr))
        times.append(end - start)
    results['O(n²)'] = (sizes, times)
    
    # Measure O(2^n) - Exponential time
    sizes, times = [], []
    for n in test_data['exponential'][:5]:  # Limit to avoid very long computations
        start = timer()
        fibonacci_recursive(n)
        end = timer()
        sizes.append(n)
        times.append(end - start)
    results['O(2^n)'] = (sizes, times)
    
    # Measure O(n!) - Factorial time
    sizes, times = [], []
    for n in test_data['factorial'][:4]:  # Limit to avoid very long computations
        arr = list(range(n))
        start = timer()
        permutations(arr, 0, n-1)
        end = timer()
        sizes.append(n)
        times.append(end - start)
    results['O(n!)'] = (sizes, times)
    
    # Create plots
    plt.figure(figsize=(15, 10))
    
    # Plot 1: Measured execution times
    plt.subplot(2, 1, 1)
    for complexity, (sizes, times) in results.items():
        plt.plot(sizes, times, 'o-', label=complexity)
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Measured Algorithm Performance')
    plt.legend()
    plt.grid(True)
    
    # Plot 2: Theoretical complexity visualization
    plt.subplot(2, 1, 2)
    x = np.linspace(1, 20, 100)
    
    # Constants chosen to make the graph visually informative
    # Adjust these constants to make curves visible on the same scale
    c1, c2, c3, c4, c5, c6, c7 = 0.1, 0.2, 0.3, 0.4, 0.05, 0.01, 0.001
    
    # Calculate theoretical complexity curves
    y_constant = np.ones_like(x) * c1
    y_log = c2 * np.log2(x)
    y_linear = c3 * x
    y_nlogn = c4 * x * np.log2(x)
    y_quadratic = c5 * x**2
    
    # For exponential and factorial, limit the domain to avoid overflow
    x_exp = np.linspace(1, 10, 50)
    y_exp = c6 * 2**x_exp
    
    x_fact = np.linspace(1, 6, 30)
    y_fact = c7 * np.array([math.factorial(int(i)) for i in x_fact])
    
    # Plot regions with colors similar to your reference image
    plt.fill_between(x, 0, y_constant, color='#50C878', alpha=0.7)  # Green - Excellent
    plt.fill_between(x, y_constant, y_log, color='#50C878', alpha=0.7)  # Green - Excellent
    plt.fill_between(x, y_log, y_linear, color='#ADFF2F', alpha=0.7)  # Light green - Good
    plt.fill_between(x, y_linear, y_nlogn, color='#FFFF00', alpha=0.7)  # Yellow - Fair
    plt.fill_between(x, y_nlogn, y_quadratic, color='#FFA500', alpha=0.7)  # Orange - Bad
    
    # Plot curves
    plt.plot(x, y_constant, 'k-', linewidth=2, label='O(1) - Constant')
    plt.plot(x, y_log, 'k-', linewidth=2, label='O(log n) - Logarithmic')
    plt.plot(x, y_linear, 'k-', linewidth=2, label='O(n) - Linear')
    plt.plot(x, y_nlogn, 'k-', linewidth=2, label='O(n log n) - Log-linear')
    plt.plot(x, y_quadratic, 'k-', linewidth=2, label='O(n²) - Quadratic')
    plt.plot(x_exp, y_exp, 'k-', linewidth=2, label='O(2^n) - Exponential')
    plt.plot(x_fact, y_fact, 'k-', linewidth=2, label='O(n!) - Factorial')
    
    # Add labels for regions
    plt.text(15, 0.05, 'Excellent', fontsize=12, color='black')
    plt.text(15, 0.5, 'Good', fontsize=12, color='black')
    plt.text(15, 2, 'Fair', fontsize=12, color='black')
    plt.text(15, 7, 'Bad', fontsize=12, color='black')
    plt.text(10, 15, 'Horrible', fontsize=12, color='red')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Operations')
    plt.title('Time Complexity Classes')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.ylim(0, 20)
    
    plt.tight_layout()
    plt.savefig('time_complexity_chart.png')
    plt.show()

if __name__ == "__main__":
    plot_time_complexities()
