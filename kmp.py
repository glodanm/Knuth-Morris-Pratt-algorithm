def read_data(file):
    with open(file, 'r') as input_file:
        data = input_file.readlines()
    return data


def longest_proper_prefix(sub_string, sub_string_length, pi):
    j = 0
    i = 1

    while i < sub_string_length:
        if sub_string[i] == sub_string[j]:
            pi[i] = j + 1 
            j += 1    
            i += 1
        else:
            if j != 0:
                j = pi[j - 1]
            else:
                pi[i] = 0
                i += 1


def kmp_search(sub_string, string):
    sub_string_length = len(sub_string)
    string_length = len(string)
    pi = [0] * sub_string_length
    j = 0
    result_list = []
    longest_proper_prefix(sub_string, sub_string_length, pi)
    i = 0

    while i < string_length:
        if sub_string[j] == string[i]:
            i += 1
            j += 1
        if j == sub_string_length:
            result_list.append(str(i - j) + "-" + str(i - j + sub_string_length - 1))
            j = pi[j - 1]
        elif sub_string[j] != string[i]:
            if j != 0:
                j = pi[j - 1]
            else:
                i += 1
    return result_list


if __name__ == '__main__':
    result = read_data("test_1.txt")
    sub_string = result[1]
    string = result[0]

    print('Result =>', kmp_search(sub_string, string))