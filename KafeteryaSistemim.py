import time
import datetime
import random
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("1366x766")
root.title("Kafeterya Sistemi")
root.configure(background="#FFFAF0")

Tops = Frame(root, bg="#FFFAF0", bd=20, pady=5, relief=FLAT)
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=("times", 40, "italic"), text="KAFETERYA YONETIM SISTEMI", bd=20, bg="#FFFAF0", fg="black",
                 justify=CENTER)
lblTitle.grid(row=0, column=0)


HesapIslemleri_F = Frame(root, bg="#FFFAF0", bd=10, relief=RIDGE)
HesapIslemleri_F.pack(side=RIGHT)
Buttons_F = Frame(HesapIslemleri_F, bg="#FFFAF0", bd=3, relief=RIDGE)
Buttons_F.pack(side=TOP)
Cal_F = Frame(HesapIslemleri_F, bg="#FFFAF0", bd=4, relief=RIDGE)
Cal_F.pack(side=BOTTOM)
Receipt_F = Frame(HesapIslemleri_F, bg="#FFFAF0", bd=3, relief=RIDGE)
Receipt_F.pack(side=TOP)

MenuFrame = Frame(root, bg="#49A", bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F = Frame(MenuFrame, bg="#49A", bd=4)
Cost_F.pack(side=BOTTOM)

Icecekler_F = Frame(MenuFrame, bg="#49A", bd=10, relief=RIDGE)
Icecekler_F.pack(side=RIGHT)
Yemekler_F = Frame(MenuFrame, bg="#49A", bd=10, relief=RIDGE)
Yemekler_F.pack(side=LEFT)


var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()

SiparisVakti = StringVar()
Hesap = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFoods = StringVar()
CostofDrinks = StringVar()
CostofSnacks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

Cay = StringVar()
Cola = StringVar()
Su = StringVar()
Ayran = StringVar()
Limonata = StringVar()
Soda = StringVar()
Turk_Kahvesi = StringVar()


Hamburger = StringVar()
Makarna = StringVar()
Salata = StringVar()
BiftekSalata = StringVar()
SoganHalkası = StringVar()
CheeseBurger = StringVar()
TavukBurger= StringVar()
Pizza = StringVar()

Cay.set("0")
Cola.set("0")
Su.set("0")
Ayran.set("0")
Limonata.set("0")
Soda.set("0")
Turk_Kahvesi.set("0")


Hamburger.set("0")
Makarna.set("0")
Salata.set("0")
BiftekSalata.set("0")
SoganHalkası.set("0")
CheeseBurger.set("0")
TavukBurger.set("0")
Pizza.set("0")

SiparisVakti.set(time.strftime("%d/%m/%Y"))

"""Function Declarations"""


def iExit():
    iExit = messagebox.askyesno("Sistemden çık", "Gerçekten çıkmak istiyor musun?")
    if iExit > 0:
        root.destroy()
        return


def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFoods.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    Cay.set("0")
    Cola.set("0")
    Su.set("0")
    Ayran.set("0")
    Limonata.set("0")
    Soda.set("0")
    Turk_Kahvesi.set("0")

  

    Hamburger.set("0")
    Makarna.set("0")
    Salata.set("0")
    BiftekSalata.set("0")
    SoganHalkası.set("0")
    CheeseBurger.set("0")
    TavukBurger.set("0")
    Pizza.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)

    txtCay.configure(state=DISABLED)
    txtCola.configure(state=DISABLED)
    txtSu.configure(state=DISABLED)
    txtAyran.configure(state=DISABLED)
    txtLimonata.configure(state=DISABLED)
    txtSoda.configure(state=DISABLED)
    txtTurk_Kahvesi.configure(state=DISABLED)
    txtHamburger.configure(state=DISABLED)
    txtMakarna.configure(state=DISABLED)
    txtSalata.configure(state=DISABLED)
    txtBiftekSalata.configure(state=DISABLED)
    txtSoganHalkası.configure(state=DISABLED)
    txtCheeseburger.configure(state=DISABLED)
    txtTavukBurger.configure(state=DISABLED)
    txtPizza.configure(state=DISABLED)


