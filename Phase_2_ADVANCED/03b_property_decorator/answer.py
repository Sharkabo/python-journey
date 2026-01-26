# Complete your task here (goals list refer to task.md)

# Goal 1: Create a Temperature Class with @property
class Temperature:
    def __init__(self, celsius) -> None:
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float) -> None:
        try:
            val = float(value)
            if val < -273.15:
                raise ValueError('Must be above absolute zero: -273.15°C')
            self._celsius = val
        except ValueError:
            raise ValueError('Temperature must be number and number only')

# Goal 2: Add Fahrenheit Conversion Property
    @property
    def fahrenheit(self) -> float:
        return self.celsius * 9/5 + 32

# Goal 3: Test the Temperature Class

