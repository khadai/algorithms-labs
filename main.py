import time
from videogame import VideoGame


def bubble_sort(array):  # by_rate_by_descending
    compares = 0
    swaps = 0
    arr = array
    length = len(arr)
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(length - 1):
            if arr[i + 1].imbd_rate > arr[i].imbd_rate:
                is_sorted = False
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                swaps += 1
            compares += 1

    print("COMPARED " + str(compares) + " TIMES," + "SWAPPED " + str(swaps) + ' TIMES')
    return arr


merge_compare = 0
merge_swap = 0


def inc_compare():
    global merge_compare
    merge_compare += 1


def inc_swaps():
    global merge_swap
    merge_swap += 1


def print_globals():
    print("COMPARED " + str(merge_compare) + " TIMES," + "SWAPPED " + str(merge_swap) + ' TIMES')


def merge_sort(array):  # by_heroes_by_ascending
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

        if left[l_idx].quantity_of_heroes < right[r_idx].quantity_of_heroes:
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


def print_list(game_list):
    for i in game_list:
        print(i)


if __name__ == '__main__':
    video_games_list = []

    for line in open('video games.txt'):
        values = line.split(',')
        video_game = VideoGame(values[0], int(values[1]), float(values[2]))
        video_games_list.append(video_game)

    print("BUBBLE SORT")  # by_rate_by_descending
    start_time = time.process_time()
    print_list(bubble_sort(video_games_list))
    print("TIME: " + str(time.process_time() - start_time))

    print("\nMERGE SORT")  # by_heroes_by_ascending
    start_time = time.time()
    print_list(merge_sort(video_games_list))
    print("TIME: " + str(time.time() - start_time))
    print_globals()
