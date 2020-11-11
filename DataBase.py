class DataBase(object):

    def __init__(self):
        self.dict = {}

    def set_value(self, key, val):
        """
        updates the db
        """
        if key in self.dict:
            self.dict[key] = val
            return True
        self.dict[key] = val
        return None

    def get_value(self, key):
        """
        get the value from db
        :return: value of the given key
        """
        return self.dict.get(key)

    def del_value(self, key):
        """
        deleting the value of the given key
        """
        return self.dict.pop(key, None)


def main():
    pass


if __name__ == '__main__':
    main()
