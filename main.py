from typing import Literal

from pydantic import BaseModel


class Vec2(BaseModel):
    x: float
    y: float

    def __add__(self, other: "Vec2") -> "Vec2":
        return Vec2(
            x=self.x + other.x,
            y=self.y + other.y,
        )

    def __mul__(self, scalar: int) -> "Vec2":
        return Vec2(
            x=self.x * scalar,
            y=self.y * scalar,
        )

    def __rmul__(self, scalar: int) -> "Vec2":
        return self.__mul__(scalar)


class Instruction(BaseModel):
    steps: int
    direction: Literal["F", "B", "L", "R"]

    def as_vec(self) -> Vec2:
        if self.direction == "F":
            return Vec2(x=0, y=self.steps)

        if self.direction == "B":
            return -1 * Vec2(x=0, y=self.steps)

        if self.direction == "R":
            return Vec2(x=self.steps, y=0)

        if self.direction == "L":
            return -1 * Vec2(x=self.steps, y=0)


def parse_instructions(input: str) -> list[Instruction]:
    pass


def main():
    pass


if __name__ == "__main__":
    main()
