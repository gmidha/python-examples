#!/usr/bin/env python3

""" This script creates a Queue of fixed size length.
"""

import queue

def create_q():
    q = queue.Queue(maxsize=2) # creating a queue of length = 2.
    q.put('bag1')
    q.put('bag2')  # we can also use q.put_nowait('bag2'), this will throw error is Q is full
    if q.full():
        print("Q is full now")
    print(q.get())
    print(q.get())

if __name__ == "__main__":
    create_q()
