from tkinter import *
import datetime
import sqlite3
from tkinter import messagebox
import math
con=sqlite3.connect('store.db')
cur=con.cursor()
def user():
	root=Toplevel()
	pro_list=[]
	pro_price=[]
	pro_qua=[]
	date=datetime.datetime.now().date()

	root.title('Reliance Store')
	left=Frame(root,width=700,height=768,bg='white')
	left.pack(side=LEFT)
	Label(left,text='Reliance store',font='corbel 18 bold',bg='White').place(x=0,y=12)

	id=Label(left,text='Enter ID',font='corbel 10 bold',bg='white').place(x=0,y=100)
	id_e=Entry(left)
	id_e.place(x=100,y=100)

	product=Label(left,text='',bg='white',fg='Orange',font='corbel 10 bold')
	product.place(x=0,y=250)
	sell=Label(left,text='',bg='white',fg='orange',font='corbel 10 bold')
	sell.place(x=0,y=300)



	right=Frame(root,width=600,height=768,bg='lightblue')
	right.pack(side=RIGHT)
	Label(right,text='Today date:' + str(date),font='corbel 15 bold',bg='lightblue').place(x=0,y=12)
	p=Label(right,text='Product',font='corbel 10 bold',bg='lightblue').place(x=0,y=80)
	q=Label(right,text='Quantity',font='corbel 10 bold',bg='lightblue').place(x=200,y=80)
	a=Label(right,text='Amount',font='corbel 10 bold',bg='lightblue').place(x=400,y=80)
	total_l=Label(right,text='',font='corbel 20 bold')
	total_l.place(x=0,y=700)

	def ajax():
		idget=id_e.get()
		sql="select * from inventory where id=?"
		res=cur.execute(sql,(idget,))
		for i in res:
			name=i[1]
			sp=i[4]
			stock=i[3]
		product.configure(text='Product name:'+str(name))
		sell.configure(text='Rs:'+str(sp))
		quantity=Label(left,text='Enter quantity',bg='white')
		quantity.place(x=0,y=350)
		quantity_e=Entry(left)
		quantity_e.place(x=350,y=350)
		def add():
				quantity_value=int(quantity_e.get())
				if quantity_value>stock:
					messagebox.showinfo('Error','Item is out of stock')
				else:
					pro_list.append(name)
					tp=float(quantity_value)*float(sp)
					pro_price.append(tp)
					pro_qua.append(quantity_value)
					x_i=0
					y_i=110
					c=0
					for p in pro_list:
						tempname=Label(right,text=str(pro_list[c]))
						tempname.place(x=0,y=y_i)
						tempquantity=Label(right,text=str(pro_qua[c]))
						tempquantity.place(x=500,y=y_i)
						tempprice=Label(right,text=str(pro_price[c]))
						tempprice.place(x=500,y=y_i)
						y_i+=50
						c+=1
						total_l.configure(text='Total:'+str(sum(pro_price)))	
		def change():
			amount_given=float(amount_e.get())
			our_total=float(sum(pro_price))
			to_give=amount_given - our_total
			c_amount=Label(left,text='Change : Rs:'+str(to_give))
			c_amount.place(x=550,y=500)

		

		dis=Label(left,text='Enter discount',bg='white')
		dis.place(x=0,y=400)
		dis_e=Entry(left)
		dis_e.place(x=350,y=400)
		Button(left,text='Add to cart',command=add).place(x=450,y=450)
		amount=Label(left,text='Given Amount',bg='white')
		amount.place(x=0,y=500)
		amount_e=Entry(left)
		amount_e.place(x=350,y=500)
		Button(left,text='Caculate change',command=change).place(x=450,y=550)
		Button(left,text='Generate bill',width=23).place(x=0,y=600)

	Button(left,text='Search',command=ajax).place(x=150,y=150)		




	root.mainloop()