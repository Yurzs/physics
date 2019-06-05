


class Gravity:
    G = 6.67 * 10 ** (-11)

    def attraction(self, object1, object2, r):
        return self.G * ((object1.mass * object2.mass) / r**2)

