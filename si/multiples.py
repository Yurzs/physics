from .core import SiUnits
import sys

class Multiple:
    _multiplier = 0
    name = ''

    def __init__(self, value):
        assert isinstance(value, int) or isinstance(value, float)
        self.value = value


class Deca(Multiple):
    name = 'da'
    _multiplier = 10 ** 1


class Hecto(Multiple):
    name = 'h'
    _multiplier = 10 ** 2


class Kilo(Multiple):
    name = 'k'
    _multiplier = 10 ** 3


class Mega(Multiple):
    name = 'M'
    _multiplier = 10 ** 6


class Giga(Multiple):
    name = 'G'
    _multiplier = 10 ** 9


class Tera(Multiple):
    name = 'T'
    _multiplier = 10 ** 12


class Peta(Multiple):
    name = 'P'
    _multiplier = 10 ** 15


class Exa(Multiple):
    name = 'E'
    _multiplier = 10 ** 18


class Zetta(Multiple):
    name = 'Z'
    _multiplier = 10 ** 21


class Yotta(Multiple):
    name = 'Y'
    _multiplier = 10 ** 24


_this_module = sys.modules[__name__]

for unit in SiUnits.__subclasses__():
    for fract in Multiple.__subclasses__():
        d = dict(unit.__dict__)
        # if not hasattr(unit, '_multiplier'):
        #     d
        d['base_class'] = unit
        d.update(fract.__dict__)
        d['name'] = f'{fract.name}{unit.name}'
        new_class = type(f'{fract.__name__}{unit.__name__}', (unit, fract), d)
        setattr(_this_module, f'{fract.__name__}{unit.__name__}', new_class)
