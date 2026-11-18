import math


class Fraction:
    """Represents a mathematical fraction with an integer numerator and a strictly positive integer denominator."""

    def __init__(self, numerator: int, denominator: int = 1) -> None:
        """Initializes and simplifies a Fraction instance."""
        if not isinstance(numerator, int) or isinstance(numerator, bool):
            raise TypeError("Numerator must be an integer.")
        if not isinstance(denominator, int) or isinstance(denominator, bool):
            raise TypeError("Denominator must be an integer.")
        if denominator <= 0:
            raise ValueError("Denominator must be strictly positive (> 0).")

        common_divisor = math.gcd(numerator, denominator)
        self.numerator: int = numerator // common_divisor
        self.denominator: int = denominator // common_divisor

    # --- String representations (Extra magic methods 1 & 2) ---

    def __str__(self) -> str:
        """Returns a readable string representation of the fraction."""
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self) -> str:
        """Returns an unambiguous string representation for debugging."""
        return f"Fraction({self.numerator}, {self.denominator})"

    # --- Comparison methods (Required) ---

    def __eq__(self, other: object) -> bool:
        """Checks if two fractions are equal (==)."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __ne__(self, other: object) -> bool:
        """Checks if two fractions are not equal (!=)."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return not self.__eq__(other)

    def __lt__(self, other: "Fraction") -> bool:
        """Checks if this fraction is strictly smaller than another (<)."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other: "Fraction") -> bool:
        """Checks if this fraction is smaller than or equal to another (<=)."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other: "Fraction") -> bool:
        """Checks if this fraction is strictly greater than another (>)."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other: "Fraction") -> bool:
        """Checks if this fraction is greater than or equal to another (>=)."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator >= other.numerator * self.denominator

    # --- Arithmetic operations (Extra magic methods 3, 4, 5 & 6) ---

    def __add__(self, other: "Fraction") -> "Fraction":
        """Adds two fractions (+)."""
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """Subtracts another fraction from this fraction (-)."""
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """Multiplies two fractions (*)."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """Divides this fraction by another fraction (/)."""
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a zero fraction.")
        if other.numerator < 0:
            return Fraction(-self.numerator * other.denominator, self.denominator * abs(other.numerator))
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)