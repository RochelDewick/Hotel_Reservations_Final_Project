class Guest:

    def __init__(self, row):
        self.GuestId = row["GuestId"]
        self.adults = row["adults"]
        self.children = row["children"]
        self.babies = row["babies"]
        self.country = row["country"]

    def __str__(self):
        sb = []
        for key in self.__dict__:
            sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))

        return ', '.join(sb)
