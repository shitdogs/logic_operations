discount = (5, 10, 15, 20)
discount_range = [(i, i+4999) for i in range(0, 20000, 5000)]
price = int(input("Введите стоимость: "))

for d_range, dis in zip(discount_range, discount):
    if d_range[0] < price < d_range[1]:
        print(f"Стоимость со скидкой - {price - price*dis/100}")
        break
else:
    print("Этот товар не имеет скидки, так как на его производство уходит много ресурсов")