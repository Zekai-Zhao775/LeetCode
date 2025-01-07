class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # directions n-0 e-1 s-2 w-3
        start_direction = 0  # Initial direction (north)
        start_location = [0, 0]  # Initial location
        current_direction = 0  # Current direction
        current_location = [0, 0]  # Current location

        i = 0
        while i < 4:
            temp_location, temp_direction = self.newLocation(current_location, current_direction, instructions)

            # Check if robot returns to the origin
            if temp_location[0] == start_location[0] and temp_location[1] == start_location[1]:
                return True

            # Update current state
            current_location[0] = temp_location[0]
            current_location[1] = temp_location[1]
            current_direction = temp_direction

            i += 1

        # If not at origin but direction changed, return True
        return current_direction != start_direction

    def newLocation(self, location, direction, instructions):
        current_direction = direction
        current_location = [location[0], location[1]]

        for instruction in instructions:
            if instruction == "G":
                if current_direction == 0:  # North
                    current_location[1] += 1
                elif current_direction == 1:  # East
                    current_location[0] += 1
                elif current_direction == 2:  # South
                    current_location[1] -= 1
                elif current_direction == 3:  # West
                    current_location[0] -= 1
            elif instruction == "L":
                current_direction -= 1
                current_direction %= 4
            elif instruction == "R":
                current_direction += 1
                current_direction %= 4

        return [current_location, current_direction]