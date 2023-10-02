def solution(board, moves):
    basket = []
    count = 0
    
    for move in moves:
        for j in range(len(board)):
            if board[j][move-1] != 0:
                basket.append(board[j][move-1])
                board[j][move-1] = 0
                
                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop(-1)
                        basket.pop(-1)
                        count += 2
                break
    return count