def CostofItem():
    Item1 = float(Cay.get())
    Item2 = float(Cola.get())
    Item3 = float(Su.get())
    Item4 = float(Ayran.get())
    Item5 = float(Limonata.get())
    Item6 = float(Soda.get())
    Item7 = float(Turk_Kahvesi.get())
    Item8 = float(Hamburger.get())
    Item9 = float(Makarna.get())
    Item10 = float(Salata.get())
    Item11 = float(BiftekSalata.get())
    Item12 = float(SoganHalkası.get())
    Item13 = float(CheeseBurger.get())
    Item14 = float(TavukBurger.get())
    Item15 = float(Pizza.get())
 

    IcecekFiyatlari = (Item1 * 4.00) + (Item2 * 6.50) + (Item3 * 2.99) + (Item4 * 6.00) + (Item5 * 8.00) + (
                Item6 * 7.90) + (Item7 * 10.00) 
    YemekFiyatlari = (Item8 * 40.00) + (Item9 * 40.50) + (Item10 * 29.95) + (Item11 * 39.75) + (Item12 * 19.90) + (
              Item13 *40.00) + (Item14 * 40.90) + (Item15 * 60.00)
   

    IcecekFiyat = str("%.2f" % (IcecekFiyatlari)), "TL"
    YemekFiyat = str("%.2f" % (YemekFiyatlari)), "TL"
    IcecekFiyatlari.set(IcecekFiyat)
    YemekFiyatlari.set(YemekFiyat)
    SC = str("%.2f" % (2.59)), "TL"
    ServiceCharge.set(SC)

    SubTotalofITEMS = str("%.2f" % (IcecekFiyatlari  + YemekFiyatlari + 1.59)), "TL"
    SubTotal.set(SubTotalofITEMS)

    Tax = str("%.2f" % ((IcecekFiyatlari + YemekFiyatlari + 1.59) * 0.15)), "TL"
    PaidTax.set(Tax)
    TT = ((IcecekFiyatlari + YemekFiyatlari + 1.59) * 0.15)
    TC = str("%.2f" % (IcecekFiyatlari + YemekFiyatlari + 1.59 + TT)), "TL"
    TotalCost.set(TC)


def chkCay():
    if (var1.get() == 1):
        txtCay.configure(state=NORMAL)
        txtCay.focus()
        txtCay.delete("0", END)
        Cay.set("")
    elif (var1.get() == 0):
        txtCay.configure(state=DISABLED)
        Cay.set("0")


def chkCola():
    if (var2.get() == 1):
        txtCola.configure(state=NORMAL)
        txtCola.focus()
        txtCola.delete("0", END)
        Cola.set("")
    elif (var2.get() == 0):
        txtCola.configure(state=DISABLED)
        Cola.set("0")


def chkSu():
    if (var3.get() == 1):
        txtSu.configure(state=NORMAL)
        txtSu.focus()
        txtSu.delete("0", END)
        Su.set("")
    elif (var3.get() == 0):
        txtSu.configure(state=DISABLED)
        Su.set("0")


def chkAyran():
    if (var4.get() == 1):
        txtAyran.configure(state=NORMAL)
        txtAyran.focus()
        txtAyran.delete("0", END)
        Ayran.set("")
    elif (var4.get() == 0):
        txtAyran.configure(state=DISABLED)
        Ayran.set("0")


def chkLimonata():
    if (var5.get() == 1):
        txtLimonata.configure(state=NORMAL)
        txtLimonata.focus()
        txtLimonata.delete("0", END)
        Limonata.set("")
    elif (var5.get() == 0):
        txtLimonata.configure(state=DISABLED)
        Limonata.set("0")


def chkSoda():
    if (var6.get() == 1):
        txtSoda.configure(state=NORMAL)
        txtSoda.focus()
        txtSoda.delete("0", END)
        Soda.set("")
    elif (var6.get() == 0):
        txtSoda.configure(state=DISABLED)
        Soda.set("0")




def chkTurk_Kahvesi():
    if (var8.get() == 1):
        txtTurk_Kahvesi.configure(state=NORMAL)
        txtTurk_Kahvesi.focus()
        txtTurk_Kahvesi.delete("0", END)
        Turk_Kahvesi.set("")
    elif (var8.get() == 0):
        txtTurk_Kahvesi.configure(state=DISABLED)
        Turk_Kahvesi.set("0")




