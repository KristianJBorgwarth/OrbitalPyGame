from enum import Enum


class AstroidType(Enum):
    small = 1
    large = 2
    AstroidType = Enum("type", ["small", "large"])
