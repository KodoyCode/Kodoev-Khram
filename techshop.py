tehnika={
    "telefon":300,
    "televizor":300
}

while True:
    print(f"List of items in the shop: {tehnika}")
    item=input("write new item name: ")
    if item=="exit":
        print("exiting..")
        break
    elif item in tehnika:
        del tehnika[item]
        print(f"removed item from shop: {item}")
    else:
        item_price=input("write item price: ")
        price = int(item_price)

        tehnika[item]=price
        print(f'added: {item}, price: {price}')

        print(tehnika)

        tehnika_sum=sum(tehnika.values())
        print(f"total price: {tehnika_sum}")