def chkHamburger():
    if (var17.get() == 1):
        txtHamburger.configure(state=NORMAL)
        txtHamburger.focus()
        txtHamburger.delete("0", END)
        E_Hamburger.set("")
    elif (var17.get() == 0):
        txtHamburger.configure(state=DISABLED)
        Hamburger.set("0")


def chkMakarna():
    if (var18.get() == 1):
        txtMakarna.configure(state=NORMAL)
        txtMakarna.focus()
        txtMakarna.delete("0", END)
        Makarna.set("")
    elif (var18.get() == 0):
        txtMakarna.configure(state=DISABLED)
        Makarna.set("0")


def chkSalata():
    if (var19.get() == 1):
        txtSalata.configure(state=NORMAL)
        txtSalata.focus()
        txtSalata.delete("0", END)
        Salata.set("")
    elif (var19.get() == 0):
        txtSalata.configure(state=DISABLED)
        Salata.set("0")


def chkBiftekSalata():
    if (var20.get() == 1):
        txtBiftekSalata.configure(state=NORMAL)
        txtBiftekSalata.focus()
        txtBiftekSalata.delete("0", END)
        BiftekSalata.set("")
    elif (var20.get() == 0):
        txtBiftekSalata.configure(state=DISABLED)
        BiftekSalata.set("0")


def chkSoganHalkası():
    if (var21.get() == 1):
        txtOnion_Rings.configure(state=NORMAL)
        txtOnion_Rings.focus()
        txtOnion_Rings.delete("0", END)
        SoganHalkası.set("")
    elif (var21.get() == 0):
        txtOnion_Rings.configure(state=DISABLED)
        SoganHalkası.set("0")


def chkCheeseburger():
    if (var22.get() == 1):
        txtCheeseburger.configure(state=NORMAL)
        txtCheeseburger.focus()
        txtCheeseburger.delete("0", END)
        CheeseBurger.set("")
    elif (var22.get() == 0):
        txtCheeseburger.configure(state=DISABLED)
        CheeseBurger.set("0")


def chkTavukBurger():
    if (var23.get() == 1):
        txtTavukBurger.configure(state=NORMAL)
        txtTavukBurger.focus()
        txtTavukBurger.delete("0", END)
        TavukBurger.set("")
    elif (var23.get() == 0):
        txtChicken_Steak.configure(state=DISABLED)
        TavukBurger.set("0")


def chkPizza():
    if (var24.get() == 1):
        txtPizza.configure(state=NORMAL)
        txtOPizza.focus()
        txtPizza.delete("0", END)
        Pizza.set("")
    elif (var24.get() == 0):
        txtOld_Italia_Pizza.configure(state=DISABLED)
        Pizza.set("0")


def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10903, 60923)
    randdomRef = str(x)
    Receipt_Ref.set("BILL" + randdomRef)

    txtReceipt.insert(END, "Hesap:\t\t" + Receipt_Ref.get() + "\t\t" + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, "Urun:\t\t\t\t" + "Urun Fiyatları" + "\n")
    txtReceipt.insert(END, "Cay:\t\t\t\t\t" + Cay.get() + "\n")
    txtReceipt.insert(END, "Cola:\t\t\t\t\t" + Cola.get() + "\n")
    txtReceipt.insert(END, "Su:\t\t\t\t\t" + Su.get() + "\n")
    txtReceipt.insert(END, "Ayran:\t\t\t\t\t" + Ayran.get() + "\n")
    txtReceipt.insert(END, "Limonata :\t\t\t\t\t" + Limonata.get() + "\n")
    txtReceipt.insert(END, "Soda :\t\t\t\t\t" + Soda.get() + "\n")
    txtReceipt.insert(END, "Turk  Kahvesi:\t\t\t\t\t" + Turk_Kahvesi.get() + "\n")
    txtReceipt.insert(END, "Hamburger:\t\t\t\t\t" + Hamburger.get() + "\n")
    txtReceipt.insert(END, "Makarna:\t\t\t\t\t" + Makarna.get() + "\n")
    txtReceipt.insert(END, "Salata:\t\t\t\t\t" +Salata.get() + "\n")
    txtReceipt.insert(END, "Biftekli Salata:\t\t\t\t\t" + BiftekSalata.get() + "\n")
    txtReceipt.insert(END, "Soğan Halkası:\t\t\t\t\t" + SoganHalkası.get() + "\n")
    txtReceipt.insert(END, "Cheeseburger:\t\t\t\t\t" + CheeseBurger.get() + "\n")
    txtReceipt.insert(END, "Tavuk Burger:\t\t\t\t\t" + TavukBurger.get() + "\n")
    txtReceipt.insert(END, "Pizza:\t\t\t\t\t" + Pizza.get() + "\n")
    txtReceipt.insert(END,
                      "Iceceklerin toplamı :\t\t\t\t" + CostofDrinks.get() + "\n Vergi Ucreti:\t\t\t\t" + PaidTax.get() + "\n")
  
    txtReceipt.insert(END, "Yemeklerin toplamı:\t\t\t\t" + CostofFoods.get() + "\nAlt toplam:\t\t\t\t" + str(
        SubTotal.get()) + "\n")
    txtReceipt.insert(END, "Servis Ucreti:\t\t\t\t" + ServiceCharge.get() + "\n Ucret:\t\t\t\t" + str(
        TotalCost.get()) + "\n")


