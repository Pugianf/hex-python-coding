#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        cont = 0
        for elem in row:
            print("{:d}".format(elem), end=(" "))
            cont += 1
        print()
