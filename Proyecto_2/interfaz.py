import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import Tk
#from analizadorlexico import *
import tkinter.messagebox as messagebox
import subprocess
from AnalizadorLexico import *
from AnalizadorSintactico import *

def abrir_archivo():
    x = ""
    Tk().withdraw()
    try:
        filename = askopenfilename(title='Selecciona un archivo', filetypes=[('Archivos', f'*.json')])
        with open(filename, encoding='utf-8') as infile:
            x = infile.read()
                                        
    except: 
        messagebox.showinfo("Error, no se ha seleccionado ningún archivo")
        return
    
    #texto_entrada.delete("1.0", tk.END)  # Limpia el contenido actual del widget de texto
    texto_entrada.insert('1.0', x)

def guardar_archivo():
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, 'w') as file:
            file.write(texto_entrada.get(1.0, tk.END))


def analizar():
    # Obtén el código del área de texto
    code = texto_entrada.get(1.0, tk.END)
    imprimir_consola = ''
    try:
        # Ejecuta el análisis léxico
        instrucciones_lexico = instruccion(code)
        lista_instrucciones = []
        while True:
            instrucciones_lenguaje = instrucciones_sintactico(instrucciones_lexico)
            if instrucciones_lenguaje:
                lista_instrucciones.append(instrucciones_lenguaje)
            else:
                break
            
        # Ejecutar instrucciones

        for elemento in lista_instrucciones:
            if isinstance(elemento, DeclaracionClaves):
                continue
            elif isinstance(elemento, Imprimir):
                imprimir_consola += elemento.ejecutarT()
            elif isinstance(elemento, Imprimirln):
                imprimir_consola += elemento.ejecutarT()


        print(imprimir_consola)
        for error in lista_errores:
            print(error.operar(None))
            
        
        # Muestra el resultado en la consola de salida
        texto_salida.config(state='normal')
        texto_salida.delete(1.0, tk.END)
        texto_salida.insert(tk.END, imprimir_consola)
        texto_salida.config(state='disabled')
        messagebox.showinfo("Análisis exitoso", "El código se analizó exitosamente.")

    except Exception as e:
        messagebox.showerror(f"Ocurrió un error al analizar el código: {str(e)}")
        print("Ocurrió un error al analizar el código: ", e)


ventana = tk.Tk()
ventana.title("ANALIZADOR LEXICO")

ancho_ventana = 900
alto_ventana = 700
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")




banda_superior = tk.Frame(ventana, bg="#627D9B")
banda_superior.pack(fill=tk.X)

menu_archivo = tk.Menu(ventana)
ventana.config(menu=menu_archivo)


btn_archivo = tk.Menubutton(banda_superior, text="ARCHIVO", font=("Century Gothic", 12), bg="#BFD4E0")        

opciones = tk.Menu(btn_archivo,tearoff=0)
btn_archivo["menu"] = opciones
opciones.add_command(label="ABRIR", font=("Century Gothic", 12), background='#BFD4E0', foreground="black", activebackground='#34619B', activeforeground='white', command=abrir_archivo)
opciones.add_command(label="GUARDAR", font=("Century Gothic", 12),  background='#BFD4E0' , foreground="black" ,activebackground='#34619B', activeforeground='white', command=guardar_archivo)
opciones.add_command(label="GUARDAR COMO", font=("Century Gothic", 12),  background='#BFD4E0' , foreground="black", activebackground='#34619B' ,activeforeground='white', command=guardar_archivo)

boton_analizar = tk.Button(banda_superior, font=("Century Gothic", 12), bg="#BFD4E0", text="ANALIZAR", command=analizar)
boton_reporte = tk.Button(banda_superior, font=("Century Gothic", 12),  bg="#BFD4E0", text="REPORTE")
boton_salir = tk.Button(banda_superior, font=("Century Gothic", 12), bg="#BFD4E0", text="SALIR", command=ventana.quit)


btn_archivo.pack(side=tk.LEFT, padx=10, pady=10)
boton_analizar.pack(side=tk.LEFT, padx=10, pady=10)
boton_reporte.pack(side=tk.LEFT, padx=10, pady=10)
boton_salir.pack(side=tk.LEFT, padx=10, pady=10)


contenedor_entrada = tk.Frame(ventana, bg="#627D9B")
contenedor_entrada.pack(side=tk.LEFT, padx=25, pady=50)

# Configurar el label de entrada
label_entrada = tk.Label(contenedor_entrada, text="ENTRADA", bg="#627D9B")
label_entrada.pack(side=tk.TOP)  # Colocar el label en la parte superior del contenedor

# Configurar el área de texto de entrada
texto_entrada = tk.Text(contenedor_entrada, wrap=tk.WORD, height=50, width=50)
scroll_y_entrada = tk.Scrollbar(contenedor_entrada, orient=tk.VERTICAL, command=texto_entrada.yview)
texto_entrada.config(yscrollcommand=scroll_y_entrada.set)
texto_entrada.pack(fill=tk.BOTH, expand=True)


# Crear un contenedor para el label de salida y el frame de salida
contenedor_salida = tk.Frame(ventana,bg="#627D9B")
contenedor_salida.pack(side=tk.LEFT, padx=20, pady=50)

# Configurar el label de salida
label_salida = tk.Label(contenedor_salida, text="SALIDA", bg="#627D9B")
label_salida.pack(side=tk.TOP)  # Colocar el label en la parte superior del contenedor

# Configurar el área de texto de salida
texto_salida = tk.Text(contenedor_salida, wrap=tk.WORD, height=50, width=50)
scroll_y_salida = tk.Scrollbar(contenedor_salida, orient=tk.VERTICAL, command=texto_salida.yview)
texto_salida.config(yscrollcommand=scroll_y_salida.set)
texto_salida.pack(fill=tk.BOTH, expand=True)




ventana.configure(bg='black')
ventana.configure(bg='#34619B') #EL color del fondo
ventana.mainloop()

