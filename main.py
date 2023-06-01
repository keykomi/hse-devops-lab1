import datetime


def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


surname, name, patronymic = input("Введите ФИО через пробел: ").split()
birth_date = input("Введите дату рождения в формате дд.мм.гггг: ")

birth_date_obj = datetime.datetime.strptime(birth_date, '%d.%m.%Y').date()

age = calculate_age(birth_date_obj)

gender = ""
if patronymic.endswith(("ич", "евич", "ович")):
    gender = "мужской"
else:
    gender = "женский"

print(surname, name[0] + ".", patronymic[0] + ".", gender, str(age) + " " + ("год" if age % 10 == 1 and age % 100 != 11 else "года" if 2 <= age % 10 <= 4 and not (12 <= age % 100 <= 14) else "лет"))
