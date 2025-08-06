#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry with integer validation."""
class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Raise Exception since area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value as an integer greater than 0.

        Args:
            name (str): name of the value (for error messages).
            value (int): the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value <= 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
