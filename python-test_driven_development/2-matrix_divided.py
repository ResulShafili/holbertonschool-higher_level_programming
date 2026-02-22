#!/usr/bin/python3
"""
Bu modul matrisin elementlərini bölən funksiyanı ehtiva edir.
Bütün elementlər rəqəm (int/float) olmalıdır.
"""


def matrix_divided(matrix, div):
    """
    Matrisin bütün elementlərini div-ə bölür.

    Args:
        matrix: Siyahıların siyahısı (tam ədədlər və ya float-lar).
        div: Bölən rəqəm (sıfırdan fərqli).

    Returns:
        Bölünmüş elementlərdən ibarət yeni matris.

    Raises:
        TypeError: Girişlər düzgün tipdə olmadıqda.
        ZeroDivisionError: div 0 olduqda.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # div NaN olarsa rədd et
    if div != div:
        raise TypeError("div must be a number")

    row_len = None
    new_matrix = []

    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(msg)
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)
            # Matris daxilində NaN və ya Inf-i rədd edirik
            if x != x or abs(x) > 1.7976931348623158e+308:
                raise TypeError(msg)
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)

    return new_matrix
