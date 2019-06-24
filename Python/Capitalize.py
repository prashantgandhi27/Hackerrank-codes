#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    mylist = []
    sec_list = []
    string_1 = ''
    string_2 = ''
    count = 0
    for i in s:
        mylist.append(i)

    list_len = len(mylist)

    for x in mylist:
        if (count != list_len):
            if (x != ' '):
                string_1 = string_1 + x
                count = count + 1
            else:
                sec_list.append(string_1)
                string_1 = ''
        else:
            break
    sec_list.append(string_1)

    for items in sec_list:
        string_2 = string_2 + items.capitalize() + ' '

    return string_2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
