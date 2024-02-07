from heapq import heappop, heappush

def solution(book_time):
    rooms = []
    room_cnt = 0
    
#     for b in book_time:
#         for i in range(2):
#             if i == 1:
#                 b[i] = int(b[i].replace(":",""))
#             else:
#                 b[i] = int(b[i].replace(":",""))
                
    for b in book_time:
        for i in range(2):
            b[i] = int(b[i].split(":")[0]) * 60 + int(b[i].split(":")[1])
            
    book_time.sort()

    for s, e in book_time:
        if not rooms:
            heappush(rooms,e)
            room_cnt += 1
            continue
        if rooms[0] <= s:
            heappop(rooms)
        else:
            room_cnt += 1
        heappush(rooms,e+10)
    
    return room_cnt

book_time = [["10:00", "10:20"], ["09:00", "09:20"], ["09:20", "09:40"], ["09:40", "10:00"]]


print(solution(book_time))