class Buffer:
    def __init__(self):
        self.buf = []

    def add(self, *a):
        for i in a:
            self.buf.append(i)
        while len(self.buf) >= 5:
            self.buf_head = self.buf[0:5]
            self.sum = 0
            for i in range(len(self.buf_head)):
                self.sum += self.buf_head[i]
                self.buf.pop(0)
            print(self.sum)

    def get_current_part(self):
        return self.buf

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]