Cay = Checkbutton(Icecekler_F, text="Cay", variable=var1, onvalue=1, offvalue=0, font=("times", 18, "bold"), bg="#49A",
                  fg="#AEB6BF", command=chkCay).grid(row=0, sticky=W)
Cola = Checkbutton(Icecekler_F, text="Cola", variable=var2, onvalue=1, offvalue=0, font=("times", 18, "bold"),
                   bg="#49A", fg="#AEB6BF", command=chkCola).grid(row=1, sticky=W)
Su = Checkbutton(Icecekler_F, text="Su", variable=var3, onvalue=1, offvalue=0, font=("times", 18, "bold"),
                    bg="#49A", fg="#AEB6BF", command=chkSu).grid(row=2, sticky=W)
Ayran = Checkbutton(Icecekler_F, text="Ayran", variable=var4, onvalue=1, offvalue=0, font=("times", 18, "bold"),
                    bg="#49A", fg="#AEB6BF", command=chkAyran).grid(row=3, sticky=W)
Limonata = Checkbutton(Icecekler_F, text="Limonata", variable=var5, onvalue=1, offvalue=0, font=("times", 18, "bold"),
                       bg="#49A", fg="#AEB6BF", command=chkLimonata).grid(row=4, sticky=W)
Soda = Checkbutton(Icecekler_F, text="Soda ", variable=var6, onvalue=1, offvalue=0, font=("times", 18, "bold"),
                         bg="#49A", fg="#AEB6BF", command=chkSoda).grid(row=5, sticky=W)

Turk_Kahvesi = Checkbutton(Icecekler_F, text="Turk  Kahvesi", variable=var8, onvalue=1, offvalue=0,
                             font=("times", 18, "bold"), bg="#49A", fg="#AEB6BF", command=chkTurk_Kahvesi).grid(
    row=7, sticky=W)

txtCay = Entry(Icecekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED, textvariable=Cay)
txtCay.grid(row=0, column=1)
txtCola = Entry(Icecekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED, textvariable=Cola)
txtCola.grid(row=1, column=1)
txtSu = Entry(Icecekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,
                 textvariable=Su)
txtSu.grid(row=2, column=1)
txtAyran = Entry(Icecekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,
                 textvariable=Ayran)
txtAyran.grid(row=3, column=1)
txtLimonata = Entry(Icecekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,
                    textvariable=Limonata)
txtLimonata.grid(row=4, column=1)
txtSoda = Entry(Icecekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,
                      textvariable=Soda)
txtSoda.grid(row=5, column=1)

txtTurk_Kahvesi= Entry(Icecekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,
                          textvariable=Turk_Kahvesi)
txtTurk_Kahvesi.grid(row=7, column=1)



"""Yemekler"""
Hamburger = Checkbutton(Yemekler_F, text="Hamburger", variable=var17, onvalue=1, offvalue=0, font=("times", 18, "bold"),
                        bg="#49A", fg="#AEB6BF", command=chkHamburger).grid(row=0, sticky=W)
Makarna = Checkbutton(Yemekler_F, text="Makarna", variable=var18, onvalue=1, offvalue=0, font=("times", 18, "bold"),
                        bg="#49A", fg="#AEB6BF", command=chkMakarna).grid(row=1, sticky=W)
