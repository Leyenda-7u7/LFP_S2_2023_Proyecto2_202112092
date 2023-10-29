UNIVESIDAD DE SAN CARLOS DE GUATEMALA

FACULTAD DE INGENIERIA

ESCUELA DE CIENCAS Y SISTEMAS

LANGUAJES FORMALES Y DE PROGRAMACION

SECCIÓN B+

SEGUNDO SEMESTRE 2023

AUX. FRANCISCO MAGDIEL ASICONA MATEO




<p align="center"> MANUAL DE USUARIO </p>



BRANDON EDUARDO PABLO GARCIA

202112092

Guatemala, noviembre del 2023









# Introduccion

Este manual describe los pasos necesarios para cualquier persona que tenga ciertas bases de sistemas pueda realizar el código implementado en Python donde se creo una herramienta que permita el diseño y creación de sentencias de bases de datos no relacionales de una forma sencilla. Esta aplicación tendrá un área de edición de código y un área de visualización de la sentencia final generada. Donde podra visualisar la cantidad de tokens y errores que tiene las sentecias a compilar.

Cuando ya se cuente con las sentencias creadas inicialmente, se procederá a realizar la compilación respectiva lo que generar los registros para poder ver los productos precios y cantidad disponible donde posteriormete visualizarlo en un tabla HTML.



# Objetivos

* Brindar la información necesaria para poder representar la funcionalidad técnica de la estructura, diseño y definición del aplicativo.

* Describir las herramientas utilizadas para el diseño y desarrollo del prototipo



# Requerimientos de funcion


|          Requerimientos      |     Descripcion |                                      
|----------------|-------------------------------|
|Visual Studio Code            |Se recomienda el uso de Visual Studio Code que fue la versión donde se programó el sistema de información. |       
|Tkinter         |Conocimiento sobre el uso de las librerias tkinter para el uso de la interfaz grafica |            |            |


##	Desarrollo

