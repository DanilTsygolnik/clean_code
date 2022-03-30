Было: переменная `track` - это многомерный массив. Хотя происходит последовательное обращение к элементам, параметры каждого из них приходится извлекать по индексу.

```python
...
for i in track:
    if i[0] > total_distance:
        continue
    else:
        curr_light_location = i[0]
        time_red = i[1]
        time_green = i[2]
...
```

Альтернатива: создать отдельный класс Checkpoint для хранения параметров контрольных точек.Получим массив объектов, свойства которых будут храниться в соответствующих полях.

```python

class Checkpoint:

    def __init__(self, DISTANCE_COVERED, RED_SIG_DURATION, GREEN_SIG_DURATION):
        self.distance_from_start = DISTANCE_COVERED
        self.red_sig_duration = RED_SIG_DURATION
        self.green_sig_duration = GREEN_SIG_DURATION
        

...
for checkpoint in track:
    if checkpoint.distance_from_start > totat_distance:
        continue
    else:
        # благодаря полям класса Checpoint далее можно не
        # создавать переменные, а сразу использовать значения
        # нужных полей в расчетах
...
```

---

Было: рассчетные значения размеров матрицы заносятся в заранее созданный список, что само по себе вынуждает использовать обращение по индексам.

```python
sizes = ['rows', 'columns']
string_length = letters_in_message **(1/2)
string_length_x10 = string_length*10
if string_length == string_length_x10 // 10:
    sizes[0] = sizes[1] = int(string_length)
else:
    sizes[0] = round_custom(string_length)
    sizes[1] = round_custom(string_length, True)
if sizes[0]*sizes[1] < letters_in_message:
    sizes[0] += 1
return sizes
```

Стало: задействовать 2 переменные для высоты и ширины, а список на вывод создать в самом конце

```python
...
# от переменной sizes избавились
string_length = letters_in_message **(1/2)
string_length_x10 = string_length*10
if string_length == string_length_x10 // 10:
    matrix_height = matrix_width = int(string_length)
else:
    matrix_height = round_custom(string_length)
    matrix_width = round_custom(string_length, True)
if matrix_height*matrix_width < letters_in_message:
    matrix_height += 1
return [matrix_height, matrix_width]
```

---

Было: в словаре хранятся пары `id--[coord_x, coord_y]`, чтение координат приходится осуществлять обращением по индексу.

```python
dx = abs(point[next_point_id][0] - point[current_point_id][0])
dy = abs(point[next_point_id][1] - point[current_point_id][1])
```

Альтернатива: использовать класс Point для хранения координат.

```python
class Point:
    
    def __init__(self, point_id, coord_x, coord_y):
        self.id = point_id
        self.x = coord_x
        self.y = coord_y

points = {} # словать пар id--объект класса Point
current_point = points[current_point_id]
next_point = points[next_point_id]
dx = abs(next_point.x - current_point.x)
dy = abs(next_point.y - current_point.y)
```

---

Аналогичные рассуждениями руководствовался, переписывая [решение](https://github.com/d-tsygolnik/exercises/blob/aea095b4f7b1c6bb06b6d8f73339166d1b471436/python/code_practice/00_simple/ex_3/ex_3_sol.py#L31) с введением [классов](https://github.com/d-tsygolnik/clean_code/blob/ex_3_v1_upgrade/ex_3_v2_classes.py) для карты и квадратов.

---

Вообще, интуитивно всегда старался избегать обращения по индексам, т.к. это создает дополнительные трудности. Особенно когда приходится возвращаться к коду после перерыва и пытаться разобраться в безобразиях вроде `array[i][j]`.

Вскоре после знакомства с библиотекой `unittest` выяснил, что для создания контрольных наборов данных гораздо удобнее пользоваться множествами, нежели списками. Продолжаю держаться такого подхода (как [здесь](https://github.com/d-tsygolnik/clean_code/blob/bceb2f98611c2eeb23e3f6d951f012691bfecb0e/test_classes.py#L77), например).
