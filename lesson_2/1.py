from datetime import date

user_date = date(
    *(int(i) for i in input("Напишите дату через пробел в формате год, месяц, день: ")
    .split())
    )

if (date.today() - user_date).days >= 6574:
    print("Челику 18")
else:
    print("Челику нету 18")