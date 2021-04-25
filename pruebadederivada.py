#####	Nombre del proyecto: Algoritmo De Newton Rapshon Estandar
#####	Version:			 V.1
#####	Descripcion:		 The Newton-Raphson method 
#####	Fecha de creacion: 	 26/04/2021
#####	Creado por:			 Armando Pineda Paredes
#####	Diseñado por:		 Armando Pineda Paredes
#####	Comentarizado por:	 Armando Pineda Paredes
#####	Profesion:			 Estudiante
#####	Universidad:		 Universidad Francisco de paula santander ocaña (ufpso)
#####	Codigo Universitario:191697
#####	E-MAIL:				 ajpineda@ufpso.edu.co - armandojosepineda26@gmail.com			
#####	Ciudad:				 Ocaña Norte De Santander
#####	Derechos reservados: Alcander.SA 			
#####	Proyecto:			 Link de git-hub





from tkinter import *    ## importamos la libreria tkinter para la interfaz grafica del programa 
from tkinter import ttk   ## hacemos el llamado de la libreria y le asignamos la variable ttk
import tkinter as tk
from math import *       ## importamos la libreria math para operaciones matematica simples
import numpy as np       ## importamos la libreria numpy para la creacion de arreglos y trabajar con ellos en operaciones matematicas
from sympy import Derivative, diff, simplify, Symbol
import sympy as sp
import time
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkinter import filedialog


##-----------------------------------------------Parte Grafica--------------------------------------------------

raiz=Tk()                                                 ## Creamos un nombre variable igualado a la tk haciendo referencia a tkinter
raiz.title("Calculadora De Metodo de Newton-Raphson")     ## Con la variable raiz. creamos un titulo para la ventana de la interfaz
raiz.geometry('1920x1060')                              ## Creamos un tamaño de 1920x1080 para que sea por defecto
raiz.configure(background='red',cursor="spraycan")        ## Configuramos la raiz, que va hacer el contenedor principal
raiz.iconbitmap("calculadora.ico")



Frame=Frame(raiz)                                              ## Creamos un contenedor donde van a ir todos los datos, dentro de raiz
Frame.pack(fill="both",expand="True")                          ## le damos la propiedad de enpaquetar y le decimos que sea algo tipo responsive
Frame.config(height="500",width="500",relief="ridge",bd=10)    ## configuramos el contenedor FRAME y le damos color de fondo y tamaño
clock=Label(Frame,font=("times",50,"bold"))

#f5f5f5
##imagene de fondo 
##img = PhotoImage(file="instagram.gif")                    ## Ceamos una variable llamada img y hacemos el llamado del archivo con el file 
##fondo = Label(Frame, image=img).place(x=0,y=0)         ##creamoon label que representa el fondo y le asignamos el nombre de la variable de la imagen







##---------------------------------------------Variables------------------------------------------------------

error_relativo = StringVar()              ## Creamos la variable error_relativo y le asignamos de tipo double para que reciba numeros decimales               
valor_inicialv = StringVar()              ## Creamos la variable Valor_inicialv y le asignamos de tipo double para que reciba numeros decimales
derivadaf = StringVar()                   ## Creamos la variable derivadaf de tipo StrinVar que es tipo texto, ya que vamos a recibir ese dato como texto
funcion = StringVar()                     ## Creamos la variable funcion de tipo StrinVar que es tipo texto, ya que vamos a recibir ese dato como texto
resultadoFuncion = StringVar()                   ## Creamos la variable resultado donde se mostrara todo de tipo StrinVar que es tipo texto


##-----------------------------------------------Parte Grafica--------------------------------------------------

##titulo del proyecto
tituloLabel=Label(Frame, text="Metodo de Newton Raphson",  font = ("Comic Sans MS", 16, "bold")) ## Creamos un label que muestra un texto que es "metodo de newton raphson" y le colocamos el tipo de letra, tamaño y en negrilla
tituloLabel.pack(padx=5,pady=5,ipadx=5,ipady=5)                                                  ## Empaquetamos el titulo y le damos 5 espacio hacia la derecha,izquierda,arriba y abajo del label
tituloLabel.config(                                                                              ## Colocamos la etiqueta config que sirve para configurar parametros de diseño del label
	foreground="#fa7014",                                                                        ## Le colocamos un color de letra de color naranja                                                                                ## Le colocamos un color de fondo gris
	justify="center"                                                                             ## Le decimos que se posicione en el centro                     
    )


