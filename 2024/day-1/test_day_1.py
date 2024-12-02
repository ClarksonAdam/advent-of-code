import day_1


def test_extract_columns_from_file():
    cols = day_1.extract_columns_from_file("day_1_input.txt")
    assert cols[0][0] == 58789
    assert cols[1][0] == 28882
    assert len(cols[0]) == 1000


def test_array_comparison():
    array1 = [1, 5, 10]
    array2 = [3, 8, 15]
    total_difference = day_1.compare_values_at_each_index_in_two_arrays(array1, array2)
    assert total_difference == 2 + 3 + 5


def test_similarity_score():
    array1 = [101, 500, 102, 400]
    array2 = [200, 101, 500, 500, 400]
    similarity = day_1.calculate_similarity_score(array1, array2)
    assert similarity == 101 + 1000 + 400
