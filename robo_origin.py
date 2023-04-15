class Solution(object):
    def judgeCircle(self, moves):
        pos=[0,0]
        posf=[0,0]
        for m in moves:
            if m=='U':
                pos[1]=pos[1]+1
            if m=='D':
                pos[1]=pos[1]-1
            if m=='L':
                pos[0]=pos[0]-1
            if m=='R':
                pos[0]=pos[0]+1
        if (pos==posf):
            return True
        else:
            return False
