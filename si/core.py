from .converter import Converter


class SiUnits:
    _multiplier = 1

    def __init__(self, value):
        self.value = value

    def converter(self):
        return Converter(self)


class SiBase:
    name = None

    def __repr__(self):
        return f'{self.value}[{self.name}]'


class Weight(SiBase):
    name = None


class Length(SiBase):
    name = None


class Time(SiBase):
    name = None


class CurrentStrength(SiBase):
    name = None


class ThermodynamicTemperature(SiBase):
    name = None


class LuminousIntensity(SiBase):
    name = None


class AmountOfSubstance(SiBase):
    name = None


class Meter(Length, SiUnits):
    name = 'm'


class Gram(Weight, SiUnits):
    name = 'g'


class Second(Time, SiUnits):
    name = 's'


class Ampere(CurrentStrength, SiUnits):
    name = 'A'


class Kelvin(ThermodynamicTemperature, SiUnits):
    name = 'K'


class Candela(LuminousIntensity, SiUnits):
    name = 'cd'


class Mole(AmountOfSubstance, SiUnits):
    name = 'mol'