##introduccion para el metodo de newton rapshon
descripcionLabel=Label(Frame, text="\n Esta calculadora en línea implementa el método de Newton (también conocido como el método de Newton-Raphson) usando  la calculadora de derivadas para obtener una forma analítica \n de la derivada de la función dada, porque este método lo requiere. La teoría para recordar los conceptos básicos del método se puede encontrar debajo de la calculadora",  font = ("Comic Sans MS", 13))
descripcionLabel.pack(padx=5,pady=5,ipadx=5,ipady=5)                                             ## Arriba se crea el label para describir el metodo de newton y se le dan propiedades
descripcionLabel.config(                                                                         ## Se configura el label de descripcion con .config
	foreground="black",                                                                          ## Le colocamos un color de letra negro
	justify="left"                                                                               ## Le decimos que se posicione a la izquerda
    )


#label para la creacion del subtitulo "funcion f(x)"                                            
funcionLabel=Label(Frame, text="Función F(x):",  font = ("Comic Sans MS", 12, "bold"))           ## Creamos el label donde va el texto de funcion f(x)
funcionLabel.pack(padx=5,pady=5,ipadx=5,ipady=5)                                                 ## Empaquetamos el titulo y le damos 5 espacio hacia la derecha,izquierda,arriba y abajo del label
funcionLabel.config(                                                                             ## Se configura el label de descripcion con .config
	foreground="#fa7014",                                                                        ## Le colocamos un color de letra naranja
	justify="left"                                                                               ## Le decimos que se ajuste a la izquierda en su cuadro de texto
    )

##caja de texto que va al lado del subtitulo "funcion f(x)""
cuadroFuncion=Entry(Frame,textvariable=funcion, font = ("Comic Sans MS", 10, "bold"))            ## Creamos un entry que sera por donde entran los datos, espeficicamente donde entran los datos del label anterior que es funcion
cuadroFuncion.pack(padx=5,pady=5,ipadx=5,ipady=5)                                                ## Empaquetamos el titulo y le damos 5 espacio hacia la derecha,izquierda,arriba y abajo del label


 
##subtitulo para la creacion de "derivada de f(x)"                                                  
derLabel=Label(Frame, text="Derivada de F(X)",  font = ("Comic Sans MS", 12, "bold") )            ## Creamos el texto que diga Derivada de f(x) y le colocamos tipo de fuente,tama{o y negrilla}
derLabel.pack(padx=5,pady=5,ipadx=5,ipady=5)                                                      ## Empaquetamos el titulo y le damos 5 espacio hacia la derecha,izquierda,arriba y abajo del label
derLabel.config(                                                                                  ## Se configura el label de descripcion con .config
	foreground="#fa7014",                                                                         ## Le colocamos un color de letra naranja
	justify="left"                                                                                ## Le decimos que se ajuste a la izquierda en su cuadro de texto
    )

##caja de texto que reprenta al subtitulo "derivada de f(x)"
cuadroder=Entry(Frame,textvariable=derivadaf, font = ("Comic Sans MS", 10, "bold"))                ## Creamos la caja de texto para que el usuario ingrese la derivada
cuadroder.pack(padx=5,pady=5,ipadx=5,ipady=5)                                                      ## Lo empaquetamos y le damos propiedades

##label que representa el subtitulo "valor inicial"
vlLabel=Label(Frame, text="Valor Inicial",  font = ("Comic Sans MS", 12, "bold"))                  ## Creamos un label donde mostrar el nombre de valor inicial 
vlLabel.pack(padx=5,pady=5,ipadx=5,ipady=5)                                                        ## Creamos una configuracion para esa caja de texto 
vlLabel.config(                                                                                    
	foreground="#fa7014",                                                                          ## Le damos un color de letra de #fa7014
	justify="left"                                                                                 ## y que cuando empiece a escribir, las letras aparescan desde la izquierda
    )

