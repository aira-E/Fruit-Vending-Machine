from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Vending Fruit Machine")
root.iconbitmap("srcs/basket.ico")
var = StringVar()

#Pera Counter
inserted_money = 0
bought = 0
totalPrice = 0

#---------------------------------------------- BUTTON FUNCTIONS----------------------------------------------
#Push Button Func
def pushmoney_button():
    global bought, inserted_money,totalPrice
    try:
        output.delete(1.0,END)
        change.delete(1.0,END)
        moneyin = moneydisplay.get()
        totalPrice = 50 * bought
        #totalPrice_display = f"Total: {totalPrice} Pesos"
        #Naglagay ng sobra o saktong pera ang user
        if float(moneyin) >= totalPrice:
            #Kapag nagcocontinue ka lang ng payment, iadd yung already inserted money sa bagong inserted money
            #Kapag walang already inserted money then ang sukli is ung freshly added money minus total price
            sukli = (float(moneyin)+inserted_money) - totalPrice if inserted_money else float(moneyin) - totalPrice
            if float(moneyin) > totalPrice: #Naglagay ng sobra ang user
                change.insert("1.0",(f"change: {sukli}"))
            else: 
                #If sakto ung nilagay na pera without previous insert then no need to display sukli
                if inserted_money:
                    change.insert("1.0",(f"change: {sukli}"))
            #Di na maglalabas ng change kapag sakto ang pera
            output.insert("2.0", "\n\n Enjoy your \n fruit/s!", ) #naibigay ang product
            inserted_money = 0 #nakuha na ang pera
            bought = 0 #reset number of bought fruits
            fruit_basket.delete(1.0,END)
            totalcost.delete(1.0,END)
            #change.delete(1.0,END)
            #b6["state"] = "disabled"

        #Naglagay ng kulang na pera ang user
        elif float(moneyin) < totalPrice:
            inserted_money += float(moneyin) #I-dagdag ang kulang na pera
            #Nagdagdag ng kulang na pera ang user
            if inserted_money < totalPrice:
                kulang = totalPrice - inserted_money
                change.insert("1.0",(f"please add: {kulang}")) #nagabiso kung ilang ang kulang

            #Nagdagdag ng sobra o saktong kulang na pera ang user
            elif inserted_money >= totalPrice :
                sukli = inserted_money - totalPrice

                #Magdisplay lang ng sukli if sobra yung total inserted money kaysa sa total price
                if sukli:
                    change.insert("1.0",(f"change: {sukli}"))
                    inserted_money = 0 #nakuha na ang pera
                    bought = 0 #reset number of bought fruits
                fruit_basket.delete(1.0,END)
                totalcost.delete(1.0,END)
                #change.delete(1.0,END)
                b6["state"] = "disabled"
                output.insert("2.0", "\n\n Enjoy your \n fruit/s!", )


        moneydisplay.delete(0,100) #na-delete ang hulugan ng pera
    except:
            output.insert("2.0","Error")

        #moneyin = pera na hinuhulog
        #moneydisplay = doon tinatype yung pera

#Reset Button Func
def reset_button ():
    global inserted_money, bought
    fruit_basket.delete(1.0,END)
    output.delete(1.0,END)
    change.delete(1.0,END)
    moneydisplay.delete(0,100)
    totalcost.delete(1.0,END)
    inserted_money = 0
    bought = 0
    b1["state"] = "normal"
    b2["state"] = "normal"
    b3["state"] = "normal"
    b4["state"] = "normal"
    b5["state"] = "disabled"
    b6["state"] = "disabled"    

#Apple Button Func
def Apple_button(): #Function na nagsasabi ano mangyayari kapag pinindot ang "apple" button
    global bought #(CLI) Matatawag ang "bought" variable
    totalcost.delete(1.0,END) #(GUI) Madedelete ang nakalagay sa Total Price frame
    bought += 1 #(CLI) Dadag-dag sa ipinamili mo
    totalPrice = 50 * bought #(CLI) Mako-compute
    fruit_basket.insert("1.0", "Apple = 50 Pesos\n") #(GUI) Malalagyan ng "Apple = 50 Pesos" sa "Your Purchases"
    totalcost.insert("1.0",f"Total: {totalPrice} Pesos") #(GUI) Ma-update ang Total Price frame
    b5["state"] = "normal" #(GUI) Iilaw ang "Reset" button
    b6["state"] = "normal" #(GUI) Iilaw ang "Push" button

#Grapes Button Func
def Grapes_button():
    global bought
    totalcost.delete(1.0,END)
    bought += 1
    totalPrice = 50 * bought
    fruit_basket.insert("1.0", "Grape = 50 Pesos\n")
    totalcost.insert("1.0",f"Total: {totalPrice} Pesos")
    b5["state"] = "normal"
    b6["state"] = "normal"

#Banana Button Func
def Banana_button():
    global bought
    totalcost.delete(1.0,END)
    bought += 1
    totalPrice = 50 * bought
    fruit_basket.insert("1.0", "Banana = 50 Pesos\n")
    totalcost.insert("1.0",f"Total: {totalPrice} Pesos")
    b5["state"] = "normal"
    b6["state"] = "normal"

