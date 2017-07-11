from random import choice

class Walker():
    """This class will generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize walk attributes"""
        self.num_points = num_points

        # Walks will begin at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def do_walk(self):
        """Determine all points in the walk"""

        # Walk continues until reaching the specified step number (num_points)
        while len(self.x_values) < self.num_points:
            # Choose a direction and how far to go
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject idle steps
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
