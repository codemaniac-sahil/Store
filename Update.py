from tkinter import*
from tkinter import messagebox
import sqlite3
con=sqlite3.connect('store.db')
cur=con.cursor()
def update():
	root=Toplevel()
	root.title('Update Product')
	f1=Frame(root,bg='#0398fc',height=200)
	root.geometry('1080x680')
	Label(f1,text='Admin page\n',bg='#0398fc',font='corbel 18 bold').pack()
	f1.pack(fill='x',pady=15,padx=23)
	p_id=Label(root,text='Product id',font='corbel 10')
	p_id.place(x=100,y=120)

	
	p=Label(root,text='Product name',font='corbel 10')
	p.place(x=100,y=170)

	def search():
		pid_e=p_id_e.get()
		p_n_e=p_e.get()
		s_e=s.get()
		c_e=c.get()
		s_p_e=s_p.get()
		v_n_e=v_n.get()
		v_p_e=v_p.get()
			
		if (pid_e==''):
			
			messagebox.showinfo('Error','Id must be inputed ')
		else:
			sql="select* from 'inventory' where id =?;"
			result=cur.execute(sql,(pid_e,))
			for i in result:
				n1=i[1]
				n2=i[2]
				n3=i[3]
				n4=i[4]
				n5=i[5]
				n6=i[6]
				
			con.commit()
			
			p_e.delete(0,END)
			p_e.insert(0,str(n1))
			
			s.delete(0,END)
			s.insert(0,str(n2))
			
			c.delete(0,END)
			c.insert(0,str(n3))
			
			s_p.delete(0,END)
			s_p.insert(0,str(n4))
			
			v_n.delete(0,END)
			v_n.insert(0,str(n5))
			
			v_p.delete(0,END)
			v_p.insert(0,str(n6))
	def update_c():
		pid_e=p_id_e.get()
		u1=p_e.get()
		u2=s.get()
		u3=c.get()
		u4=s_p.get()
		u5=v_n.get()
		u6=v_p.get()
		sql="update inventory set name =?,stock=? ,cp=?,sp=? ,vendor_name=? ,vendor_phone=? where id=? "
		val=(u1,u2,u3,u4,u5,u6,pid_e)
		cur.execute(sql,val)
		messagebox.showinfo('Success','Item updated successfully')
	
		
		
		
	p=Label(root,text='Stock',font='corbel 10')
	p.place(x=100,y=220)
	
	p=Label(root,text='Cost Price',font='corbel 10')
	p.place(x=100,y=270)
	
	p=Label(root,text='Selling Price',font='corbel 10')
	p.place(x=100,y=320)
	
	p=Label(root,text='Vendor Name',font='corbel 10')
	p.place(x=100,y=370)
	
	p=Label(root,text='Vender phone number',font='corbel 10')
	p.place(x=100,y=420)
	
	p_id_e=Entry(root)
	p_id_e.place(x=380,y=120)
	
	p_e=Entry(root)
	p_e.place(x=380,y=170)
	
	s=Entry(root)
	s.place(x=380,y=220)
	
	c=Entry(root)
	c.place(x=380,y=270)
	
	s_p=Entry(root)
	s_p.place(x=380,y=320)
	
	v_n=Entry(root)
	v_n.place(x=380,y=370)
	
	v_p=Entry(root)
	v_p.place(x=380,y=420)
	
	Button(root,text='Search',command=search).place(x=550,y=120)
	Button(root,text='Update',command=update_c).place(x=450,y=450)
	
	root.mainloop()