def read_graph(file_in):
    pupil = []
    matrix = []
    with open(file_in) as f:
        pupil.extend(f.readline().split())
    for char in pupil:
        matrix.append([ch for ch in char])

    length = len(matrix)
    num_of_friends = []

    for i in range(0, length):
        num = set()
        for j in range(0, length):
            if matrix[i][j] == 'Y':
                num.add(j)
                for row in range(0, length):
                    if matrix[row][j] == 'Y':
                        num.add(row)
                num.remove(i)
        num_of_friends.append(num.__len__())
    print(num_of_friends)
    return max(num_of_friends)


if __name__ == '__main__':
    print(read_graph('file.in'))
