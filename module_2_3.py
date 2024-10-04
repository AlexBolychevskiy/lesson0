my_list = [42,69,322,13,0,99,-5,9,8,7-6,5]
zero = 0
while my_list != zero:
    if my_list[0] < zero and my_list[1] < zero and my_list[2] < zero and my_list[3] < zero  and my_list[4] < zero and my_list[5] < zero and my_list[6] < zero or my_list[0:12] == len(my_list):
        print(my_list[0], my_list[1], my_list[2], my_list[3],my_list[4], my_list[5], my_list[6])
        break
    elif my_list[0] > zero and my_list[1] > zero and my_list[2] > zero and my_list[3]> zero or my_list[4] > zero or my_list[5] > zero:
        print(my_list[0], my_list[1], my_list[2], my_list[3],  my_list[5])
        break
