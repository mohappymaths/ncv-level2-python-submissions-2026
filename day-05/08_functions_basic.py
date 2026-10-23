# def place_order(item):
#     print(f'Order Placed. Your order is: {item}')
#     
# #eggs =>4
# #tot = (base_price + 5) * 1.5
# def calculate_total(item):
#     price = 25.50
#     VAT = 0.15
#     totalprice = ((price + len(item))*1.5)
#     return totalprice
#     
# def get_order():
#     print('Preparing Order')
#     return 'Collect Your Order'
# 
# myFood = input('What would you like to eat?')
# 
# place_order(myFood)
# 
# print(get_order())
# 
# ordertotal = calculate_total(myFood)
# print(f'Your order costs: R{ordertotal}')

#PIGEONHOLES (1-D LIST)
# marks = [62, 75, 48, 91, 70]
# 
# print("First:", marks[0])
# print("Third:", marks[2])
# print("Number of marks:", len(marks))

marks = []

mark = int(input('Enter mark (or -1 to stop): '))

while mark!= -1:
    marks.append(mark)
    mark = int(input('Enter mark (or -1 to stop): '))
    
print(f'Our list has {len(marks)} elements')

for x in range(len(marks)):
    print(marks[x])
