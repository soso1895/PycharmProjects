import threading
import time

#
# def greet(index):
#     print('hello world-%d' % index)
#     time.sleep(0.5)
#
#
# def line_run():
#     for x in range(5):
#         greet(x)
#
#
# def async_run():
#     for x in range(5):
#         th = threading.Thread(target=greet, args=[x])
#         th.start()
import random


def Procuder():
    while True:
        random_money = random.randint(10, 100)
def customer():
    while True:
        random_money = random.randint(10, 100)



if __name__ == '__main__':
    # line_run()
    async_run()
