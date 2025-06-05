import random

class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar']
        velocity = observations['velocity']

        left, fleft, front, fright, right = lidar

        if left > right + 0.4:
            direction = 'left'
        elif right > left + 0.4:
            direction = 'right'
        else:
            direction = 'straight'

        # Decide motion
        if front < 0.4:
            motion = 'brake'
        elif velocity < 0.4 and front > 1.0:
            motion = 'accelerate'
        else:
            motion = 'coast'

        return (direction, motion)