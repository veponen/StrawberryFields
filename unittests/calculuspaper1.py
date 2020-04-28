import time
'''
Simple Calculator for mocking
'''
class Calculator:
    def sum(self, a, b):
        #time.sleep(10) # long running process
        self.sleeping10second()
        return a + b

    def sleeping10second(self):
        time.sleep(10)

def calculator( a, b):
    return a + b