selling = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]
def sum_selling(product_sold):
    product_sum = 0
    for sold in product_sold:
        product_sum += sold
    return product_sum

def avg_selling(product_sold):
    product_sum = 0
    for sold in product_sold:
        product_sum += sold
        avg=product_sum/len(product_sold)
    return avg

for every_item in selling:
    item = sum_selling(every_item['items_sold'])
    avg = avg_selling(every_item['items_sold'])
    print(f"сумма продаж {every_item['product']}: {item}")
    print(f"среднее число продаж {every_item['product']}: {avg}")

all_item_sum = 0
for every_item in selling:
    all_item_sum = all_item_sum + sum_selling(every_item['items_sold'])
    avg_summ = all_item_sum /len(selling)
print(f"сумма всех продаж: {all_item_sum}")
print(f"среднее число всех продаж: {avg_summ}")
