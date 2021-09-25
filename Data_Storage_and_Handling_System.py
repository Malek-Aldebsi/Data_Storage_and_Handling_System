import pandas as pd
import os.path
class Car:

  def __init__(self, ID, Model, Year_of_Production, Kilometers_traveled, Price):
        self.ID = ID
        self.Model = Model
        self.Year_of_Production = Year_of_Production
        self.Kilometers_traveled = Kilometers_traveled
        self.Price = Price

  global cars_system
  if os.path.isfile('D:\pycharm projects\cars_system.csv'):
    cars_system = pd.read_csv('D:\pycharm projects\cars_system.csv')
  else:
    cars_system = pd.DataFrame(columns=['ID','Model','Year_of_Production','Kilometers_traveled','Price'])
    cars_system.to_csv('cars_system.csv', index=False)
del_IDs=[]


def Add():
    def generateID():
        if len(del_IDs) != 0:
            ID = del_IDs[0]
            del_IDs.pop(0)
        else:
            ID = len(cars_system) + 1
        return ID

    ID = generateID()
    Model = input('Your car model is: ')
    Year_of_Production = input('Year of production of your car is: ')
    Kilometers_traveled = input('How many Kilometers does your car traveled: ')
    Price = input('Your car price is: ')

    new_car = Car(ID, Model, Year_of_Production, Kilometers_traveled, Price)

    lst = [new_car.ID, new_car.Model, new_car.Year_of_Production, new_car.Kilometers_traveled, new_car.Price]
    cars_system_length = len(cars_system)
    cars_system.loc[cars_system_length] = lst

def Find ():
  car_id = int(input("Please enter ID of the car: "))
  if (cars_system.ID==car_id).any():
    print(cars_system.loc[cars_system['ID'] == car_id])
  else:
    print("Please enter a valid ID")
    Find()

def Update():
  print("To update the car model enter 1")
  print("To update the year of production enter 2")
  print("To update the traveled kilometers enter 3")
  print("To update the price enter 4")
  print("To end this proccess enter 5")
  operation = int(input('what do you want to update: '))
  if operation in [1,2,3,4]:
    car_id = int(input('Please enter ID of the car: '))
    if (cars_system.ID==car_id).any():
      if operation == 1:
        upd = input('Please enter the updated car model: ')
        cars_system.loc[cars_system['ID']==car_id,'Model']=upd
      elif operation == 2:
        upd = input('Please enter the updated year of production: ')
        cars_system.loc[cars_system['ID']==car_id,'Year_of_Production']=upd
      elif operation == 3:
        upd = input('Please enter the updated traveled kilometers: ')
        cars_system.loc[cars_system['ID']==car_id,'Kilometers_traveled']=upd
      elif operation == 4:
        upd = input('Please enter the updated price: ')
        cars_system.loc[cars_system['ID']==car_id,'Price']=upd
    else:
      print("Please enter a valid ID")
    Update()
  elif operation == 5:
    Exit()
  else:
    print('out of range')
    Update()

def Delete():
  car_id = int(input('please enter ID of car which you want to delete: '))
  if (cars_system.ID==car_id).any():
    del_IDs.append(car_id)
    cars_system.drop(cars_system[cars_system['ID']==car_id].index,inplace=True)
    cars_system.reset_index(inplace=True, drop=True)
  else:
    print("Please enter a valid ID")
    Delete()

def Exit():
  cars_system.sort_values(by=['ID'],inplace=True)
  cars_system.reset_index(inplace=True, drop=True)
  cars_system.to_csv('cars_system.csv', index=False)
  print(cars_system)


def main():
    print("To add a new car to the system enter 1")
    print("To find a car enter 2")
    print("To update the info of any car enter 3")
    print("To delete a car from the system enter 4")
    print("To get out from the system enter 5")
    operation = int(input('what do you want to do: '))

    if operation == 1:
        Add()
        main()

    elif operation == 2:
        Find()
        main()

    elif operation == 3:
        Update()
        main()

    elif operation == 4:
        Delete()
        main()

    elif operation == 5:
        Exit()

    else:
        print('out of range')
        main()

main()