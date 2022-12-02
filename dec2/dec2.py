input = open("input.txt", "r").read().split("\n")
score = 0

for i in range(0,len(input)-1):
    match(input[i][2]):
        case "X":
            score += 1
            match(input[i][0]):
                case "A":
                    score += 3
                case "B":
                    score += 0
                case "C":
                    score += 6
        case "Y":
            score += 2
            match(input[i][0]):
                case "A":
                    score += 6
                case "B":
                    score += 3
                case "C":
                    score += 0
        case "Z":
            score += 3
            match(input[i][0]):
                case "A":
                    score += 0
                case "B":
                    score += 6
                case "C":
                    score += 3

print(score)