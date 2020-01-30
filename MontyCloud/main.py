import random
import os
import requests


def start_app():
    flag = True

    link = 'http://127.0.0.1:5000'
    while flag:
        print("*** 1. Write Data ***\n*** 2. Read Data ***\n*** 3. Exit ***")
        choice =  int(input())

        if choice == 3:
            flag = False
            break
        elif choice == 1:
            name = input("Enter name: ")
            age = input("Enter age: ")

            PARAMS = {'name':name,
                      'age':age,
                      'action':choice}
            
            req = requests.get(url = link+'/log', params = PARAMS)

            data = req.json()

            print(data)
             
            
            
        elif choice == 2:
            name = input("Enter name you want to search: ")

            PARAMS = {'name':name,
                      'action': choice}

            req = requests.get(url = link+'/log', params = PARAMS)

            data = req.json()

            print(data)
            
            
            
            




if __name__ == "__main__":
    start_app()
    
    
