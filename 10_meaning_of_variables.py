# ---------------------------------------------------------------------------

# было
xy_marker = 0
day = 0
LANDING_AREA_SIZE = MAP_HEIGHT*MAP_WIDTH

seize_coord_this_day = {}
S = {}
seize_coord_next_day = {}

del_coord_duplicates(battalion, seize_coord_this_day)

while LANDING_AREA_SIZE > 0:
    # ... // много кода

# стало
xy_marker = 0

seize_coord_this_day = {}
del_coord_duplicates(battalion, seize_coord_this_day)
seize_coord_next_day = {}

LANDING_AREA_SIZE = MAP_HEIGHT*MAP_WIDTH
while LANDING_AREA_SIZE > 0:
    # ... // много кода

# перенес инициализацию переменных (day, S), которые не используются в цикле
# перенес инициализацию LANDING_AREA_SIZE ближе к вызову

# ---------------------------------------------------------------------------

# было
def MassVote(num_candidates, votes):
    total_votes = 0
    max_num_votes = 0
    votes_index_cnt = 0
    for i in votes:
        total_votes += i
        # ... // много кода
    if winner != None:
        proportion = 100 * round((max_num_votes/total_votes), 3)
        # ... // много кода

# стало
def MassVote(num_candidates, votes):
    max_num_votes = 0
    votes_index_cnt = 0
    total_votes = 0 # перенес ближе к вызову
    for i in votes:
        total_votes += i
        # ... // много кода
    if winner != None:
        assert total_votes != 0 # добавил отладочный код
                                # ниже м.б. деление на ноль
        proportion = 100 * round((max_num_votes/total_votes), 3)
        # ... // много кода

# ---------------------------------------------------------------------------

# было
def Unmanned(distance, num_traffic_lights, track): 
    ride_duration = 0
    prev_light_location = 0
    for i in track:
        # ... // много кода
            if (ride_duration % (time_red + time_green)) <= time_red:
                ride_duration += time_red - (ride_duration % (time_red + time_green))
        # ... // много кода

# стало
def Unmanned(distance, num_traffic_lights, track): 
    ride_duration = 0
    prev_light_location = 0
    for i in track:
        # ... // много кода
            assert (time_red + time_green) != 0 # добавил отладочный код
                                                # ниже м.б. деление на ноль
            assert (time_red + time_green) != 0
            if (ride_duration % (time_red + time_green)) <= time_red:
                ride_duration += time_red - (ride_duration % (time_red + time_green))
        # ... // много кода

# ---------------------------------------------------------------------------
