def admin():
    print("****************** Welcome Admin ********************\n")
    print("***************************************************")
    user_name=input("Enter User Name : ")
    print("***************************************************")
    user_password=input("Enter Your Password : ")
    print("***************************************************")
    user_name_original="vpm743"
    user_password_original="Ved@07042003"
    log_in=0
    if(user_name==user_name_original):
        if(user_password==user_password_original):
            print("***************************************************")
            print("""Successfully Loged In 
            Welcome Admin""")
            print("***************************************************")
            log_in=1 
def customer():
    print("***************************************************")
    print("What You Want TO Buy")
    print("***************************************************")
    print("""\n1 : Bread  
    2 : Vegitables  
    3 : Home Accessories  
    4 : Pet Food  
    5 : Exit  """)
    print("***************************************************")

store_itme_bread=["1 : Aata Bread","2 : Flour Bread","3 : Bun","4 : Pav"]
store_itme_bread_price=[30,20,10,25]
store_itme_bread_quantity=[10,10,10,10]
store_itme_vegitables=["Tommato","Potato","Onion","Chilli"]
store_itme_vegitables_price=[30,40,50,15]
store_itme_vegitables_quantity=[10,10,10,10]
store_itme_home_accessories=["Mop","Broom","Chair","Table"]
store_itme_home_accessories_price=[150,60,1000,2500]
store_itme_home_accessories_quantity=[10,10,10,10]
store_itme_pet_food=["Nestle","Freshpet","Wellpet","Ainsworth"]
store_itme_pet_food_price=[400,250,750,625]
store_itme_pet_food_quantity=[10,10,10,10]
customer_cart=[]
customer_purchase=[]
customer_purchase_quantity=[]
customer_purchase_total=[]
def billing():
    total_billing=0
    print("***************************************************")
    print("***************************************************")
    print("ITEMS     PRICE    QUANTITY")
    print("***************************************************")
    for i in customer_purchase_total:
        total_billing=total_billing+i
    for i in range(len(customer_purchase)):
        print("***************************************************")
        print(customer_purchase[i],customer_purchase_total[i],customer_purchase_quantity[i])
        print("***************************************************")
    print("Your Grand Total Is :  ",total_billing)
    print("***************************************************")



def bread():
    buy_bread=int(input("Enter What You Want"))
    buy_bread_quantity=int(input("Enter How Much You Want To Buy"))
    if(buy_bread==1):
        if(store_itme_bread_quantity[0]>=buy_bread_quantity):
            customer_purchase.append("Aata Bread")
            customer_purchase_total.append(store_itme_bread_price[0]*buy_bread_quantity)
            customer_purchase_quantity.append(buy_bread_quantity)
            atat_bread_stock=store_itme_bread_quantity[0]
            atat_bread_stock_now=atat_bread_stock-buy_bread_quantity
            store_itme_bread_quantity[0]=atat_bread_stock_now
        else:
            print("***************************************************")
            print("Product is Not Available ")
            print("***************************************************")
        
    elif(buy_bread==2):
        if(store_itme_bread_quantity[1]>=buy_bread_quantity):
            customer_purchase.append("Flour Bread")
            customer_purchase_total.append(store_itme_bread_price[1]*buy_bread_quantity)
            customer_purchase_quantity.append(buy_bread_quantity)
            flour_bread_stock=store_itme_bread_quantity[1]
            flour_bread_stock_now=flour_bread_stock-buy_bread_quantity
            store_itme_bread_quantity[1]=flour_bread_stock_now
        else:
            print("***************************************************")
            print("Product is Not Available ")
            print("***************************************************")
    elif(buy_bread==3):
        customer_purchase.append("Bun")
        customer_purchase_total.append(store_itme_bread_price[2]*buy_bread_quantity)
        customer_purchase_quantity.append(buy_bread_quantity)
    elif(buy_bread==4):
        customer_purchase.append("Pav")
        customer_purchase_total.append(store_itme_bread_price[3]*buy_bread_quantity)
        customer_purchase_quantity.append(buy_bread_quantity)
def vegitable():
    buy_vegitable=int(input("Enter What You Want"))
    buy_vegitables_quantity=int(input("Enter How Much You Want To Buy"))
    if(buy_vegitable==1):
        customer_purchase.append("Tommato")
        customer_purchase_total.append(store_itme_vegitables_price[0]*buy_vegitables_quantity)
        customer_purchase_quantity.append(buy_vegitables_quantity)
    elif(buy_vegitable==2):
        customer_purchase.append("Potato")
        customer_purchase_total.append(store_itme_vegitables_price[1]*buy_vegitables_quantity)
        customer_purchase_quantity.append(buy_vegitables_quantity)
    elif(buy_vegitable==3):
        customer_purchase.append("Onion")
        customer_purchase_total.append(store_itme_vegitables_price[2]*buy_vegitables_quantity)
        customer_purchase_quantity.append(buy_vegitables_quantity)
    elif(buy_vegitable==4):
        customer_purchase.append("Chilli")
        customer_purchase_total.append(store_itme_vegitables_price[3]*buy_vegitables_quantity)
        customer_purchase_quantity.append(buy_vegitables_quantity)
