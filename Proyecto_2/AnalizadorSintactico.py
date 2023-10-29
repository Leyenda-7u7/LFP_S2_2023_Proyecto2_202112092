from Errores.Errores import *
from Instrucciones.DeclaracionClaves import *
from Instrucciones.Imprimir import *
from Instrucciones.Imprimirln import *
from Instrucciones.Registros import *
from Instrucciones.Promedio import *
from Instrucciones.Conteo import *
from Instrucciones.Contarsi import *
from Instrucciones.Datos import *
from Instrucciones.Sumar import *
from Instrucciones.Max import *
from Instrucciones.Min import *
from Instrucciones.Reporte import *
#from Instrucciones.Conteo import *

global n_linea
global n_columna
global lista_lexemas_sintacticos
global instrucciones_sintacticas
lista_errores = []


def instrucciones_sintactico(lista_lexemas):

    while lista_lexemas:
        lexema = lista_lexemas.pop(0)

        if lexema.operar(None) == 'Claves':
            lista_elementos = []
            palabra_reservada = lexema
            igual = lista_lexemas.pop(0)
            if igual.operar(None) == '=':
                corchete_izq = lista_lexemas.pop(0)
                if corchete_izq.operar(None) == '[':
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        if lex.operar(None) == '"':
                            continue
                        elif lex.operar(None) == ',':
                            continue
                        elif lex.operar(None) == ']':
                            return DeclaracionClaves(palabra_reservada.lexema, lista_elementos, lex.getFila(), lex.getColumna())
                        else:
                            lista_elementos.append(lex.lexema)
            else: #! para detectar errores sintácticos
                print("Error sintáctico en la declaración de claves")
                lista_errores.append(Errores(igual.lexema,"Sintáctico", igual.getFila(), igual.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ']':
                        print("Final de la declaración de claves")
                        break
                    
        if lexema.operar(None) == 'Registros':
            lista_elementos = []
            palabra_reservada = lexema
            igual = lista_lexemas.pop(0)
            if igual.operar(None) == '=':
                corchete_izq = lista_lexemas.pop(0)
                if corchete_izq.operar(None) == '[':
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        if lex.operar(None) == '{':
                            registro = {}  # Inicializamos un diccionario para cada registro
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                if lex.operar(None) == '}':
                                    lista_elementos.append(registro)  # Agregamos el registro a la lista
                                    break
                                elif lex.operar(None) == 'Número' or lex.operar(None) == 'TEXTO':
                                    # Añadimos el valor al registro, usando la posición como clave
                                    registro[len(registro) + 1] = lex.lexema

                    if corchete_izq.operar(None) == ']':
                        # Devolvemos un objeto Registros con la lista de registros procesados
                        return Registros(palabra_reservada.lexema, lista_elementos, lexema.getFila(), lexema.getColumna())


        if lexema.operar(None) == 'imprimir':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Imprimir(texto.lexema, lexema.getFila(), lexema.getColumna())
        
        if lexema.operar(None) == 'imprimirln':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Imprimirln(texto.lexema, lexema.getFila(), lexema.getColumna())
        
        if lexema.operar(None) == 'conteo':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                parentesis = lista_lexemas.pop(0)
                if parentesis.operar(None) == ')':
                    punto_coma = lista_lexemas.pop(0)
                    if punto_coma.operar(None) == 'PUNTOYCOMA':
                        return Conteo(lexema.getFila(), lexema.getColumna())

        if lexema.operar(None) == 'promedio':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Promedio(texto.lexema, lexema.getFila(), lexema.getColumna())
                        
        if lexema.operar(None) == 'CONTARSI':
            lexema = lista_lexemas_sintacticos.pop(0)
            if lexema.operar(None) == 'PARIZQ':
                # Procesa los elementos necesarios para Contarsi y crea un objeto Contarsi
                campo = None  # Lógica para obtener el campo
                valor = None  # Lógica para obtener el valor
                # ...
                return Contarsi(campo, valor, lexema.getFila(), lexema.getColumna())
            
        if lexema.operar(None) == 'DATOS':
            lexema = lista_lexemas_sintacticos.pop(0)
            if lexema.operar(None) == 'PUNTOYCOMA':
                return Datos(lexema.getFila(), lexema.getColumna())
            
        if lexema.operar(None) == 'SUMAR':
            lexema = lista_lexemas_sintacticos.pop(0)
            if lexema.operar(None) == 'PARIZQ':
                # Procesa los elementos necesarios para Sumar y crea un objeto Sumar
                campo = None  # Lógica para obtener el campo
                # ...
                return Sumar(campo, lexema.getFila(), lexema.getColumna())
            
        if lexema.operar(None) == 'MAX':
            lexema = lista_lexemas_sintacticos.pop(0)
            if lexema.operar(None) == 'PARIZQ':
                # Procesa los elementos necesarios para Max y crea un objeto Max
                campo = None  # Lógica para obtener el campo
                # ...
                return Max(campo, lexema.getFila(), lexema.getColumna())
            
        if lexema.operar(None) == 'MIN':
            lexema = lista_lexemas_sintacticos.pop(0)
            if lexema.operar(None) == 'PARIZQ':
                # Procesa los elementos necesarios para Min y crea un objeto Min
                campo = None  # Lógica para obtener el campo
                # ...
                return Min(campo, lexema.getFila(), lexema.getColumna())

        if lexema.operar(None) == 'EXPORTARREPORTE':
            lexema = lista_lexemas_sintacticos.pop(0)
            if lexema.operar(None) == 'PARIZQ':
                comillas = lista_lexemas_sintacticos.pop(0)
                if comillas.operar(None) == 'COMILLA':
                    titulo = lista_lexemas_sintacticos.pop(0)
                    comillas = lista_lexemas_sintacticos.pop(0)
                    if comillas.operar(None) == 'COMILLA':
                        parentesis = lista_lexemas_sintacticos.pop(0)
                        if parentesis.operar(None) == 'PARDER':
                            return Reporte(titulo.lexema, lexema.getFila(), lexema.getColumna())