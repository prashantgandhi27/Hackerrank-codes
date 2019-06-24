def count_substring(string, sub_string):
    string_list = list(string)
    substr_list = list(sub_string)
    string_lenght = len(string)
    substr_lenght = len(substr_list)
    count_0 = 0
    count_1 = 0
    for x in range((string_lenght - substr_lenght) + 1):
        for y in range(substr_lenght):
            if (string_list[x + y] == substr_list[y]):
                count_0 = count_0 + 1
            else:
                count_0 = 0
                break
        if (count_0 == substr_lenght):
            count_0 = 0
            count_1 = count_1 + 1
    return count_1


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)