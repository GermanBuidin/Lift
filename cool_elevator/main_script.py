from cool_elevator.data_generator import DataGenerator
from cool_elevator.elevator import get_next_floor, get_go_out, go, get_all_people


class Move:
    def go_into_elevator(self, people, floor, elevator, past_floor):
        in_out_elevator = get_go_out(floor, elevator)
        data_elevator = go(people=people, elevator=in_out_elevator['in_elevator'], floor=floor, past_floor=past_floor)
        next_floor = get_next_floor(floor, in_out_elevator['in_elevator'], len(people), past_floor)
        people = get_all_people(in_out_elevator['out_elevator'], data_elevator['people'], floor)
        return {'in_elevator': data_elevator['elevator'], 'on_floors': people, 'next_floor': next_floor}


class Output:
    def finish(self, elevator, floor):
        print(f'passengers in elevator: {len(elevator)} passengers')
        print(f'floors for passengers: {sorted(set(elevator))}')
        print(f'next floor: {floor}')
        print('')


def run_lift(steps):
    floor = 1
    past_floor = 0
    elevator = []
    data_elevator = DataGenerator().generation_all_data()
    for i in range(steps):
        print(f'**** Step {i+1} ****')
        print(f'floor: {floor}')
        passengers = Move().go_into_elevator(data_elevator, floor, elevator, past_floor)
        data_elevator = passengers['on_floors']
        elevator = passengers['in_elevator']
        past_floor = floor
        floor = passengers['next_floor']
        Output().finish(elevator, floor)


run = run_lift(int(input('input number steps: ')))