#Lemon Button Func
def Lemons_button():
    global bought
    totalcost.delete(1.0,END)
    bought += 1
    totalPrice = 50 * bought
    fruit_basket.insert("1.0", "Lemon = 50 Pesos\n")
    totalcost.insert("1.0",f"Total: {totalPrice} Pesos")
    b5["state"] = "normal"
    b6["state"] = "normal"

#---------------------------------------------- INTERFACE ----------------------------------------------
#Frames
f1 = Frame(relief= RAISED, bd = 20, bg= "#BEE8F8") 
f1.grid(row=1, column=0, padx= 10, pady=10)

f2 = Frame(f1,relief= FLAT, bd = 10, bg = "#99663B")
f2.grid (row=1, column=1, padx= 10, pady=10)

f3 = Frame(f2,relief= FLAT, bd = 10, bg = "#A8755A")
f3.grid (row=0, column=2, padx= 5, pady=5, rowspan=3)

f4= Frame(f1,relief= FLAT, bd = 10, bg = "#73CFC4")
f4.grid (row=1, column=0, padx= 10, pady=10)

basket_image = ImageTk.PhotoImage(Image.open("srcs/basket.png"))
root = Label(f1, text= "Fruit Vending Machine", font = "arial 18 bold",
            height= 100, width = 1300, bg = "#37B54A", bd = 10, fg = "WHITE", relief= RIDGE, image= basket_image, compound="left",)
root.grid (row=0, column=0, columnspan=3)

#Cost
totalcost = Text(f2, width= 18, height= 2, bd = 10, bg = "#222223", font = "arial 15 bold", fg = "white")
totalcost.grid(row=2, column=1, padx=10, pady=10)

#Input Money
money = Label (f3, text= "Input your money here",bg= "#E7612B", fg = "WHITE", width= 20, font= "arial 15 bold", relief= SUNKEN)
money.grid (row=0, column=0,padx = 10, pady= 10)
moneydisplay = Entry(f3, width= 18, bd= 7, font= "arial 15 bold", justify= "center", textvariable=int)
moneydisplay.grid(row = 1, column=0,padx=10, pady=10)

#Change
change = Text(f3, width= 18, height= 2, bd = 10, bg = "#222223", font = "arial 15 bold", fg = "white")
change.grid(row=3, column=0, padx=10, pady=10)

#Output
output = Text(f1, width= 15, height= 11, bd = 10, bg = "#222223", font = "arial 15 bold", fg = "white")
output.grid(row=1, column=2, padx=10, pady=10)

#Your Purchase
basket = Label (f4, text= "Your Purchases",bg= "#ACC1FF", fg = "#222223", width= 20, font= "arial 15 bold", relief= SUNKEN)
basket.grid (row=0, column=0,padx = 10, pady= 10)
fruit_basket = Text(f4, width= 19, height= 9, bd = 10, bg = "#222223", font = "arial 15 bold", fg = "white")
fruit_basket.grid(row=1, column=0, padx=10, pady=10)
scrollbar = Scrollbar(f4)
scrollbar.grid(row=1, column=1, sticky=N+S)
fruit_basket.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=fruit_basket.yview)

#---------------------------------------------- BUTTONS ----------------------------------------------
#AppleButton
apple_image = ImageTk.PhotoImage(Image.open("srcs/apple.png"))
b1 = Button(f2, text = "Apple", font= "Arial 20 bold", image= apple_image, compound="left", width= 200, bd = 10, bg = "#B0E57C", fg= "black", relief= GROOVE, command= Apple_button)
b1.grid(row = 0 , column = 0, padx = 10, pady= 10)

#GrapesButton
grapes_image = ImageTk.PhotoImage(Image.open("srcs/grapes.png"))
b2 = Button(f2, text = "Grape", font= "Arial 20 bold", image= grapes_image, compound="left", width= 200, bd = 10, bg = "#B0E57C", fg= "black", relief= GROOVE, command= Grapes_button)
b2.grid(row = 1 , column = 0, padx = 10, pady= 10)

#BananaButton
banana_image = ImageTk.PhotoImage(Image.open("srcs/banana.png"))
b3 = Button(f2, text = "Banana", font= "Arial 20 bold", image= banana_image, compound="left", width= 200, bd = 10, bg = "#B0E57C", fg= "black", relief= GROOVE, command= Banana_button)
b3.grid(row = 0 , column = 1, padx = 10, pady= 10)

#LemonsButton
lemon_image = ImageTk.PhotoImage(Image.open("srcs/lemon.png"))
b4 = Button(f2, text = "Lemon", font= "Arial 20 bold", image= lemon_image, compound="left", width= 200, bd = 10, bg = "#B0E57C", fg= "black", relief= GROOVE, command= Lemons_button)
b4.grid(row = 1 , column = 1, padx = 10, pady= 10)

#ResetButton
b5 = Button(f2, width= 18, text = "Reset", font= "Arial 15 bold", bd = 10, bg = "#E3353A", fg= "white", relief= GROOVE , command= reset_button)
b5.grid(row = 2, column = 0, padx = 10, pady= 10)

#PushMoneyButton
b6 = Button(f3, width= 18, text = "Push Money",state= "disabled", font= "Arial 15 bold", bd = 10, bg = "#E3353A", fg= "white", relief= GROOVE, command= pushmoney_button)
b6.grid(row = 2, column = 0, padx = 10, pady= 10)
root.mainloop()