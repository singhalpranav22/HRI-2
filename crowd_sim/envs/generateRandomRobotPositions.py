""" 
Script to generate random human positions within the constraints
"""
import time
import random
from numpy.linalg import norm
from .utils.utils import determineQuadrant, getDistance
from .utils.utils import determineQuadrant


def checkIfPreexistingCoordinates(x, y, humanCoordinates):
    print("check if pe coordinates called")
    # print(humanCoordinates)
    for humanCoordinate in humanCoordinates:
        # print("Robot position: ", x, y)
        # print("Human position: ", humanCoordinates[0], humanCoordinates[1])
        # print("Ditsance between them: ", getDistance(x, y, humanCoordinate[0], humanCoordinate[1]))
        if (getDistance(x, y, humanCoordinate[0], humanCoordinate[1]) <= 1.5) :
        # if abs(coordinate[0] - x) <= 3 or abs(coordinate[1] - y) <= 3:
            # print("Violated condition", x, y, humanCoordinates)
            return True
    # print("Called checkIfPreexistingCoordinates for ", x, y, humanCoordinates)
    return False

def generateRandomRobotPositions(robot_nums, robot_radius, initialHumanPositions):
    """
    Returns in this format:  robotPosHc = [[(-6,0),(7,-1.25)],[(1,-7),(-1.25,7.5)],[(4.5,0),(-1.25,-4)]]
    """
    robotPos = []
    random.seed(time.time())

    checkIfPreexistingCoordinates(2.5, -3.5, [])

    # Filter out the starting and goal positions
    print("INITIAL HUMAN POSITIONS: ", initialHumanPositions)
    starting_positions = []
    goal_positions = []
    for item in initialHumanPositions:
        starting_positions.append(item[0])
        goal_positions.append(item[1])

    # for i in range(human_nums):
    while True and len(robotPos) < robot_nums:
        while True:
            # generate random source and goal positions
            xSource = round(random.uniform(-7.3, 7.3), 1)
            ySource = round(random.uniform(-7.3, 7.3), 1)

            while (checkIfPreexistingCoordinates(xSource, ySource, starting_positions) or 
                    (-7.75 <= xSource <= -1.25 and -7.75 <= ySource <= -1.25) or (
                    -7.75 <= xSource <= -1.25 and 1.25 <= ySource <= 7.75) or (
                           1.25 <= xSource <= 7.75 and -7.75 <= ySource <= -1.25) or (
                           1.25 <= xSource <= 7.75 and 1.25 <= ySource <= 7.75) or
                    (determineQuadrant(xSource, ySource) == 0)):
                # print(xSource,ySource)
                xSource = round(random.uniform(-7.3, 7.3), 1)
                ySource = round(random.uniform(-7.3, 7.3), 1)
                # print("Called xsource ysource")

            quadrant_for_source = determineQuadrant(xSource, ySource)

            xGoal = round(random.uniform(-7.3, 7.3), 1)
            yGoal = round(random.uniform(-7.3, 7.3), 1)

            while (checkIfPreexistingCoordinates(xGoal, yGoal, goal_positions) or 
                (-7.75 <= xGoal <= -1.25 and -7.75 <= yGoal <= -1.25) or (-7.75 <= xGoal <= -1.25 and 1.25 <= yGoal <= 7.75) or (
                    1.25 <= xGoal <= 7.75 and -7.75 <= yGoal <= -1.25) or (1.25 <= xGoal <= 7.75 and 1.25 <= yGoal <= 7.75) or ( (-2<=xGoal<=2 and -2<=yGoal<=2)) or
                   (quadrant_for_source == determineQuadrant(xGoal, yGoal) or (determineQuadrant(xGoal, yGoal) == 0))):
                xGoal = round(random.uniform(-7.3, 7.3), 1)
                yGoal = round(random.uniform(-7.3, 7.3), 1)

            collide = False
            for [(xS, yS), (xG, yG)] in robotPos:
                if norm((xS - xSource, yS - ySource)) < 2 * robot_radius:
                    collide = True
                    break
                if norm((xG - xGoal, yG - yGoal)) < 2 * robot_radius:
                    collide = True
                    break
            if not collide:
                robotPos.append([(xSource, ySource), (xGoal, yGoal)])
                break
            else:
                continue
    # print(robotPos)
    return robotPos
