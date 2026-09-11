class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Time taken to arrive = (target - position[i]) / speed[i]
        # Cars can only form fleets with cars ahead of it
        # If a car takes less time than a car ahead of it, then it becomes a fleet
        # If a car takes more or same time as a car behind it, it becomes a fleet

        n = len(position)
        cars = [[position[i], speed[i]] for i in range(n)]
        cars.sort(reverse=True)  # Sort position in descending order

        stack = []  # Keep track of times
        for car in cars:
            pos, spd = car[0], car[1]
            time = (target - pos) / spd
            stack.append(time)

            # Check for fleet, stack[-1] is the car "behind"
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # The car behind forms a fleet, so remove

        return len(stack)
        