##caja de texto que pertenece al subtitulo "valor inicial"
cuadrovl=Entry(Frame,textvariable=valor_inicialv, font = ("Comic Sans MS", 10, "bold"))            ## Creamos la respectiva caja de texto donde el usuario ingresara ese valor inicial
cuadrovl.pack(padx=5,pady=5,ipadx=5,ipady=5)                                                       ## Le damos propiedades de posicionamiento a esa caja donde el usuario va a escribir 

##creacion del label para el subtitulo "error relativo"
errorLabel=Label(Frame, text="Error Relativo",  font = ("Comic Sans MS", 12, "bold"))              ## Creamos un label donde va a mostrar el mensaje error relativo 
errorLabel.pack(padx=5,pady=5,ipadx=5,ipady=5)                                                     ## le damos una configuracion para que se ubique correctamnete a ese label de mensaje
errorLabel.config(                                        										   ## Le empezamos a dar una caonfiguracion
	foreground="#fa7014",                                                                          ## Le colocamos color de letras naranja a ese mensaje que aparece
	justify="left"                  														       ## y que cuando empiece a escribir, las letras aparescan desde la izquierda
    )

##creacion de la caja de texto para el subtitulo "error relativo"
cuadroerror=Entry(Frame,textvariable=error_relativo, font = ("Arial", 10, "bold"))                  ## Creamos la caja de texto que es donde va a escribir el eror relativo, le asignamos la valiebra y le damos propiedades de letra, tamañao y negrilla
cuadroerror.pack(padx=5,pady=5,ipadx=5,ipady=5) 


errorLabel=Label(Frame, text="Calculadora De Derivadas",  font = ("Comic Sans MS", 12, "bold"))              ## Creamos un label donde va a mostrar el mensaje error relativo 
errorLabel.place(x=1050,y=257)                                                     ## le damos una configuracion para que se ubique correctamnete a ese label de mensaje
errorLabel.config(                                        										   ## Le empezamos a dar una caonfiguracion
	foreground="#fa7014",                                                                          ## Le colocamos color de letras naranja a ese mensaje que aparece
	justify="left"                  														       ## y que cuando empiece a escribir, las letras aparescan desde la izquierda
    )                                                    ## y le damos uss respectivas propiedades

##Mostrar lo ingresado
Mostrar_Funcion= StringVar()
Mostrar_Derivada=  StringVar()
Mostrar_ValorI= StringVar()
Mostrar_Error= StringVar()
Resultado_Mio= StringVar()

TextoRespuesta=Label(raiz,text="el resultado es: ",textvariable=Resultado_Mio,font=("",12))
TextoRespuesta.place(x=500,y=870)


##-----------------------------------------------Operaciones Matematicas Del Metodo Newton Raphson--------------------------------------------------

rest = StringVar()
##creacion del label para mostrar derivada
textoR = Label(Frame,text="el resultado es: ",textvariable=rest, font = ("Comic Sans MS", 12))
textoR.place(x=1050,y=303)

