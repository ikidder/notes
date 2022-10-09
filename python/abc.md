# abc

```python
from abc import ABC

class MyABC(ABC):
    pass

type(MyABC)
-> abc.ABCMeta
```

```python
from abc import abstractmethod, ABC

class Vehicle(ABC):
    @abstractmethod
    def tire_pressure(self):
        raise NotImplemented()

class Car(Vehicle):
    def __init__(self):
        self.tires = [1, 2, 3, 4]
    def tire_pressure(self):
        return sum(self.tires)/len(self.tires)

car = Car()
car.tire_pressure()
```
