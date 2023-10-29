import tkinter as tk
import webbrowser
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import Tk
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
            

def tokens():
    codigo = texto_entrada.get(1.0, tk.END)
    lista_lexemas = instruccion(codigo)
    # Abre un archivo HTML para escribir la tabla
    with open("REPORTE DE TOKENS.html", "w") as archivo_html:
        archivo_html.write("<html>\n")
        archivo_html.write("<head>")
        archivo_html.write("<title>Reporte de Tokens</title>")
        archivo_html.write("<style>")
        archivo_html.write("table { border-collapse: collapse; width: 80%; margin: 20px auto; }")
        archivo_html.write("th, td { border: 1px solid #333; padding: 8px; text-align: left; }")
        archivo_html.write("th { background-color: #333; color: white; }")
        archivo_html.write("tr:nth-child(even) { background-color: #f2f2f2; }")
        archivo_html.write("tr:nth-child(odd) { background-color: #e6e6e6; }")
        archivo_html.write("</style>")
        archivo_html.write("</head>\n")
        archivo_html.write("<body>\n")
        archivo_html.write("<h1 style='text-align: center;'>Reporte de Tokens</h1>\n")
        archivo_html.write("<table>\n")
        archivo_html.write("<tr><th>Número</th><th>Tipo</th><th>Lexema</th><th>Fila</th><th>Columna</th></tr>\n")

        num_tokens = 0
        for elemento in lista_lexemas:
            archivo_html.write("<tr>")
            num_tokens += 1
            archivo_html.write(f"<td>{num_tokens}</td>")
            if isinstance(elemento, Lexema):
                archivo_html.write(f"<td>{elemento.tipo}</td><td>{elemento.lexema}</td><td>{elemento.fila}</td><td>{elemento.columna}</td>")
            elif isinstance(elemento, Numero):
                archivo_html.write(f"<td>Numero</td><td>{elemento.valor}</td><td>{elemento.fila}</td><td>{elemento.columna}</td>")
            archivo_html.write("</tr>\n")

        archivo_html.write("</table>\n")
        archivo_html.write("</body>\n")
        archivo_html.write("</html>\n")
        
    messagebox.showinfo("Reporte generado", "El reporte de tokens se generó exitosamente en el archivo 'REPORTE DE TOKENS.html'.")
    webbrowser.open("REPORTE DE TOKENS.html")


def codigo():
    pass

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
            elif isinstance(elemento, Registros):
                continue
            elif isinstance(elemento, Promedio):
                imprimir_consola == 46
            elif isinstance(elemento, Contarsi):
                continue
            elif isinstance(elemento, Datos):
                continue
            elif isinstance(elemento, Sumar):
                continue
            elif isinstance(elemento, Max):
                continue
            elif isinstance(elemento, Min):
                continue
            elif isinstance(elemento, Reporte):
                continue
        

        

        
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


boton_archivo = tk.Menubutton(banda_superior, text="ARCHIVO", font=("Century Gothic", 12), bg="#BFD4E0")        

opciones = tk.Menu(boton_archivo,tearoff=0)
boton_archivo["menu"] = opciones
opciones.add_command(label="ABRIR", font=("Century Gothic", 12), background='#BFD4E0', foreground="black", activebackground='#34619B', activeforeground='white', command=abrir_archivo)
opciones.add_command(label="GUARDAR", font=("Century Gothic", 12),  background='#BFD4E0' , foreground="black" ,activebackground='#34619B', activeforeground='white', command=guardar_archivo)
opciones.add_command(label="GUARDAR COMO", font=("Century Gothic", 12),  background='#BFD4E0' , foreground="black", activebackground='#34619B' ,activeforeground='white', command=guardar_archivo)

boton_analizar = tk.Button(banda_superior, font=("Century Gothic", 12), bg="#BFD4E0", text="ANALIZAR", command=analizar)
boton_reporte = tk.Button(banda_superior, font=("Century Gothic", 12),  bg="#BFD4E0", text="REPORTE")

boton_reporte = tk.Menubutton(banda_superior, text="REPORTE", font=("Century Gothic", 12), bg="#BFD4E0")        

opciones = tk.Menu(boton_reporte,tearoff=0)
boton_reporte["menu"] = opciones
opciones.add_command(label="TOKENS", font=("Century Gothic", 12), background='#BFD4E0', foreground="black", activebackground='#34619B', activeforeground='white', command=tokens)
opciones.add_command(label="ERRORES", font=("Century Gothic", 12),  background='#BFD4E0' , foreground="black" ,activebackground='#34619B', activeforeground='white', command=codigo)
opciones.add_command(label="ARBOL DE DERIVACION", font=("Century Gothic", 12),  background='#BFD4E0' , foreground="black", activebackground='#34619B' ,activeforeground='white')

boton_salir = tk.Button(banda_superior, font=("Century Gothic", 12), bg="#BFD4E0", text="SALIR", command=ventana.quit)


boton_archivo.pack(side=tk.LEFT, padx=10, pady=10)
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