##funcion que recibe y realiza todas las operaciones
def mostrar(): 
	answer=messagebox.askyesno('Validacion De Datos', 'Los Datos Ingresados Son Correctos? '+'\n1. La Funcion ingresada es '+ str(funcion.get()) +'\n2. La Derivada ingresada es ' + str(derivadaf.get())+'\n3. El valor inicial es ' + str(valor_inicialv.get()) + '\n4. El eror relativo es ' + str(error_relativo.get()))
	if answer:
	                                                                               				   ## Creamos la funcion con el nombre de "mostrar()", que hace que solo se active esa funcion solo si se activa el boton que se llama de la misma forma "mostrar"
		f = lambda x:eval(funcion.get())															   ## Llamamos la caja de texto (entry)  llamada funcion y la convertimos de texto a matematica y la guardamos en la variable f				
		df = lambda x:eval(derivadaf.get())															   ## Hacemos el llamado de la caja de texto (entry)  derivada f y la convertimos en matematica y la guardamos en la variable df 
		xi = eval(valor_inicialv.get())																   ## Hacemos el llamado de la caja de texto (entry)  valor inicial y la convertimos en matematica y la guardamos en la variable xi 
		tol = eval(error_relativo.get())															   ## Hacemos el llamado de la caja de texto (entry) error relativo y la convertimos en matematica y la guardamos en la variable tol (haciendo referencia a tolerancia o erroe relativo)
		tramo = abs(tol)																			   ## La variable tol le colocamos abs(tol) para que la tolerancia ingresada se convierta en valor absoluto, siempre positiva, nunca un valor negativo y la guardamos en la variable tramo
		x = xi                                                                                         ## la variable xi luego de transformada la guardamos en la variable x 

	
		print("valores del problema")                                                                    
		print('* la funcion ingresada es = ',(funcion.get()))
		print('* la derivada ingresada es = ',derivadaf.get())
		print('* el valor inicial es x0 = ',xi)
		print('* la error es = ',tol)
		print('----------------------------------------------')

		iteraciones=100
		c=0
		xprimero=x
		tv.insert('',20,values=(c,'{:.4f}'.format(xprimero),'{:.4f}'.format(f(xprimero)),'{:.4f}'.format(df(xprimero)),'---'))
		
		while ( tramo >= tol and c <= iteraciones):  																										 ## Creamos un while para realizar todas las iteraciones solo si el tramo(error relativo) es mayor o igual al tol(valor inicial) que es lo que el usuario ingresa
			xnuevo = (x) - (f(x)/df(x))                                                                                                                      ## Aplicamos la formula para sacar xi+1 y la guardamos en una variable llamada xi nuevo que hace referencia a xi siguiente
			tramo  = abs(((xnuevo-x)/xnuevo)*100)                                                                                                            ## Aplicamos la formula para calcula el error relativo y con el abs() lo convertimos en 
			##tabla.append([x,xnuevo,tramo])
			x = xnuevo
			c+=1                                                                                                                                        ## Aca guaradamos a x nuevo de nuevo en la variable de x y es como si e usuario estuviera ingresando de nuevo el xi, y asi realiza todas las iteraciones
			tv.insert('',20,values=(c,'{:.4f}'.format(x),'{:.4f}'.format(f(x)),'{:.4f}'.format(df(x)),'{:.4f}'.format(tramo) + '%'),tags=('BUY'))              ## Aca solo nos encargamos de llamar todas las variables para imprimirlas, y como esta dentro del while cada ves que ahce las iteraciones las arroja, y le decimos que las arroje con 4 decimales depues del punto 
			print('\nxi: {:.4f}'.format(x))                                                                                                                  ## Este comando es para imprimir la x inicial pero en consola, esta zona el usuario no la ve, es solo para llevar un control del funcionamiento
			print('con un error relativo de: {:.4f}'.format(tramo) + '%')                                                                                    ## Este comando es para imprimir la error relativo porcentual pero en consola, esta zona el usuario no la ve, es solo para llevar un control del funcionamiento
			print('f(x): {:.4f}'.format(f(xnuevo)))                                                                                                          ## Este comando es para imprimir la F(XI)pero en consola, esta zona el usuario no la ve, es solo para llevar un control del funcionamiento
			print('f(xi): {:.4f}'.format(df(xnuevo))) 
                                                                                                     ## Este comando es para imprimir la DF(XI) inicial pero en consola, esta zona el usuario no la ve, es solo para llevar un control del funcionamiento

		##('el valor aproximado del 0 de la funcion es: ','{:.4f}'.format(x),'para un error relativo porcentual aproximado de : {:.4f}'.format(tramo),' que es menor a: ',tol)
		res=str(('El valor aproximado del 0 de la funcion es {:.4f}'.format(x) + ' Para un error relativo porcentual aproximado de  {:.4f}'.format(tramo) + ' Que es menor a ' + str(tol)))  ## Aca solo estamos imprimiendo las respuesta oficial y haciendo el tamaño de los componenten como: xi, el porcentaje y hacemos alucion que ese porcentaje es menor al error ingresado por el usuario, y lo guardamos en una variable res(resultado)  
		Resultado_Mio.set(res)
		funcion.set("")
		derivadaf.set("")
		valor_inicialv.set("")                                                                                                                                                     ## Hacemos el llamado de la caja de texto y dentro del parentesis le damos el valor de la variable res (resultado)
		error_relativo.set("")

def Limpiar ():
	rest.set("")
	Resultado_Mio.set("")
	for borrar in tv.get_children():
		tv.delete(borrar)

