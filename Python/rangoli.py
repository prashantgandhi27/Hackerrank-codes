def print_rangoli(size):
    # your code goes here
    if size == 1:
        print('a')
    else:
        count = size-1
        count_reverse = 1
        mylist = []
        right_range = 97 + size
        for items in range(97,right_range):
            mylist.append(chr(items))
        len_list = len(mylist)
        temp = len_list - 1
        temp_sec = len_list - 1
        temp_sec_reserse = len_list - 1
        sum = len_list + temp
        for i in range(sum,size-1,-1):
            output_list = []
            output_list_1 = []
            for j in range(size):
                if (j == count):
                    temp_sec  = temp
                    for x in range(count,size):
                        output_list.append(mylist[temp_sec])
                        temp_sec = temp_sec - 1
                    break
                else:
                    output_list.append('-')
            for q in output_list:
                output_list_1.append(q)
            output_list_1.reverse()
            output_list_1 = "-".join(output_list_1[1:])
            output_list = "-".join(output_list)
            print(output_list + '-' + output_list_1)
            count = count - 1
        for a in range(sum,size,-1):
            output_list_2 = []
            output_list_3 = []
            for j in range(size):
                if (j == count_reverse):
                    temp_sec_reserse  = temp
                    for x in range(count_reverse,size):
                        output_list_2.append(mylist[temp_sec_reserse])
                        temp_sec_reserse = temp_sec_reserse - 1
                    break
                else:
                    output_list_2.append('-')
            for q in output_list_2:
                output_list_3.append(q)
            output_list_3.reverse()
            output_list_3 = "-".join(output_list_3[1:])
            output_list_2 = "-".join(output_list_2)
            print(output_list_2 + '-' + output_list_3)
            count_reverse = count_reverse + 1



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)