from consts import *
import numpy as np
from sklearn import preprocessing


def fill_matrix(dataset):

    assert type(dataset) == str
    assert len(dataset) > 0, print("Dataset must be > 0")

    matrix = []

    for i in rang:
        matrix.append([])
        for o in rang:
            matrix[i].append(0)

    dataset = dataset.lower()

    for i in range(len(dataset)-1):
        accepted = list("abcdefghijklmnopqrstuvqxyz") + ['\n']
        if (dataset[i+1:i+2] in accepted and dataset[i:i+1] in accepted):
            ind1 = get_ord(dataset[i:i+1])
            ind2 = get_ord(dataset[i+1:i+2])
            matrix[ind1][ind2] += 1

    matrix = preprocessing.normalize(matrix, norm='l1')

    for i in range(len(matrix)):
        su = sum(matrix[i])
        if su - 1:
            matrix[i][len(list(rang))-1] += 1-su

    return matrix


if __name__ == '__main__':
    print(fill_matrix("james as"))
