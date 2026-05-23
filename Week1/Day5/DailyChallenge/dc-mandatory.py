import math


class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is None and diameter is None:
            raise ValueError("You must provide either a radius or a diameter.")
        if radius is not None and diameter is not None:
            raise ValueError("Provide only one of radius or diameter, not both.")
        try:
            if radius is not None:
                radius = float(radius)
                if radius < 0:
                    raise ValueError("Radius cannot be negative.")
                self._radius = radius
            else:
                diameter = float(diameter)
                if diameter < 0:
                    raise ValueError("Diameter cannot be negative.")
                self._radius = diameter / 2
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid value for radius/diameter: {e}")

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError(f"Radius must be a number, got {value!r}.")
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError(f"Diameter must be a number, got {value!r}.")
        if value < 0:
            raise ValueError("Diameter cannot be negative.")
        self._radius = value / 2

    @property
    def area(self):
        return math.pi * self._radius ** 2

    def __str__(self):
        return f"Circle(radius={self._radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __repr__(self):
        return f"Circle(radius={self._radius})"

    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(radius=self._radius + other._radius)

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius == other._radius

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius > other._radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius < other._radius

    def __hash__(self):
        return hash(self._radius)


if __name__ == "__main__":
    try:
        c1 = Circle(radius=5)
        c2 = Circle(diameter=10)
        c3 = Circle(radius=3)
        c4 = Circle(radius=8)

        print("c1:", c1)
        print("c2:", c2)
        print("c3:", c3)

        print("\nc1 == c2 ?", c1 == c2)
        print("c1 > c3 ?", c1 > c3)
        print("c3 < c4 ?", c3 < c4)

        c5 = c1 + c3
        print("\nc1 + c3 =", c5)

        circles = [c4, c1, c3, c2]
        circles.sort()
        print("\nSorted circles (smallest to largest):")
        for c in circles:
            print(" ", c)
    except Exception as e:
        print(f"Unexpected error in demo: {e}")

    for bad in [{}, {"radius": -1}, {"radius": "abc"}, {"radius": 1, "diameter": 2}]:
        try:
            Circle(**bad)
        except ValueError as e:
            print(f"Error caught for {bad}: {e}")