def Derivar():
	x=Symbol('x')
	n=funcion.get()
	derivada=diff(n,x)
	rest.set("la derivada es " + str(derivada))




##-----------------------------------------------Parte Grafica Botom--------------------------------------------------

##boton 
botonMostrar=Button(Frame, text="Resolver",font = ("MS Sans Serif", 11, "bold"), command=mostrar, bg="#fa7014",  fg = "#E6E9ED")                  ## Creamos el boton llamado resolver y lo guardamos en un comando que se llame mostrar, que es presionar este boton ejecuta todas las lienas de codigo anteriores
botonMostrar.pack(padx=5,pady=5,ipadx=5,ipady=5)  

botonLimpiar=Button(Frame, text="Limpiar tabla",font = ("MS Sans Serif", 11, "bold"), command=Limpiar, bg="#fa7014",  fg = "#E6E9ED")                  ## Creamos el boton llamado resolver y lo guardamos en un comando que se llame mostrar, que es presionar este boton ejecuta todas las lienas de codigo anteriores
botonLimpiar.pack(padx=5,pady=5,ipadx=5,ipady=5)

botonDerivar=Button(Frame, text="Derivar Funcion",font = ("MS Sans Serif", 11, "bold"), command=Derivar, bg="#fa7014",  fg = "#E6E9ED")                  ## Creamos el boton llamado resolver y lo guardamos en un comando que se llame mostrar, que es presionar este boton ejecuta todas las lienas de codigo anteriores
botonDerivar.place(x=1280,y=257)
botonDerivar.config(width="14",height="1")
                                                                                              ## Le damos unas propiedaes de posisionamiento

##-----------------------------------------------Parte Grafica Tabla-------------------------------------------------

##tabla
tv=ttk.Treeview(raiz,columns=('I','XI','F(XI)','DF(XI)','|EA|'), show='headings')   
tv.column('I',minwidth=0, width=85,anchor="n")                            ## Creamos una tabla y le definimos las columnas que va a tener y lo guardamos en TV
tv.column('XI',minwidth=0, width=85,anchor="n")                                                            ## Creamos la columna llamada XI y le damos propiedades de tamaño
tv.column('F(XI)',minwidth=0, width=105,anchor="n")                                                        ## Creamos la columna llamada F(XI) y le damos propiedades de tamaño
tv.column('DF(XI)',minwidth=0, width=105,anchor="n")                                                       ## Creamos la columna llamada DF(XI) y le damos propiedades de tamaño                                                                      
tv.column('|EA|',minwidth=0, width=105,anchor="n")        
tv.heading('I',text='I')                                                  ## Creamos la columna llamada EA(error porcentual) y le damos propiedades de tamaño            
tv.heading('XI',text='XI')                                                                                 ## Ahora aca le estamos asignando una variable a esas columnas para poder identificar quien es quien y a la hora de mostrar saber donde mostrar, aca le asignamos XI que tenga un texto de XI
tv.heading('F(XI)',text='F(XI)')                                                                           ## Ahora aca le estamos asignando una variable a esas columnas para poder identificar quien es quien y a la hora de mostrar saber donde mostrar, aca le asignamos F(XI) que tenga un texto de F(XI)
tv.heading('DF(XI)',text='DF(XI)')                                                                         ## Ahora aca le estamos asignando una variable a esas columnas para poder identificar quien es quien y a la hora de mostrar saber donde mostrar, aca le asignamos DF(XI) que tenga un texto de DF(XI)
tv.heading('|EA|',text='|EA|')                                                                             ## Ahora aca le estamos asignando una variable a esas columnas para poder identificar quien es quien y a la hora de mostrar saber donde mostrar, aca le asignamos EA que tenga un texto de EA(ERROR RELATIVO)
tv.place(x=710,y=640)                                                                                      ## Aca le estamos dando donde se debe posicionar esa tabla en la interfaz

##boton crear nueva ventana 
def v2():
	raiz2 = Toplevel()
	raiz2.geometry("1100x900")
	raiz2.title("Guia De Usuario")
	raiz2.iconbitmap("libro.ico")

##imagen del boton
imgBoton=PhotoImage(file="rueda.gif")

