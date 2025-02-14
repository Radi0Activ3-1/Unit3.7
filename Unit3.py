#Drake Pierce-Demksi
#

def count_zeros(array):
    count = 0
    for row in array:
        count += row.count(0)
    return count

# Example usage with different numbers
array = [[5, 0, 7], [8, 0, 2], [0, 1, 4]]
result = count_zeros(array)
print("The number of zeros in the 2D array is:", result)  # Output: The number of zeros in the 2D array is: 3

def replace_negatives_with_zero(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] < 0:
                array[i][j] = 0

# Example usage with different numbers
array = [[3, -1, 4], [-2, 6, -5], [7, -3, 9]]
replace_negatives_with_zero(array)
print("Updated 2D array:", array)  # Output: Updated 2D array: [[3, 0, 4], [0, 6, 0], [7, 0, 9]]
