class Solution(object):
    def finalValueAfterOperations(self, operations):
        x=0
        for operation in operations:
            if operation in ("--X", "X--"):
                x -= 1
            else:
                x += 1
        return x 
        