from abc import abstractmethod
import sqlite3
import pandas as pd

# 1���� ���� �ٳ�� ���Ե鿡�� ����� �ۼ��ϴ� ���α׷� ����/ ���� ���� : �Ź߰��� (����Ű, �Ƶ�ٽ�, ǻ��, ������), �ʰ��� (����, ��� 5�� ) , ���� ���� (���� ���� 10��) �� ���� excel ������ ����� ����
# �ι�° ����, �񵿱� �� �����ְ��� ���Ĵ�ó�� ���α׷� ������ 
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
            