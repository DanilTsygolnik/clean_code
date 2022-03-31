# Ненужные комментарии (п. 4)
def test_get_all_indexes(self):
    #  0123456789
    # "5==ooooooo" --> []
    # "abc=7==hdj" --> []
    # "axxb6===4x" --> [[5,8]]
    # "9===1===9=" --> [[1,4], [5,8]]

    self.assertEqual(ex_26_sol.get_all_indexes("5==ooooooo"), [])
    self.assertEqual(ex_26_sol.get_all_indexes("abc=7==hdj"), [])
    self.assertEqual(ex_26_sol.get_all_indexes("axxb6===4x"), [[5,8]])
    self.assertEqual(ex_26_sol.get_all_indexes("9===1===9="), [[1,4], [5,8]])
# Информация о корректных результатах видна в assert'ах
# Сведения о нумерации индексов должны быть отражены в коде функции get_all_indexes()



# По п. 12 нужно использовать правильные названия переменных
for i in s_res: # для каждой i-й строки из tanks...
    for j in i: # ...среди всех найденных позиций i-й строки в map...

# Например
for string in output_strings:
    for char in string:



# п. 7 избыточные комментарии
# можно попытаться воспользоваться функциями, чтобы суть операций стала очевидной
while i < H2:
    j = i  # не каждое слово из массива words имеет смысл искать с самой первой строки в strings 
    search_res_line = []
    while j <= H1 - H2 + i: # не каждое слово из массива words имеет смысл искать ниже определенной строки в strings



# п. 11 закоментированный код

# id1 "h1w1" -- ["h1w2", "h2w1",] 
# id2 "h2w1" -- ["h1w1", "h2w2", "h3w1"]
# id3 "h3w1" -- ["h2w1", "h3w2",]
# id4 "h1w2" -- ["h1w1", "h2w2", "h1w2",]
# id5 "h2w2" -- ["h2w1", "h1w2", "h2w3", "h3w2"]
# id6 "h3w2" -- ["h3w1", "h2w2", "h3w3",]
# id7 "h1w3" -- ["h1w2", "h2w3",]
# id8 "h2w3" -- ["h1w3", "h2w2", "h3w3"]
# id9 "h3w3" -- ["h3w2", "h2w3",]
def test_get_neighbors_squares_ids__id1(self):
    neighbors_ids_correct = set(["h1w2", "h2w1",] )
    neighbors_ids_test = self.map3x3.get_square_neighbors_ids("h1w1")
    self.assertEqual(neighbors_ids_test, neighbors_ids_correct)

# В данном случае нужно было активно использовать коммиты:
# - наметить содержание тестов приведенным комментарием;
# - заменить поочередно или разом, с помощью макроса, все комментарии на модульные тесты;
# - для каждой итерации создавать коммит.
