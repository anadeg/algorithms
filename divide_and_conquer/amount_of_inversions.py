def merge_sort(array, amount_of_inversions):
    current_amount_of_inversions = 0
    if len(array) > 1:
        middle = len(array) // 2
        left_array = array[:middle]
        right_array = array[middle:]

        merge_sort(left_array, amount_of_inversions)
        merge_sort(right_array, amount_of_inversions)

        i = 0
        j = 0
        k = 0

        len_left = len(left_array)
        len_right = len(right_array)

        while i < len_left and j < len_right:
            if left_array[i] <= right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                current_amount_of_inversions += len(left_array) - i
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len_left:
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len_right:
            array[k] = right_array[j]
            j += 1
            k += 1

    amount_of_inversions.append(current_amount_of_inversions)


def main():
    n = int(input())
    A = list(map(int, input().split()))

    lst = []
    merge_sort(A, lst)
    s = 0
    for el in lst:
        s += el
    print(s)


if __name__ == "__main__":
    main()

