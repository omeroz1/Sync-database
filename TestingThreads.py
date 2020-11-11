import logging
import threading
import time
from threading import Thread
from DBsync import DBSync
from DBfile import DBFile

output = 0
READER_THREADS = 20
WRITER_THREADS = 3
THREAD_LOOP = 10

database = DBFile()  # creates a db file
database.set_value(1, "omer")
database.set_value(2, "oz")
database.set_value(3, "even")
database.set_value(4, "yehuda")
sync_db = DBSync(database, True)  # the True indicates it should handle the Threads


class Thread(threading.Thread):
    """
    creates a new thread.
    the thread's name is the given name
    the thread's target is the given function
    """
    def __init__(self, func, name):
        threading.Thread.__init__(self, target=func, name=name)
        self.start()


def read_from_db():
    """
    reads from the database. leave a message to the console when done
    """
    val = sync_db.get_value(2)
    logging.getLogger().setLevel(logging.INFO)
    logging.info('the given value is ' + val)


def write_to_db():
    """
    updates the database. leave a message to the console when done
    """
    global output
    output += 1
    sync_db.set_value(2, str(output))
    logging.getLogger().setLevel(logging.INFO)
    logging.info('written successfully')


def main():
    rthreads = []
    wthreads = []
    for i in range(0, READER_THREADS):
        if i % 8 == 0:
            thread = Thread(write_to_db, str(i))
            wthreads.append(thread)
            for thread in wthreads:
                thread.join()
        thread = Thread(read_from_db, str(i))
        rthreads.append(thread)
    for thread in rthreads:
        thread.join()

    time.sleep(3)
    print(sync_db.get_value(1))


if __name__ == "__main__":
    main()
