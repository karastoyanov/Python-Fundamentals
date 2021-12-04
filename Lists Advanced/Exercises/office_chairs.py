rooms_number = int(input())
rooms = []
total_free_chairs = 0

for index in range(rooms_number):
    # calculate number of chairs and persons in each room
    rooms = input().split(" ")
    chairs = len(rooms[0])
    persons = int(rooms[-1])
    # calculate how many free chairs in each room
    free_chairs_in_rooms = chairs - persons
    total_free_chairs += free_chairs_in_rooms
    # cases that chairs are not enough
    if free_chairs_in_rooms < 0:
        needed_chairs = abs(persons - chairs)
        print(f"{needed_chairs} more chairs needed in room {int(index+1)}")
        


if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")
