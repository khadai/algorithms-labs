binary_degrees = []


def read_from_file(file_in):
    line = open(file_in).readline()
    values = line.split()
    return values


def make_binary(decimal):
    return '{0:b}'.format(decimal)


def make_decimal(binary):
    return int(binary, 2)


def make_degrees_list(num, bin_num):
    binary_deg = []
    j = 1
    i = num ** 0
    while i <= make_decimal(bin_num):
        binary_deg.append(make_binary(i))
        i = num ** j
        j += 1
    return binary_deg


if __name__ == '__main__':
    nums = read_from_file('file.in')
    the_num = int(nums[1])
    bin_num_str = nums[0]

    binary_degrees = make_degrees_list(the_num, bin_num_str)

    answer = 0
    binary_number = bin_num_str
    i = len(binary_degrees) - 1

    while i >= 0:
        answr = 0
        j = i
        temp_bin_num = binary_number

        while j >= 0:
            num = binary_degrees[j]
            answr = answr + temp_bin_num.count(num)
            temp_bin_num = temp_bin_num.replace(num, '.')

            j -= 1

        if temp_bin_num.count('0') == 0:
            answer = answr
            break
        else:
            i -= 1
    print(answer)
