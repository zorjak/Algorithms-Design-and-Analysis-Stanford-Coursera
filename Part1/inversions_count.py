#!/usr/bin/env python3.4
# -*- coding: utf8 -*-

#!/tools/bin/python
# -*- coding: utf8 -*-

'''
Algorithms: Design and Analysis Coursera Stanford, Part I.
Programming Assignment 1:
Sorting an array and counting inversions
test

@author: Zoran Jaksic
'''

import sys

def sort_and_count_inversions(inp_lst, start, end):
    """ sort array and count inversions by using merge sort """
    if start == end:
        return 0
    else:
        part_1_inv = sort_and_count_inversions(inp_lst, start, (end+start)//2)
        part_2_inv = sort_and_count_inversions(inp_lst, (end+start)//2+1, end)
        merged_inv = _merge_and_count_inversions(inp_lst, start, (end+start)//2+1, end)
        return part_1_inv + part_2_inv + merged_inv

def _merge_and_count_inversions(lst, start, midle, end):
    """ merging two arrays and counting inversions"""
    i = start
    j = midle
    sorted_lst = []

    inv_count = 0

    while i < midle or j <= end:
        if i == midle:
            sorted_lst.append(lst[j])
            j += 1
        elif j > end:
            sorted_lst.append(lst[i])
            i += 1
        elif lst[i] <= lst[j]:
            sorted_lst.append(lst[i])
            i += 1
        else:
            inv_count += (midle-i)
            sorted_lst.append(lst[j])
            j += 1

    i = start
    while i <= end:
        lst[i] = sorted_lst[i-start]
        i += 1

    return inv_count

def main(int_lst_file_name):
    """ main function that reads an input file and creates a list of integers
        and calculates number of inversions """

    inp_file_h = open(int_lst_file_name, 'r')
    inp_lst = []
    line = inp_file_h.readline()
    while line != '':
        inp_lst.append(int(line))
        line = inp_file_h.readline()

    print('Inversions Number: ' + str(sort_and_count_inversions(inp_lst, 0, len(inp_lst)-1)))


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit(0)

    main(sys.argv[1])
    print('Finished')
