def binary_search(number, lst):
    begin = 0
    end = len(lst) - 1
    while begin <= end:
        index = (begin + end) // 2
        if lst[index] == number:
            return index
        elif lst[index] > number:
            end = index - 1
        else:
            begin = index + 1
    return -1


def main():
    n, *A = map(int, input().split())
    k, *B = map(int, input().split())

    index_list = []

    for b in B:
        index = binary_search(b, A)
        index_list.append(index)

    print(*index_list)


if __name__ == "__main__":
    main()
