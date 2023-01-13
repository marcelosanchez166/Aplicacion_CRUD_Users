import sqlite3
from sqlite3.dbapi2 import Row
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

"""Las ventanas emegentes no vienen con la biblioteca de tkinter hay que importarlas por aparte"""
from tkinter import messagebox


# Abrir y crear Conexion a la base de sql lite
conexion = sqlite3.connect("Administrar_Usuarios")

# Crear Puntero
cursor = conexion.cursor()


"""Para no permitir que se repita un registro en un campo se usa UNIQUE en SQLite"""

# Lista_Users=[
#           ("Marcelo","Sanchez", 26," colonia altos del palmar","1234"),
#           ("Juan", "Perez",15,"Las margaritas","1234"),
#           ("Liz", "Hernandez", 20, "Santa maria ","1234"),
#           ("Lucas", "Lopez", 10, "Los alpes suizos","1234"),
#           ("Marcos","Menendez",8, "San Salvador","1234")
# ]


raiz = Tk()
raiz.title(" Aplicacion de Usuarios ")
# raiz.geometry("750x750")
raiz.config(bg="#A9A9E9")
raiz.columnconfigure(1, weight=1)
raiz.rowconfigure(1, weight=1)


FrameCampos = Frame(raiz)
FrameCampos.columnconfigure(0, weight=0)
FrameCampos.rowconfigure(0, weight=0)
FrameCampos.grid(row=0, column=0, sticky='nsew')
FrameCampos.config(bg="#E9F9E9")  # color del frame
# Tamaño del fram, para que este surja efecto el de la raiz debe estar desactivado
FrameCampos.config(width="1300", height="300")
FrameCampos.grid_propagate(0)
FrameCampos.config(bd=2)  # tamaño al borde del frame
FrameCampos.config(relief="raised")  # tipo de marco para el frame


Name = StringVar()
lastname = StringVar()
age = StringVar()
address = StringVar()
Contra = StringVar()


Nombrelabel = Label(FrameCampos, text="Nombre ")
Nombrelabel.grid(row=2, column=0, pady=4, padx=2)
textNombre = Entry(FrameCampos, textvariable=Name)
textNombre.grid(row=2, column=1, padx=8, pady=8)
textNombre.focus()

Apellidolabel = Label(FrameCampos, text="Apellido ")
Apellidolabel.grid(row=3, column=0, pady=4, padx=2)
Apellidotext = Entry(FrameCampos, textvariable=lastname)
Apellidotext.grid(row=3, column=1, padx=8, pady=8)

Edadlabel = Label(FrameCampos, text="Edad ", width=7)
Edadlabel.grid(row=4, column=0, pady=4, padx=2)
Edadtext = Entry(FrameCampos, textvariable=age)
Edadtext.grid(row=4, column=1, padx=8, pady=8)


Direccionlabel = Label(FrameCampos, text="Direccion ")
Direccionlabel.grid(row=5, column=0, pady=4, padx=2)
Direcciontext = Entry(FrameCampos, textvariable=address)
Direcciontext.grid(row=5, column=1, padx=8, pady=8)


Passlabel = Label(FrameCampos, text="Contraseña ")
Passlabel.grid(row=6, column=0, pady=4, padx=2)
Passtext = Entry(FrameCampos, textvariable=Contra)
Passtext.grid(row=6, column=1, padx=8, pady=8)
Passtext.config(show="*")


lista = []


def InsertarUsers():
    # Abrir y crear Conexion a la base de sql lite
    conexion = sqlite3.connect("Administrar_Usuarios")

    # Crear Puntero
    cursor = conexion.cursor()
    # Se coloca NULL cuando se coloca en autoincremente un id
    #cursor.executemany("INSERT INTO Usuarios VALUES (NULL,?,?,?,?,?)", Lista_Users)
    # cursor.execute ('''
    # CREATE TABLE Usuarios(
    # Id_User INTEGER PRIMARY KEY AUTOINCREMENT,
    # Nombre VARCHAR(50),
    # Apellido  VARCHAR(50),
    # Edad INTEGER,
    # Direccion VARCHAR(20),
    # Password VARCHAR(10))
    # ''')
    lista = [
        (Name.get(), lastname.get(), age.get(), address.get(), Contra.get())
    ]
    hola = cursor.executemany(
        "INSERT INTO Usuarios VALUES (NULL,?,?,?,?,?)", lista)
    print(hola)
    # Name.set("")        #
    # lastname.set("")    #
    # age.set("")         #Metodo .set para limpiar los entry
    # address.set("")     #
    # Contra.set("")      #
    messagebox.showinfo("INFO", "Usuario Insertado Correctamente")
    limpiarCampos()
    textNombre.focus()
    # cursor.execute("INSERT INTO Usuarios VALUES (NULL,'" + Name.get()+
    # "','" + lastname.get() +
    # "','" + age.get() +
    # "','" + address.get() +
    # "','" + Contra.get() + "')")
    conexion.commit()
    # print(lista)


