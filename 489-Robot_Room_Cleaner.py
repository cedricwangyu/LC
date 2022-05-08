# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def __init__(self):
        self.cleaned = set()
        self.dirs = ((-1, 0), (0, -1), (1, 0), (0, 1))
        self.robot = None
        
    def go_back(self):
        self.robot.turnRight()
        self.robot.turnRight()
        self.robot.move()
        self.robot.turnRight()
        self.robot.turnRight()
    
    def backtrack(self, pos=(0, 0), idx=0):
        self.robot.clean()
        self.cleaned.add(pos)
        for i in range(idx, idx+4):
            j = i % 4
            new_pos = (pos[0] + self.dirs[j][0], pos[1] + self.dirs[j][1])
            if new_pos not in self.cleaned and self.robot.move():
                self.backtrack(new_pos, j)
                self.go_back()
            self.robot.turnLeft()
            
        
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.robot = robot
        self.backtrack()
        
        
        
        
        