from consts import *
import numpy as np
from sklearn import preprocessing


def fill_matrix(dataset):
  # type(dataset) = string

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

    for i in range(len(matrix)):
        mag = 0
        for o in matrix[i]:
            mag += o*o
        mag = mag ** 0.5

        # for o in range(len(matrix[i])):
        #     matrix[i][o] = matrix[i][o]/mag if mag else matrix[i][o]
    # np.seterr(divide='ignore', invalid='ignore')
    # for i in range(len(matrix)):
    #     # print("THIS ROW IS: " +
    #     #       str(matrix[i]) + "\nIt's strength: " + str(np.linalg.norm(matrix[i])) + "\n")
    #     # matrix[i] = [float(val) for val in matrix[i]]
    #     matrix[i] = preprocessing.normalize(matrix[i], norm='l1')

    #     print(sum(matrix[i]))

    matrix = preprocessing.normalize(matrix, norm='l1')

    for i in range(len(matrix)):
        su = sum(matrix[i])
        if su != 1:
            matrix[i][len(list(rang))-1] += 1-su
            if sum(matrix[i]) != 1:
                matrix[i][len(list(rang))-1] += 1-sum(matrix[i])

    # for firstlet in matrix:
    # let_sum = 0
    # for num in firstlet:
    #     let_sum += num
    # for i in range(len(firstlet)):
    #     firstlet[i] = firstlet[i]/let_sum if let_sum else firstlet[i]

    # print(matrix)
    return matrix


if __name__ == '__main__':
    print(fill_matrix("james as"))
