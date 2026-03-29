
##
# for this we are using 2*val - min if value is min so that we are retrive next previous
# if current element will be minimum example min= 10 and current element is 9 so we needs to store min=9 
# but when we pop the element which is on top and is min then minimum will be 10 so 
# preseving the minimum element we are doing calculation val < prev_min so we can say val - prev_min < 0
#  2val - prev_min < val is it true, so we will store this 2*val - prev_min at top of stack and min will be the value so val=min or min=val whenever we will pop this then we need to retrive back original element using
#  2*min - val we can say min is val --> 2*val - 2*val +  prev_min  --> prev_min we get prev_min
##
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val):
        if not self.stack:
            self.stack.append(val)
            self.min = val
        elif val >= self.min:
            self.stack.append(val)
        else:
            # store encoded value
            self.stack.append(2 * val - self.min)
            self.min = val

    def pop(self):
        if not self.stack:
            return None
        
        top = self.stack.pop()
        
        if top >= self.min:
            return top
        else:
            # retrieve previous min
            original_min = self.min
            self.min = 2 * self.min - top
            return original_min

    def top(self):
        if not self.stack:
            return None
        
        top = self.stack[-1]
        
        if top >= self.min:
            return top
        else:
            return self.min

    def getMin(self):
        return self.min