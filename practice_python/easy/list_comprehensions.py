import itertools as it

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    loop = list(it.product(range(x + 1), range(y + 1), range(z + 1)))
    my_list = [[i, j, k] for i, j, k in loop if i + j + k != n]
    print(my_list)
