import sys
import argparse


def print_matrix(matrix):
    for arr in matrix:
        a = ' '.join([str(x) for x in arr[:-1]]) + ' | ' + str(arr[-1])
        print(a)
    print('-' * len(matrix[0]))


def main(args):
    if args.infile is None or args.outfile is None:
        print('No files specified')
        return
    with open(args.infile) as file:
        lines = file.readlines()
    n = int(lines[0])
    equations = []
    for i in range(1, n + 1):
        equations.append([float(x) for x in lines[i].split(' ')])
    print_matrix(equations)
    for r in range(0, n - 1):
        p = equations[r][r]
        for c in range(r + 1, n):
            f = equations[c][r] / p * -1
            for i in range(r, n + 1):
                equations[c][i] = equations[c][i] + equations[r][i] * f
    print_matrix(equations)
    for r in range(n - 1, 0, -1):
        p = equations[r][r]
        for c in range(r - 1, -1, -1):
            f = equations[c][r] / p * -1
            for i in range(n, r - 1, -1):
                equations[c][i] = equations[c][i] + equations[r][i] * f
    print_matrix(equations)
    sol = []
    for i in range(0, n):
        sol.append(equations[i][n]/equations[i][i])
    print(sol)
    with open(args.outfile, 'w') as file:
        file.writelines('\n'.join([str(x) for x in sol]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Linear equation solver')
    parser.add_argument('--infile')
    parser.add_argument('--outfile')
    parsed = parser.parse_args()
    main(parsed)
