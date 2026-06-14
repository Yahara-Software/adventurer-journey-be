# How To Run My Solution
Make sure requirements are installed. 

## Requirements
```
python >= 3.12 (can't guarentee this will work for older versions)
uv (recommended) or pip
```
[uv install instructions](https://docs.astral.sh/uv/getting-started/installation/)

## Running With uv (Recommended)
To run the main script with uv simply run:
```
uv run main.py
```
To exectute unit tests run:
```
uv python -m pytest
```

## Running With Pip
## With pip
Create a virtual enviroment and activate
```
python -m venv venv
source venv/bin/activate
```

install packages with
```
pip install -r requirements.txt
```

Execute the script:
```
python main.py
```

Run tests:
```
python -m pytest
```

# Adventurer Journey - Back End
Please complete the story below and create a program to solve the problem. Commit any work back to the remote no later than 48 hours before the next interview.

*Please use whatever languages, references and tooling you would like to complete the story.*

- *This problem is meant as a starting point for interview discussion*
- *This is meant to be a simple problem with an open ended solution to see what you do with it*
- *Be prepared to talk about solving this problem in the context of a full development lifecycle*

## Story Instructions
You are an adventurer standing in the center of a map facing North, and you’re trying to weave through the terrain to your final destination. You have the directions to your destination indicating the number of steps and the direction to travel.

Adventurer Path & Instructions - [./Adventurer Path.md](./Adventurer%20Path.md)

Given the Path Instructions above, programmatically parse the instructions and determine what is the Euclidean (straight line) distance from your starting point to the destination in steps?

**Tech Notes:**
- Use whatever languages, references and tooling you would like.
- Provide any needed instructions to run program.
- Do not round to the nearest step.
- After program executes the answer should be returned.
