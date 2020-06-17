from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from linkable_ring_signature import ring_signature, verify_ring_signature
from ecdsa.util import randrange
from ecdsa.curves import *


window = Tk()

window.title("Firma en anillo enlazado o vinculado (Linkable ring signature)")
window.geometry("1800x1200")
window.config(bd="10",relief="groove")
tab_control = ttk.Notebook(window)



tab1 = ttk.Frame(tab_control, borderwidth=10, relief="groove")
tab2 = ttk.Frame(tab_control, borderwidth=10, relief="groove")
tab_control.add(tab1, text='Firma')
tab_control.add(tab2, text='Verificacion')


#Tab1
## Labels
lblTitle1 = Label(tab1, text="Generación de firma en anillo sobre curva secp256k1", background="orange red", foreground="black", font="none 25 bold", 
	width=100, anchor=CENTER)
lblTitle1.grid(row=1, column=0,columnspan=4,pady=30)

lblParticipants= Label(tab1, text="Selecccione el número de participantes en el grupo de firma: ", foreground="black", font ="none 15 ").grid(row=2, 
	column=1,pady=10,padx=10,sticky="e")

msg11 = Label(tab1, text="Introduzca el mensaje 1 para ser firmado: ", foreground="black",font ="none 15 ").grid(row=3, column=1,pady=50,padx=10,sticky="e")

msg12 = Label(tab1, text="Introduzca el mansaje 2 para ser firmado: ", foreground="black",font ="none 15 ").grid(row=7, column=1,pady=50,padx=10,sticky="e")


## Entrys
numberParticipants1 = Combobox(tab1,font ="none 15 bold")
numberParticipants1['values']= (3, 4, 5, 6, 7, 8, 9, 10)
numberParticipants1.current(0)
numberParticipants1.grid(row=2,column=2,columnspan=3,pady=50,sticky="w")

msgText11 = Text(tab1,width=50, height=5,font ="none 15 bold")
msgText11.grid(row=3, column=2,columnspan=2,sticky="w")
msgText11.focus_set()

msgText12 = Text(tab1,width=50, height=5,font ="none 15 bold")
msgText12.grid(row=7, column=2,columnspan=3,sticky="w")
msgText12.focus_set()

lblSignature1 = Label(tab1,text = "La firma generadas es: ",font ="none 15 ")
lblSignature1.grid(row=5,column=0,sticky="e")

signature1 = Label(tab1,font ="none 15 bold")
signature1.grid(row=5,column=1,columnspan=2,sticky='w')

lblKeyimage1 = Label(tab1,text="La clave imagen es: ",font ="none 15 ")
lblKeyimage1.grid(row=6,column=0,sticky='e',pady=20)

keyimage1 = Label(tab1,font ="none 15 bold")
keyimage1.grid(row=6,column=1,columnspan=2,sticky='w')

lblSignature2 = Label(tab1,text = "La firma generadas es: ",font ="none 15")
lblSignature2.grid(row=9,column=0,sticky='e')

signature2 = Label(tab1,font ="none 15 bold")
signature2.grid(row=9,column=1,columnspan=2,sticky='w')

lblKeyimage2 = Label(tab1,text="La clave imagen es: ",font ="none 15")
lblKeyimage2.grid(row=10,column=0,sticky='e', pady=20)

keyimage2 = Label(tab1,font ="none 15 bold")
keyimage2.grid(row=10,column=1,columnspan=2,sticky='w')


n = int(numberParticipants1.get())
x = [ randrange(SECP256k1.order) for i in range(n)]
x_pi = x[0]
signature11=''
keyimage11=''
signature12=''
keyimage12=''
y=list(map(lambda xi: SECP256k1.generator * xi, x))
sig1= ring_signature(x_pi, 0, 'hola', y)
sig2= ring_signature(x_pi, 0, 'hola', y)
msg1=''
msg2=''

def confirm():
	n = int(numberParticipants1.get())
	x_list = [ randrange(SECP256k1.order) for i in range(n)]
	global x, x_pi
	x = x_list
	global y
	y = list(map(lambda xi: SECP256k1.generator * xi, x))
	x_pi = x_list[0]
	messagebox.showinfo("Número de integrantes del grupo de firmas", "Se ha elegido "+ str(n) +" participantes para formar el grupo.")

	


btnConfirm = Button(tab1, text="Confirmar",command=confirm)
btnConfirm.grid( row=2,column=2,padx=200)

def ringSign1():

	if msgText11:
		msg = msgText11.get("1.0","end")
		global sig1, msg1
		msg1 = msg
		sig1 = ring_signature(x_pi, 0, msg, y)
		signature1.configure(text=str(sig1[0])+","+"\n"+(str(sig1[1])).strip('[]').replace(',',',\n'))
		keyimage1.configure(text=str(sig1[2]).strip('()').replace(',',',\n'))
		global signature11, keyimage11
		signature11 = str(sig1[0])+","+"\n"+(str(sig1[1])).strip('[]').replace(',',',\n')
		keyimage11 = str(sig1[2]).strip('()').replace(',',',\n')
		 
btn1 = Button(tab1, text="Firmar mensaje 1",command=ringSign1)
btn1.grid( row=4,column=2)


