class Temperature:
    def __init__(self, value, unit="C"):
        self._value = float(value)
        if not isinstance(unit, str):
            raise ValueError("Unit must be string")
        self._unit = unit.upper()
        self.legalunits = ("C", "F", "K")
        self.islegalunit()
        self.subzero()
            
        
    def to_celsius(self) -> float:
        if self._unit == "K":
            return self._value - 273.15
            
        elif self._unit == "F":
            return (self._value - 32) * (5/9)
        
        return self._value
        
    def to_fahrenheit(self) -> float:
        if self._unit == "C":
            return self._value * (9/5) + 32
        if self._unit == "K":
            return (self._value-273.15) * (9/5) + 32
        
        return self._value

    def to_kelvin(self) -> float:
        if self._unit == "C":
            return self._value + 273.15
        elif self._unit == "F":
            return (self._value - 32) * (5/9) + 273.15
        
        return self._value

    def convert_to(self, target_unit: str) -> "Temperature":
        if not isinstance(target_unit, str) or target_unit.upper() not in self.legalunits:
            raise ValueError("The target unit given is not allowed")
        target = target_unit.upper()

        if target == "C":
            return Temperature(self.to_celsius(),"C")
        elif target =="K":
            return Temperature(self.to_kelvin(),"K")
        return Temperature(self.to_fahrenheit(),"F")

    def __repr__(self) -> str:
        return f"Temperature({self._value}, '{self._unit}')"

    def  __str__(self) -> str:
        return f"{self._value:.2f} °{self._unit}"
        
    
    def subzero(self):
        if self.to_kelvin() < -1e-9:
            raise ValueError("Temperatures under zero kelvin is not valid")
        else:
            pass
    
    def islegalunit(self):
        
        if self.unit in self.legalunits:
            pass
        else:
            raise ValueError("The unit given is not allowed")
    @property
    def unit(self):
        return self._unit
    @property
    def value(self):
        return self._value
    
    def __eq__(self,other)->bool: #Equal
        if not isinstance(other, Temperature):
            return NotImplemented
        return abs(self.to_kelvin() - other.to_kelvin()) < 1e-9
    def __ne__(self,other)->bool: #Not equal
        if not isinstance(other, Temperature):
            return NotImplemented
        return not (self == other)
    def __lt__(self,other)->bool: #Less than
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self.to_kelvin() < other.to_kelvin() - 1e-9)
    def __le__(self,other)->bool: #Less or equal
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self.to_kelvin() <= other.to_kelvin()+1e-9)
    def __gt__(self,other)->bool: #Greater than
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self.to_kelvin() > other.to_kelvin() + 1e-9)
    def __ge__(self,other)->bool: #Greater or equal
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self.to_kelvin()>=other.to_kelvin()-1e-9)