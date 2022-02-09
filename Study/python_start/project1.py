from abc import abstractmethod
import sqlite3
import pandas as pd

# 1주일 동안 다녔던 가게들에서 가계부 작성하는 프로그램 개발/ 가게 종류 : 신발가게 (나이키, 아디다스, 퓨마, 르꼬끄), 옷가게 (샤넬, 등등 5곳 ) , 음식 가게 (음식 종류 10개) 에 대한 excel 간단히 만들고 연동
# 두번째 플젝, 비동기 를 보여주고자 강식당처럼 프로그램 만들어보기 
class Customer:
    
    def __init__(self, name):
        self.name = name
        self.turn = 0
        self.lst = dict()
        self.foodlst = dict
        print("New person has been made.")

    def get_count(self):
        return self.turn
    
    def get_account(self):
        
        return 
    def get_information(self):
        
        return

    def __str__(self):

        return  '{0} : {1}'.format(self.name, self.foodlst)
        
class store:
    @abstractmethod
    def make_list(self):
        pass

class Ordinary(store):
    def make_list(self):
        return super().make_list()

class rest(store):
    def make_list(self):
        return super().make_list()



if __name__ == "__main__":

    cv = pd.DataFrame
    print("How many customers?")
    number = int(input())
    lst = dict()
    flag = 0
    for i in range(number):
        temp = input("Name: ")
        lst[temp] = Customer(temp)
        flag = int(input("How many foods you enjoyed?"))
        for j in range(flag):
            print("What did you eat when you were at that place?")
            