##boton
botonabrirventana=Button(Frame, text="guia de usuario",image=imgBoton,font = ("MS Sans Serif", 11, "bold"),command=v2,borderwidth="5",relief="flat")
botonabrirventana.place(x=1800,y=40)
botonabrirventana.config(
	width="40",
	height="40"
	)
##reloj
def times():
	current_time=time.strftime("%H:%M:%S") 
	clock.config(text=current_time,fg="#fa7014",font=("Helvetica",17))
	clock.after(1000,times)

clock.place(x=0,y=5)
times()


##menu
menubar = Menu(raiz)
raiz.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)

def NuevoA ():
	for borrar in tv.get_children():
		tv.delete(borrar) 
	funcion.set("")
	derivadaf.set("")
	valor_inicialv.set("")                                                                                                                                                     ## Hacemos el llamado de la caja de texto y dentro del parentesis le damos el valor de la variable res (resultado)
	error_relativo.set("")
	Mostrar_Funcion.set("")
	Mostrar_Derivada.set("")
	Mostrar_ValorI.set("")
	Mostrar_Error.set("")
	Resultado_Mio.set("")
filemenu.add_command(label="Nuevo Archivo",command=NuevoA)

filemenu.add_separator()

def AbrirA():
    print(filedialog.askopenfilename(initialdir = "/",title = "Abrir Archivo",defaultextension=".txt",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))
filemenu.add_command(label="Abrir Archivo",command=AbrirA)

filemenu.add_separator()

def GuardarA():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Guardar Archivo",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))
filemenu.add_command(label="Guardar Archivo",command=GuardarA)

filemenu.add_separator()

def clicked():
	answer=messagebox.askyesno('Advertencia', 'Seguro que quieres salir?')
	if answer:
		raiz.destroy()
filemenu.add_command(label="Salir",command=clicked)



editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_separator()
editmenu.add_command(label="Copiar")
editmenu.add_separator()
editmenu.add_command(label="Pegar")


helpmenu = Menu(menubar, tearoff=0)

def VAyuda():
	raiz2 = Toplevel()
	raiz2.geometry("500x600")
	raiz2.title("Ayuda De Usuario")
	raiz2.iconbitmap("libro.ico")
helpmenu.add_command(label="Ayuda",command=VAyuda)

helpmenu.add_separator()

def AcercaD():
	raiz3 = Toplevel()
	raiz3.geometry("900x639")
	raiz3.title("Acerca Del software")
	raiz3.iconbitmap("libro.ico")

	fondoacercad=PhotoImage(file="picasoacercade.gif")
	fondo7 = Label(raiz3, image=fondoacercad).place(x=0,y=0)
	raiz3.mainloop()
helpmenu.add_command(label="Acerca de...",command=AcercaD)

guiamenu = Menu(menubar, tearoff=0)

def GuiaM():
	raiz4 = Toplevel()
	raiz4.geometry("1200x675")
	raiz4.title("Guia De Metodo Newton-Raphson")
	raiz4.iconbitmap("libro.ico")
	raiz4.config(bg="white")
	
	fondoguiame=PhotoImage(file="picasometodo2.gif")
	fondo7 = Label(raiz4, image=fondoguiame).place(x=0,y=0)
	

	raiz4.mainloop()
guiamenu.add_command(label="Guia del metodo",command=GuiaM)

guiamenu.add_separator()

guiamenu.add_command(label="Guia del software",command=v2)

guiamenu.add_separator()

def EntradaD():
	raiz6 = Toplevel()
	raiz6.geometry("932x550")
	raiz6.title("Guiar Para Entrada De Los Datos")
	raiz6.iconbitmap("entradad.ico")
	raiz6.config(bg="white")

	Titulodatos = Label(raiz6,text="Operadores Matematicos Para La Entrada Del Software", font = ("Comic Sans MS", 13,"bold"))
	Titulodatos.place(x=250,y=0)
	Titulodatos.config(foreground="#fa7014",bg="white")
	Definiciondatos = Label(raiz6,text="En cuanto a los operadores aritméticos, estos permiten realizar las diferentes operaciones aritméticas del álgebra: suma, resta,",font = ("Comic Sans MS", 12))
	Definiciondatos.place(x=0,y=56)
	Definiciondatos.config(bg="white")
	Definiciondatos = Label(raiz6,text="producto, división, …Estos operadores de Python son de los más utilizados. El listado completo es el siguiente:", font = ("Comic Sans MS", 12))
	Definiciondatos.place(x=0,y=80)
	Definiciondatos.config(bg="white")

	fondoentradaD=PhotoImage(file="picasotabla.gif")
	fondo6 = Label(raiz6, image=fondoentradaD).place(x=140,y=129)
	raiz6.mainloop()

