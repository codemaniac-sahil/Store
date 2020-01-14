from tkinter import*
from tkinter import messagebox
from Update import update

import sqlite3
con=sqlite3.connect('store.db')
cur=con.cursor()
def admin():
	root=Toplevel()
	root.title('Reliance Store')
	f1=Frame(root,bg='#0398fc',height=200)
	root.geometry('1080x680')
	Label(f1,text='Admin page\n',bg='#0398fc',font='corbel 18 bold').pack()
	f1.pack(fill='x',pady=15,padx=23)
	p_id=Label(root,text='Product id',font='corbel 10')
	p_id.place(x=100,y=120)
	
	p=Label(root,text='Product name',font='corbel 10')
	p.place(x=100,y=170)

	def getval():
		pid_e=p_id_e.get()
		p_n_e=p_e.get()
		s_e=s.get()
		c_e=c.get()
		s_p_e=s_p.get()
		v_n_e=v_n.get()
		v_p_e=v_p.get()
			
		if (p_n_e=='' or s_e=='' or c_e=='' or s_p_e=='' or v_n_e=='' or v_p_e==''):
			messagebox.showinfo('Error','Fill all the enteries')
		else:
			sql="insert into 'inventory'(id ,name ,stock ,cp ,sp ,vendor_name ,vendor_phone)  values(?,?,?,?,?,?,?)"
			values=(pid_e,p_n_e,s_e,c_e,s_p_e,v_n_e,v_p_e)
			cur.execute(sql,values)
			con.commit()
			messagebox.showinfo('Success','Item added successfully')
			
		
		
		
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
	
	Button(root,text='Add',command=getval).place(x=450,y=450)
	Button(root,text='Update',command=update).place(x=300,y=450)
	
	root.mainloop()