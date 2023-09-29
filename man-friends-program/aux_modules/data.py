import datetime


class Data:
    def __init__(self, data: list):
        self.creation_date = datetime.datetime.today()
        self.__data = data

    def __str__(self):
        return " ".join([str(i) for i in self.__data])

    def append(self, item):
        self.__data.append(item)

    def __iter__(self):
        for i in self.__data:
            yield i

    def __getitem__(self, index: int):
        return self.__data[index]

    def __len__(self):
        return len(self.__data)

    def get_by_param(self, param_name: str, param_value: any):
        for i in self.__data:
            if str(getattr(i, param_name)) == str(param_value):
                return i

    def remove(self, item):
        self.__data.remove(item)