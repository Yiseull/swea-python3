def check(film):
    for i in range(W):
        proper = film[0][i]
        cnt = 0
        for j in range(D):
            if film[j][i] == proper:
                cnt += 1
                if cnt >= K:
                    break
            else:
                proper = film[j][i]
                cnt = 1
        if cnt < K:
            return False
    return True


def change_proper(index, cnt, film):
    global answer
    if answer <= cnt:
        return

    if check(film):
        answer = min(answer, cnt)
        return

    for i in range(index, D):
        tmp = film[i][:]
        for j in range(W):
            film[i][j] = 0
        change_proper(i + 1, cnt + 1, film)
        for j in range(W):
            film[i][j] = 1
        change_proper(i + 1, cnt + 1, film)
        film[i] = tmp


T = int(input())
for test_case in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    answer = 13
    change_proper(0, 0, film)
    print('#' + str(test_case) + ' ' + str(answer))
