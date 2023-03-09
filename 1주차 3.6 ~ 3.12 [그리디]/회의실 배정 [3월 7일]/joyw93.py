N = int(input())

rooms = []
selected_rooms = []
count = 0

for i in range(N):
    conf = tuple(map(int, input().split()))
    rooms.append(conf)

sorted_rooms = sorted(rooms, key=lambda x: (x[1], x[0]))
first_room = sorted_rooms.pop(0)
selected_rooms.append(first_room)

for room in sorted_rooms:
    start = room[0]
    end = room[1]
    if(start < selected_rooms[-1][1]):
        continue
    else:
        selected_rooms.append(room)

print(len(selected_rooms))