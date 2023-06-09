def reducing_matrix_to_triangle(matrix: list, free_vector: list) -> tuple:
    """
    Прямой ход Гаусса. Функция обрабатывает значения в матрице и приводит матрицу к треугольному виду
    :param matrix: входная матрица (А)
    :param free_vector: свободный вектор (b)
    :return: треугольная матрица, преобразованный вектор свободных членов
    """

    #zero_columns_count: int
    matrix_final = [line for line in matrix]
    free_vector_final = [x for x in free_vector]

    def column_to_zero(matrix, free_vector):

        matrix_res: list = []
        free_vector_res: list = []
        zero_columns_count = 0

        j = 1
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
            ee = free_vector[j]
            ea = free_vector[0]
            eb = raw[0]
            ec = matrix[0][0]
            vector = ee - ea * (eb / ec)
            free_vector_res.append(vector)
            j += 1

        else:
            zero_columns_count += 1
        h = 1
        for line_res in matrix_res[::-1]:
            g = 1
            for el in line_res[::-1]:
                matrix_final[-h][-g] = el
                g += 1
            h += 1
        k = 1
        for vect in free_vector_res[::-1]:
            free_vector_final[-k] = vect
            k += 1

        if zero_columns_count < (len(matrix) - 1):
            matrix_ = []
            for part in matrix_res:
                matrix_.append(list(part[1:]))
            column_to_zero(matrix_, free_vector_res)


    column_to_zero(matrix, free_vector)
    return (matrix_final, free_vector_final)

reducing_matrix_to_triangle([[1, 2, 1], [3, -1, -1], [-2, 2, 3]], [0, 0, 11])
reducing_matrix_to_triangle([[3, 2, 1, 1], [1, -1, 4, -1], [-2, -2, -3, 1], [1, 5, -1, 2]], [2, -1, 9, 4])



def calculation_slae_roots(matrix_res: list, free_vector_res: list) -> list:
    """
    Обратный ход. Решение СЛАУ.
    :param matrix_res: треугольная матрица
    :param free_vector_res: преобразованный вектор свободных членов.
    :return: список корней СЛАУ
    """
    roots_slae = []
    return roots_slae

