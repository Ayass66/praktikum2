class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def factorial_with_stack(n):
    stack = Stack()
    result = 1

    for i in range(n, 0, -1):
        stack.push(i)

    while not stack.is_empty():
        result *= stack.pop()

    return result

while True:
    print("Masukkan 1 untuk menghitng faktorial")
    print("Masukkan 0 untuk keluar dari program")
    print("------------------------------------")
    pilih = input("Masukkan pilihan : ")
    print("")
    if pilih == "1":
        number = int(input("Masukkan nilai faktorial : "))
        print("Faktorial dari", number, "adalah", factorial_with_stack(number)) 
        print("")
    elif pilih == "0":
        break
    else:
        print("Angka yang anda masukkan tidak valid")
        print("") 
