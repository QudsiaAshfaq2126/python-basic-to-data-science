
import statistics

stocks = {
    'info': [600,630,620],
    'ril': [1430,1490,1567],
    'mtl': [234,180,160]
}

def print_all():
    for stock,p_l in stocks.items():
        avg = statistics.mean(p_l)
        print(f"{stock} ==> {p_l} ==> avg: ")


def add():
    s = input("Enter a stock  to add:")
    p = input("Enter price of this stock:")
    p=float(p)
    if s in stocks:
        stocks[s].append(p)
    else:
        stocks[s] = [p]
    print_all()


def main():
    op=input("Enter operation (print, add or amend):")
    if op.lower() == 'print':
        print_all()
    elif op.lower() == 'add':
        add()
    else:
        print("Unsupported operation:",op)

if __name__ == '__main__':
    main()

