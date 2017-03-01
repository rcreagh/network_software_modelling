#! /usr/bin/python
"""This script is for creating a class PriorityQueue for the use in Dijkstra's
single and bidirectional algorithms, making use of the heapq library."""

import itertools
from heapq import heapify, heappush, heappop

class PriorityQueue:
    """Priority queue implementation based on standard library heapq module.
    Also iterable, printable, len-able and allowing to view the lowest priority 
    node."""

    def __init__(self, tasks_prios=None):
        self.pq = []
        self.entry_finder = {} # mapping of tasks to entries
        self.counter = itertools.count() # unique sequence count
        if tasks_prios:
            for task, prio in tasks_prios:
                self.add_task(task, prio)

    def __iter__(self):
        return ((task, prio) for (prio, count, task) in self.pq)

    def __len__(self):
        return len(list(self.__iter__()))

    def __str__(self):
        return str(list(self.__iter__()))

    def add_task(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            del self.entry_finder[task]
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            return task, priority
        raise KeyError('pop from an empty priority queue')

    def lowest_priority(self):
        priority, count, task = min(self.pq)
        return task, priority
