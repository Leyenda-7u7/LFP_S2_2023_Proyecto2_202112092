from Abstract.Numero import *
from Abstract.Lexema import *
from Instrucciones.Texto import *
from Errores.Errores import *
import webbrowser
import tkinter.messagebox as messagebox


reserverd = {
    'RCLAVES': 'Claves',
    'RREGISTROS': 'Registros',
    'RCONTEO': 'conteo',
    'RIMPRIMIR': 'imprimir',
    'RIMPIRMIRLN': 'imprimirln',
    'RPROMEDIO': 'promedio',
    'RCONTARSI': 'contarsi',
    'RDATOS': 'datos',
    'RSUMAR': 'sumar',
    'RMAX': 'max',
    'RMIN': 'min',
    'RREPORTE': 'exportarReporte',
    'IGUAL': '=',
    'CORIZQ': '[',
    'CORDER': ']',
    'COMILLA': '"',
    'PARIZQ': '(',
    'PARDER': ')',
    'PLLAVEIZ': '{',
    'PLLAVEDE': '}',
    'COMA': ',',
    'PUNTOYCOMA': ';',
}

lexema = list(reserverd.values())
global n_linea
global n_columna
global instrucciones
global lista_lexemas
global is_comment_open

n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []
lista_errores = []


def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = 0
    palabras_reservadas = ['Claves', 'imprimir', 'imprimirln', 'Registros', 'conteo', 'promedio']
    

        
    while cadena:
        char = cadena[puntero]
        puntero += 1

        if char == '"':       #! leemos nuestra cadena y al encontrar " que habre empieza a crear el token
            l = Lexema('"', n_linea, n_columna, 'COMILLA')
            lista_lexemas.append(l)
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena:
                n_columna += 1
                #Armar lexema como clase
                l = Lexema(lexema, n_linea, n_columna, 'TEXTO')
                lista_lexemas.append(l)  #! Agregamos los lexemas a la lista_lexema
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('"', n_linea, n_columna, 'COMILLA')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("Claves"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'CLAVES')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('[', n_linea, n_columna, 'CORIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0
            l = Lexema('=', n_linea, n_columna, 'IGUAL')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

                
        elif cadena.startswith("Registros"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'REGISTROS')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('[', n_linea, n_columna, 'CORIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0
            l = Lexema('=', n_linea, n_columna, 'IGUAL')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0
            num_tokens = 0

        elif cadena.startswith("imprimir"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'IMPRIMIR')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0
            
        elif cadena.startswith("imprimirln"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'IMPRIMIRLN')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0
            
        elif cadena.startswith("conteo"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'CONTEO')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0
            

        elif cadena.startswith("promedio"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'PROMEDIO')  
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0

        
        elif cadena.startswith("contarsi"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'CONTARSI')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

            
        elif cadena.startswith("datos"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'DATOS')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0

        
        elif cadena.startswith("sumar"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'SUMAR')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0

        elif cadena.startswith("max"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'MAX')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0

        elif cadena.startswith("min"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'MIN')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            num_tokens = 0
            for elemento in lista_lexemas:
                if isinstance(elemento, Lexema):  # Verificar si el elemento es un Lexema
                    num_tokens += 1
                    print(f"Token {num_tokens} - Tipo: {elemento.tipo}, Fila: {elemento.fila}, Columna: {elemento.columna}")
                elif isinstance(elemento, Numero):  # Verificar si el elemento es un Numero
                    num_tokens += 1
                    print(f"Token {num_tokens} - Tipo: Numero, Valor: {elemento.valor}, Fila: {elemento.fila}, Columna: {elemento.columna}")

                
                
        elif cadena.startswith("exportarReporte"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'REPORTE')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0

                
        elif char.isdigit():
            token, cadena = armar_numero(cadena)
            if token and cadena:
                n_columna += 1
                #! Armamos lexema como clase
                n = Numero(token, n_linea, n_columna)

                lista_lexemas.append(n)
                n_columna += len(str(token)) + 1
                puntero = 0
            

        elif char == '[' or char == ']':
            # ! Armamos lexema como clase
            c = Lexema(char, n_linea, n_columna, 'CORCHETE')

            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == ';':

            c = Lexema(char, n_linea, n_columna, 'PUNTOYCOMA')

            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == '=':
            c = Lexema(char, n_linea, n_columna, 'IGUAL')
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == ',':
            c = Lexema(char, n_linea, n_columna, 'COMA')
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
        
        elif char == '(':
            lexema, cadena = armar_lexema(cadena[len(puntero):])
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'PARIZQ')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
            n_columna += 1
            puntero = ''

        elif char == ')':
            c = Lexema(char, n_linea, n_columna, 'PARDER')
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
        
        elif char == '{':
            c = Lexema(char, n_linea, n_columna, 'PLLAVEIZ')
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
            
        elif char == '}':
            c = Lexema(char, n_linea, n_columna, 'PLLAVEDE')
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
            
            
        elif char == '#':
            while puntero < len(cadena) and cadena[puntero] != '\n':
                puntero += 1
            n_linea += 1
            n_columna = 1
            if puntero < len(cadena):
                puntero += 1  
            cadena = cadena[puntero:]
            puntero = 0
            
        elif cadena.startswith(" ''' "):
            if not is_comment_open:
                is_comment_open = True
                end_comment_index = cadena.find(" ''' ", 3) 
                if end_comment_index != -1:
                    is_comment_open = False  # Cerramos el comentario
                    cadena = cadena[end_comment_index + 3:]  # Ignorar el comentario
                else:
                    print("Error: Comentario no se cierra correctamente")
                    break
            else:
                # El comentario ya está abierto, buscamos el cierre
                end_comment_index = cadena.find("'''", 3)
                if end_comment_index != -1:
                    is_comment_open = False  # Cerramos el comentario
                    cadena = cadena[end_comment_index + 3:]  # Ignorar el comentario
                else:
                    break  # Error si no se cierra el comentario        
                    

        elif char == "\t":
            n_columna += 4
            cadena = cadena[4:]
            puntero = 0
        elif char == "\n":
            cadena = cadena[1:]
            puntero = 0
            n_linea += 1
            n_columna = 1
        elif char == ' ' or char == '\r' or char == '.' or char == ':':
            n_columna += 1
            cadena = cadena[1:]
            puntero = 0
        else:
            lista_errores.append(Errores(char, "Léxico",n_linea, n_columna))
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
            
    return lista_lexemas

def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''

    for char in cadena:
        puntero += char
        if char == '"' or char == '\n' or char == '\t' or char == '(' or char == ')':
            return lexema, cadena[len(puntero):]    #! si encuentra una  " termino de leer el token
        else:
            lexema += char   #! creamos nuestros Token
    return None, None


def armar_numero(cadena):
    numero = ''
    puntero = ''
    is_decimal =  False

    for char in cadena:
        puntero += char
        if char == '.':
            is_decimal = True

        if char == ' ' or char == '\n' or char == '\t':
            if is_decimal:
                return float(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:]
        else:
            if char != ',': #! si no es una coma lo agregamos al numero
                numero += char
    return None, None

def errores():
    global lista_errores
    contador = 1

    with open("INFORME DE ERRORES.html", "w") as archivo_html:
        archivo_html.write("<html>\n")
        archivo_html.write("<head>")
        archivo_html.write("<title>Informe de Errores</title>")
        archivo_html.write("<style>")
        archivo_html.write("table { border-collapse: collapse; width: 80%; margin: 20px auto; }")
        archivo_html.write("th, td { border: 1px solid #333; padding: 8px; text-align: left; }")
        archivo_html.write("th { background-color: #333; color: white; }")
        archivo_html.write("tr:nth-child(even) { background-color: #f2f2f2; }")
        archivo_html.write("tr:nth-child(odd) { background-color: #e6e6e6; }")
        archivo_html.write("</style>")
        archivo_html.write("</head>\n")
        archivo_html.write("<body>\n")
        archivo_html.write("<h1 style='text-align: center;'>Informe de Errores</h1>\n")
        archivo_html.write("<table>\n")
        archivo_html.write("<tr><th>Número de Error</th><th>Tipo de Error</th><th>Error</th><th>Fila</th><th>Columna</th></tr>\n")

        dataErrores = "{\n"
        while lista_errores:
            error = lista_errores.pop(0)
            archivo_html.write("<tr>")
            archivo_html.write(f"<td>{contador}</td>")
            archivo_html.write(f"<td>{error.tipo}</td><td>{error.lexema}</td><td>{error.fila}</td><td>{error.columna}</td>")
            archivo_html.write("</tr>\n")
            dataErrores += error.operar(contador)
            dataErrores += ',\n'

        archivo_html.write("</table>\n")
        archivo_html.write("</body>\n")
        archivo_html.write("</html>\n")
    messagebox.showinfo("Reporte generado", "El reporte de errores se generó exitosamente en el archivo 'REPORTE DE ERRORES.html'.")
    webbrowser.open("REPORTE DE ERRORES.html")


