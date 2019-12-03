"""
Written by: Jonas Vander Vennet
on: 2019/12/04
Answer: 151754
"""


def sort_routine(routine):
    return sorted(routine, key=lambda x: x[:18])


def get_guard_id_from_step(step):
    return step.split('#')[-1].split(' ')[0]


def get_minutes(time):
    return int(time[-3:-1])


def get_most_sleep(routine):
    guard_sleeps = {}
    current_guard = None
    started_sleeping_time = None
    for step in routine:
        if 'Guard' in step:
            current_guard = get_guard_id_from_step(step)
            if current_guard not in guard_sleeps.keys():
                guard_sleeps[current_guard] = {}
            started_sleeping_time = None
        elif 'falls asleep' in step:
            started_sleeping_time = step[:18]
        elif 'wakes up' in step:
            for i in range(get_minutes(started_sleeping_time), get_minutes(step[:18])):
                if str(i) not in guard_sleeps[current_guard].keys():
                    guard_sleeps[current_guard][str(i)] = 0
                guard_sleeps[current_guard][str(i)] += 1

    most_sleep = None
    guard = None
    for guard_id, sleep_minutes in guard_sleeps.items():
        sleep_time = sum(sleep_minutes.values())
        if most_sleep is None or sleep_time > most_sleep:
            most_sleep = sleep_time
            guard = guard_id
    most_sleep = None
    best_minute = None
    for minute, amount in guard_sleeps[guard].items():
        if most_sleep is None or amount > most_sleep:
            most_sleep = amount
            best_minute = minute
    return int(guard), int(best_minute)


def main():
    test_values = [
        ([
            '[1518-11-01 00:00] Guard #10 begins shift',
            '[1518-11-01 00:05] falls asleep',
            '[1518-11-01 00:25] wakes up',
            '[1518-11-01 00:30] falls asleep',
            '[1518-11-01 00:55] wakes up',
            '[1518-11-01 23:58] Guard #99 begins shift',
            '[1518-11-02 00:40] falls asleep',
            '[1518-11-02 00:50] wakes up',
            '[1518-11-03 00:05] Guard #10 begins shift',
            '[1518-11-03 00:24] falls asleep',
            '[1518-11-03 00:29] wakes up',
            '[1518-11-04 00:02] Guard #99 begins shift',
            '[1518-11-04 00:36] falls asleep',
            '[1518-11-04 00:46] wakes up',
            '[1518-11-05 00:03] Guard #99 begins shift',
            '[1518-11-05 00:45] falls asleep',
            '[1518-11-05 00:55] wakes up',
        ], 240),
    ]

    for routine, answer in test_values:
        routine = sort_routine(routine)
        guard_id, best_minute = get_most_sleep(routine)
        assert(guard_id * best_minute == answer)

    with open('../input.txt') as ifp:
        routine = ifp.readlines()
    routine = sorted(routine)
    guard_id, best_minute = get_most_sleep(routine)
    print(guard_id * best_minute)


if __name__ == '__main__':
    main()
