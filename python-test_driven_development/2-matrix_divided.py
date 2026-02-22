#!/usr/bin/python3
"""
Bu modul matrisin elementlərini bölən funksiyanı ehtiva edir.
Matris siyahıların siyahısı (list of lists) olmalıdır.
Bütün elementlər rəqəm (int/float) olmalıdır.
"""


def matrix_divided(matrix, div):
    """
    Matrisin bütün elementlərini div-ə bölür və 2 rəqəmə qədər yuvarlaqlaşdırır.

    Args:
        matrix (list): Siyahıların siyahısı (integers və ya floats).
        div (int/float): Bölən rəqəm.

    Returns:
        list: Bölünmüş elementlərdən ibarət yeni matris.

    Raises:
        TypeError: Matris formatı səhv olduqda və ya div rəqəm olmadıqda.
        ZeroDivisionError: div 0 olduqda.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = None
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(msg)

        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    return [[round(item / div, 2) for item in row] for row in matrix]
