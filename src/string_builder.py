from io import StringIO


class StringBuilder:

    def __init__(self, string: str = None) -> None:
        self.buffer = StringIO()
        if string is not None:
            self.add(string)

    def add(self, string: str) -> None:
        self.buffer.write(string)

    def __str__(self) -> str:
        return self.buffer.getvalue()

    def __repr__(self) -> str:
        return self.buffer.getvalue()