def ringSign2():

	if msgText12:
		msg = msgText12.get("1.0","end")		
		global sig2, msg2
		msg2 = msg
		sig2 = ring_signature(x_pi, 0, msg, y)
		signature2.configure(text=str(sig2[0])+","+"\n"+(str(sig2[1])).strip('[]').replace(',',',\n'))
		keyimage2.configure(text=str(sig2[2]).strip('()').replace(',',',\n'))
		global signature12, keyimage12
		signature12 = str(sig2[0])+","+"\n"+(str(sig2[1])).strip('[]').replace(',',',\n')
		keyimage12 = str(sig2[2]).strip('()').replace(',',',\n')
		

btn2 = Button(tab1, text="Firmar mensaje 2",command=ringSign2)
btn2.grid( row=8,column=2)

#Tab2
## Labels
lblTitle2 = Label(tab2, text="Verificación de firma en anillo sobre curva secp256k1", background="green yellow", foreground="black", font="none 25 bold", 
	width=100, anchor=CENTER)
lblTitle2.grid(row=1, column=0,columnspan=4,pady=30)

lblParticipants2= Label(tab2, text="El numero de participantes en el grupo es de: ", foreground="black",font ="none 15 ").grid(row=2, 
	column=0,sticky="e")

msg21 = Label(tab2, text="El contenido del mensaje 1 es: ",font ="none 15").grid(row=3, column=0,sticky="e")

msg22 = Label(tab2, text="El contenido del mensaje 2 es: ",font ="none 15 ").grid(row=4, column=0,sticky="e")

lblsignature21 = Label(tab2, text="El valor de la firma 1 es: ",font ="none 15")
lblsignature21.grid(row=5, column=0,sticky="e",pady=20)

lblsignature22 = Label(tab2, text="El valor de la firma 2 es: ",font ="none 15 ")
lblsignature22.grid(row=6, column=0,sticky="e",pady=20)

lblKeyImage21 = Label(tab2, text="El valor de la clave imagen 1 es: ",font ="none 15 ")
lblKeyImage21.grid(row=7, column=0,sticky="e",pady=20)

lblKeyImage22 = Label(tab2, text="El valor de la clave imagen 2 es: ",font ="none 15 ")
lblKeyImage22.grid(row=8, column=0,sticky="e",pady=20)

lblVer11 = Label(tab2, text="Resultado verificación de la firma 1 sobre mensaje 1 : ",font ="none 15 ")
lblVer11.grid(row=9, column=0,sticky="e")

lblVer21 = Label(tab2, text="Resultado verificación de la firma 2 sobre mensaje 1 : ",font ="none 15 ")
lblVer21.grid(row=10, column=0,sticky="e")

## Entrys
numberParticipants2 = Label(tab2,font ="none 15 bold")
numberParticipants2.grid(row=2,column=1,sticky="w")

msgText21 = Label(tab2,font ="none 15 bold")
msgText21.grid(row=3, column=1,sticky="w")

msgText22 = Label(tab2,font ="none 15 bold")
msgText22.grid(row=4, column=1,sticky="w")

signature21 = Label(tab2,font ="none 15 bold")
signature21.grid(row=5, column=1,sticky="w")

signature22 = Label(tab2,font ="none 15 bold")
signature22.grid(row=6, column=1,sticky="w")

keyimage21 = Label(tab2,font ="none 15 bold")
keyimage21.grid(row=7,column=1,sticky='w')

keyimage22 = Label(tab2,font ="none 15 bold")
keyimage22.grid(row=8,column=1,sticky="w")

ver11 = Label(tab2,font ="none 15 bold")
ver11.grid(row=9, column=1,sticky="w")

ver21 = Label(tab2,font ="none 15 bold")
ver21.grid(row=10, column=1,sticky="w")

msg1=msgText11.get("1.0","end").strip()

def verification11():
	print(verify_ring_signature(msg1, y, *sig1))
	if verify_ring_signature(msg1, y, *sig1):
	 	ver11.config(text="Verificado correctamente",font ="none 18 bold", foreground="green")
	 	messagebox.showinfo("Verificación de firma", "La firma ha sido verificado correctamente")
	else:
	 	ver11.config(text="Fallo en la verificación",font ="none 18 bold",foreground="red")
	 	messagebox.showwarning("Verificación de firma", "Error en la verificación de la firma")	
	

btnVer11 = Button(tab2, text='Verificar firma 1 sobre mensaje 1',command=verification11)
btnVer11.grid(row=9, column=1,sticky="e")

def verification21():
	print(verify_ring_signature(msg1, y, *sig2))
	#print(verify_ring_signature('hola', y, *sig1))
	if verify_ring_signature(msg1, y, *sig2):
		ver21.config(text="Verificado correctamente",font ="none 18 bold",foreground="green")
		messagebox.showinfo("Verificación de firma", "La firma ha sido verificado correctamente")
	else:
		ver21.config(text="Fallo en la verificación",font ="none 18 bold",foreground='red')
		messagebox.showwarning("Verificación de firma", "Error en la verificación de la firma")	
	

btnVer21 = Button(tab2,text='Verificar firma 2 sobre mensaje 1', command=verification21)
btnVer21.grid(row=10, column=1,sticky="e")

def update():
	numberParticipants2.configure(text=numberParticipants1.get())
	msgText21.configure(text=msgText11.get("1.0","end").strip())
	msgText22.configure(text=msgText12.get("1.0","end").strip())
	signature21.configure(text=signature11)
	signature22.configure(text=signature12)
	keyimage21.configure(text=keyimage11)
	keyimage22.configure(text=keyimage12)


btnUpdate = Button(tab2, text="Actualizar datos de las firmas generadas",command=update)
btnUpdate.grid( row=2,column=1)

tab_control.pack(expand=1, fill='both')

window.mainloop()

