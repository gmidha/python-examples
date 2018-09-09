#!/usr/bin/env python3

""" This program demonsrates the usage of Queues using queue module.  We are going to use get and put method.
"""

import queue

def create_queue():
    q = queue.Queue()
    if q.empty():
        print("Q is empty")
    q.put('bag1')
    q.put('bag2')
    q.put('bag3')
    q.put('bag4')
    print("Items have been added in Q")
    if not q.empty():
        print("Q has items")
    print(q.get(False)) # We are using False in get method to make sure that it throw exception if we are doing get on an empty queue.
    print(q.get(False))
    print(q.get(False))
    print(q.get(False))

if __name__ == '__main__':
    create_queue()