def home_accessories():
    buy_home_accessories=int(input("Enter What You Want"))
    buy_home_accessories_quantity=int(input("Enter How Much You Want To Buy"))
    if(buy_home_accessories==1):
        customer_purchase.append("Mop")
        customer_purchase_total.append(store_itme_home_accessories_price[0]*buy_home_accessories_quantity)
        customer_purchase_quantity.append(buy_home_accessories_quantity)
    elif(buy_home_accessories==2):
        customer_purchase.append("Broom")
        customer_purchase_total.append(store_itme_home_accessories_price[1]*buy_home_accessories_quantity)
        customer_purchase_quantity.append(buy_home_accessories_quantity)
    elif(buy_home_accessories==3):
        customer_purchase.append("Chair")
        customer_purchase_total.append(store_itme_home_accessories_price[2]*buy_home_accessories_quantity)
        customer_purchase_quantity.append(buy_home_accessories_quantity)
    elif(buy_home_accessories==4):
        customer_purchase.append("Table")
        customer_purchase_total.append(store_itme_home_accessories_price[3]*buy_home_accessories_quantity)
        customer_purchase_quantity.append(buy_home_accessories_quantity)
def pet_food():
    buy_pet_food=int(input("Enter What You Want"))
    buy_pet_food_quantity=int(input("Enter How Much You Want To Buy"))
    if(buy_pet_food==1):
        customer_purchase.append("Nestle")
        customer_purchase_total.append(store_itme_pet_food_price[0]*buy_pet_food_quantity)
        customer_purchase_quantity.append(buy_pet_food_quantity)
    elif(buy_pet_food==2):
        customer_purchase.append("Freshpet")
        customer_purchase_total.append(store_itme_pet_food_price[1]*buy_pet_food_quantity)
        customer_purchase_quantity.append(buy_pet_food_quantity)
    elif(buy_pet_food==3):
        customer_purchase.append("Wellpet")
        customer_purchase_total.append(store_itme_pet_food_price[2]*buy_pet_food_quantity)
        customer_purchase_quantity.append(buy_pet_food_quantity)
    elif(buy_pet_food==4):
        customer_purchase.append("Ainsworth")
        customer_purchase_total.append(store_itme_pet_food_price[3]*buy_pet_food_quantity)
        customer_purchase_quantity.append(buy_pet_food_quantity)
def customer_entery_product():
    customer()
    print("***************************************************")
    customer_entry=int(input("Enter Your Choice"))
    print("***************************************************")
    if(customer_entry==1):
        print("For Bread We Have")
        print("Item       Price")
        for i in range(len(store_itme_bread)):
            print(store_itme_bread[i],store_itme_bread_price[i])
            print("***************************************************")
        bread()

    elif(customer_entry==2):
        print("For Vegitables We Have")
        print("Item       Price")
        for i in range(len(store_itme_vegitables)):
            print(store_itme_vegitables[i],store_itme_vegitables_price[i])
            print("***************************************************")
        vegitable()
    elif(customer_entry==3):
        print("For House Accessories We Have")
        print("Item       Price")
        for i in range(len(store_itme_home_accessories)):
            print(store_itme_home_accessories[i],store_itme_home_accessories_price[i])
            print("***************************************************")
        home_accessories()
    elif(customer_entry==4):
        print("For Pet Food We Have")
        print("Item       Price")
        for i in range(len(store_itme_pet_food)):
            print(store_itme_pet_food[i],store_itme_pet_food_price[i])
            print("***************************************************")
        pet_food()
    else:
        print("ThankYou For Using Aur App")
        
        
while True:
    print("***************************************************")
    print("***************************************************")
    print("************ WELCOME TO VED MART ******************")
    print("***************************************************")
    print("***************************************************")
    print("")
    print("***************************************************")
    print("***************** 1 : ADMIN ***********************")
    print("**************** 2 : CUSTOMER *********************")
    print("***************************************************")
    admin_customer=int(input("Enter Who You Are ?  "))
    if(admin_customer==1):
        print("Programm Under Process")
    elif(admin_customer==2):
        print("***************************************************")
        again=1
        while(again==1):
            again=again-1
            customer_entery_product()
            print("1 : Do You Want TO Buy More Items Or We Will Procede To Billing")
            print("2 : Do You Want TO Exit Program With out buying")
            exit_choice=int(input("Enter Exit Mode"))
            if(exit_choice==1):
                again=int(input("Do You Want TO Buy More Items Or We Will Procede To Billing"))
                if(again==1):
                    continue
                if(again==0):
                    billing()
                    print("Thankyou For Using Our Program")
                    
            else:
                break
                
            
            


    break
