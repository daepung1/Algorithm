def solution(price, money, count):
    all_price=0

    for i in range(count):
        all_price=all_price+(i+1)*price
    if all_price-money>0:
        return all_price-money
    else:
        return 0
    

price=3
money=20
count=2
all_price=0

for i in range(count):
    all_price=all_price+(i+1)*price
if all_price-money>0:
    print(all_price-money)
else:
    print(0)