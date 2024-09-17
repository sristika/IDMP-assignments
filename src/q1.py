import numpy as np

# Creating a 10x10 random integer array
arr = np.random.randint(1, 101, size=(10, 10))
print("Array:\n", arr)

# (a) The minimum and maximum values in the array
print("Min:\n", arr.min())
print("Max:\n", arr.max())

# (b) The average value of every even row (rows 0, 2, ..., 8).
even_rows_avg = np.mean(arr[::2, :], axis=1)
print("Average of even rows:", even_rows_avg)

# (c) The standard deviation in every odd column (columns 1, 3, ..., 9).
odd_columns_std = np.std(arr[:, 1::2], axis=0)
print("Standard deviation of odd columns:", odd_columns_std)

# (d) How many rows contain a number less than 5?
rows_lt5 = np.any(arr < 5, axis=1)
print("Rows with numbers less than 5:", np.sum(rows_lt5))

# (e) Which columns contain a number greater than 90? (print the indexes of the
# columns).
columns_gt90 = np.any(arr > 90, axis=0)
print("Columns with numbers greater than 90:", np.where(columns_gt90)[0])

# (f) Which numbers appear in the matrix more than twice?
unique, counts = np.unique(arr, return_counts=True)
more_than_twice = unique[counts > 2]
print("Numbers appearing more than twice:", more_than_twice)


# (g) How many rows contain duplicate values?
def has_dupes(row):
    return len(np.unique(row)) < len(row)


rows_with_dupes = np.apply_along_axis(has_dupes, axis=1, arr=arr)
print("Rows with duplicate values:", np.sum(rows_with_dupes))
