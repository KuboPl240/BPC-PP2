import math
import random

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def magnitude(self):
        return math.sqrt(self.real**2 + self.imag**2)
    
    def angle(self):
        return math.atan2(self.imag, self.real)
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.real + self.real * other.imag
        return ComplexNumber(real, imag)
    
    def __repr__(self):
        return f"{self.real} + {self.imag}i"


class ComplexVector:
    def __init__(self, dimension, elements=None):
        self.dimension = dimension
        if elements:
            self.elements = elements
        else:
            self.elements = [ComplexNumber(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(dimension)]
    
    def magnitude(self):
        return math.sqrt(sum([element.magnitude()**2 for element in self.elements]))
    
    def add_vector(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension to add")
        return ComplexVector(self.dimension, [self.elements[i] + other.elements[i] for i in range(self.dimension)])
    
    def multiply_vector(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension to multiply")
        return ComplexVector(self.dimension, [self.elements[i] * other.elements[i] for i in range(self.dimension)])
    
    def max_magnitude_position(self):
        magnitudes = [element.magnitude() for element in self.elements]
        max_index = magnitudes.index(max(magnitudes))
        return max_index
    
    def __repr__(self):
        return f"ComplexVector: {[str(e) for e in self.elements]}"


class ComplexMatrix(ComplexVector):
    def __init__(self, rows, cols):
        super().__init__(rows)
        self.rows = rows
        self.cols = cols
        self.matrix = [[ComplexNumber(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(cols)] for _ in range(rows)]
    
    def __repr__(self):
        return f"ComplexMatrix:\n" + "\n".join([" ".join([str(e) for e in row]) for row in self.matrix])

c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, -1)
print("ComplexNumber c1:", c1)
print("Magnitude of c1:", c1.magnitude())
print("Angle of c1:", c1.angle())
print("Addition of c1 and c2:", c1 + c2)
print("Multiplication of c1 and c2:", c1 * c2)

v1 = ComplexVector(3)
v2 = ComplexVector(3)
print("\nComplexVector v1:", v1)
print("Magnitude of v1:", v1.magnitude())
print("Addition of v1 and v2:", v1.add_vector(v2))
print("Multiplication of v1 and v2:", v1.multiply_vector(v2))
print("Position of max magnitude in v1:", v1.max_magnitude_position())

m1 = ComplexMatrix(2, 2)
print("\nComplexMatrix m1:\n", m1)
