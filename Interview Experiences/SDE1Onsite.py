
# Amazon Interview Question 1: 23. Merge k Sorted Lists

# Amazon Interview Question 2

def solve(strg, k ):
    n = len(strg)
    freq = {}
    
    i = 0
    j = k - 1
    
    while j<n:
        sub = s[i:j+1]
        freq[sub] = freq.get(sub,0) + 1
        
        i +=1
        j += 1
        
    return max(freq.values())
        
    
    '''
    for i in range(n-k+1):
        temp = s[i:i+k]
        if temp not in freq:
            freq[temp] = 1
        else:
            freq[temp] += 1
                    
    return max(freq.values())
    
    '''
                


s = ' aabbaaccaabaa '
k = 2
print(solve(s,k))


'''

Amazon SDE-1 Onsite Interview Experience (Rejected – Round 1)

Interview Format
	•	Onsite (Virtual)
	•	Round 1
	•	Mostly 1 interviewer (brief interaction with a second interviewer as exception)
	•	Pen & Paper Coding (no IDE, full code required)

⸻

Interview Breakdown

Question 1: Introduction
	•	Asked to introduce myself briefly
	•	Focused on background, preparation, and interest in SDE role

⸻

Question 2: DSA – Merge K Sorted Lists (LeetCode 23)
	•	Initially asked to solve Merge K Sorted Lists
	•	I struggled to directly derive the optimal approach on paper
	•	Interviewer guided the problem down to:
	•	Merge Two Sorted Linked Lists
	•	I was able to solve the two-list merge correctly
	•	We discussed how this can be extended to K lists (divide & conquer / heap), but I couldn’t fully implement it on paper in time

Learning
	•	Pen-paper coding requires very clear structure
	•	Even known problems feel harder without an editor
	•	Should practice writing full linked list code without shortcuts

⸻

Question 3: DSA – Fixed Size Sliding Window

Problem

Given a string and an integer k, find the maximum frequency of any substring of size k.

Approach
	•	Used fixed-size sliding window
	•	Maintained a HashMap to count substring frequencies
	•	Time Complexity: O(n)
	•	Space Complexity: O(n)

Outcome
	•	Core logic was correct
	•	Had minor bugs (indexing / edge cases) due to rushing
	•	Interviewer focused more on:
	•	Reasoning
	•	Communication
	•	Why this approach is optimal

⸻

Question 4: Leadership Principle (LP)
	•	Asked to talk about a project I’m proud of
	•	Explained:
	•	Problem statement
	•	My contribution
	•	Challenges faced
	•	What I learned

⸻

Final Question

“Do you have any questions for us?”
	•	Asked about team culture and learning opportunities

⸻

Result

❌ Rejected in Round 1

⸻

Honest Self-Assessment

What went well
	•	Communication was clear
	•	Core logic was understood
	•	Could explain reasoning and trade-offs
	•	Best interview experience so far in terms of discussion quality

What went wrong
	•	Rushed while coding
	•	Didn’t slow down enough on pen-paper
	•	Minor bugs affected confidence
	•	Merge K Lists needed stronger recall under pressure

⸻

Key Takeaways (For Future Candidates)
	1.	Pen & paper coding is a different skill
	•	Practice writing complete code
	•	No shortcuts, no assumptions
	2.	Slow down
	•	Interviewers value correctness over speed
	•	Pausing to think is better than fixing bugs later
	3.	Core patterns matter
	•	Sliding window
	•	Linked list manipulation
	•	Divide & conquer thinking
	4.	Rejection ≠ Bad Interview
	•	Sometimes it’s about execution polish, not knowledge

⸻

Final Thoughts

This was my best interview experience so far.
It reinforced that if core logic is clear, problems are solvable — but execution under constraints (pen & paper, time pressure) needs deliberate practice.

I’ll be refining:
	•	Writing bug-free code slowly
	•	Explaining edge cases upfront
	•	Practicing classic problems without an IDE

Hope this helps others preparing for Amazon SDE-1 onsite interviews.

'''