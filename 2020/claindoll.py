# 크레인 인형뽑기 게임




def solution(board, moves):
    answer = 0
    array = []
    N = len(board)
    for move in moves:
        move = move - 1
        for idx in range(N):
            if board[idx][move] != 0:
                array.append(board[idx][move])
                board[idx][move] = 0
                K = len(array)
                if K > 1 and array[K-1] == array[K-2]:
                    array.pop()
                    answer = answer + 1
                    array.pop()
                    answer = answer + 1
                break
    return answer

result = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(result)