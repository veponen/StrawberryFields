import time
'''
Simple Calculator for mocking
'''
class Calculator:
    def sum(self, a, b):
        time.sleep(10) # long running process
        return a + b

def calculator( a, b):
    return a + b