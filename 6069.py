grade = input()

def getGradeText(grade):
    match(grade):
        case 'A':
            return 'best!!!'
        case 'B':
            return 'good!!'
        case 'C':
            return 'run!'
        case 'D':
            return 'slowly~'
        case _:
            return 'what?'
        
print(getGradeText(grade))