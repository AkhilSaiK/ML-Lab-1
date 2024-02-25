import numpy as np

def find_missing_data(arr):
    missing_indices = np.isnan(arr)
    missing_values = arr[missing_indices]
    return missing_values

# Example usage
arr = np.array([1, 2, np.nan, 4, np.nan, 6])
missing_data = find_missing_data(arr)
print("Missing data:", missing_data)
