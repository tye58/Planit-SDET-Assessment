Menu=[
  {"name":"wild burger joint","soda":1, "fries":2, "burger":15, "shake":3, "cookie":5, "chicken strips":6},
  {"name":"Awesome pizza place","pepperoni pizza":20, "Hawaiian pizza":21}
]


def get_order():
    current_order = {"name":"","recipe":"","price":None,}
    while True:
        print("Input order: ")
        order = input()
        have_or_not = False
        for i in range(0,len(Menu)):
            if order in Menu[i]:
            
                current_order["name"]=Menu[i]["name"]
                current_order["recipe"]=order
                current_order["price"]=Menu[i][order]
                have_or_not=True
                           
        if have_or_not==False:
            print("I'm sorry, we don't serve that.")
            
        if have_or_not:
            
            output_order(current_order)


def output_order(order_list):
    
    print(f'{order_list["name"]},{order_list["recipe"]},${order_list["price"]}')


def main():
    order = get_order()
    


if __name__ == "__main__":
    main()