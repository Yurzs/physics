class Weight:

    def __init__(self, value: int):
        assert isinstance(value, int) or isinstance(value, float)
        self.value = value

    def __repr__(self):
        return f'{self.value}[{self._shortname}]'

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.value - other.value)
        elif issubclass(other.__class__, Weight):
            pass
        else:
            return self.__class__(self.value - other)

    def __isub__(self, other):
        if isinstance(other, self.__class__):
            self.value -= other.value
        elif issubclass(other.__class__, Weight):
            pass
        else:
            self.value -= other

    def __int__(self):
        return self.value

    def __truediv__(self, other):
        if issubclass(other.__class__, Weight):
            return self._toGram().value / other._toGram().value
        return self.value / other

    def __floordiv__(self, other):
        if issubclass(other.__class__, Weight):
            return self._toGram().value / other._toGram().value
        return self.value / other

    def __idiv__(self, other):
        if issubclass(other.__class__, Weight):
            self.value /= other.value
        self.value /= other

    def __mul__(self, other):
        return self.value * other


class Gram(Weight):
    """
    Base class for all measurements
    """
    _shortname = 'grams'
    _toGram = lambda x: Gram(x.value)


class Kilogram(Weight):
    _shortname = 'kg'
    _toGram = lambda x: Gram(x.value * 1000)

    @property
    def pound(self):
        return self.value * 2.2046226218488

    @property
    def gram(self):
        return self.value * 1000

    @property
    def ounce(self):
        return self.value * 35.2739619


class Pound(Weight):
    _shortname = 'lbs'
    _toGram = lambda x: Gram(x.value * 453.592)


class Ounce(Weight):
    _shortname = 'ounces'
    _toGram = lambda x: Gram(x.value * 28.35)


class Ton(Weight):
    _shortname = 'ton'
    _toGram = lambda x: Gram(x.value / 1e-6)


class MilliGram(Weight):
    _shortname = 'mg'
    _toGram = lambda x: Gram(x.value / 1000)


class MicroGram(Weight):
    _shortname = 'mcg'
    _toGram = lambda x: Gram(x.value / 1e+6)


class EnglishTon(Weight):
    _toGram = lambda x: Gram(x.value * 1.016e+6)


class AmericanTon(Weight):
    _toGram = lambda x: Gram(x.value * 907184.74)


class Ston(Weight):
    _toGram = lambda x: Gram(x.value * 6350.293)


class Converter:
    def __new__(cls, value, to_typeclass):
        if not issubclass(to_typeclass, Weight):
            raise TypeError(f'{to_typeclass} is unknown weight type')
        elif not issubclass(value.__class__, Weight):
            raise TypeError(f'{value} is unknown weight type')
        else:
            return to_typeclass(value / to_typeclass(1))
