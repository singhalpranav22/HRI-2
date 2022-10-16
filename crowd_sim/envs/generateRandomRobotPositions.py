""" 
Script to generate random human positions within the constraints
"""
import time
import random
from numpy.linalg import norm
def generateRandomRobotPositions(robot_nums,robot_radius):
    """
    Returns in this format:  robotPosHc = [[(-6,0),(7,-1.5)],[(1,-7),(-1.5,7.5)],[(4.5,0),(-1.5,-4)]]
    """
    robotPos = []
    random.seed(time.asctime)
    # for i in range(human_nums):
    while True and len(robotPos)<robot_nums:
        while True:
            # generate random source and goal positions
            xSource = round(random.uniform(-8,8), 1)
            ySource = round(random.uniform(-8,8), 1)
            while ((-8<=xSource<=-1.5 and -8<=ySource<=-1.5) or (-8<=xSource<=-1.5 and 1.5<=ySource<=8) or (1.5<=xSource<=8 and -8<=ySource<=-1.5) or (1.5<=xSource<=8 and 1.5<=ySource<=8)):
                print(xSource,ySource)
                xSource = round(random.uniform(-8,8), 1)
                ySource = round(random.uniform(-8,8), 1)
            xGoal = round(random.uniform(-8,8), 1)
            yGoal = round(random.uniform(-8,8), 1)
            while ((-8<=xGoal<=-1.5 and -8<=yGoal<=-1.5) or (-8<=xGoal<=-1.5 and 1.5<=yGoal<=8) or (1.5<=xGoal<=8 and -8<=yGoal<=-1.5) or (1.5<=xGoal<=8 and 1.5<=yGoal<=8)):
                xGoal = round(random.uniform(-8,8), 1)
                yGoal = round(random.uniform(-8,8), 1)
            collide = False
            for [(xS,yS),(xG,yG)] in robotPos:
                 if norm((xS - xSource, yS - ySource )) < 2*robot_radius:
                        collide = True
                        break
                 if norm((xG - xGoal, yG - yGoal )) < 2*robot_radius:
                        collide = True
                        break
            if not collide:
                robotPos.append([(xSource,ySource),(xGoal,yGoal)])
                break
            else:
                continue
    # print(robotPos)
    return robotPos
                
        