[![Rojo-Negro-Moderno-Cronograma-Agenda-de-Proyecto-Planificador.jpg](https://i.postimg.cc/L6X2cwmf/Rojo-Negro-Moderno-Cronograma-Agenda-de-Proyecto-Planificador.jpg)](https://postimg.cc/YjJ5gXGq)

# Contenido tecnico

Para obtener los lexemas se se creo un metodo `Abstract` donde se crearon los constructores de `Lexema` y `Numer`o como se muestra en las imagenes.

[![code1.png](https://i.postimg.cc/J7TGHbnN/code1.png)](https://postimg.cc/V5CY30Xv)

El código presenta la definición de una clase en Python. La clase tiene cuatro atributos: `nombre`, `lexema`, `fila` y `columna`, todos de tipo str o int. El método constructor `__init__` toma como argumentos cuatro parámetros, nombre, lexema, fila y columna, que son asignados a los respectivos atributos de la instancia creada.

El codigo de lexema se implemento de la siguente manera 

[![code12.png](https://i.postimg.cc/y8CBDdFh/code12.png)](https://postimg.cc/3d1z63fW)
 
Y el de numero de la siguente manera

[![code12.png](https://i.postimg.cc/y8CBDdFh/code12.png)](https://postimg.cc/3d1z63fW)

Se definido un método llamado `instrucciones` y recibe una cada dónde se manda a llamar a la línea y columna, por lo mismo en esta parte se va leyendo partes del archivo JSON donde se usaron condicionales para ir viendo que cuando entra una palabra reservada e ir armando cada lexema. Esto fue posible por un “while” para tener ciclos y así seguir dentro de la función mientras se cumplan ciertas condiciones, como notan se usa un puntero el cual se iguala a cero para no acumular demasiada información.

Junto con esto se crearon la clase llamada un diccionario de palabras reservadas las cuales son:

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



La clase tiene varios métodos, pero el principal es `Analizadorlexico`. Es método es el encargado de leer una lista de tokens que se le pasan como argumento, y de acuerdo a los comandos definidos en la lista "comandos", ejecuta distintas acciones dependiendo del comando reconocido en el token actual.

Cada comando está definido como un método dentro de la clase cada una con su funcion las cuales son `Claves`, `Registros`. Estos métodos ejecutan distintas acciones según el comando reconocido.

Se creo un método llamado `armar_lexema` aquí recorremos nuestra cadena y si leímos unas comillas se arma el lexema, para que no falle se retorna un None.

    def armar_lexema(cadena):
        global n_lineas
        global n_columnas
        global lista_lexemas
        lexema = ''
        puntero = ''
        for char in cadena:    
                puntero += char
                if char == '\"':        
                    return lexema, cadena[len(puntero):]
                else:
                    lexema += char
        return None, None

Aquí en operaciones se define las operaciones a realizar todo esto fue posible con el métodos abstractos. Aqui tambien se implemento un `AnalizadorSintactico` para poder leer cada palabra esto fue posible a trevez de los constructores de cada `palabras reservadas` que se guardaron en la carpeta de `Instrucciones`. Dichas palabras reservadas se muestran a continuacion.


### Palabras Reservadas:

*Claves*

*Registros*

*conteo*

*imprimir*

*imprimirln*

*promedio*

*contarsi*

*contar*

*datos*

*sumar*

*max*

*min*

*exportarReporte*

*(*

*)*

*[*

*]*

*{*

*}*

*,*

*;*

*=*

*ID -> [a-z_A-Z_] [a-z_A-Z_0-9]*

*NUMERO -> [0-9]+*

*STRING -> "[^"]"*

*IGNORE -> /t/r*

*COMENTARIOS -> //.*

Para esto se utilizaron listas a nivel globales que guardaran todo la informacion de los lexemas asi como el de los errores como se muestran a continuacion 

        lexema = ''
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
        
 # Interfaz
 
En la interfaz se llamaron las funciones del archivo analizarolexico para que asi crear otras funciones que se usaran en los botones como lo fueron las funciones de `ARCHIVO`, `ANALIZAR`, `REPORTE`, `SALIR`,  este ultimo hara que salgamos de nuestra pantalla 

Para realizar la interfaz fue necesario la implementacion de la libreria `tkinter` la cual nos ayudo a crear una interfaz mas agradable al usuario, donde de la misma manera se uso para llenar de funciones las cuales ayudaron a generar respuestas de toda la parte logica del proyecto y generar muchas mas aplicaciones.

[![code1234.png](https://i.postimg.cc/DwCFyKcn/code1234.png)](https://postimg.cc/fV01BpFr)

la funcion para el boton para generar los tokens el HTML es el siguiente


[![code12345.png](https://i.postimg.cc/RCGgYVCS/code12345.png)](https://postimg.cc/pyhQhvn4)

La estrucutra de los botones es la estrutura dada por tkinnter para cada uno de la siguiente manera 

  
        boton_salir = tk.Button(banda_superior, font=("Century Gothic", 12), bg="#BFD4E0", text="SALIR", command=ventana.quit)
 
 La interfaz quedaria de la siguiente manera donde podemos ver mas opciones en la parte de arriba.
 
 [![Captura-de-pantalla-2023-10-29-093918.png](https://i.postimg.cc/pL5BmcXn/Captura-de-pantalla-2023-10-29-093918.png)](https://postimg.cc/fVZdFKdw)
 
 Aqui se muestra el sub menu de `ARCHIVO` que cuenta con `ABRIR ARCHIVO`, `GUARDAR` y `GUARDAR COMO`

[![cadfasdfasd.png](https://i.postimg.cc/pLQ39ddj/cadfasdfasd.png)](https://postimg.cc/k24TzqKM)

Y para terminar se muestra el sub menu de `REPORTE` que cuenta con `TOKENS`, `ERRORES` y `ARBOR GENERADOR`

[![Captura-de-pantalla-2023-10-29-100107.png](https://i.postimg.cc/J4YSZF3r/Captura-de-pantalla-2023-10-29-100107.png)](https://postimg.cc/JGJTWPdv)

## AFD del analizar lexico

Este grafo marca de manera teorica como se utilozo los AFD para comprender como poder aplicar la logica de programacion y asi poder llevarla acabo de manera ordenada y funcional.

[![cap-8.png](https://i.postimg.cc/CLh7PgGN/cap-8.png)](https://postimg.cc/QVzcCvn9)

## Arbol generador

La siguiente imagen represtan lo que seria el arbol generador para el codigo implementado en este proyecto. Donde cada funcion cumple condiciones y hace un recorrido llamado Post Orden

[![68747470733a2f2f692e706f7374696d672e63632f686a4343573576532f436170747572612d64652d70616e74616c6c612d.png](https://i.postimg.cc/c4h2SBsn/68747470733a2f2f692e706f7374696d672e63632f686a4343573576532f436170747572612d64652d70616e74616c6c612d.png)](https://postimg.cc/LnqNkfg9)
