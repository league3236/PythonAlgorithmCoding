

def solution(boxes):
    answer = 0
    for i in range(len(boxes)):
        if boxes[i][0] != boxes[i][1]:
            for j in range(i+1,len(boxes)):
                if boxes[j][0] != boxes[j][1]:
                    if boxes [i][0] == boxes[j][0]:
                        tmp = boxes[i][1]
                        boxes[i][1] = boxes[j][0]
                        boxes[j][0] = tmp
                        break
                    elif boxes[i][0] == boxes[j][1]:
                        tmp = boxes[i][1]
                        boxes[i][1] = boxes[j][1]
                        boxes[j][1] = tmp
                        break
                    elif boxes[i][1] == boxes[j][0]:
                        tmp = boxes[j][0]
                        boxes[j][0] = boxes[i][0]
                        boxes[i][0] = tmp
                    elif boxes[i][1] == boxes[j][1]:
                        tmp = boxes[i][0]
                        boxes[i][0] = boxes[j][1]
                        boxes[j][1] = tmp 
                else:
                    continue
    for i in boxes:
        if i[0] != i[1]:
            answer = answer + 1
    return answer
