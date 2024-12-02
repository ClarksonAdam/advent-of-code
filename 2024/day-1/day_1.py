import numpy as np


def extract_columns_from_file(filepath):
    cols = []
    with open(filepath, "r") as file:
        for line in file:
            strings = line.strip().split("   ")
            for j, value in enumerate(strings):
                if len(cols) <= j:
                    cols.append([])
                cols[j].append(int(value))
    return cols


def compare_values_at_each_index_in_two_arrays(array1, array2):
    total = 0
    for i in range(len(array1)):
        row_total = abs(array1[i] - array2[i])
        total += row_total
    return total


def calculate_similarity_score(array1, array2):
    similarity_score = 0
    for item in array1:
        similarity_score = similarity_score + item * array2.count(item)
    return similarity_score


columns = extract_columns_from_file("day_1_input.txt")

# Task 1
column1 = np.sort(columns[0])
column2 = np.sort(columns[1])
total_dif = compare_values_at_each_index_in_two_arrays(column1, column2)
print(f"Task 1. Total: {total_dif}")

# Task 2
score = calculate_similarity_score(columns[0], columns[1])
print(f"Task 2. Similarity Score: {score}")
