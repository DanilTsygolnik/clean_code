from ex_3_v2_classes import *

def get_squares_from_coord(squares_coord, map_used):
    '''Возвращает словарь из объектов класса Square'''
    squares_dict = {}
    width_index = 1
    while width_index <= len(squares_coord):
        width = squares_coord[width_index]
        height = squares_coord[width_index - 1]
        square_id = "".join(["h", str(height), "w", str(width)])
        square = map_used.access_square(square_id)
        squares_dict[square_id] = square
        width_index += 2
    return squares_dict 

def get_campaign_days(squares, campaign_map, day_num):
    is_captured = True
    # сперва захватить все (!) квадраты по плану на текущий день
    for i in squares:
        square = campaign_map.access_square(i)
        square.set_status(is_captured)
    # только после этого собирать свободных соседей на сл день
    squares_next_day = {}
    free_only = True
    for i in squares:
        square = campaign_map.access_square(i)
        square.set_status(is_captured)
        square_neighbors = square.get_neighbors(free_only)
        # добавить свободных соседей в список захвата на сл. день
        for neighbor in square_neighbors:
            neighbor_id = neighbor.get_id()
            squares_next_day[neighbor_id] = neighbor
    if squares_next_day == {}:
        return day_num
    return get_campaign_days(squares_next_day, campaign_map, day_num+1)

def ConquestCampaign(MAP_HEIGHT, MAP_WIDTH, num_capture_squares, first_day_coord):
    '''
    Функция возвращает целое число: за сколько дней будет захвачена вся карта
    
    Входные данные:
    MAP_HEIGHT, MAP_WIDTH - размеры карты
    num_capture_squares - число квадратов для высадки в первый день;
                          задает длину массива с координатами.
    first_day_coord - массив с координатами квадратов высадки;
                            [высота, ширина, высота_2, ширина_2, ...]
    '''
    campaign_map = CampaignMap(MAP_HEIGHT, MAP_WIDTH)
    first_day_squares = get_squares_from_coord(first_day_coord, campaign_map)
    day_num = 1
    return get_campaign_days(first_day_squares, campaign_map, day_num)