ingresarUsuarios = Button(FrameCampos, width=8,text=" Insertar ", command=InsertarUsers)
ingresarUsuarios.config(bg="#008B8B", fg="#191970", font="cursiva")
ingresarUsuarios.grid(row=10, column=0, pady=10)

# ----------------------Limpiar los campos-----------------


def limpiarCampos():
    Name.set("")
    lastname.set("")
    age.set("")
    address.set("")
    Contra.set("")


Limpiarcampos = Button(FrameCampos, width=12,text=" Limpiar campos ", command=limpiarCampos)
Limpiarcampos.config(bg="#008B8B", fg="#191970", font="cursiva")
Limpiarcampos.grid(row=10, column=1, pady=20)


"""               Frame de la parte de abajo de la app      """

FrameListarUsers = Frame(raiz)
FrameListarUsers.columnconfigure(0, weight=1)
FrameListarUsers.columnconfigure(1, weight=1)
FrameListarUsers.rowconfigure(2, weight=1)
FrameListarUsers.grid(row=11, column=0, sticky='nsew')
FrameListarUsers.config(bg="#A9F9E9")  # color del frame
# Tamaño del fram, para que este surja efecto el de la raiz debe estar desactivado
FrameListarUsers.config(width="1300", height="350")
FrameListarUsers.grid_propagate(0)
FrameListarUsers.config(bd=2)  # tamaño al borde del frame
FrameListarUsers.config(relief="raised")  # tipo de marco para el frame


# ---------------Funcion para poder seleccionar un valor de la tabla y poder modificar----------
def FuncDobleclickTabla(self):
    global Nombreviejo
    Nombreviejo = str(tabla.item(tabla.selection())["values"][0])
    # textNombre.delete(0,END)      #
    # Apellidotext.delete(0,END)    #
    # Edadtext.delete(0,END)        #Eliminar registros actuales de los entry
    # Direcciontext.delete(0,END)   #
    # Passtext.delete(0,END)        #
    limpiarCampos()
    # ingresarUsuarios["state"]="disable"#Deshabilitar el boton ingresar users
    # ButonEditar["state"]="normal"#Poner estado normal activo al boton editar cuando se selecciono un registro y aparesca en los entry
    textNombre.insert(0, str(tabla.item(tabla.selection())["values"][0]))
    # Insertar los registros con values para que se
    Apellidotext.insert(0, str(tabla.item(tabla.selection())["values"][1]))
    # muestre y ponga cada valor donde corresponda
    Edadtext.insert(0, str(tabla.item(tabla.selection())["values"][2]))
    Direcciontext.insert(0, str(tabla.item(tabla.selection())["values"][3]))  # en los entry
    Passtext.insert(0, str(tabla.item(tabla.selection())
                    ["values"][4]))              #


tabla = ttk.Treeview(FrameListarUsers, columns=("#1", "#2", "#3", "#4", "#5"))
#tabla['show'] = 'headings'
# FuncDobleclickTabla=""
# Evento doble click para seleccionar un registro de la tabla con la funcion,
tabla.bind("<Double-Button-1>", FuncDobleclickTabla)
# con la funcion bind que se enfoca en estar al pendiente de un evento
tabla.grid(row=13, column=0, sticky='nsew')
tabla.heading("#0", text="ID")
tabla.heading("#1", text="Nombre")
tabla.heading("#2", text="Apellido")
tabla.heading("#3", text="Edad")
tabla.heading("#4", text="Direccion")
tabla.heading("#5", text="Password")


FrameListarUserslabel = Label(
    FrameListarUsers, text="Mostrar Usuarios ", height=2)
FrameListarUserslabel.grid(row=12, column=0, pady=4, padx=2)


