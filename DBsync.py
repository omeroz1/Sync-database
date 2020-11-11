import logging
import multiprocessing
import threading


class DBSync(object):
    NUM_OF_THREADS = 10

    def __init__(self, db, thread_mode):
        """
        creates a sync db
        :param db: the info of the db
        :param thread_mode: indicates if it should handle the thread or process
        """
        if thread_mode:
            self.lock = threading.Lock()
            self.read_semaphore = threading.Semaphore(self.NUM_OF_THREADS)
        else:
            self.lock = multiprocessing.Lock()
            self.read_semaphore = multiprocessing.Semaphore(self.NUM_OF_THREADS)
        self.db = db

    def lock_read(self):
        """
        lock when reading
        :return: a message that it locked successfully
        """
        logging.debug('trying to read')
        self.read_semaphore.acquire()
        logging.debug('locked successfully')

    def release_read(self):
        """
        release lock when reading
        :return: a message that it released successfully
        """
        self.read_semaphore.release()
        logging.debug('released successfully')

    def lock_write(self):
        """
        lock when writing
        :return: a message that it locked successfully
        """
        logging.debug('trying to write')
        self.lock.acquire()
        for i in range(0, self.NUM_OF_THREADS):
            self.lock_read()
        logging.debug('locked successfully')

    def release_write(self):
        """
        release lock when writing
        :return: a message that it released successfully
        """
        for i in range(0, self.NUM_OF_THREADS):
            self.release_read()
        self.lock.release()
        logging.debug('released')

    def get_value(self, key):
        """
        gets the value
        :return: the value of the given key
        """
        self.lock_read()
        value = self.db.get_value(key)
        self.release_read()
        return value

    def set_value(self, key, val):
        """
        updates the db
        """
        self.lock_write()
        value = self.db.set_value(key, val)
        self.release_write()
        return value

    def del_value(self, key):
        """
        deleting the db
        """
        self.lock_write()
        value = self.db.del_value(key)
        self.release_write()
        return value


def main():
    pass


if __name__ == "__main__":
    main()
