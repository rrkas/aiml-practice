# can be atomic, factored or structured depending on the problem and requirements


class AbstractState:
    def __init__(self, heuristic_value: float):
        self.heuristic_value: float = heuristic_value

    def __str__(self):
        return f"<{self.__class__.__name__} heuristic_value={self.heuristic_value} {hash(self)}>"

    def __repr__(self):
        return str(self)
