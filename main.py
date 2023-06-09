def reducing_matrix_to_triangle(matrix: list, free_vector: list) -> list:
    """
    Прямой ход Гаусса. Функция обрабатывает значения в матрице и приводит матрицу к треугольному виду
    :param matrix: входная матрица (А)
    :param free_vector: свободный вектор (b)
    :return: треугольная матрица, преобразованный вектор свободных членов
    """

    #zero_columns_count: int
    matrix_final = []
    for line in matrix:
        matrix_final.append(line)

    def column_to_zero(matrix):

        matrix_res: list = []
        zero_columns_count = 0

        for raw in matrix[1::]:
            new_raw: list = []
            matrix_res.append(new_raw)
            i = 0
            for element in raw:
                # if el=0 pass
                a = matrix[0][i]
                b = raw[0]
                c = matrix[0][0]
                new_element = element - a * (b / c)
                new_raw.append(new_element)
                i += 1
        else:
            zero_columns_count += 1
        h = 1
        for line_res in matrix_res[::-1]:
            g = 1
            for el in line_res[::-1]:
                matrix_final[-h][-g] = el
                g += 1
            h += 1

        if zero_columns_count < (len(matrix) - 1):
            matrix_ = []
            for part in matrix_res:
                matrix_.append(list(part[1:]))
            column_to_zero(matrix_)


    column_to_zero(matrix)
    free_vector_res: list = []
    return print([matrix_final])
    #, free_vector_res
reducing_matrix_to_triangle([[1, 2, 1], [3, -1, -1], [-2, 2, 3]], [0, 0, 11])
reducing_matrix_to_triangle([[3, 2, 1, 1], [1, -1, 4, -1], [-2, -2, -3, 1], [1, 5, -1, 2]], [2, -1, 9, 4])





def calculation_slae_roots(matrix_res: list, free_vector_res: list) -> list:
    """
    Обратный ход. Решение СЛАУ.
    :param matrix_res: треугольная матрица
    :param free_vector_res: преобразованный вектор свободных членов.
    :return: список корней СЛАУ
    """
    n = len(matrix_res)
    roots_slae = [0]*n
    for i in range(n-1, -1, -1):
        roots_slae[i] = free_vector_res[i] / matrix_res[i][i]
        for j in range(i-1, -1, -1):
            free_vector_res[j] = free_vector_res[j] - matrix_res[j][i] * roots_slae[i]
    return roots_slae