guiamenu.add_command(label="Guia para entrada de datos",command=EntradaD)

guiamenu.add_separator()

def AnalisisD():
	raiz7 = Toplevel()
	raiz7.geometry("1200x675")
	raiz7.title("Analisis De Los Resultados")
	raiz7.iconbitmap("libro.ico")


	fondoanalisisd=PhotoImage(file="picasodatosm.gif")
	fondo6 = Label(raiz7, image=fondoanalisisd).place(x=0,y=0)
	raiz7.mainloop()
guiamenu.add_command(label="Analisis de los datos",command=AnalisisD)

contacmenu = Menu(menubar, tearoff=0)

def DatosDe():
	raiz8 = Toplevel()
	raiz8.geometry("720x500")
	raiz8.title("Datos De Desarrollador")
	raiz8.iconbitmap("libro.ico")

	fondodesa=PhotoImage(file="picasodesarrollador.gif")
	fondo2 = Label(raiz8, image=fondodesa).place(x=0,y=0)
	raiz8.mainloop()
contacmenu.add_command(label="Desarrollador",command=DatosDe)

contacmenu.add_separator()

def DatosDi():
	raiz9 = Toplevel()
	raiz9.geometry("720x500")
	raiz9.title("Datos De Diseñador")
	raiz9.iconbitmap("libro.ico")

	fondodis=PhotoImage(file="picasodiseñador.gif")
	fondo2 = Label(raiz9, image=fondodis).place(x=0,y=0)
	raiz9.mainloop()
contacmenu.add_command(label="Diseñador",command=DatosDi)

contacmenu.add_separator()

def DatosMa():
	raiz10 = Toplevel()
	raiz10.geometry("720x500")
	raiz10.title("Datos Del Matematico")
	raiz10.iconbitmap("libro.ico")

	fondoma=PhotoImage(file="picasomatematico.gif")
	fondo3 = Label(raiz10, image=fondoma).place(x=0,y=0)
	raiz10.mainloop()
contacmenu.add_command(label="Matematico",command=DatosMa)

contacmenu.add_separator()


def DatosRe():
	raiz11 = Toplevel()
	raiz11.geometry("720x500")
	raiz11.title("Redes")

	RedeLabel=Label(raiz11, text="adsadsadsads",  font = ("Comic Sans MS", 16, "bold"))
	RedeLabel.place(x=100,y=200)
	raiz11.iconbitmap("libro.ico")

	fondoBoton=PhotoImage(file="instagram.gif")
	fondo1=PhotoImage(file="picasoredes.gif")
	fondo = Label(raiz11, image=fondo1).place(x=0,y=0)
	##botonabrirventana=Button(raiz11, text="mouse",image=fondoBoton,font = ("MS Sans Serif", 11, "bold"),borderwidth="5")
	##botonabrirventana.place(x=100,y=40)
	raiz11.mainloop()
	
contacmenu.add_command(label="Redes",command=DatosRe)

contacmenu.add_separator()

def DatosCor():
	raiz12 = Toplevel()
	raiz12.geometry("720x500")
	raiz12.title("Datos De Correo")
	raiz12.iconbitmap("libro.ico")

	fondodesa=PhotoImage(file="picasocorreo.gif")
	fondo4 = Label(raiz12, image=fondodesa).place(x=0,y=0)
	raiz12.mainloop()
contacmenu.add_command(label="Correo",command=DatosCor)



menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Guia Usuarios", menu=guiamenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)
menubar.add_cascade(label="Contacto", menu=contacmenu)





raiz.mainloop()                                                                                            ## Esta es una de las partes mas importantes de la interfaz, cierra todo y une todo las lineas, todo lo que se encuentre despues de este comando no lo interpreta como interfaz grafica de tkinter