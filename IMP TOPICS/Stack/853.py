class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        sorted_cars = sorted(zip(position, speed), reverse = True)

        stck = []
        for p, s in sorted_cars:
            time = (target - p)/s
            stck.append(time)

            if len(stck) >= 2 and stck[-1] <= stck[-2]:
                stck.pop()


        return len(stck)

        