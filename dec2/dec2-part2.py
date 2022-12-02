input = open("input.txt", "r").read().split("\n")
score = 0

for i in range(0,len(input)-1):
    match(input[i][2]):
        case "X":
            score += 0
            match(input[i][0]):
                case "A":
                    score += 3
                case "B":
                    score += 1
                case "C":
                    score += 2
        case "Y":
            score += 3
            match(input[i][0]):
                case "A":
                    score += 1
                case "B":
                    score += 2
                case "C":
                    score += 3
        case "Z":
            score += 6
            match(input[i][0]):
                case "A":
                    score += 2
                case "B":
                    score += 3
                case "C":
                    score += 1

print(score)