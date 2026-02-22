#!/usr/bin/python3
"""
Bu modul matrisin elementlərini bölən funksiyanı ehtiva edir.
Matris siyahıların siyahısı (list of lists) olmalıdır.
"""


def matrix_divided(matrix, div):
    """
    Matrisin bütün elementlərini div-ə bölür.

    Args:
        matrix: Tam ədədlərdən və ya float-lardan ibarət matris.
        div: Bölən rəqəm (integer və ya float).

    Returns:
        Bölünmüş elementlərdən ibarət yeni matris.

    Raises:
        TypeError: Matris formatı səhv olduqda və ya div rəqəm olmadıqda.
        ZeroDivisionError: div 0 olduqda.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not matrix or not matrix[0]:
        raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div != div:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)
            if element != element or \
               abs(element) > 1.7976931348623158e+308:
                raise TypeError(msg)

    return [[round(i / div, 2) for i in row] for row in matrix]
