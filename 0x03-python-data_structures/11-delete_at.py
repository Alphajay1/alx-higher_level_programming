#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        new_list = [val for i, val in enumerate(my_list) if i != idx]

        return(new_list)

    else:
        return (my_list)
