from abc import abstractmethod, ABC


class Token(ABC):
    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def __str__(self) -> str:
        pass

