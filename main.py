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
    pass


def parse_instructions(input: str) -> list[Instruction]:
    pass


def main():
    input = "15F6B6B5L16R8B16F20L6F13F11R"
    to_match = {"F", "B", "L", "R"}
    instructions = []

    while True:
        index = next_match(to_match, input)

        if index == -1:
            break

        instruction = input[: index + 1]
        instructions.append(instruction)
        input = input[index + 1 :]


if __name__ == "__main__":
    main()
