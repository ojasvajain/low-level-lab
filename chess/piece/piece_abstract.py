from abc import ABC, abstractmethod


class PieceAbstract(ABC):
    def __init__(self, color):
        self.color = color
        self.name = None

    @abstractmethod
    def get_path(self, from_pos, to_pos):
        pass

    @staticmethod
    @abstractmethod
    def get_type():
        pass
