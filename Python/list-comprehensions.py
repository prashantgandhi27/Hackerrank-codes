    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    mylist = []
    for x_items in range(x+1):
        for y_items in range(y+1):
            for z_items in range(z+1):
                if (x_items + y_items + z_items) != n:
                    out_list = [x_items,y_items,z_items]
                    mylist.append(out_list)
                else:
                    continue
    print(mylist)
