import math
from typing import Literal

from pydantic import BaseModel


class Vec2(BaseModel):
    x: float
    y: float

    @staticmethod
    def zero() -> "Vec2":
        return Vec2(x=0.0, y=0.0)

    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

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


def next_match(chars: set[str], input: str) -> int:
    """
    Return the index of the first occurence of any character in chars
    within input.

    Args:
        chars: Characters to search for.
        input: String to search.

    Returns:
        The index of the first match.
        Returns -1 if the no character matching chars is found.
    """
    indices = [input.find(c) for c in chars]
    if all(index == -1 for index in indices):
        return -1
    return min(index for index in indices if index >= 0)


def parse_instruction(input: str) -> Instruction:
    """
    Parse a single instruction from a string.

    Example the string '44F' will be parsed to
    Instruction(steps=44, direction='F')

    Args:
        input: The string to parse into an instruction.

    Returns:
        A instruction object.

    Raises:
        A validation error if the instruction is not valid.
        The instruction is invalid in two cases:
            - The number of steps is not a valid integer
            - The dirction is not F B L or R

    """
    direction = input[-1]
    steps = input[: len(input) - 1]
    return Instruction(steps=steps, direction=direction)


def parse_instructions(input: str) -> list[Instruction]:
    to_match = {"F", "B", "L", "R"}
    instructions = []

    while True:
        index = next_match(to_match, input)

        if index == -1:
            break

        instruction = input[: index + 1]
        instructions.append(instruction)
        input = input[index + 1 :]

    return [parse_instruction(instruction) for instruction in instructions]


def solution(input) -> float:
    instructions = parse_instructions(input)
    vecs = [instruction.as_vec() for instruction in instructions]

    total = Vec2.zero()
    for vec in vecs:
        total += vec

    return total.length()


def main():
    input = "15F6B6B5L16R8B16F20L6F13F11R"
    distance = solution(input)
    print(f"The total distance traveled is {distance}")


if __name__ == "__main__":
    main()
