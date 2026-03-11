class Solution:
    def simplifyPath(self, path: str) -> str:
        stck = []
        curr = ''

        for i in path + '/':
            if i == '/':
                if curr  ==  '..':
                    if stck : stck.pop()

                elif curr != '' and curr != '.':
                    stck.append(curr)

                curr = ''
            
            else:
                curr += i

        return '/' + '/'.join(stck)

