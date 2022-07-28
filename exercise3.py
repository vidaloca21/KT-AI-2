left = int(input('LEFT : '))
right = int(input('RIGHT : '))
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        p=0
        for j in range(1, i+1):
            if i % j: continue
            p += 1
        if p%2 == 0:
            answer += i
        else: answer += -i
    return answer

c = solution(left, right)
print(c)