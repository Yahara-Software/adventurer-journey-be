import pytest
from pydantic import ValidationError

from main import (
    Instruction,
    next_match,
    parse_instruction,
    parse_instructions,
    solution,
)


@pytest.fixture
def test_input() -> str:
    return "15F6B5L"


def test_next_match(test_input: str):
    to_match = {"F", "B", "L", "R"}
    assert next_match(to_match, test_input) == 2


def test_parse_valid_instruction():
    instruction = "67F"
    assert parse_instruction(instruction) == Instruction(steps=67, direction="F")


def test_parse_invalid_instruction():
    instruction = "67H"
    with pytest.raises(ValidationError):
        parse_instruction(instruction)

    instruction = "FFF"
    with pytest.raises(ValidationError):
        parse_instruction(instruction)


def test_parse_instructions(test_input: str):
    expected = [
        Instruction(steps=15, direction="F"),
        Instruction(steps=6, direction="B"),
        Instruction(steps=5, direction="L"),
    ]

    assert parse_instructions(test_input) == expected


def test_solution(test_input: str):
    assert solution(test_input) == pytest.approx(10.29563)
