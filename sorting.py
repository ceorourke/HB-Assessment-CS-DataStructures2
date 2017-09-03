#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    # loop through range of list, subtract 1 because range starts at 1
    for i in range(len(lst) - 1):
        # keep track of whether you swapped, initialize to False at first
        made_swap = False
        # loop through list but don't waste time on the last number on the 2nd
        # time through because you know it's sorted. 3rd time through don't check
        # the last 2 numbers because you know they're sorted, etc.
        for j in range(len(lst) - 1 - i):
            # check equality of current num and next num
            if lst[j] > lst[j + 1]:
                # swap numbers if applicable
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                # note that you swapped
                made_swap = True
        # if you didn't swap the numbers, break
        if not made_swap:
            break

    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """
    # make a container for the sorted list
    result_list = []
    # if items left in both lists, compare first items of each list
    while len(list1) > 0 or len(list2) > 0:
        # check if list1 is empty, add end of list2
        if list1 == []:
            result_list.append(list2.pop(0))
        # check if list2 is empty, add end of list1
        elif list2 == []:
            result_list.append(list1.pop(0))
        # check if 1st item in list1 is smaller than 1st item in list2
        elif list1[0] < list2[0]:
            # append and remove first item of list1
            result_list.append(list1.pop(0))
        # otherwise you know it's bigger...
        else:
            # append and remove first item of list2
            result_list.append(list2.pop(0))

    return result_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    # if length of lst is 1, return lst (because a list of 1 is sorted)
    if len(lst) < 2:
        return lst

    # find the halfway point
    mid = int(len(lst) / 2)
    # use list slicing to cut the list at the halfway point
    # use recursion to keep chopping it in half
    lst1 = merge_sort(lst[:mid])
    # use list slicing to store the other half
    # use recursion to keep chopping it in half
    lst2 = merge_sort(lst[mid:])

    # call the other function to put the lists back together, sorted
    return merge_lists(lst1, lst2)




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
