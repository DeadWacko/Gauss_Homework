def reducing_matrix_to_triangle(matrix: list, free_vector: list) -> tuple:
    """
    Прямой ход Гаусса. Функция обрабатывает значения в матрице и приводит матрицу к треугольному виду
    :param matrix: входная матрица (А)
    :param free_vector: свободный вектор (b)
    :return: треугольная матрица, преобразованный вектор свободных членов
    """

    matrix_final = [line for line in matrix]
    free_vector_final = [x for x in free_vector]

    def column_to_zero(matrix, free_vector):

        matrix_res: list = []
        free_vector_res: list = []
        zero_columns_count = 0

        j = 1
        for raw in matrix[1::]:
            matrix_res.append(new_raw := [])
            i = 0
            for element in raw:
                new_raw.append(element - matrix[0][i] * (raw[0] / matrix[0][0]))
                i += 1
            free_vector_res.append(free_vector[j] - free_vector[0] * (raw[0] / matrix[0][0]))
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
    return matrix_final, free_vector_final


def calculation_slae_roots(matrix_res: list, free_vector_res: list) -> list:
    """
    Обратный ход. Решение СЛАУ.
    :param matrix_res: треугольная матрица
    :param free_vector_res: преобразованный вектор свободных членов.
    :return: список корней СЛАУ
    """
    n = len(matrix_res)
    roots_slae = [0] * n
    for i in range(n - 1, -1, -1):
        roots_slae[i] = free_vector_res[i] / matrix_res[i][i]
        for j in range(i - 1, -1, -1):
            free_vector_res[j] = free_vector_res[j] - matrix_res[j][i] * roots_slae[i]
    return roots_slae


A = [[10, 1, 1], [2, 10, 1], [2, 2, 10]]
b = [12, 13, 14]


def main(A, b):
   treulo_matr = reducing_matrix_to_triangle(A, b)
   print(treulo_matr)
   A_rez, b_rez = treulo_matr
   print(calculation_slae_roots(A_rez, b_rez))
main(A,b)