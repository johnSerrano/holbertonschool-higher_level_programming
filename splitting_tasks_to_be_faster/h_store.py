import time
import random
from threading import Lock

class Store:
    def __init__(self, item_number, person_capacity):
        self.items_remaining_lock = Lock()
        self.space_available_lock = Lock()
        self.item_number = item_number
        self.person_capacity = person_capacity
        self.items_remaining = self.item_number
        self.space_available = self.person_capacity

    def enter(self):
        while True:
            self.space_available_lock.acquire()
            if self.space_available > 0:
                self.space_available -= 1
                self.space_available_lock.release()
                break
            self.space_available_lock.release()

    def buy(self):
        self.items_remaining_lock.acquire()
        if self.items_remaining <= 0:
            return False
        self.items_remaining_lock.release()
        time.sleep(random.randint(5, 10))
        self.items_remaining_lock.acquire()
        if self.items_remaining <= 0:
            return False
        self.items_remaining -= 1
        self.items_remaining_lock.release()
        self.space_available_lock.acquire()
        self.space_available += 1
        self.space_available_lock.release()
        return True

if __name__ == '__main__':
    import thread
    import datetime
    from h_store import Store

    my_store = Store(10, 3)

    def emulate_people(idx):
        my_store.enter()
        print "%d is in at %s!" % (idx, datetime.datetime.now().strftime("%M:%S"))
        if my_store.buy():
            print "%d has one item at %s!" % (idx, datetime.datetime.now().strftime("%M:%S"))
        else:
            print "No more item for %d at %s" % (idx, datetime.datetime.now().strftime("%M:%S"))

    for idx_people in range(0, 15):
        thread.start_new_thread( emulate_people, (idx_people, ) )

    while True:
        pass
