import json
def food_items(filename,foodId,food_name,food_quantity,food_price,food_discount,food_stock):
            food_details={
                'FoodID':foodId,
                'name':food_name,
                'quantity':food_quantity,
                'price':food_price,
                'discount':food_discount,
                'stock':food_stock
            }
            file = open(filename,"r+")
            try:
                data=json.load(file)
                if food_details not in data:
                    data.append(food_details)
                    file.seek(0)
                    file.truncate()
                    json.dump(data,file)
                    file.close()
                    return True
            except json.decoder.JSONDecodeError:
                lst=[]
                lst.append(food_details)
                json.dump(lst,file)
                file.close()
                return True
            finally:
                file.close()
            return False

def edit_items(filename,foodId,food_name,food_quantity,food_price,food_discount,food_stock):
    file = open(filename,"r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["FoodID"] == foodId:
            data[i]["name"] = food_name
            data[i]["quantity"] = food_quantity
            data[i]["price"] = food_price
            data[i]["discount"]=food_discount
            data[i]["stock"]=food_stock
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    return False

def view_items(filename):
    file = open(filename,"r+")
    data = json.load(file)
    return data

def delete_items(filename,foodId):
    file = open(filename,"r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["FoodID"] == foodId:
            data.pop(i)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    return False


def user_details(filename,full_name,phone_no,email,address,password):
    userDetail={
        "Name":full_name,
        "Phone no":phone_no,
        "Email id":email,
        "Address":address,
        "Password":password
    }
    file = open(filename,"r+")
    try:
        data=json.load(file)
        if userDetail not in data:
            data.append(userDetail)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    except json.decoder.JSONDecodeError:
        lst=[]
        lst.append(userDetail)
        json.dump(lst,file)
        file.close()
        return True
    finally:
        file.close()
    return False

def customer_login(filename_food,filename_user,email,password):
    file = open(filename_user,"r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["Email id"]==email and data[i]["Password"]==password:
            print("login sucessful")
            while True:
                try:
                    user_input=int(input("select for:\n1.Place new order\n2.Order history\n3.Update profile\n4.exit\n"))
                except ValueError:
                    print("please enter a valid choice ")
                    continue
                if user_input==1:
                    file_food =open(filename_food,"r+")
                    data_food =json.load(file_food)
                    ls=[]
                    for i in range(len(data_food)):
                        ls.append(data_food[i]["name"]+" ("+data_food[i]["quantity"]+") "+" ["+data_food[i]["price"]+"] ")
                    print(ls)
                    order=list(map(int,input("enter the list of items you want to order: ").strip().split(",")))[:len(ls)+1]
                    order_history=[]
                    print("your ordered items are:")
                    for i in order:
                        print(i,".",ls[i-1])
                        order_history.append(ls[i-1])

        
                if user_input==2:
                    print("your ordred history is: ")
                    for i in order_history:
                        print(i)

                if user_input==3:
                    full_name=input("enter the full name whose data you want to update: ")
                    file = open("user.json","r+")
                    data = json.load(file)
                    for i in range(len(data)):
                        if data[i]["Name"]==full_name:
                            phone_no=input("enter your new mobile number with country code: ")
                            email=input("enter your new email id: ")
                            address=input("enter your new address: ")
                            password=input("enter your new password: ")
                            data[i]["Phone no"]=phone_no
                            data[i]["Email id"]=email
                            data[i]["Address"]=address
                            data[i]["Password"]=password
                            file.seek(0)
                            file.truncate()
                            json.dump(data,file)
                            file.close()
                            print("updated sucessfully")
                        else:
                            print("not updated")

                if user_input==4:
                    exit()
        else:
            print("login unsucessful, enter valid email and password ")            
