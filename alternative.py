def gaussian_elimination(matrix, current_row=0):
    if current_row == len(matrix):
        return matrix

    for i in range(current_row + 1, len(matrix)):
        factor = matrix[i][current_row] / matrix[current_row][current_row]
        for j in range(current_row, len(matrix[i])):
            matrix[i][j] -= factor * matrix[current_row][j]

    return gaussian_elimination(matrix, current_row + 1)


def forward_elimination(A, b):
    n = len(A)

    # Прямой ход метода Гаусса
    for i in range(n):
        # Находим максимальный элемент в i-м столбце
        max_el = abs(A[i][i])
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > max_el:
                max_el = abs(A[j][i])
                max_row = j

        # Обменяем строки, чтобы максимальный элемент был на диагонали
        for k in range(i, n):
            tmp = A[max_row][k]
            A[max_row][k] = A[i][k]
            A[i][k] = tmp
        tmp = b[max_row]
        b[max_row] = b[i]
        b[i] = tmp

        # Приводим i-й столбец к ступенчатому виду
        for j in range(i + 1, n):
            c = -A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] = A[j][k] + c * A[i][k]
            b[j] = b[j] + c * b[i]

    return A, b