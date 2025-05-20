class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        count = 0 #Number of students rotated

        while students:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                count = 0

            else:
                students.append(students.popleft()) # move to back
                count+=1

            if count == len(students):   # if all students have rotated without eating → break
                break

        return len(students) # students left who couldn't eat


        '''
        Approach:

        - Convert both arrays to deque
        - Initialize a count with 0
        - Start a loop till students is true
        - if student and sandwich preferences are same popleft() both
        - else add the unmatched student to the end of students[]
        - lastly check if count == len(students) , if yes break loop
        - Return len(students)
        
        Time Complexity: O(n) -  each student is processed at most twice
        Space Complexity: O(n) -  using deque for efficient pop/append operations
        '''
