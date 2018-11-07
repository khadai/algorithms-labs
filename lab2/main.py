merge_compare = 0
merge_swap = 0


def inc_compare():
    global merge_compare
    merge_compare += 1


def inc_swaps():
    global merge_swap
    merge_swap += 1


def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return array
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
    inc_compare()
    return merge(left, right)


def merge(left, right):
    new_array = []
    l_idx = r_idx = 0
    while l_idx < len(left) and r_idx < len(right):

        if left[l_idx] < right[r_idx]:
            new_array.append(left[l_idx])
            l_idx += 1
            inc_compare()
            inc_swaps()
        else:
            new_array.append(right[r_idx])
            r_idx += 1
            inc_swaps()
    inc_compare()
    inc_compare()
    new_array.extend(left[l_idx:])
    new_array.extend(right[r_idx:])
    return new_array


def readfile():
    num_file = open('numbers.txt')
    nums = num_file.readline().split(',')
    nums = map(int, nums)
    return nums


def binary_search(m_list, key, start):
    start_idx = start
    end_idx = int(m_list.__len__() - 1)

    while start_idx <= end_idx:
        middle = start_idx + (end_idx - start_idx) // 2

        if m_list[middle] == key:
            return middle
        elif m_list[end_idx] == key:
            return end_idx
        elif m_list[start_idx] == key:
            return start_idx

        if m_list[middle] > key:
            end_idx = middle - 1
        else:
            start_idx = middle + 1

    return -1


def cut_off_bigger(array, key):
    end_idx = array.__len__() - 1
    merge_sort(array)
    i = end_idx
    while i > 0:
        if array[i] > key:
            array.remove(array[i])
        else:
            break
        i -= 1
    return array


def find_terms(array, key):
    start_idx = 0
    end_idx = array.__len__() - 1
    for i in range(start_idx, end_idx):
        for j in range(i + 1, end_idx):
            third = binary_search(array, key - array[i] - array[j], j + 1)
            if third != -1:
                return str(array[i]) + ' ' + str(array[j]) + ' ' + str(
                    array[third])
            else:
                continue


if __name__ == '__main__':
    NUM = input(' -- Andriy, if u love me find if there is terms of the number - ')
    numbers = readfile()
    numbers = merge_sort(numbers)
    numbers = cut_off_bigger(numbers, NUM)
    print numbers
    nums = find_terms(numbers, NUM)
    if nums:
        print(' -- Ilona, these three numbers as you, me, and our love - addicted to your choice: ' + str(nums))
    else:
        print(' -- I didn\'t find them, but I still love you, Ilona, so let\'s learn Hibernate tonight ' + unichr(9829))