Salata = Checkbutton(Yemekler_F, text="Salata", variable=var19, onvalue=1, offvalue=0, font=("times", 18, "bold"),
                         bg="#49A", fg="#AEB6BF", command=chkSalata).grid(row=2, sticky=W)
BiftekSalata = Checkbutton(Yemekler_F, text="Biftekli Salata", variable=var20, onvalue=1, offvalue=0, font=("times", 18, "bold"),
                         bg="#49A", fg="#AEB6BF", command=chkBiftekSalata).grid(row=3, sticky=W)
SoganHalkası = Checkbutton(Yemekler_F, text="Soğan Halkası", variable=var21, onvalue=1, offvalue=0, font=("times", 18, "bold"),
                          bg="#49A", fg="#AEB6BF", command=chkSoganHalkası).grid(row=4, sticky=W)
Cheeseburger = Checkbutton(Yemekler_F, text="Cheeseburger", variable=var22, onvalue=1, offvalue=0,
                           font=("times", 18, "bold"), bg="#49A", fg="#AEB6BF", command=chkCheeseburger).grid(row=5,
                                                                                                                 sticky=W)
TavukBurger = Checkbutton(Yemekler_F, text="Tavuk Burger", variable=var23, onvalue=1, offvalue=0,
                            font=("times", 18, "bold"), bg="#49A", fg="#AEB6BF", command=chkTavukBurger).grid(
    row=6, sticky=W)
Pizza = Checkbutton(Yemekler_F, text="Pizza", variable=var24, onvalue=1, offvalue=0,
                               font=("times", 18, "bold"), bg="#49A", fg="#AEB6BF",
                               command=chkPizza).grid(row=7, sticky=W)


txtHamburger = Entry(Yemekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,
                     textvariable=Hamburger)
txtHamburger.grid(row=0, column=1)
txtMakarna = Entry(Yemekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,
                     textvariable=Makarna)
txtMakarna.grid(row=1, column=1)
txtSalata = Entry(Yemekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,
                      textvariable=Salata)
txtSalata.grid(row=2, column=1)
txtBiftekSalata = Entry(Yemekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,
                      textvariable=BiftekSalata)
txtBiftekSalata.grid(row=3, column=1)
txtSoganHalkası = Entry(Yemekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,
                       textvariable=SoganHalkası)
txtSoganHalkası.grid(row=4, column=1)
txtCheeseburger = Entry(Yemekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,
                        textvariable=CheeseBurger)
txtCheeseburger.grid(row=5, column=1)
txtTavukBurger = Entry(Yemekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,
                         textvariable=TavukBurger)
