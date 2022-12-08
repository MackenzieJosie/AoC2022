input = open("input.txt", "r").read()

def solution(length):
    for i in range(length,len(input)):
        if (len(set([j for j in input[i-length:i]])) == length): return i
        
print(solution(4))
print(solution(14))