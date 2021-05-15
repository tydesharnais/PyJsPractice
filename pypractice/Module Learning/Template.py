from string import Template

def Main():
    cart = []
    cart.append(dict(item="Coke", price="80", qty="2"))
    cart.append(dict(item="Heroin", price="30", qty="1"))
    cart.append(dict(item="Meth", price="35", qty="5"))

    t = Template("$qty x $item = $price")
    total = 0
    print('Cart:')
    for data in cart:
        print(t.substitute(data))
        total += data["price"]
    print("Total: "+str(total))

if __name__ == '__main__':
    Main()
