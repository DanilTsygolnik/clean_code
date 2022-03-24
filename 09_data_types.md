// было - стало        
```python
result - STRING_IS_VALID
result - DATA_IS_SORTED
```
// Комментарии        
Булева константа с новым именем повысит ясность кода на предмет результата работы функции, например:
`return STRING_IS_VALID` и `return not STRING_IS_VALID`

---

// было
```python
if string[0] == '*' and string[len(string)-1] == '*':
    ...
```
// стало
```python
VALID_HEAD_AND_TAIL = (string[0] == '*' and string[len(string)-1] == '*')
if VALID_HEAD_AND_TAIL:
    ...
```


// было
```python
if command[0] == '1':
    ...
if command[0] == '2':
    ...
if command[0] == '3':
    ...
if command[0] == '4':
    ...
if command[0] == '5':
    ...
```
// стало
```python
COMMAND_ADD = (command[0] == '1')
COMMAND_DELETE = (command[0] == '2')
COMMAND_GET = (command[0] == '3')
COMMAND_UNDO = (command[0] == '4')
COMMAND_REDO = (command[0] == '5')

if COMMAND_ADD:
    ...
if COMMAND_DELETE:
    ...
if COMMAND_GET:
    ...
if COMMAND_UNDO:
    ...
if COMMAND_REDO:
    ...
```
// Комментарии        
Замена длинного логического выражения на константу добавит строки кода, но упростит разбирательство позднее.

---

// было - стало           
```python
"(" - BRACKET_OPEN
")" - BRACKET_CLOSE
```
// Комментарии        
Избавился от магических символов

---

```python
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(response.text)
```
// Комментарии        
В соответствии с рекомендацией п.4 ввел кодировку Unicode в явном виде.
