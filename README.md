# Adventurer Journey - Back End
Please complete the story below and create a program to solve the problem. Commit any work back to the remote no later than 48 hours before the next interview.

*Please use whatever languages, references and tooling you would like to complete the story.*

## Story Instructions
You are an adventurer standing in the center of a map facing North, and you’re trying to weave through the terrain to your final destination. You have the directions to your destination indicating the number of steps and the direction to travel.

Adventurer Path & Instructions - [./Adventurer Path.md](./Adventurer%20Path.md)

Given the Path Instructions above, programmatically parse the instructions and determine what is the Euclidean (straight line) distance from your starting point to the destination in steps?

**Tech Notes:**
- Use whatever languages, references and tooling you would like.
- Provide any needed instructions to run program.
- Do not round to the nearest step.
- After program executes the answer should be returned.


**Instructions to Run**
- Clone the solution
- Navigate to the clone directory 
- If you have not install python. Install Python using pip install Python3
- run the program with python3 solution.py
- progam will prompt you to enter the path: <enter_the_path>
- If you don't want to enter path enter "QUIT" to stop the program

**Assumptions & Clarification**
- "You have the directions to your destination indicating the number of steps and the direction to travel" : I interpreted this sentence as when we change direction we also change direction (ex when traveler is facing north and move 5 steps left(5L) then he will be facing West)
- If this interpretation was wrong and I should interprete as we don't change direction when we move (ex when traveler is facing north and move 5 steps left(5L) then he will be still facing north but just moved 5 in the left directions) then we would need to change the following functions:

    # walk <steps> forward
    def moveForward(self,steps):
        self.yPos += ySteps
        return
    
    # walk <steps> backwards
    def moveBackward(self,steps):
        self.yPos -= ySteps
        return
    
    # walk <steps> in right direction
    def moveRight(self,steps):        
        self.xPos += xSteps
        return
    
    # walk <steps> in left direction 
    def moveLeft(self,steps):
        self.xPos -= xSteps
        return