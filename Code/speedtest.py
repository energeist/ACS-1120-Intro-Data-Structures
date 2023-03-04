from linkedlist import LinkedList
from hashtable import HashTable
import sys
import timeit
import random

"""testing append methods for linked list and hashtable"""
def create_linked_list(iterations):
    linked_list = LinkedList()
    for _ in range(iterations):
        linked_list.append(_)
    print(sys.getsizeof(linked_list))
    # print('head: {}'.format(linked_list.head))
    # print('tail: {}'.format(linked_list.tail))
    return linked_list

def create_hashtable():
    iterations = 10
    return hashtable


def test_ll_creation(length):
    print(f"Testing average creation time of LL with {length} items:")
    start = timeit.default_timer()
    for _ in range(1000):
        create_linked_list(length)
    end = timeit.default_timer()
    return f"Time to run {(end - start)/1000} seconds per iteration on average\n"

def test_ll_find(linked_list, length):
    print(f"Testing average seek time in LL with {length} items:")
    start = timeit.default_timer()
    for _ in range (1000):
        item = random.randint(0, length)
        linked_list.find(item)
    end = timeit.default_timer()
    return f"Time to run {(end - start)/1000} seconds per iteration on average\n"

"""Test creation times of linked lists of varying lengths"""
print(test_ll_creation(100))
print(test_ll_creation(1000))

"""Test seek times of linked lists of varying lengths"""
length = 100
ll = create_linked_list(length)
print(test_ll_find(ll, length))

length = 10000
ll = create_linked_list(length)
print(test_ll_find(ll, length))

length = 1000000
ll = create_linked_list(length)
print(test_ll_find(ll, length))






