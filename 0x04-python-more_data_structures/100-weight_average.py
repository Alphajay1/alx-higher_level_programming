#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)

    return (sum([mul(i[0], i[1]) for i in my_list]) / sum(i[1] for i in my_list))
def mul(i, j):
    return (i * j)
