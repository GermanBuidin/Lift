import copy
from random import randint, choice


def go(people, elevator, floor, past_floor):
    man_on_floor = copy.deepcopy(people[floor])
    if floor > past_floor and floor != len(people) or floor == 1:
        for i in man_on_floor:
            if len(elevator) < 5 and i > floor:
                elevator.append(i)
                people[floor].remove(i)
            else:
                break
    else:
        for i in man_on_floor:
            if len(elevator) < 5 and i < floor:
                elevator.append(i)
                people[floor].remove(i)
            else:
                break
    return {'elevator': elevator, 'people': people}


def get_go_out(floor, elevator):
    left_in_elevator = [i for i in elevator if i != floor]
    go_out = [i for i in elevator if i == floor]
    print(f'go out: {len(go_out)} passengers')
    return {'in_elevator': left_in_elevator, 'out_elevator': go_out}


def get_next_floor(floor, elevator, floors, past_floor):
    if floor > past_floor and floor != floors or floor == 1:
        try:
            next_floor = min(elevator)
        except ValueError:
            print(f'go on {floor + 1} floor')
            next_floor = floor + 1
    else:
        try:
            next_floor = max(elevator)
        except ValueError:
            print(f'go on {floor - 1} floor')
            next_floor = floor - 1
    return next_floor


def get_all_people(in_out_elevator, data_elevator, floor):
    if len(in_out_elevator) != 0:
        for n in in_out_elevator:
            if floor == 1:
                data_elevator[floor].append(randint(2, len(data_elevator)))
            elif floor == len(data_elevator):
                data_elevator[floor].append(randint(1, len(data_elevator)-1))
            else:
                floors = (randint(1, floor - 1), randint(floor + 1, len(data_elevator)))
                new_floor = choice(floors)
                data_elevator[floor].append(new_floor)
    return data_elevator
