Комментарий [здесь](https://github.com/d-tsygolnik/exercises/blob/86a92ce53b98c46e0c8d05c2e09aef3dc15da315/python/algorithms/12_native_cache/native_cache.py#L45) можно удалить - имя переменной в команде однозначно указывает на сценарий, а комментарий ранее описывает контекст. -- п.1

Совершенно лишний неинформативный [комментарий](https://github.com/d-tsygolnik/exercises/blob/fceabb6088d51e461fd9319c89fb557e4b8880cb/python/code_practice/00_simple/ex_20/test_ex_20.py#L73)

---

Было:
```python
class TestPowerSetBasicMethods(unittest.TestCase):

    def test_main(self):

        # __init__()
        PS = PowerSet()
        self.assertEqual(PS.size(), 0)

        # put(value)
        PS.put("a")
        self.assertEqual(PS.size(), 1)

        # get(value)
        self.assertTrue(PS.get("a"))
        self.assertFalse(PS.get("b"))

        # get_val
        self.assertEqual(PS.get_val(), ["a"])

        # remove(value)
        self.assertFalse(PS.remove("b"))
        self.assertTrue(PS.remove("a"))
        self.assertEqual(PS.size(), 0)
        self.assertEqual(PS.get_val(), [])

```

Комментарии в [классе](https://github.com/d-tsygolnik/exercises/blob/b97b280a3827d68893014a195776aa0a8c09f095/python/algorithms/10_set/test_sets.py#L6) заменил на названия функций (п.1). Дополнительная выгода: тесты стали действительно модульными (один метод - один тест).

```python
class TestPowerSetBasicMethods(unittest.TestCase):

    def setUp(self):
        self.PS = PowerSet()

    def test_constructor(self):
        self.assertEqual(self.PS.size(), 0)

    def test_put(self):
        self.PS.put("a")
        self.assertEqual(self.PS.size(), 1)

    def test_get(self):
        self.assertTrue(self.PS.get("a"))
        self.assertFalse(self.PS.get("b"))

    def test_get_val(self):
        self.assertEqual(self.PS.get_val(), ["a"])

    def test_remove(self):
        self.assertFalse(self.PS.remove("b"))
        self.assertTrue(self.PS.remove("a"))
        self.assertEqual(self.PS.size(), 0)
        self.assertEqual(self.PS.get_val(), [])
```

---

Было:
```python

# ---- map() ----

def digitize_opt_1(n):
    return map(int, str(n)[::-1])

# ---- new_str = src_str[::-1] & list(iterable) ----

def digitize_opt_2(n):
    return [int(x) for x in str(n)[::-1]]
```

Написал подробнее, чтобы стороннему наблюдателю стало сразу понятно, для чего в одном файле решения 3 варианта функции (по п.2).
```python

# Решение с использованием функции map()
def digitize_opt_1(n):
    return map(int, str(n)[::-1])

# Решение с помощью сокращенной записи циклов 
# и генерации списка из объекта iterable
def digitize_opt_2(n):
    return list(int(x) for x in str(n)[::-1])
```

---

Комментарий нужно удалить и переработать код (по п. 1)

Было:
```python
if (total_time % (time_red + time_green)) <= time_red: # В случае остановки
    total_time += time_red - (total_time % (time_red + time_green))
```

Стало:
```python
stop_at_red_light = (total_time % (time_red + time_green)) <= time_red
if stop_at_red_light:
    total_time += time_red - (total_time % (time_red + time_green))
```

---

Было:
```python
def prepare_matrix(matrix_src):
    templ = []
    for i in matrix_src: # go through each row in matrix
        curr_row = []
        for j in i: # put each letter from the matrix_src[i] string into curr_row
            curr_row += [j]
        templ.append(curr_row)
    return templ
```

От обоих комментариев можно избавиться, переписав код с более наглядными именованиями.
По входным данным, наоборот, стоит добавить пояснение.

```python
def get_prepared_matrix(src_matrix): # src_matrix = [str1, str2, ..., strN]
    prep_matrix = []
    for row in src_matrix:
        new_row = []
        for char in row:
            new_row.append(char)
        prep_matrix.append(new_row)
    return prep_matrix
```
