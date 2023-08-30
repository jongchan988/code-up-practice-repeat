

def getMb(hz, bitNum, trackCnt, second):
    return str(format(int(hz)*int(bitNum)*int(trackCnt)*int(second)/8/1024/1024, '.1f')) + " MB"

h, b, c, s = input().split()
print(getMb(h, b, c, s))

