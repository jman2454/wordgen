import generator
import data_gen
import consts
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--num_strings', required=False)
parser.add_argument('--dataset', required=False)
parser.add_argument('--test', action='store_true')

args = parser.parse_args()

dataset = args.dataset

if (not dataset is None and type(dataset == str)):
    if args.dataset.find(".txt") > 0:
        dataset = open(args.dataset, 'r')
        dataset = dataset.read()

if args.test:
    dataset = open('wordgen/test.txt', 'r')
    dataset = dataset.read()

matrix = data_gen.fill_matrix(dataset)

generator.generate(matrix, int(args.num_strings))
