from abc import ABC, abstractmethod


class Equation(ABC):
    degree: int
    
    def __init__(self):
        pass
    
    @abstractmethod
    def solve(self):
        pass
        
    @abstractmethod
    def analyze(self):
        pass


class LinearEquation(Equation):
    def solve(self):
        pass

    def analyze(self):
        pass


lin_eq = LinearEquation()