def editarregistro():
    # Abrir y crear Conexion a la base de sql lite
    conexion = sqlite3.connect("Administrar_Usuarios")

    # Crear Puntero
    cursor = conexion.cursor()
    # lista=[
    # (Name.get(),lastname.get(),age.get(),address.get(),Contra.get())
    # ]
    #cursor.execute("UPDATE Usuarios SET Nombre=?, Apellido=?, Edad=?, Direccion=?, Password=?"+ "WHERE Nombre="+ Name.get(),lista)
    cursor.execute("UPDATE Usuarios SET nombre='" + Name.get() +
    "',Apellido='" + lastname.get() + "',Edad='" + age.get() +
    "',Direccion='" + address.get() +
    "',Password='" + Contra.get()+"' WHERE Nombre='" + Nombreviejo + "'")
    # ingresarUsuarios["state"]="normal"#Deshabilitar el boton ingresar users
    # ButonEditar["state"]="disable"#Poner estado normal activo al boton editar cuando se selecciono un registro y aparesca en los entry
    # textNombre.delete(0,END)      #
    # Apellidotext.delete(0,END)    #
    # Edadtext.delete(0,END)        #Eliminar registros actuales de los entry
    # Direcciontext.delete(0,END)   #
    # Passtext.delete(0,END)
    messagebox.showinfo("BBDD", "Usuario Actualizado")
    limpiarCampos()
    textNombre.focus()
    conexion.commit()
    ListarUsuarios()


ButonEditar = Button(FrameListarUsers, text=" Actualizar ",command=editarregistro)
ButonEditar.config(bg="#008B8B", fg="#191970", font="cursiva")
ButonEditar.grid(row=14, column=1, pady=4, padx=2)


def Eliminar():
    # Abrir y crear Conexion a la base de sql lite
    conexion = sqlite3.connect("Administrar_Usuarios")

    # Crear Puntero
    cursor = conexion.cursor()
    # lista=[
    # (Name.get(),lastname.get(),age.get(),address.get(),Contra.get())
    # ]
    cursor.execute("DELETE FROM Usuarios WHERE Nombre='" + Name.get() + "'")
    # Name.set("")        #
    # lastname.set("")    #
    # age.set("")         #Metodo .set para limpiar los entry
    # address.set("")     #
    # Contra.set("")      #
    messagebox.showinfo("INFO", "Usuario Eliminado")
    textNombre.focus()
    conexion.commit()
    limpiarCampos()
    ListarUsuarios()


Butonborrar = Button(FrameListarUsers, height=1,text="Borrar ", command=Eliminar)
Butonborrar.config(bg="#008B8B", fg="#191970", font="cursiva")
Butonborrar.grid(row=15, column=0, pady=4, padx=2)
# --------------------------Funcion listar Datos---------------------


def ListarUsuarios():
    # Abrir y crear Conexion a la base de sql lite
    conexion = sqlite3.connect("Administrar_Usuarios")

    # Crear Puntero
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM  Usuarios")
    # Variable para guardar lo extraido de la base con el select
    valoresextraidos = cursor.fetchall()
    width = 5
    # ----------------------------Ciclo for para  que los registros no se muestren repeditos al consultarlos
    registros = tabla.get_children()
    for registro in registros:
        tabla.delete(registro)

    # ----------------------------ciclo for para mostrar los regirstros en la tabla
    for (Id, Nombre, Apellido, Edad, Direccion, password) in valoresextraidos:
        # print(i)
        #print("Id: ", i[0], " Nombre: ", i[1], " Apellido: ",i[2], "Edad: ", i[3], "password: ", i[4])
        tabla.insert('', 0, text=Id, values=(
            Nombre, Apellido, Edad, Direccion, password))
    conexion.commit()
    limpiarCampos()


# crea un boton con texto dentro y se le pasa la funcion boton1
botonlistar = Button(FrameListarUsers, height=1,text=" Mostrar usuarios ", command=ListarUsuarios)
botonlistar.config(bg="#008B8B", fg="#191970", font="cursiva")
botonlistar.grid(row=14, column=0)


# ----------------Funcion actualizar registros
# def Actualizar():
#           #Abrir y crear Conexion a la base de sql lite
#           conexion=sqlite3.connect("Administrar_Usuarios")

#           #Crear Puntero
#           cursor=conexion.cursor()
#           cursor.execute("UPDATE  Usuarios SET Usuarios ")


# #Se coloca NULL cuando se coloca en autoincremente un id
# cursor.executemany("INSERT INTO Productos VALUES (NULL,?,?,?)", ListaProductos)

conexion.commit()
raiz.mainloop()
conexion.close()
