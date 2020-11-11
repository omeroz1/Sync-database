import logging
import multiprocessing
import time

from DBfile import DBFile
from DBsync import DBSync

NUM_PROCESSES = 20
output = 0
database = DBFile()  # creates a db
database.set_value(1, "omer")
database.set_value(2, "oz")
database.set_value(3, "even")
database.set_value(4, "yehuda")
sync_db = DBSync(database, False)  # the False indicates it should handle the Processes


def read_from_db():
    """
    reads from the database. leave a message to the console when done
    """
    val = sync_db.get_value(1)
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
    rprocess = []
    wprocess = []
    for i in range(0, NUM_PROCESSES):
        if i % 8 == 0:
            p = multiprocessing.Process(target=write_to_db)
            wprocess.append(p)
            p.start()
        m = multiprocessing.Process(target=read_from_db)
        rprocess.append(m)
        m.start()

    time.sleep(3)
    print(sync_db.get_value(1))


if __name__ == '__main__':
    main()
