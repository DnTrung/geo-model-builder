from abc import ABC, abstractmethod
import collections
import numbers

from util import FuncInfo

class Point(collections.namedtuple("Point", ["val"])):
    def __str__(self):
        if isinstance(self.val, str):
            return self.val
        else:
            return f"({self.val[0]} {' '.join([str(v) for v in self.val[1]])})"

class Num(collections.namedtuple("Num", ["val"])):
    def __str__(self):
        if isinstance(self.val, numbers.Number):
            return str(self.val)
        else:
            return f"({self.val[0]} {' '.join([str(v) for v in self.val[1]])})"


class Cline(ABC):
    def __init__(self, val):
        self.val = val
        super().__init__()

    '''
    @abstractmethod
    def pointsOn(self):
        pass
    '''

    @abstractmethod
    def __str__(self):
        pass


class Circle(Cline):
    '''
    def pointsOn(self):
        if self.pred == "coa":
            return [self.points[1]]
        elif self.pred == "c3":
            return self.points
        elif self.pred == "cong":
            return list()
        elif self.pred == "diam":
            return self.points
        else:
            raise RuntimeError("[Circle.pointsOn] Invalid circle pred")
    '''

    def __str__(self):
        if isinstance(self.val, str):
            return self.val
        elif isinstance(self.val, FuncInfo):
            pred, args = self.val
            return f"({pred} {' '.join([str(a) for a in args])})"
        else:
            raise RuntimeError("Invalid circle")

class Line(Cline):
    '''
    def pointsOn(self):
        if self.pred == "connecting":
            return self.points
        elif self.pred == "paraAt":
            return [self.points[0]]
        elif self.pred == "perpAt":
            return [self.points[0]]
        elif self.pred == "mediator":
            return list()
        elif self.pred == "iBisector":
            return [self.points[1]]
        elif self.pred == "eBisector":
            return [self.points[1]]
        elif self.pred == "eqOAngle":
            return [self.points[0]]
        else:
            raise RuntimeError("[Line.pointsOn] Invalid line pred")
    '''

    def __str__(self):
        if isinstance(self.val, str):
            return self.val
        elif isinstance(self.val, FuncInfo):
            pred, args = self.val
            return f"({pred} {' '.join([str(a) for a in args])})"
        else:
            raise RuntimeError("Invalid line")
