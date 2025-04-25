class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire= deque()
        radiant = deque()

        n = len(senate)

        for i in range(n):
            if senate[i] == "D":
                dire.append(i)
            else:
                radiant.append(i)

        while dire and radiant:
            d=dire.popleft()
            r=radiant.popleft()

            if r < d:
                radiant.append( r + n )
            else:
                dire.append(d + n )

        return "Radiant" if radiant else "Dire"


        '''
        Approach:

        •	Initialize two queues: one for “Dire” senators and one for “Radiant” senators, storing their indices.
	    •	Iterate through the input string and populate the respective queues with indices of senators.
	    •	While both queues are non-empty, simulate each round of voting:
	    •	Pop the front senator from each queue.
	    •	The senator with the smaller index gets to ban the other and re-enters the queue with a new index incremented by n (to simulate the next round).
	    •	Continue until one queue is empty.
	    •	Return the name of the remaining party.

        Complexities:

        Time Complexity: O(n)
	    •	Each senator gets added to a queue once and re-added at most once per round.
	    •	In the worst case, each senator can ban another only once before the simulation ends.
	    •	So each element is processed at most O(1) times per round, and total operations are linear with respect to the number of senators.

Space Complexity: O(n)
	    •	Two queues (radiant and dire) are used to hold up to n elements (in worst case, all senators are from one party).
	    *   Therefore, the space required is also O(n).


        '''
