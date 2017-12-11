# -*- encoding:utf-8 -*-
# __author__=='Gan'

from collections import namedtuple

Event = namedtuple('Event', 'time proc action')


def taxi_process(ident, trips, start_time=0):
    """Yield to simular issuing event at each state change."""
    time = yield Event(start_time, ident, 'leave garge.')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger.')
        time = yield Event(time, ident, 'drop off passenger.')
    yield Event(time, ident, 'going home.')


import queue


class Simulator(object):
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        """Schedule and display events utill time is up."""
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id * '  ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


def compute_duration(previous_action):
    duration = 1
    if previous_action == 'pick up passenger.':
        duration = 3
    elif previous_action == 'drop off passenger.':
        duration = 5
    return duration


if __name__ == '__main__':
    # taxi = taxi_process(ident=1, trips=2)
    # print(next(taxi))
    # print(taxi.send(7))
    # print(taxi.send(15))
    # print(taxi.send(16))
    # print(taxi.send(23))
    # print(taxi.send(30))
    DEPARTURE_INTERVAL = 2
    num_taxis = 3
    taxis = {
        i: taxi_process(i, (i + 2) * 2, i * DEPARTURE_INTERVAL)
        for i in range(num_taxis)
    }
    sim = Simulator(taxis)
    sim.run(100)