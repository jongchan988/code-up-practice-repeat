def getMb(width, height, bit):
    return str(round(int(width)*int(height)*int(bit)/8/1024/1024, 2)) + " MB"

w, h, b = input().split()
print(getMb(w, h, b))