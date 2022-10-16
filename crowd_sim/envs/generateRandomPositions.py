""" 
Script to generate random human positions within the constraints
"""
import time
import random
from numpy.linalg import norm
def generateRandomPositions(human_nums,human_radius):
    """
    Returns in this format:  humanPosHc = [[(-6,0),(7,-1.5)],[(1,-7),(-1.5,7.5)],[(4.5,0),(-1.5,-4)]]
    """
    humanPos = []
    random.seed(time.time)
    # for i in range(human_nums):
    while True and len(humanPos)<human_nums:
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
            for [(xS,yS),(xG,yG)] in humanPos:
                 if norm((xS - xSource, yS - ySource )) < 2*human_radius:
                        collide = True
                        break
                 if norm((xG - xGoal, yG - yGoal )) < 2*human_radius:
                        collide = True
                        break
            if not collide:
                humanPos.append([(xSource,ySource),(xGoal,yGoal)])
                break
            else:
                continue
    # print(humanPos)
    return humanPos
                
        
