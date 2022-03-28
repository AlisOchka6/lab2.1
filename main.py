def input_n():
    n = -1
    while n < 0:
        try:
            n = int(input("Введите количество гостей: "))
        except ValueError:
            print("Столько гостей не может быть!")
    return n

def one_piece(n):
    snip1 = n-1
    return snip1

def two_pieces(n):
    snip2 = round(n * 1.5)-1
    return snip2

def ten_pieces(n):
    snip3 = n + 9
    return snip3

def output_rezult(snip1, snip2, snip3):
    print(f"По одному куску: {snip1} \nПоловина гостей получит 2 куска: {snip2} \n10 кусков останется: {snip3} \n")

def main():
    n = input_n()
    output_rezult(one_piece(n), two_pieces(n), ten_pieces(n))

if __name__ == "__main__":
    main()