txtTavukBurger.grid(row=6, column=1)
txtPizza = Entry(Yemekler_F, font=("times", 16, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,
                            textvariable=Pizza)
txtPizza.grid(row=7, column=1)


lblCostofDrinks = Label(Cost_F, font=("times", 14, "bold"), text="İçecek Fiyatları\t   ", bd=7, bg="#49A",
                        fg="#AEB6BF")
lblCostofDrinks.grid(row=0, column=0, sticky=W)
txtCostofDrinks = Entry(Cost_F, font=("times", 14, "bold"), textvariable=CostofDrinks, bd=7, bg="#AEB6BF",
                        insertwidth=2, justify=RIGHT)
txtCostofDrinks.grid(row=0, column=1)



lblCostofFoods = Label(Cost_F, font=("times", 14, "bold"), text="Yemek Fiyatları \t   ", bd=7, bg="#49A", fg="#AEB6BF")
lblCostofFoods.grid(row=1, column=0, sticky=W)
txtCostofFoods = Entry(Cost_F, font=("times", 14, "bold"), textvariable=CostofFoods, bd=7, bg="#AEB6BF", insertwidth=2,
                       justify=RIGHT)
txtCostofFoods.grid(row=1, column=1)

lblServiceCharge = Label(Cost_F, font=("times", 14, "bold"), text="Servis Ucreti \t   ", bd=7, bg="#49A",
                         fg="#AEB6BF")
lblServiceCharge.grid(row=2, column=0, sticky=W)
txtServiceCharge = Entry(Cost_F, font=("times", 14, "bold"), textvariable=ServiceCharge, bd=7, bg="#AEB6BF",
                         insertwidth=2, justify=RIGHT)
txtServiceCharge.grid(row=2, column=1)

#Ödeme
lblPaidTax = Label(Cost_F, font=("times", 14, "bold"), text="\tKDV   ", bd=7, bg="#49A", fg="#AEB6BF")
lblPaidTax.grid(row=0, column=2, sticky=W)
txtPaidTax = Entry(Cost_F, font=("times", 14, "bold"), textvariable=PaidTax, bd=7, bg="#AEB6BF", insertwidth=2,
                   justify=RIGHT)
txtPaidTax.grid(row=0, column=3)

lblSubTotal = Label(Cost_F, font=("times", 14, "bold"), text="\t Alt Toplam ", bd=7, bg="#49A", fg="#AEB6BF")
lblSubTotal.grid(row=1, column=2, sticky=W)
txtSubTotal = Entry(Cost_F, font=("times", 14, "bold"), textvariable=SubTotal, bd=7, bg="#AEB6BF", insertwidth=2,
                    justify=RIGHT)
txtSubTotal.grid(row=1, column=3)

lblTotalCost = Label(Cost_F, font=("times", 14, "bold"), text=" \tToplam Fiyat", bd=7, bg="#49A", fg="#AEB6BF")
lblTotalCost.grid(row=2, column=2, sticky=W)
txtTotalCost = Entry(Cost_F, font=("times", 14, "bold"), textvariable=TotalCost, bd=7, bg="#AEB6BF", insertwidth=2,
                     justify=RIGHT)
txtTotalCost.grid(row=2, column=3)


txtReceipt = Text(Receipt_F, width=50, height=9, bg="#AEB6BF", bd=4, font=("times", 12, "bold"))
txtReceipt.grid(row=0, column=0)


btnTotal = Button(Buttons_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="Total",
                  bg="#49A", command=CostofItem).grid(row=0, column=0)
btnReceipt = Button(Buttons_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=5, text="Makbuz",
                    bg="#49A", command=Receipt).grid(row=0, column=1)
btnReset = Button(Buttons_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=5, text="Reset",
                  bg="#49A", command=Reset).grid(row=0, column=2)
btnExit = Button(Buttons_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="Çıkış",
                 bg="#49A", command=iExit).grid(row=0, column=3)

"""Hesap makinesi"""


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClear():
    global operator
    operator = ""
    text_Input.set("")


def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


txtDisplay = Entry(Cal_F, width=50, bg="#AEB6BF", bd=4, font=("times", 12, "bold"), justify=RIGHT,
                   textvariable=text_Input)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")


btn7 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="7", bg="#49A",
              command=lambda: btnClick(7)).grid(row=2, column=0)
btn8 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="8", bg="#49A",
              command=lambda: btnClick(8)).grid(row=2, column=1)
btn9 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="9", bg="#49A",
              command=lambda: btnClick(9)).grid(row=2, column=2)
btnAdd = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="+", bg="#49A",
                command=lambda: btnClick("+")).grid(row=2, column=3)

btn4 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="4", bg="#49A",
              command=lambda: btnClick(4)).grid(row=3, column=0)
btn5 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="5", bg="#49A",
              command=lambda: btnClick(5)).grid(row=3, column=1)
btn6 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="6", bg="#49A",
              command=lambda: btnClick(6)).grid(row=3, column=2)
btnSub = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="-", bg="#49A",
                command=lambda: btnClick("-")).grid(row=3, column=3)

btn1 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="1", bg="#49A",
              command=lambda: btnClick(1)).grid(row=4, column=0)
btn2 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="2", bg="#49A",
              command=lambda: btnClick(2)).grid(row=4, column=1)
btn3 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="3", bg="#49A",
              command=lambda: btnClick(3)).grid(row=4, column=2)
btnMult = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="*",
                 bg="#49A", command=lambda: btnClick("*")).grid(row=4, column=3)

btn0 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="0", bg="#49A",
              command=lambda: btnClick(0)).grid(row=5, column=0)
btnClear = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="C",
                  bg="#49A", command=btnClear).grid(row=5, column=1)
btnEquals = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="=",
                   bg="#49A", command=btnEquals).grid(row=5, column=2)
btnDivision = Button(Cal_F, padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="/",
                     bg="#49A", command=lambda: btnClick("/")).grid(row=5, column=3)

root.mainloop()