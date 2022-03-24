Задание 3.1

```python
class CustomColor:

    def __init__(self):
        self.rgb = None
        self.hex = None

    def convert_rgb_to_hex(red, green, blue: int) -> str:
        ...
        return hex_code

    def convert_hex_to_rgb(hex_code: str) -> list:
        ...
        return rgb_values_list

    def create_using_rgb(self, red, green, blue):
        self.rgb = [red, green, blue]
        self.hex = convert_rgb_to_hex(red, green, blue)

    def create_using_hex(self, hex_code):
        self.hex = hex_code
        self.rgb = convert_hex_to_rgb(hex_code)

    def get_rgb_code(self):
        return self.rgb

    def get_hex_code(self):
        return self.hex


user_bg_color = CustomColor.create_using_rgb(192,192,192)
user_text_color = CustomColor.create_using_hex("#000000")
```

```python
class Student:

    def __init__(self):
        self.FirstName = None
        self.SecondName = None
        self.Faculty = None
        self.Year = None
        self.Semester = None

    def create_manually(self, FirstName, SecondName, Faculty, Year, Semester):
        self.FirstName = FirstName
        self.SecondName = SecondName
        self.Faculty = Faculty
        self.Year = Year
        self.Semester = Semester
    
    def create_by_copy(self, student):
        self.FirstName = student.FirstName
        self.SecondName = student.SecondName
        self.Faculty = student.Faculty
        self.Year = student.Year
        self.Semester = student.Semester


new_student = Student.create_by_copy(old_student)
```
