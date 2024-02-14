import math

# Traveler class:
    #Att: current location, current direction
    #Prop: moveForward, moveBackward, moveLeft, moveRight

class Traveler:
    def __init__(self,xPos,yPos,dir) -> None:
        self.xPos = xPos
        self.yPos = yPos
        self.dir = dir
        self.startXPos = xPos
        self.startYPos = yPos
        self.internalDir = None
        self.setInternalDir(self.dir)

    def setInternalDir(self,dir):
        dir = dir.upper()
        match dir:
            case "NORTH":
                self.internalDir = (0,1)
            case "SOUTH":
                self.internalDir = (0,-1)
            case "EAST":
                self.internalDir = (1,0)
            case "WEST":
                self.internalDir = (-1,0)
        
    def getIntenalDir(self):
        return self.internalDir
    
    def updateInternalDir(self, xDir,yDir):
        self.internalDir = (xDir,yDir)

    def move(self,steps,dir):
        match dir:
            case 'F':
                self.moveForward(steps)
            case 'B':
                self.moveBackward(steps)
            case 'L':
                self.moveLeft(steps)
            case 'R':
                self.moveRight(steps)
        return
    # gets current position of traveller.
    def getPosition(self):
        return (self.xPos,self.yPos)
    
    # walk <steps> forward
    def moveForward(self,steps):
        xDir,yDir = self.getIntenalDir()
        xSteps =  xDir*steps
        ySteps = yDir*steps
        self.xPos += xSteps
        self.yPos += ySteps
        return
    
    # walk <steps> backwards
    def moveBackward(self,steps):
        xDir,yDir = self.getIntenalDir()
        #change the directions:
        xDir = -xDir
        yDir = -yDir
        self.updateInternalDir(xDir,yDir)
        xSteps =  xDir*steps
        ySteps = yDir*steps
        self.xPos += xSteps
        self.yPos += ySteps
        return
    
    # walk <steps> in right direction
    def moveRight(self,steps):
        dirMap = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1)
        }
        xDir,yDir = self.getIntenalDir()
        #change the directions:
        xDir,yDir = dirMap[(xDir,yDir)]
        self.updateInternalDir(xDir,yDir)
        xSteps =  xDir*steps
        ySteps = yDir*steps
        self.xPos += xSteps
        self.yPos += ySteps
        return
    
    # walk <steps> in left direction 
    def moveLeft(self,steps):
        dirMap = {
            (0,1): (-1,0),
            (-1,0): (0,-1),
            (0,-1): (1,0),
            (1,0): (0,1)
        }
        xDir,yDir = self.getIntenalDir()
        #change the directions:
        xDir,yDir = dirMap[(xDir,yDir)]
        self.updateInternalDir(xDir,yDir)
        xSteps =  xDir*steps
        ySteps = yDir*steps
        self.xPos += xSteps
        self.yPos += ySteps
        return
    # find the distance from the start
    def getDistanceFromStart(self):
        xDiff = self.xPos - self.startXPos
        yDiff = self.yPos - self.startYPos
        return math.sqrt((xDiff**2) + (yDiff**2))
        


# checks path for valid direction and format
def validatePath(path):
    allowedChar = "FBRL"
    try:
        path = path.upper()
        idx = 0
        stepFound = False #store to check for step first than directions.
        n = len(path)
        while(idx < n):
            # If
            #check for steps first
            while(idx < n and path[idx].isdigit()):
                stepFound = True
                idx+=1
            
            #checking if step is found.
            if not stepFound:
                return False
            
            # check for direction
            if idx < n and path[idx] in allowedChar:
                stepFound = False
            else:
                return False
            
            idx+=1
        
        return True
    except Exception as e:
       print(f"{type(e)} : {e} \n")
       return False


def traversePath(path,traveler):
    idx = 0
    try:
        n = len(path)
        while(idx < n):
            step = 0

            #check for steps first
            while(idx < n and path[idx].isdigit()):
                step = (step*10) + int(path[idx])
                idx+=1
            
            
            # check for direction
            if idx < n and path[idx] in "FBLR":
                dir = path[idx]
            
            traveler.move(step,dir)
            idx+=1
    except ValueError:
        print(f"Error at path index {idx}")
        return
    except AttributeError:
        print(f"Traveler object does not have a 'move' method.")
        return
    except Exception as e:
       print(f"{type(e)} : {e} \n")
       return

    return

def main():
    inputStr = """Brave adventurer waits for your comand.
Provide the path you want him to follow.
Remember to provided the number of steps first and the direction(F - Forward | B - Backward | L - Left | R - Right) second (ex: 6F, 12F6B) or QUIT to stop the program.: """

    path = ""

    while path == "":
        path = input(inputStr)
        if path == "QUIT":
            print("No path provided.\nProgram stoped.")
            return

    path = path.strip() # clear whitespace from front and end

    if validatePath(path):
        traveler1 = Traveler(0,0,"North")

        traversePath(path,traveler1)

        distance = traveler1.getDistanceFromStart()

        print(f"Adventurer is {distance} step(s) away form the starting position")
    
    else:
        print("-- Invalid path --\nProgram stoped.")
    
    return


if __name__ == "__main__":
    main()