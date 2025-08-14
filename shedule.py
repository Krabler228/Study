from datetime import datetime, timedelta

trudyaga_1 = {
    "name": "Pupa",
}

trudyaga_2 = {
    "name": "lupa",
}

trudyaga_3 = {
    "name": "Zalupa",
}



trudyaga_list = [trudyaga_1, trudyaga_2, trudyaga_3]
today = datetime.today()
starting_day = (today - timedelta(days=21)).replace(hour=0, minute=0, second=0, microsecond=0) #starting_day = datetime.strptime("2025-11-01", "%Y-%m-%d")


def shedule_start(starting_day, trudyaga_list):
    ending_day = starting_day + timedelta(days=7)
    cur = starting_day
    iterations = 0
    while cur <= ending_day:
        for trudyaga in trudyaga_list:
            trudyaga["vacation"] = None
            trudyaga["notice check"] = False
        cur += timedelta(days=1)
        iterations += 1
    return iterations


def notice(starting_day, trudyaga_list):
    starting_day += timedelta(days=7)
    ending_day = starting_day + timedelta(days=7)
    cur = starting_day
    iterations = 0
    while cur <= ending_day:
        for trudyaga in trudyaga_list:
            if trudyaga["notice check"] is False:
                trudyaga["notice check"] = True
            else:
                pass
        cur += timedelta(days=1)
        iterations += 1
    return iterations

def select_vac(starting_day, trudyaga_list):
    starting_day += timedelta(days=14)
    ending_day = starting_day + timedelta(days=7)
    cur = starting_day
    iterations = 0
    while cur <= ending_day:
        for trudyaga in trudyaga_list:
            if trudyaga["vacation"] is None:
                trudyaga["vacation"] = [
                    {
                        "start": datetime.strptime("2026-07-01", "%Y-%m-%d"),
                        "end": datetime.strptime("2026-07-14", "%Y-%m-%d"),
                    },
                    {
                        "start": datetime.strptime("2026-09-01", "%Y-%m-%d"),
                        "end": datetime.strptime("2026-09-14", "%Y-%m-%d"),
                    },
                ]
            else:
                pass
        cur += timedelta(days=1)
        iterations = 0
    return iterations

print("starting_day:", starting_day.date())
print("shedule_start iterations:", shedule_start(starting_day, trudyaga_list))
print("notice iterations:", notice(starting_day, trudyaga_list))
print("select_vac iterations:", select_vac(starting_day, trudyaga_list))

print(trudyaga_list)



