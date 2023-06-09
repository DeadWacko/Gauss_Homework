def reducing_matrix_to_triangle(matrix: list, free_vector: list) -> list:
    """
    Прямой ход Гаусса. Функция обрабатывает значения в матрице и приводит матрицу к треугольному виду
    :param matrix: входная матрица (А)
    :param free_vector: свободный вектор (b)
    :return: треугольная матрица, преобразованный вектор свободных членов
    """
    matrix_res: list = []
    free_vector_res: list = []
    return [matrix_res, free_vector_res]

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
