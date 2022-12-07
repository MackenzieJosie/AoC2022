input = open("input.txt", "r").read()

def solution(length):
    for i in range(length,len(input)):
        combo = set([j for j in input[i-length:i]])
        if (len(combo) == length):
            return i         
        
print(solution(4))
print(solution(14))