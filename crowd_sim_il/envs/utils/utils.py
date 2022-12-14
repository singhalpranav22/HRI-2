import numpy as np


def point_to_segment_dist(x1, y1, x2, y2, x3, y3):
    """
    Calculate the closest distance between point(x3, y3) and a line segment with two endpoints (x1, y1), (x2, y2)

    """
    px = x2 - x1
    py = y2 - y1

    if px == 0 and py == 0:
        return np.linalg.norm((x3 - x1, y3 - y1))

    u = ((x3 - x1) * px + (y3 - y1) * py) / (px * px + py * py)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    # (x, y) is the closest point to (x3, y3) on the line segment
    x = x1 + u * px
    y = y1 + u * py

    return np.linalg.norm((x - x3, y - y3))


def closest_point_on_segment(x1, y1, x2, y2, x3, y3):
    """
    Calculate the closest distance between point(x3, y3) and a line segment with two endpoints (x1, y1), (x2, y2)

    """
    px = x2 - x1
    py = y2 - y1

    if px == 0 and py == 0:
        return (x1, y1)

    u = ((x3 - x1) * px + (y3 - y1) * py) / (
                px * px + py * py)  # RK check if (x3-x1),(y3-y1) should be pre-normalized(checked)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    # (x, y) is the closest point to (x3, y3) on the line segment
    x = x1 + u * px
    y = y1 + u * py

    return (x, y)


def isIntersectionCrowded(humans, robots):
    isCrowded = False
    numAgentsInIntersection = 0
    for human in humans:
        if human.px >= -2 and human.px <= -2 and human.py >= -2 and human.py <= 2:
            numAgentsInIntersection += 1
    for robot in robots:
        if robot.px >= -2 and robot.px <= -2 and robot.py >= -2 and robot.py <= 2:
            numAgentsInIntersection += 1
    if numAgentsInIntersection >= 2:
        isCrowded = True
    return isCrowded


def isIntersectionCrossing(agent):
    currentQuad = determineQuadrant(agent.px, agent.py)
    goalQuad = determineQuadrant(agent.gx, agent.gy)
    if currentQuad == 0:
        return False
    elif currentQuad == goalQuad:
        return False
    else:
        return True


def determineQuadrant(x, y):
    """
    Interesection area -> 0
    else all are 1,2,3,4 (first quadrant is right, and anticlockwise afterwards)
    """
    if x >= -2 and x <= 2 and y >= -2 and y <= 2:
        return 0
    elif x >= 2 and x <= 8 and y >= -2 and y <= 2:
        return 1
    elif x >= -2 and x <= 2 and y >= 2 and y <= 8:
        return 2
    elif x >= -8 and x <= -2 and y >= -2 and y <= 2:
        return 3
    else:
        return 4


def determineSubGoal(px, py, egx, egy):
    # if the agent is in the intersection area, then the subgoal is the ending goal
    # Default subgoal is the middle point of quadrant 
    # subGoals = {
    #     1 : (1.5,0),
    #     2 : (0,1.5),
    #     3 : (-1.5,0),
    #     4 : (0,-1.5)
    # }
    # LOGIC changed: have a line as subgoal according to quadrant, one coordinate will be constant.
    # Other coordinate to be determined by min distance from egx egy
    current_quadrant = determineQuadrant(px, py)
    if current_quadrant == 0:
        return (egx, egy)
    else:  # RK: check if 2 and 4 are swapped(resolved)
        if current_quadrant == 1:
            return closest_point_on_segment(1.9, -1.9, 1.9, 1.9, egx, egy)
        if current_quadrant == 2:
            return closest_point_on_segment(-1.9, 1.9, 1.9, 1.9, egx, egy)
        if current_quadrant == 3:
            return closest_point_on_segment(-1.9, -1.9, -1.9, 1.9, egx, egy)
        if current_quadrant == 4:
            return closest_point_on_segment(-1.9, -1.9, 1.9, -1.9, egx, egy)


def addRandomNoise(x, y, noise):
    # Add random noise between -0.5 and 0.5 in x and y
    x_noise =  np.random.uniform(-noise, noise)
    x += x_noise
    # print("x_noise",x_noise)
    y_noise =  np.random.uniform(-noise, noise)
    # print("y_noise",y_noise)
    y += y_noise
    return x, y
