#!/usr/bin/env python3.4
# -*- coding: utf8 -*-

#!/tools/bin/python
# -*- coding: utf8 -*-

"""
Algorithms: Design and Analysis Coursera Stanford, Part I.
Programming Assignment 2:
Sorting and array with quick_sort algorithm and counting the number
of comparisons when different array element is used as a pivot

@author: Zoran Jaksic
"""
import sys

def swap(lst, i, j):
    """ swap two elements of a lst """
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

def _median3(lst, i, j, k):
    """ returns the index of the median element of 3 elements of a list
    """
    if (lst[i] <= lst[j] and lst[j] <= lst[k]) or\
       (lst[k] <= lst[j] and lst[j] <= lst[i]):
        return j
    elif (lst[j] <= lst[i] and lst[i] <= lst[k]) or\
         (lst[k] <= lst[i] and lst[i] <= lst[j]):
        return i
    else:
        return k

def _quick_sort_and_count_compare(lst, start, end, pivot_mode):
    """ quick_sort algorithm and counting comparisons """

    if start >= end:
        return 0

    if pivot_mode == "PIVOT_FIRST":
        pivot = lst[start]
        pivot_id = start
    elif pivot_mode == "PIVOT_LAST":
        pivot = lst[end]
        pivot_id = end
    elif pivot_mode == "PIVOT_MEDIAN":
        midle = start + ((end-start) >> 1)
        pivot_id = _median3(lst, start, midle, end)
        pivot = lst[pivot_id]

    swap(lst, start, pivot_id)

    # partitioning the list
    i = start+1
    for j in range(start+1, end+1):
        if lst[j] < pivot:
            swap(lst, i, j)
            i += 1
    swap(lst, start, i-1)

    compare_num_first_half = _quick_sort_and_count_compare(lst, start, i-2, pivot_mode)
    compare_num_second_half = _quick_sort_and_count_compare(lst, i, end, pivot_mode)

    return end - start + compare_num_first_half + compare_num_second_half

def quick_sort_and_count_compare(lst, pivot_mode):
    """
    Sorts the array with quck_sort algorithm
    Pivot is chosen as:
    PIVOT_FIRST - the first element;
    PIVOT_LAST - the last element
    PIVOT_MEDIAN - median of first medium and last element
    """
    return _quick_sort_and_count_compare(lst, 0, len(lst)-1, pivot_mode)

def main(int_lst_file_name):
    """ main function that reads an input file and creates a list of integers
        and calculates the number of comparisons """

    inp_file_h = open(int_lst_file_name, 'r')
    inp_lst = []
    line = inp_file_h.readline()
    while line != '':
        inp_lst.append(int(line))
        line = inp_file_h.readline()

    inp_lst_tmp = inp_lst[:]
    print(quick_sort_and_count_compare(inp_lst_tmp, "PIVOT_FIRST"))
    inp_lst_tmp = inp_lst[:]
    print(quick_sort_and_count_compare(inp_lst_tmp, "PIVOT_LAST"))
    inp_lst_tmp = inp_lst[:]
    print(quick_sort_and_count_compare(inp_lst_tmp, "PIVOT_MEDIAN"))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(0)

    main(sys.argv[1])
    print('Finished')
