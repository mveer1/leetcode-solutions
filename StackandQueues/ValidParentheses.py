# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


# mysol 86%:

class Solution:
    def match(self, bracket):
        if bracket == ")":
            return "("
        elif bracket == "}":
            return "{"
        elif bracket == "]":
            return "["
        
    def isValid(self, s: str) -> bool:
        stack = []
        for brac in s:
            if brac=="(" or brac=="[" or brac=="{": 
                stack.append(brac)
                            
            elif (brac==")" or brac=="]" or brac=="}"):
                if len(stack)==0:
                    return False
                elif self.match(brac) == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not len(stack)==0:
            return False
        return True


# official sol time same syntax better and simple:
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        return not stack



# other sol:
def isValid(self, s):
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
        else:
            return False
    return stack == []
