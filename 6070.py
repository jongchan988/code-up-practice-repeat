n = int(input())

def getWeather(number):
    shareNum = number//3
    match(shareNum):
        case 1:
            return 'spring'
        case 2:
            return 'summer'
        case 3:
            return 'fall'
        case _:
            return 'winter'
        
print(getWeather(n))