import pickle

from DataBase import DataBase


class DBFile(DataBase):

    def __init__(self):
        super(DBFile, self).__init__()

    def set_value(self, key, val):
        """
        updates the db
        """
        self.update_dict()  # read file
        ret = super().set_value(key, val)  # call super
        if ret is True:
            self.get_dict(self.dict)  # write to file
        return ret

    def get_value(self, key):
        """
        get the value from db
        :return: value of the given key
        """
        self.update_dict()  # read file
        return super().get_value(key)  # call super

    def del_value(self, key):
        """
        deleting the value of the given key
        """
        self.update_dict()  # read file
        super().del_value(key)  # call super
        self.get_dict(self.dict)  # write to file

    def get_dict(self, dict):
        """
        pickle the db
        :param dict: db
        """
        pickling_on = open("pfile.pickle", "wb")
        pickle.dump(dict, pickling_on)
        pickling_on.close()

    def update_dict(self):
        """
        unpickle the db
        """
        open("pfile.pickle", 'rb')


def test():
    """
    testing
    :return:
    """
    database = DBFile()
    database.set_value("omer", "oz")
    print(database.get_value("omer"))
    database.del_value("omer")
    print(database.get_value("omer"))


def main():
    test()


if __name__ == '__main__':
    main()

"""
 database = DBFile()
    database.set_value("omer", "oz")
    print(database.get_value("omer"))
    database.del_value("omer")
    print(database.get_value("omer"))"""
