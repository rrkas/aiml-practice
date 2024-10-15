class AbstractAction:
    pass

    def __str__(self):
        return f"<{self.__class__.__name__} {hash(self)}>"
