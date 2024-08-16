# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
        
    second_score = sorted(set(scores))[1]
    ans = []
    for student in range(len(names)):
        if scores[student] == second_score:
            ans.append(names[student])
    ans.sort()
    for name in ans:
        print(name)