def ConquestCampaign(N, M, L, battalion):

    def add_pair(n, m, targetDict):
        targetDict[str(n) + ", " + str(m)] = [n, m]
    
    def uniqueList(valuesList, targetDict):
        ind = 0
        for i in valuesList:
            if ind % 2 == 0:
                nc = i
            else:
                mc = i
                if targetDict.get(str(nc) + ", " + str(mc)) == None:
                    add_pair(nc, mc, targetDict)
            ind += 1

    ind = 0
    day = 0
    A = N*M

    capture_today = {}
    capture_done = {}
    capture_next_day = {}

    uniqueList(battalion, capture_today)

    while A > 0:
        for l in capture_today:
            # в словаре capture_today l:[height_index, width_index]
            # весь цилк -- перебор квадратов из списка захвата текущего дня (capture_today)
            #              с каждого квадрата берется информация о соседях:
            #              по каким направлениям можно продвинуться (moves_n, moves_m)
            #              координаты соседей заносятся в список захвата следующего дня
            ind = 0
            while ind < 2: # цикл повторяется 2 раза
                coord = capture_today[l][ind] # 1 раз - проверка соседей сверху и снизу
                                   # 2 раз - проверка соседей побокам
                # что обозначает moves_m / moves_n ??
                if coord == 1:
                    if ind == 0:
                        moves_n = coord + 1
                    else:
                        moves_m = coord + 1
                else:
                    if ind == 0:
                        if coord == N:
                            moves_n = coord - 1
                        else:
                            moves_n = [coord + 1, coord - 1]
                    else:
                        if coord == M:
                            moves_m = coord - 1
                        else:
                            moves_m = [coord + 1, coord - 1]
                ind += 1

            if type(moves_n) == type(1):
                add_pair(moves_n, capture_today[l][1], capture_next_day)
            else:
                for n in moves_n:
                    add_pair(n, capture_today[l][1], capture_next_day)

            if type(moves_m) == type(1):
                add_pair(capture_today[l][0], moves_m, capture_next_day)
            else:
                for m in moves_m:
                    add_pair(capture_today[l][0], m, capture_next_day)

        # в данный момент список захвата на сл. день - черновой
        # в нем могут быть уже захваченные узлы
        # удаляем квадраты если:
        # - они есть в списке текущего дня (capture_today)
        # - если они захвачены ранее (capture_done)

        already_captured = [] # заготовка списка на удаление
        for k in capture_next_day.keys():
            if (k in capture_done) or (k in capture_today):
                already_captured.append(k)

        for square in already_captured:
            del capture_next_day[square]

        # уменьшаем число свободных квадратов на кол-во захваченных в текущем дне
        A -= len(capture_today.keys())

        # добавляем квадраты текущего дня в общий список захваченных
        for k in capture_today.keys():
            capture_done[k] = capture_today[k]
        capture_today.clear()

        # готовим список захвата будущего текущего дня
        for k in capture_next_day.keys():
            capture_today[k] = capture_next_day[k]
        capture_next_day.clear()

        day += 1

    return day
