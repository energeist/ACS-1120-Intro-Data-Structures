import sys
import random


def rearrange_words():
    rearranged_string = ""
    arg_list = sys.argv.copy()
    arg_list.pop(0)
    random.shuffle(arg_list)
    for i in range(len(arg_list)):
        rearranged_string += arg_list[i]
        if i < len(arg_list) - 1:
            rearranged_string += " "
    return rearranged_string

if __name__ == "__main__":
    print(rearrange_words())