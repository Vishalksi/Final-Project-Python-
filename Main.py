from operations import *
import random
if __name__ =="__main__":
    while True:
        try:
            choice=int(input("Enter choice:\n 1.Admin \n 2.User\n 3.exit\n"))
        except ValueError:
            print("please enter a valid choice ")
            continue
        
        if choice==1:
            print("***Hello admin***")
            admin_userid=input("Enter the user id: ")
            admin_password=input("Enter the password: ")
            if admin_userid == 'vishalkumar' and admin_password == 'Vishal@123':
                while True:
                    try:
                        food_choice=int(input("enter the choice: \n1.add new food item \n2.edit food item \n3.view food item \n4.delete food item \n5.exit\n"))
                    except ValueError:
                        print("please enter a valid choice ")
                        continue
                    if food_choice==1:
                        foodID=random.randint(100,200)
                        food_name=input("enter the name of the food: ")
                        food_quantity=input("enter the quantity of the food: ")
                        food_price=input("enter the price of the food: ")
                        food_discount=input("enter the discount for the food: ")
                        food_stock=input("enter the stock of the food: ")
                        flag=food_items("food.json",foodID,food_name,food_quantity,food_price,food_discount,food_stock)
                        if flag:
                                print("item added sucessfully")
                        else:
                                print("item not added")
                
                    if food_choice==2:
                        foodId=int(input("enter the food id that you want to edit: "))
                        food_name=input("enter the new name of the food: ")
                        food_quantity=input("enter the new quantity of the food: ")
                        food_price=input("enter the new price of the food: ")
                        food_discount=input("enter the new discount for the food: ")
                        food_stock=input("enter the new stock of the food: ")
                        flag=edit_items("food.json",foodId,food_name,food_quantity,food_price,food_discount,food_stock)
                        if flag:
                                print("item updated sucessfully")
                        else:
                                print("item not updated")

                    if food_choice==3:
                        data = view_items("food.json")
                        for i in data:
                            print(i)

                    if food_choice==4:
                        foodId=int(input("enter the food id that you want to delete: "))
                        flag=delete_items("food.json",foodId)
                        if flag:
                                print("item deleted sucessfully")
                        else:
                                print("item not deleted")

                    if food_choice==5:
                        exit()



        if choice==2:
            print("*****welcome user*****")
            while True:
                try:
                    customer_choice=int(input("1.Register as user\n2.login as user\n3.exit\n"))
                except ValueError:
                    print("please enter a valid choice ")
                    continue
                
                if customer_choice==1:
                    full_name=input("enter your full name: ")
                    phone_no=input("enter your mobile number with country code: ")
                    email=input("enter your email id: ")
                    address=input("enter your address: ")
                    password=input("enter your password: ")
                    flag=user_details("user.json",full_name,phone_no,email,address,password)
                    if flag:
                        print("register sucessfully")
                    else:
                        print("register unsucessful")


                if customer_choice==2:
                    email=input("enter yout registered email id: ")
                    password=input("enter your registered password: ")
                    customer_login("food.json","user.json",email,password)


                if customer_choice==3:
                    exit()



        if choice==3:
            exit()
            