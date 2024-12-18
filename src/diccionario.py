# Diccionario:
# Cabe recalcar que todos esos términos pertenecen al ecosistema de Python. parte de la biblioteca estándar de Python y otros provienen de bibliotecas adicionales como Pandas y NumPy que sirven para el análisis de datos y operaciones numéricas.
#J_J
'''

Estructura del diccionario.
diccionario = {
"A":{"terminos,": {"categoría": "categoria en español", "traducción": "definicion en español"}},
}
'''
diccionario = {
    "a": {
        "abs": {
            "categoria": ("Matemáticas",),
            "definicion": "Devuelve el valor absoluto de un número.",
            "traduccion": "Returns the absolute value of a number."},
        "all": {
            "categoria": ("Funciones de lista",),
            "definicion": "Devuelve True si todos los elementos en un iterable son verdaderos.",
            "traduccion": "Returns True if all elements in an iterable are true."},
        "any": {
            "categoria": ("Funciones de lista",),
            "definicion": "Devuelve True si algún elemento en un iterable es verdadero.",
            "traduccion": "Returns True if any element in an iterable is true."},
        "ascii": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Devuelve la versión ASCII de un objeto, eliminando caracteres especiales.",
            "traduccion": "Returns the ASCII version of an object, escaping non-ASCII characters."},
        "append": {
            "categoria": ("Listas",),
            "definicion": "Agrega un elemento al final de una lista.",
            "traduccion": "Adds an element to the end of a list."},
        "argmax": {
            "categoria": ("Funciones NumPy",),
            "definicion": "Devuelve el índice del elemento máximo en una lista o array.",
            "traduccion": "Returns the index of the maximum element in a list or array."},
        "argmin": {
            "categoria": ("Funciones NumPy",),
            "definicion": "Devuelve el índice del elemento mínimo en una lista o array.",
            "traduccion": "Returns the index of the minimum element in a list or array."},
        "array": {
            "categoria": ("Estructura de datos",),
            "definicion": "Estructura de datos que puede almacenar múltiples valores del mismo tipo.",
            "traduccion": "Data structure that can store multiple values of the same type."},
        "as": {
            "categoria": ("Sintaxis de lenguaje",),
            "definicion": "Usado para crear un alias en una importación.",
            "traduccion": "Used to create an alias in an import."},
        "assert": {
            "categoria": ("Depuración",),
            "definicion": "Usado para declarar una condición que debe ser verdadera en el programa.",
            "traduccion": "Used to declare a condition that must be true in the program."},
        "async": {
            "categoria": ("Programación asincrónica",),
            "definicion": "Declara una función como asincrónica.",
            "traduccion": "Declares a function as asynchronous."},
        "await": {
            "categoria": ("Programación asincrónica",),
            "definicion": "Usado para esperar una coroutine en un entorno asincrónico.",
            "traduccion": "Used to wait for a coroutine in an asynchronous context."},
        "attribute": {
            "categoria": ("Programación orientada a objetos",),
            "definicion": "Una propiedad o método de un objeto.",
            "traduccion": "A property or method of an object."},
        "at": {
            "categoria": ("Indexación",),
            "definicion": "Usado para acceder a un índice específico en una lista o array.",
            "traduccion": "Used to access a specific index in a list or array."},
        "args": {
            "categoria": ("Funciones",),
            "definicion": "Argumentos posicionales pasados a una función.",
            "traduccion": "Positional arguments passed to a function."},
        "kwargs": {
            "categoria": ("Funciones",),
            "definicion": "Argumentos con nombre pasados a una función.",
            "traduccion": "Keyword arguments passed to a function."},
        "apply": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Usado para aplicar una función a un iterable.",
            "traduccion": "Used to apply a function to an iterable."},
        "assertEqual": {
            "categoria": ("Pruebas unitarias",),
            "definicion": "Verifica que dos valores son iguales.",
            "traduccion": "Checks that two values are equal."},
        "assertIsNone": {
            "categoria": ("Pruebas unitarias",),
            "definicion": "Verifica que el valor sea None.",
            "traduccion": "Checks that the value is None."},
        "attributeError": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Excepción lanzada cuando un atributo de un objeto no se encuentra.",
            "traduccion": "Exception raised when an attribute of an object is not found."},
        "add": {
            "categoria": ("Matemáticas",),
            "definicion": "Devuelve la suma de dos números.",
            "traduccion": "Returns the sum of two numbers."},
        "allclose": {
            "categoria": ("Funciones NumPy",),
            "definicion": "Verifica si dos arrays son iguales dentro de una tolerancia específica.",
            "traduccion": "Checks if two arrays are equal within a specific tolerance."},
        "average": {
            "categoria": ("Estadística",),
            "definicion": "Calcula el promedio de una lista de números.",
            "traduccion": "Calculates the average of a list of numbers."},
        "assertAlmostEqual": {
            "categoria": ("Pruebas unitarias",),
            "definicion": "Verifica que dos números son aproximadamente iguales.",
            "traduccion": "Checks that two numbers are approximately equal."},
        "absolute_import": {
            "categoria": ("Importación de módulos",),
            "definicion": "Importación que se refiere a un módulo desde la raíz del paquete.",
            "traduccion": "Import that refers to a module from the root of the package."},
        "allexcept": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Usado para capturar todas las excepciones excepto una específica.",
            "traduccion": "Used to catch all exceptions except for a specific one."},
        "as_tuple": {
            "categoria": ("Estructura de datos",),
            "definicion": "Devuelve los resultados como una tupla.",
            "traduccion": "Returns the results as a tuple."},
        "atleast_1d": {
            "categoria": ("Funciones NumPy",),
            "definicion": "Convierte una entrada en un array de al menos una dimensión.",
            "traduccion": "Converts input to an array of at least one dimension."},
        "atleast_2d": {
            "categoria": ("Funciones NumPy",),
            "definicion": "Convierte una entrada en un array de al menos dos dimensiones.",
            "traduccion": "Converts input to an array of at least two dimensions."},
        "arange": {
            "categoria": ("Funciones NumPy",),
            "definicion": "Crea un array con valores espaciados uniformemente en un rango específico.",
            "traduccion": "Creates an array with evenly spaced values within a specified range."},
        "arccos": {
            "categoria": ("Matemáticas",),
            "definicion": "Devuelve el arco coseno de un número.",
            "traduccion": "Returns the arc cosine of a number."},
        "arcsin": {
            "categoria": ("Matemáticas",),
            "definicion": "Devuelve el arco seno de un número.",
            "traduccion": "Returns the arc sine of a number."},
        "arctan": {
            "categoria": ("Matemáticas",),
            "definicion": "Devuelve el arco tangente de un número.",
            "traduccion": "Returns the arc tangent of a number."},
        "argparse": {
            "categoria": ("Análisis de argumentos",),
            "definicion": "Módulo para analizar argumentos de línea de comandos.",
            "traduccion": "Module for parsing command-line arguments."},
        "array_like": {
            "categoria": ("Estructura de datos",),
            "definicion": "Cualquier objeto que pueda ser convertido a un array.",
            "traduccion": "Any object that can be converted to an array."}},
    
    "b": {
        "bin": {
            "categoria": ("Conversión de datos",),
            "definicion": "Convierte un número en su representación binaria.",
            "traduccion": "Converts a number to its binary representation."},
        "bool": {
            "categoria": ("Tipos de datos",),
            "definicion": "Convierte un valor en su equivalente booleano (True o False).",
            "traduccion": "Converts a value to its boolean equivalent (True or False)."},
        "break": {
            "categoria": ("Control de flujo",),
            "definicion": "Termina el ciclo en el que se encuentra.",
            "traduccion": "Terminates the loop it is in."},
        "bytes": {
            "categoria": ("Tipos de datos",),
            "definicion": "Convierte a una secuencia inmutable de bytes.",
            "traduccion": "Converts to an immutable sequence of bytes."},
        "bytearray": {
            "categoria": ("Tipos de datos",),
            "definicion": "Crea una secuencia mutable de bytes.",
            "traduccion": "Creates a mutable sequence of bytes."},
        "byteswap": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Invierte el orden de los bytes en una estructura de datos.",
            "traduccion": "Swaps the byte order in a data structure."},
        "buffer": {
            "categoria": ("Memoria",),
            "definicion": "Interfaz para acceder a los datos sin copiarlos.",
            "traduccion": "Interface to access data without copying it."},
        "base64": {
            "categoria": ("Codificación y decodificación",),
            "definicion": "Codifica y decodifica datos en el formato base64.",
            "traduccion": "Encodes and decodes data in base64 format."},
        "bitwise_and": {
            "categoria": ("Operadores bit a bit",),
            "definicion": "Operador AND bit a bit entre dos números.",
            "traduccion": "Performs a bitwise AND operation between two numbers."},
        "bitwise_or": {
            "categoria": ("Operadores bit a bit",),
            "definicion": "Operador OR bit a bit entre dos números.",
            "traduccion": "Performs a bitwise OR operation between two numbers."},
        "bitwise_xor": {
            "categoria": ("Operadores bit a bit",),
            "definicion": "Operador XOR bit a bit entre dos números.",
            "traduccion": "Performs a bitwise XOR operation between two numbers."},
        "bitwise_not": {
            "categoria": ("Operadores bit a bit",),
            "definicion": "Operador NOT bit a bit que invierte los bits de un número.",
            "traduccion": "Performs a bitwise NOT operation, inverting bits of a number."},
        "binomial": {
            "categoria": ("Estadística",),
            "definicion": "Distribución binomial en estadística.",
            "traduccion": "Binomial distribution in statistics."},
        "binascii": {
            "categoria": ("Conversión de datos",),
            "definicion": "Módulo para conversiones entre datos binarios y representaciones ASCII.",
            "traduccion": "Module for conversions between binary data and ASCII representations."},
        "byteorder": {
            "categoria": ("Memoria",),
            "definicion": "Propiedad que determina el orden de los bytes en un sistema ('big' o 'little').",
            "traduccion": "Property determining byte order in a system ('big' or 'little')."},
        "bit_length": {
            "categoria": ("Operaciones numéricas",),
            "definicion": "Devuelve el número de bits necesarios para representar un número en binario.",
            "traduccion": "Returns the number of bits required to represent a number in binary."},
        "breakpoint": {
            "categoria": ("Depuración",),
            "definicion": "Punto de interrupción para depurar el código.",
            "traduccion": "Breakpoint for debugging code."},
        "binhex": {
            "categoria": ("Conversión de datos",),
            "definicion": "Convierte datos binarios en formato hexadecimal.",
            "traduccion": "Converts binary data to hexadecimal format."},
        "bitset": {
            "categoria": ("Estructura de datos",),
            "definicion": "Conjunto de bits para operaciones bit a bit.",
            "traduccion": "Set of bits for bitwise operations."},
        "broadcast": {
            "categoria": ("Manipulación de arrays",),
            "definicion": "Extiende dimensiones para operaciones en arrays.",
            "traduccion": "Extends dimensions for operations on arrays."},
        "bitarray": {
            "categoria": ("Estructura de datos",),
            "definicion": "Estructura de datos que representa una secuencia de bits.",
            "traduccion": "Data structure representing a sequence of bits."},
        "buffer": {
            "categoria": ("Memoria",),
            "definicion": "Interfaz para manejar objetos de memoria sin copiarlos.",
            "traduccion": "Interface for handling memory objects without copying them."},
        "bitwise_left_shift": {
            "categoria": ("Operadores bit a bit",),
            "definicion": "Desplaza los bits de un número a la izquierda, equivalente a multiplicación por potencias de dos.",
            "traduccion": "Shifts the bits of a number to the left, equivalent to multiplication by powers of two."},
        "bitwise_right_shift": {
            "categoria": ("Operadores bit a bit",),
            "definicion": "Desplaza los bits de un número a la derecha, equivalente a división por potencias de dos.",
            "traduccion": "Shifts the bits of a number to the right, equivalent to division by powers of two."},
        "bz2": {
            "categoria": ("Compresión de datos",),
            "definicion": "Módulo para compresión y descompresión de archivos en formato bzip2.",
            "traduccion": "Module for compressing and decompressing files in bzip2 format."},
        "bool_": {
            "categoria": ("Tipos de datos",),
            "definicion": "Tipo de dato booleano en bibliotecas como NumPy.",
            "traduccion": "Boolea"}},
    "c": {
        "callable": {
            "categoria": ("Funciones",),
            "definicion": "Devuelve True si el objeto es llamable (función, método, etc.).",
            "traduccion": "Returns True if the object is callable (function, method, etc.)."},
        "chr": {
            "categoria": ("Conversión de datos",),
            "definicion": "Convierte un código ASCII en su carácter correspondiente.",
            "traduccion": "Converts an ASCII code to its corresponding character."},
        "class": {
            "categoria": ("Programación orientada a objetos",),
            "definicion": "Define una nueva clase para crear objetos personalizados.",
            "traduccion": "Defines a new class to create custom objects."},
        "classmethod": {
            "categoria": ("Programación orientada a objetos",),
            "definicion": "Convierte un método en un método de clase, accesible desde la clase sin instanciarla.",
            "traduccion": "Converts a method to a class method, accessible from the class without instantiating it."},
        "compile": {
            "categoria": ("Compilación",),
            "definicion": "Compila una cadena de texto en código ejecutable de Python.",
            "traduccion": "Compiles a text string into executable Python code."},
        "complex": {
            "categoria": ("Tipos de datos",),
            "definicion": "Crea un número complejo a partir de dos valores (real e imaginario).",
            "traduccion": "Creates a complex number from two values (real and imaginary)."},
        "continue": {
            "categoria": ("Control de flujo",),
            "definicion": "Salta la iteración actual de un bucle y pasa a la siguiente.",
            "traduccion": "Skips the current iteration of a loop and moves to the next one."},
        "copy": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Crea una copia superficial de una lista, diccionario u otro objeto mutable.",
            "traduccion": "Creates a shallow copy of a list, dictionary, or other mutable object."},
        "coroutine": {
            "categoria": ("Programación asincrónica",),
            "definicion": "Define una función especial que puede pausarse y reanudarse (asincrónica).",
            "traduccion": "Defines a special function that can be paused and resumed (asynchronous)."},
        "count": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Cuenta la cantidad de ocurrencias de un valor en una lista o cadena.",
            "traduccion": "Counts the occurrences of a value in a list or string."},
        "clear": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Elimina todos los elementos de una lista o diccionario.",
            "traduccion": "Removes all elements from a list or dictionary."},
        "cmath": {
            "categoria": ("Matemáticas complejas",),
            "definicion": "Módulo para operaciones matemáticas complejas.",
            "traduccion": "Module for complex mathematical operations."},
        "chain": {
            "categoria": ("Manipulación de iterables",),
            "definicion": "Función del módulo itertools que concatena múltiples iterables.",
            "traduccion": "Function from itertools module that concatenates multiple iterables."},
        "csv": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Módulo para manipular archivos CSV (valores separados por comas).",
            "traduccion": "Module for handling CSV (comma-separated values) files."},
        "copyreg": {
            "categoria": ("Serialización",),
            "definicion": "Módulo que registra funciones para serialización de objetos.",
            "traduccion": "Module that registers functions for object serialization."},
        "counter": {
            "categoria": ("Estructura de datos",),
            "definicion": "Clase de collections para contar elementos en un iterable.",
            "traduccion": "Class from collections to count elements in an iterable."},
        "cProfile": {
            "categoria": ("Depuración y optimización",),
            "definicion": "Herramienta para realizar un perfil de rendimiento de código Python.",
            "traduccion": "Tool for profiling Python code performance."},
        "capitalize": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Devuelve una copia de la cadena con la primera letra en mayúscula.",
            "traduccion": "Returns a copy of the string with the first letter capitalized."},
        "center": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Devuelve una cadena centrada, con ancho especificado y relleno opcional.",
            "traduccion": "Returns a centered string with specified width and optional fill character."},
        "ceil": {
            "categoria": ("Matemáticas",),
            "definicion": "Redondea un número al entero más próximo hacia arriba.",
            "traduccion": "Rounds a number up to the nearest integer."},
        "call": {
            "categoria": ("Funciones",),
            "definicion": "Ejecuta una función o método específico en un objeto.",
            "traduccion": "Executes a specific function or method on an object."},
        "clamp": {
            "categoria": ("Matemáticas",),
            "definicion": "Restringe un valor dentro de un rango especificado (no en la biblioteca estándar).",
            "traduccion": "Restricts a value within a specified range (not in standard library)."},
        "choice": {
            "categoria": ("Generación de datos aleatorios",),
            "definicion": "Selecciona un elemento aleatorio de una secuencia.",
            "traduccion": "Selects a random element from a sequence."},
        "collections": {
            "categoria": ("Estructura de datos",),
            "definicion": "Módulo que proporciona estructuras de datos especializadas.",
            "traduccion": "Module providing specialized data structures."},
        "compress": {
            "categoria": ("Manipulación de iterables",),
            "definicion": "Filtra elementos de un iterable según un selector booleano.",
            "traduccion": "Filters elements in an iterable according to a boolean selector."},
        "complex_conjugate": {
            "categoria": ("Matemáticas complejas",),
            "definicion": "Devuelve el conjugado de un número complejo.",
            "traduccion": "Returns the conjugate of a complex number."},
        "ctypes": {
            "categoria": ("Interoperabilidad",),
            "definicion": "Módulo para manipular datos en bibliotecas compartidas en C.",
            "traduccion": "Module for handling data in C shared libraries."},
        "clear_screen": { 
            "categoria": ("Interacción con el sistema",),
            "definicion": "Limpia la pantalla en algunos entornos de terminal (no es una función estándar).",
            "traduccion": "Clears the screen in some terminal environments (not a standard function)."},
        "call_later": {
            "categoria": ("Programación asincrónica",),
            "definicion": "Programa la ejecución de una función después de un tiempo en asyncio.",
            "traduccion": "Schedules the execution of a function after a delay in asyncio."},
        "chunk": {
            "categoria": ("Manipulación de iterables",),
            "definicion": "Divide un iterable en partes de tamaño fijo (disponible en itertools y otras bibliotecas).",
            "traduccion": "Splits an iterable into fixed-size chunks (available in itertools and other libraries)."},
        "cycle": {
            "categoria": ("Manipulación de iterables",),
            "definicion": "Itertools: Cicla infinitamente a través de un iterable.",
            "traduccion": "Itertools: Cycles infinitely through an iterable."},
        "coerce": {
            "categoria": ("Conversión de datos",),
            "definicion": "Convierte parámetros a un tipo común (obsoleto en Python 3).",
            "traduccion": "Converts parameters to a common type (obsolete in Python 3)."},
        "current_thread": {
            "categoria": ("Hilos",),
            "definicion": "Obtiene el hilo actual de ejecución en threading.",
            "traduccion": "Gets the current thread in threading."},
        "configparser": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Módulo para manipular archivos de configuración estilo INI.",
            "traduccion": "Module for handling INI-style configuration files."},
        "compileall": {
            "categoria": ("Compilación",),
            "definicion": "Compila recursivamente archivos .py en bytecode.",
            "traduccion": "Recursively compiles .py files to bytecode."},
        "copytree": {
            "categoria": ("Manipulación de archivos",),
            "definicion": "Copia recursivamente un directorio completo.",
            "traduccion": "Recursively copies an entire directory."}},
    
    "d": {
        "def": {
            "categoria": ("Función",),
            "definicion": "Declara una función o método.",
            "traduccion": "Declares a function or method."},
        "delattr": {
            "categoria": ("Función",),
            "definicion": "Elimina un atributo de un objeto.",
            "traduccion": "Deletes an attribute from an object."},
        "dataframe": {
            "categoria": ("Estructura de datos",),
            "definicion": "Estructura de datos de Pandas para manipulación de datos tabulares.",
            "traduccion": "Pandas data structure for manipulating tabular data."},
        "decode": {
            "categoria": ("Método",),
            "definicion": "Convierte bytes en una cadena utilizando una codificación.",
            "traduccion": "Converts bytes into a string using an encoding."},
        "decimal": {
            "categoria": ("Módulo",),
            "definicion": "Módulo para operaciones aritméticas con decimales de precisión exacta.",
            "traduccion": "Module for arithmetic operations with exact decimal precision."},
        "device": {
            "categoria": ("Atributo",),
            "definicion": "Atributo en PyTorch para definir el dispositivo (CPU o GPU) donde se almacenan los tensores.",
            "traduccion": "Attribute in PyTorch to define the device (CPU or GPU) for tensor storage."},
        "dict.get": {
            "categoria": ("Método",),
            "definicion": "Obtiene el valor de una clave en un diccionario o un valor predeterminado si la clave no existe.",
            "traduccion": "Gets the value of a dictionary key or a default if the key doesn't exist."},
        "dropna": {
            "categoria": ("Método",),
            "definicion": "Elimina filas o columnas con valores nulos en un DataFrame de Pandas.",
            "traduccion": "Removes rows or columns with null values in a Pandas DataFrame."},
        "dtype": {
            "categoria": ("Atributo",),
            "definicion": "Especifica el tipo de datos de un array en NumPy.",
            "traduccion": "Specifies the data type of a NumPy array."},
        "deque.appendleft": {
            "categoria": ("Método",),
            "definicion": "Agrega un elemento al inicio de una deque.",
            "traduccion": "Adds an element to the beginning of a deque."},
        "dict.update": {
            "categoria": ("Método",),
            "definicion": "Actualiza un diccionario con pares clave-valor de otro diccionario.",
            "traduccion": "Updates a dictionary with key-value pairs from another dictionary."},
        "del": {
            "categoria": ("Operador",),
            "definicion": "Elimina una variable, elemento o atributo.",
            "traduccion": "Deletes a variable, element, or attribute."},
        "dict": {
            "categoria": ("Tipo de dato",),
            "definicion": "Tipo de dato de diccionario que almacena pares clave-valor.",
            "traduccion": "Dictionary data type that stores key-value pairs."},
        "dir": {
            "categoria": ("Función",),
            "definicion": "Devuelve una lista de atributos y métodos disponibles para un objeto.",
            "traduccion": "Returns a list of attributes and methods available for an object."},
        "divmod": {
            "categoria": ("Función",),
            "definicion": "Devuelve el cociente y el residuo de una división.",
            "traduccion": "Returns the quotient and remainder of a division."},
        "deque": {
            "categoria": ("Clase",),
            "definicion": "Clase de collections para una cola de doble extremo.",
            "traduccion": "Class from collections for a double-ended queue."},
        "defaultdict": {
            "categoria": "Tipo de dato",
            "definicion": "Diccionario que asigna un valor predeterminado a claves no existentes.",
            "traduccion": "Dictionary that assigns a default value to nonexistent keys."},
        "decode": {
            "categoria": ("Método",),
            "definicion": "Convierte bytes a una cadena usando una codificación específica.",
            "traduccion": "Converts bytes to a string using a specific encoding."},
        "deflate": {
            "categoria": ("Método",),
            "definicion": "Método de compresión para reducir el tamaño de archivos.",
            "traduccion": "Compression method to reduce file sizes."},
        "deepcopy": {
            "categoria": ("Método",),
            "definicion": "Copia un objeto y todos sus objetos anidados.",
            "traduccion": "Copies an object and all its nested objects."},
        "detach": {
            "categoria": ("Método",),
            "definicion": "Desconecta un buffer de un flujo (usado en IO).",
            "traduccion": "Disconnects a buffer from a stream (used in IO)."},
        "dump": {
            "categoria": ("Método",),
            "definicion": "Serializa un objeto a un archivo en formato binario o JSON.",
            "traduccion": "Serializes an object to a file in binary or JSON format."},
        "dumps": {
            "categoria": ("Método",),
            "definicion": "Serializa un objeto a una cadena en formato JSON.",
            "traduccion": "Serializes an object to a string in JSON format."},
        "difference": {
            "categoria": ("Método",),
            "definicion": "Devuelve la diferencia entre conjuntos.",
            "traduccion": "Returns the difference between sets."},
        "difference_update": {
            "categoria": ("Método",),
            "definicion": "Actualiza un conjunto, eliminando elementos encontrados en otro conjunto.",
            "traduccion": "Updates a set by removing elements found in another set."},
        "decode_header": {
            "categoria": ("Método",),
            "definicion": "Decodifica un encabezado de correo electrónico.",
            "traduccion": "Decodes an email header."},
        "disk_usage": {
            "categoria": ("Función",),
            "definicion": "Devuelve el uso de espacio en disco de un directorio o disco (en shutil).",
            "traduccion": "Returns disk space usage of a directory or disk (in shutil)."},
       "datetime": {
           "categoria": ("Fecha",),
           "traduccion": "Class for manipulating dates and times.",
           "definicion": "Proporciona funciones y objetos para trabajar con fechas y horas en Python."
        "difference": {
            "categoria": ("Método",),
            "definicion": "Devuelve la diferencia entre dos o más conjuntos.",
            "traduccion": "Returns the difference between two or more sets."},
        "disk_cache": {
            "categoria": ("Caché",),
            "definicion": "Caché que almacena temporalmente datos en el disco.",
            "traduccion": "Cache that temporarily stores data on disk."}},
    
    "e":{
        "enumerate": {
            "categoria": ("Manipulación de iterables",),
            "definicion": "Agrega un contador a un iterable y lo devuelve como un objeto enumerado.",
            "traduccion": "Adds a counter to an iterable and returns it as an enumerated object."},
        "eval": {
            "categoria": ("Evaluación de expresiones",),
            "definicion": "Ejecuta una expresión Python desde una cadena dada.",
            "traduccion": "Executes a Python expression from a given string."},
        "exec": {
            "categoria": ("Ejecución de código",),
            "definicion": "Ejecuta un código Python dinámico en el entorno actual.",
            "traduccion": "Executes dynamic Python code in the current environment."},
        "except": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Bloque que captura excepciones en el manejo de errores.",
            "traduccion": "Block that catches exceptions in error handling."},
        "else": {
            "categoria": ("Control de flujo",),
            "definicion": "Bloque que se ejecuta cuando no se cumple una condición if.",
            "traduccion": "Block that runs when an if condition is not met."},
        "elif": {
            "categoria": ("Control de flujo",),
            "definicion": "Condición alternativa en una declaración if.",
            "traduccion": "Alternative condition in an if statement."},
        "exit": {
            "categoria": ("Control de programa",),
            "definicion": "Finaliza el programa actual.",
            "traduccion": "Terminates the current program."},
        "end": {
            "categoria": ("Impresión",),
            "definicion": "Argumento en print() que especifica el carácter final en la salida.",
            "traduccion": "Argument in print() specifying the end character in output."},
        "expandtabs": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Convierte tabulaciones en espacios en una cadena.",
            "traduccion": "Converts tabs to spaces in a string."},
        "encode": {
            "categoria": ("Codificación",),
            "definicion": "Convierte una cadena en bytes usando una codificación específica.",
            "traduccion": "Converts a string to bytes using a specified encoding."},
        "element": {
            "categoria": ("Estructura de datos",),
            "definicion": "Un item en una colección como listas o conjuntos.",
            "traduccion": "An item in a collection such as lists or sets."},
        "error": {
            "categoria": ("Manejo de errores",),
            "definicion": "Indica que ha ocurrido un problema en el programa.",
            "traduccion": "Indicates that an issue has occurred in the program."},
        "exception": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Un error que ocurre durante la ejecución del programa.",
            "traduccion": "An error that occurs during program execution."},
        "evaluate": {
            "categoria": ("Evaluación de expresiones",),
            "definicion": "Determina el valor de una expresión o variable.",
            "traduccion": "Determines the value of an expression or variable."},
        "elements": {
            "categoria": ("Estructura de datos",),
            "definicion": "Conjunto de items en una colección.",
            "traduccion": "Set of items in a collection."},
        "exponential": {
            "categoria": ("Matemáticas",),
            "definicion": "Función que calcula la potencia de un número.",
            "traduccion": "Function that calculates the power of a number."},
        "enumerations": {
            "categoria": ("Estructura de datos",),
            "definicion": "Tipo de dato que permite definir conjuntos de constantes.",
            "traduccion": "Data type that allows defining sets of constants."},
        "encode_utf8": {
            "categoria": ("Codificación",),
            "definicion": "Convierte una cadena a bytes usando la codificación UTF-8.",
            "traduccion": "Converts a string to bytes using UTF-8 encoding."},
        "execfile": {
            "categoria": ("Ejecución de código",),
            "definicion": "Ejecuta un archivo Python como si fuera un script.",
            "traduccion": "Executes a Python file as if it were a script."},
        "edit_distance": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Número mínimo de operaciones necesarias para transformar una cadena en otra.",
            "traduccion": "Minimum number of operations needed to transform one string into another."},
        "eval_input": {
            "categoria": ("Evaluación de expresiones",),
            "definicion": "Evalúa una expresión ingresada por el usuario.",
            "traduccion": "Evaluates an expression entered by the user."},
        "exceed": {
            "categoria": ("Comparación",),
            "definicion": "Sobrepasar un límite o cantidad.",
            "traduccion": "To go beyond a limit or amount."},
        "expected": {
            "categoria": ("Comparación",),
            "definicion": "El resultado que se prevé en una operación.",
            "traduccion": "The outcome that is anticipated in an operation."},
        "encode_base64": {
            "categoria": ("Codificación",),
            "definicion": "Convierte datos en una representación Base64.",
            "traduccion": "Converts data into a Base64 representation."},
        "execute": {
            "categoria": ("Ejecución de código",),
            "definicion": "Llevar a cabo un comando o instrucción.",
            "traduccion": "Carry out a command or instruction."},
        "exit_code": {
            "categoria": ("Control de programa",),
            "definicion": "Valor devuelto al finalizar un programa.",
            "traduccion": "Value returned when a program finishes."},
        "evaluate_expression": {
            "categoria": ("Evaluación de expresiones",),
            "definicion": "Evalúa una expresión para determinar su valor.",
            "traduccion": "Evaluates an expression to determine its value."},
        "environment": {
            "categoria": ("Configuración",),
            "definicion": "Conjunto de variables que afectan la ejecución de un programa.",
            "traduccion": "Set of variables that affect the execution of a program."},
        "environment_variable": {
            "categoria": ("Configuración",),
            "definicion": "Variable que define el comportamiento de procesos en el sistema.",
            "traduccion": "Variable that defines the behavior of processes in the system."},
        "exp": {
            "categoria": ("Matemáticas",),
            "definicion": "Función que devuelve el valor de e elevado a la potencia especificada.",
            "traduccion": "Function that returns the value of e raised to the specified power."},
        "exception_handling": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Mecanismo para manejar errores y excepciones en el código.",
            "traduccion": "Mechanism to handle errors and exceptions in code."},
        "expand": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Desarrolla variables o estructuras de datos.",
            "traduccion": "Expands variables or data structures."},
        "environment_config": {
            "categoria": ("Configuración",),
            "definicion": "Configuraciones que definen el entorno de ejecución.",
            "traduccion": "Configurations that define the runtime environment."},
        "equal": {
            "categoria": ("Comparación",),
            "definicion": "Operador que verifica la igualdad entre dos valores.",
            "traduccion": "Operator that checks equality between two values."},
        "error_handling": {
            "categoria": ("Manejo de errores",),
            "definicion": "Proceso de gestionar errores en el código.",
            "traduccion": "Process of managing errors in code."},
        "event": {
            "categoria": ("Eventos",),
            "definicion": "Acción que ocurre en un programa, como un clic de ratón.",
            "traduccion": "An action that occurs in a program, such as a mouse click."},
        "event_loop": {
            "categoria": ("Programación asincrónica",),
            "definicion": "Ciclo que espera y despacha eventos o mensajes.",
            "traduccion": "Loop that waits for and dispatches events or messages."},
        "exception_type": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Tipo de error que se puede manejar en Python.",
            "traduccion": "Type of error that can be handled in Python."},
        "error_message": {
            "categoria": ("Manejo de errores",),
            "definicion": "Mensaje que describe el error ocurrido.",
            "traduccion": "Message describing the error that occurred."},
        "extract": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Obtiene un valor específico de una colección.",
            "traduccion": "Retrieves a specific value from a collection."},
        "exit_status": {
            "categoria": ("Control de programa",),
            "definicion": "Estado de salida que indica si un programa finalizó con éxito.",
            "traduccion": "Exit status indicating whether a program finished successfully."}},
    
    "f": {
        "filemode": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Modo en el que se abre un archivo, como lectura o escritura.",
            "traduccion": "Mode in which a file is opened, such as read or write."},
        "frozen_set": {
            "categoria": ("Estructura de datos",),
            "definicion": "Colección inmutable de elementos únicos.",
            "traduccion": "Immutable collection of unique elements."},
        "format_map": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Devuelve una cadena formateada usando un diccionario.",
            "traduccion": "Returns a formatted string using a dictionary."},
        "find": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Busca una subcadena dentro de una cadena y devuelve su índice.",
            "traduccion": "Searches for a substring within a string and returns its index."},
        "float32": {
            "categoria": ("Tipos de datos",),
            "definicion": "Tipo de dato que representa un número en punto flotante de 32 bits.",
            "traduccion": "Data type representing a 32-bit floating-point number."},
        "float64": {
            "categoria": ("Tipos de datos",),
            "definicion": "Tipo de dato que representa un número en punto flotante de 64 bits.",
            "traduccion": "Data type representing a 64-bit floating-point number."},
        "formatting": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Proceso de dar formato a la salida de texto.",
            "traduccion": "Process of formatting the output of text."},
        "flush_output": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Forza la escritura de datos en la salida estándar.",
            "traduccion": "Forces the writing of data to standard output."},
        "function_definition": {
            "categoria": ("Funciones",),
            "definicion": "La forma en que se define una función en Python.",
            "traduccion": "The way a function is defined in Python."},
        "filepath": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Ruta que especifica la ubicación de un archivo en el sistema de archivos.",
            "traduccion": "Path that specifies the location of a file in the file system."},
        "flask": {
            "categoria": ("Frameworks",),
            "definicion": "Microframework para desarrollar aplicaciones web en Python.",
            "traduccion": "Microframework for developing web applications in Python."},
        "filtering": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Proceso de eliminar elementos no deseados de una colección.",
            "traduccion": "Process of removing unwanted elements from a collection."},
        "futures": {
            "categoria": ("Programación asincrónica",),
            "definicion": "Una forma de trabajar con programación asíncrona en Python.",
            "traduccion": "A way to work with asynchronous programming in Python."},
        "fold": {
            "categoria": ("Funciones",),
            "definicion": "Función que aplica una operación acumulativa sobre un iterable.",
            "traduccion": "Function that applies an accumulating operation over an iterable."},
        "fromkeys": {
            "categoria": ("Estructura de datos",),
            "definicion": "Método de diccionario que crea un nuevo diccionario con claves y un valor por defecto.",
            "traduccion": "Dictionary method that creates a new dictionary with keys and a default value."},
        "flask_restful": {
            "categoria": ("Frameworks",),
            "definicion": "Extensión de Flask para construir APIs RESTful de manera sencilla.",
            "traduccion": "Flask extension for building RESTful APIs easily."},
        "fix": {
            "categoria": ("Depuración",),
            "definicion": "Corregir o ajustar errores en el código.",
            "traduccion": "To correct or adjust bugs in code."},
        "float_conversion": {
            "categoria": ("Conversión de datos",),
            "definicion": "Proceso de convertir un número a su representación en punto flotante.",
            "traduccion": "Process of converting a number to its floating-point representation."},
        "full_path": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Ruta completa a un archivo, incluyendo el nombre del archivo y su directorio.",
            "traduccion": "Complete path to a file, including the filename and its directory."},
        "filter": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Crea una lista de elementos para los cuales una función devuelve True.",
            "traduccion": "Creates a list of elements for which a function returns True."},
        "float": {
            "categoria": ("Tipos de datos",),
            "definicion": "Tipo de dato que representa un número en punto flotante.",
            "traduccion": "Data type that represents a floating-point number."},
        "for": {
            "categoria": ("Control de flujo",),
            "definicion": "Crea un bucle que itera sobre un iterable.",
            "traduccion": "Creates a loop that iterates over an iterable."},
        "format": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Devuelve una cadena formateada.",
            "traduccion": "Returns a formatted string."},
        "from": {
            "categoria": ("Importación de módulos",),
            "definicion": "Utilizado para importar módulos o partes de un módulo.",
            "traduccion": "Used to import modules or parts of a module."},
        "function": {
            "categoria": ("Funciones",),
            "definicion": "Bloque de código reutilizable que realiza una tarea específica.",
            "traduccion": "Reusable block of code that performs a specific task."},
        "fibonacci": {
            "categoria": ("Matemáticas",),
            "definicion": "Secuencia de números donde cada número es la suma de los dos anteriores.",
            "traduccion": "Sequence of numbers where each number is the sum of the two preceding ones."},
        "file": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Objeto que representa un archivo en el sistema de archivos.",
            "traduccion": "Object that represents a file in the file system."},
        "fwrite": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Escribe datos en un archivo abierto.",
            "traduccion": "Writes data to an open file."},
        "fread": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Lee datos de un archivo abierto.",
            "traduccion": "Reads data from an open file."},
        "finally": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Bloque que se ejecuta después de un try/except, sin importar si se produjo un error.",
            "traduccion": "Block that executes after a try/except, regardless of whether an error occurred."},
        "freeze": {
            "categoria": ("Estructura de datos",),
            "definicion": "Convierte un objeto en un formato inmutable.",
            "traduccion": "Converts an object into an immutable format."},
        "flush": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Vacía el búfer de un archivo para asegurar que todos los datos se escriban.",
            "traduccion": "Flushes the file buffer to ensure all data is written."},
        "fstring": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Cadena formateada literal, que permite incrustar expresiones.",
            "traduccion": "Formatted string literal, allowing embedded expressions."},
        "factorial": {
            "categoria": ("Matemáticas",),
            "definicion": "Producto de todos los números enteros positivos hasta un número dado.",
            "traduccion": "Product of all positive integers up to a given number."},
        "frozen": {
            "categoria": ("Estructura de datos",),
            "definicion": "Un tipo de conjunto inmutable.",
            "traduccion": "An immutable set type."},
        "filterfalse": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Devuelve un iterador que filtra elementos de una secuencia para los cuales la función es False.",
            "traduccion": "Returns an iterator filtering elements from a sequence for which the function is False."},
        "fuzzy": {
            "categoria": ("Manejo de datos",),
            "definicion": "Método que permite trabajar con datos inexactos o imprecisos.",
            "traduccion": "Method that allows working with inaccurate or imprecise data."},
        "fibonacci_sequence": {
            "categoria": ("Matemáticas",),
            "definicion": "Genera la secuencia de Fibonacci hasta un número específico.",
            "traduccion": "Generates the Fibonacci sequence up to a specific number."},
        "format_spec": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Especificación que define cómo se debe formatear un valor.",
            "traduccion": "Specification that defines how a value should be formatted."},
        "fork": {
            "categoria": ("Procesos del sistema",),
            "definicion": "Crea un nuevo proceso en sistemas operativos basados en Unix.",
            "traduccion": "Creates a new process in Unix-based operating systems."},
        "forking": {
            "categoria": ("Procesos del sistema",),
            "definicion": "Proceso de dividir un programa en varios procesos para ejecutar tareas en paralelo.",
            "traduccion": "Process of dividing a program into multiple processes to run tasks in parallel."},
        "first": {
            "categoria": ("Manipulación de iterables",),
            "definicion": "Método para obtener el primer elemento de una secuencia.",
            "traduccion": "Method to get the first element of a sequence."},
        "float_format": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Especificación de formato para representar números en punto flotante.",
            "traduccion": "Format specification for representing floating-point numbers."},
        "filter_none": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Devuelve un iterador que filtra elementos que no son None.",
            "traduccion": "Returns an iterator filtering elements that are not None."},
        "func_code": {
            "categoria": ("Funciones",),
            "definicion": "Código byte que representa el cuerpo de una función.",
            "traduccion": "Bytecode representing the body of a function."},
        "float_power": {
            "categoria": ("Matemáticas",),
            "definicion": "Función que eleva un número a la potencia de otro número en punto flotante.",
            "traduccion": "Function that raises a number to the power of another floating-point number."},
        "format_string": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Cadena que especifica cómo se deben formatear los valores en Python.",
            "traduccion": "String that specifies how values should be formatted in Python."},
        "filename": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Nombre de un archivo, que puede incluir su extensión.",
            "traduccion": "Name of a file, which may include its extension."},
        "file_object": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Objeto que permite interactuar con un archivo abierto en Python.",
            "traduccion": "Object that allows interaction with an open file in Python."},
        "finally_clause": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Parte de una estructura try/except que se ejecuta siempre, independientemente de los errores.",
            "traduccion": "Part of a try/except structure that always executes, regardless of errors."},
        "file_read": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Operación que lee el contenido de un archivo.",
            "traduccion": "Operation that reads the content of a file."},
        "form": {
            "categoria": ("Web",),
            "definicion": "Representación de datos en un formato estructurado, a menudo utilizado en aplicaciones web.",
            "traduccion": "Representation of data in a structured format, often used in web applications."},
        "function_call": {
            "categoria": ("Funciones",),
            "definicion": "Invocación de una función para ejecutar su código.",
            "traduccion": "Invocation of a function to execute its code."},
        "force": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Método para forzar la ejecución de un proceso o función.",
            "traduccion": "Method to force the execution of a process or function."},
        "function_pointer": {
            "categoria": ("Funciones",),
            "definicion": "Referencia a una función que puede ser pasada como argumento.",
            "traduccion": "Reference to a function that can be passed as an argument."},
        "float_precision": {
            "categoria": ("Tipos de datos",),
            "definicion": "Precisión de un número en punto flotante, que afecta la exactitud de los cálculos.",
            "traduccion": "Precision of a floating-point number, affecting the accuracy of calculations."},
        "format_error": {
            "categoria": ("Manejo de errores",),
            "definicion": "Error que ocurre al formatear datos de manera incorrecta.",
            "traduccion": "Error that occurs when formatting data incorrectly."},
        "file_write": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Operación que escribe datos en un archivo.",
            "traduccion": "Operation that writes data to a file."},
        "fibonacci_search": {
            "categoria": ("Algoritmos de búsqueda",),
            "definicion": "Algoritmo de búsqueda que utiliza la secuencia de Fibonacci para encontrar elementos.",
            "traduccion": "Search algorithm that uses the Fibonacci sequence to find elements."},
        "filter_map": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Combinación de la funcionalidad de filter y map en una operación.",
            "traduccion": "Combination of the functionality of filter and map in a single operation."}},
    







        
    
    "h": {
        "hash": {
            "definicion": "Devuelve el valor hash de un objeto.",
            "traduccion": "Returns the hash value of an object."},
        "help": {
            "definicion": "Muestra la ayuda de un módulo, función o clase.",
            "traduccion": "Displays the help information of a module, function, or class."},
        "hex": {
            "definicion": "Convierte un número en su representación hexadecimal.",
            "traduccion": "Converts a number to its hexadecimal representation."},
        "head": {
            "definicion": "Devuelve las primeras filas de un DataFrame en pandas.",
            "traduccion": "Returns the first rows of a DataFrame in pandas."},
        "heapq": {
            "definicion": "Proporciona funciones para crear y manipular montículos.",
            "traduccion": "Provides functions to create and manipulate heaps."},
        "hstack": {
            "definicion": "Apila arrays en secuencia horizontal.",
            "traduccion": "Stacks arrays in a horizontal sequence."},
        "hypot": {
            "definicion": "Calcula la hipotenusa de un triángulo rectángulo.",
            "traduccion": "Calculates the hypotenuse of a right triangle."},
        "hist": {
            "definicion": "Genera un histograma de datos en matplotlib.",
            "traduccion": "Generates a histogram of data in matplotlib."},
        "hostname": {
            "definicion": "Devuelve o establece el nombre del host de la máquina.",
            "traduccion": "Returns or sets the machine's hostname."},
        "hashlib": {
            "definicion": "Ofrece funciones de hashing seguras.",
            "traduccion": "Provides secure hashing functions."},
        "homedir": {
            "definicion": "Devuelve el directorio de inicio del usuario.",
            "traduccion": "Returns the user's home directory."},
        "highlight": {
            "definicion": "Resalta el código para mejorar la legibilidad.",
            "traduccion": "Highlights code for readability."},
        "histogram": {
            "definicion": "Calcula la frecuencia de datos en rangos específicos.",
            "traduccion": "Calculates data frequency in specific ranges."},
        "hook": {
            "definicion": "Define una función personalizada para extender una operación.",
            "traduccion": "Defines a custom function to extend an operation."},
        "http": {
            "definicion": "Proporciona soporte para el protocolo HTTP en Python.",
            "traduccion": "Provides support for the HTTP protocol in Python."},
        "hist2d": {
            "definicion": "Genera un histograma bidimensional en matplotlib.",
            "traduccion": "Generates a two-dimensional histogram in matplotlib."},
        "histc": {
            "definicion": "Calcula la cuenta de histogramas en Numpy.",
            "traduccion": "Calculates histogram counts in Numpy."},
        "hamming": {
            "definicion": "Calcula la distancia de Hamming entre dos secuencias.",
            "traduccion": "Calculates the Hamming distance between two sequences."},
        "heapify": {
            "definicion": "Convierte una lista en un montículo.",
            "traduccion": "Transforms a list into a heap."},
        "hsv": {
            "definicion": "Modelo de color basado en matiz, saturación y valor.",
            "traduccion": "Color model based on hue, saturation, and value."},
        "headless": {
            "definicion": "Ejecuta aplicaciones gráficas sin entorno de visualización.",
            "traduccion": "Runs graphical applications without a display environment."},
        "histcounts": {
            "definicion": "Cuenta elementos para rangos especificados en un histograma.",
            "traduccion": "Counts elements for specified ranges in a histogram."},
        "hexbin": {
            "definicion": "Crea un gráfico de contenedores hexagonales.",
            "traduccion": "Creates a hexbin plot."},
        "http.client": {
            "definicion": "Módulo para realizar peticiones HTTP.",
            "traduccion": "Module for making HTTP requests."},
        "hook_fn": {
            "definicion": "Función personalizada que se llama en puntos específicos.",
            "traduccion": "Custom function called at specific points."},
        "hue": {
            "definicion": "Ajusta el tono de color en gráficos de seaborn.",
            "traduccion": "Adjusts the color hue in seaborn plots."},
        "hashset": {
            "definicion": "Estructura de datos para almacenar elementos únicos en hashing.",
            "traduccion": "Data structure for storing unique items in hashing."},
        "hdf5": {
            "definicion": "Formato de archivo para almacenar datos de gran tamaño.",
            "traduccion": "File format for storing large data."},
        "hanning": {
            "definicion": "Aplica la ventana de Hanning en procesamiento de señales.",
            "traduccion": "Applies the Hanning window in signal processing."},
        "help_module": {
            "definicion": "Proporciona ayuda sobre un módulo específico.",
            "traduccion": "Provides help on a specific module."},
        "handle": {
            "definicion": "Representa un recurso o elemento de sistema gestionado.",
            "traduccion": "Represents a managed system resource or element."},
        "hstack_block": {
            "definicion": "Apila bloques en horizontal.",
            "traduccion": "Stacks blocks horizontally."},
        "hotspot": {
            "definicion": "Punto de acceso para operaciones frecuentes en programación.",
            "traduccion": "Access point for frequent operations in programming."},
        "http.server": {
            "definicion": "Módulo para iniciar un servidor HTTP básico.",
            "traduccion": "Module to start a basic HTTP server."},
        "haversine": {
            "definicion": "Calcula la distancia entre dos puntos en una esfera.",
            "traduccion": "Calculates the distance between two points on a sphere."},
        "hspace": {
            "definicion": "Controla el espacio horizontal entre elementos gráficos.",
            "traduccion": "Controls horizontal spacing between graphical elements."},
        "hex_color": {
            "definicion": "Representación hexadecimal de un color.",
            "traduccion": "Hexadecimal representation of a color."},
        "handle_request": {
            "definicion": "Gestión de una solicitud en un servidor.",
            "traduccion": "Handling a request in a server."},
        "html": {
            "definicion": "Modulo que permite manejar y analizar código HTML.",
            "traduccion": "Module that handles and parses HTML code."},
        "hybrid": {
            "definicion": "Método que combina características de dos o más algoritmos.",
            "traduccion": "Method combining features of two or more algorithms."},
        "hclust": {
            "definicion": "Realiza el clustering jerárquico.",
            "traduccion": "Performs hierarchical clustering."},
        "harden": {
            "definicion": "Refuerza la seguridad de un sistema.",
            "traduccion": "Strengthens system security."},
        "hist_equalize": {
            "definicion": "Iguala el histograma de una imagen.",
            "traduccion": "Equalizes the histogram of an image."},
        "httpx": {
            "definicion": "Cliente HTTP asíncrono para Python.",
            "traduccion": "Asynchronous HTTP client for Python."},
        "hdf": {
            "definicion": "Formato de archivo para datos jerárquicos.",
            "traduccion": "File format for hierarchical data."},
        "histmatch": {
            "definicion": "Iguala el histograma de una imagen con otra.",
            "traduccion": "Matches the histogram of one image with another."},
        "hasattr": {
            "definicion": "Comprueba si un objeto tiene un atributo.",
            "traduccion": "Checks if an object has an attribute."},
        "httpx_session": {
            "definicion": "Gestiona sesiones de solicitudes HTTP en httpx.",
            "traduccion": "Manages HTTP request sessions in httpx."},
        "hash_table": {
            "definicion": "Estructura de datos que permite almacenar datos únicos.",
            "traduccion": "Data structure that stores unique data."},
        "hough_transform": {
            "definicion": "Detecta líneas y formas en imágenes.",
            "traduccion": "Detects lines and shapes in images."},
        "hsv_to_rgb": {
            "definicion": "Convierte un color de HSV a RGB.",
            "traduccion": "Converts a color from HSV to RGB."},
        "http_code": {
            "definicion": "Código de respuesta HTTP.",
            "traduccion": "HTTP response code."},
        "http_status": {
            "definicion": "Código que indica el estado de una solicitud HTTP.",
            "traduccion": "Code that indicates the status of an HTTP request."},
        "hessian": {
            "definicion": "Matriz de segundas derivadas en optimización.",
            "traduccion": "Matrix of second derivatives in optimization."},
        "huber": {
            "definicion": "Función de pérdida en estadística robusta.",
            "traduccion": "Loss function in robust statistics."},
        "hue_shift": {
            "definicion": "Ajusta el matiz de una imagen o color.",
            "traduccion": "Adjusts the hue of an image or color."},
        "hard_limit": {
            "definicion": "Límite rígido en una operación o parámetro.",
            "traduccion": "Rigid limit in an operation or parameter."},
        "highlight_text": {
            "definicion": "Resalta texto para mejorar la legibilidad.",
            "traduccion": "Highlights text for readability."},
        "hierarchical": {
            "definicion": "Relacionado con estructuras en niveles o jerarquías.",
            "traduccion": "Related to structures in levels or hierarchies."},
        "hash_code": {
            "definicion": "Representación numérica de un objeto.",
            "traduccion": "Numeric representation of an object."},
        "hermite": {
            "definicion": "Función ortogonal en procesamiento de señales.",
            "traduccion": "Orthogonal function in signal processing."},
        "handle_event": {
            "definicion": "Gestiona un evento específico en un sistema.",
            "traduccion": "Handles a specific event in a system."},
        "homogeneous": {
            "definicion": "Estructura consistente sin variaciones.",
            "traduccion": "Consistent structure without variations."},
        "hash_set": {
            "definicion": "Conjunto de elementos únicos basado en hashing.",
            "traduccion": "Set of unique elements based on hashing."},
        "hough_line": {
            "definicion": "Detecta líneas rectas en imágenes.",
            "traduccion": "Detects straight lines in images."},
        "http_methods": {
            "definicion": "Métodos estándar para solicitudes HTTP.",
            "traduccion": "Standard methods for HTTP requests."},
        "http_response": {
            "definicion": "Respuesta generada a una solicitud HTTP.",
            "traduccion": "Response generated to an HTTP request."},
        "hex_to_bin": {
            "definicion": "Convierte de hexadecimal a binario.",
            "traduccion": "Converts from hexadecimal to binary."},
        "hist_interpolate": {
            "definicion": "Interpolación en histogramas.",
            "traduccion": "Interpolation in histograms."},
        "hyperlink": {
            "definicion": "Vincula un recurso a través de URL.",
            "traduccion": "Links a resource through a URL."},
        "hypertune": {
            "definicion": "Ajuste de parámetros para optimización.",
            "traduccion": "Parameter tuning for optimization."},
        "http_parser": {
            "definicion": "Analizador de solicitudes HTTP.",
            "traduccion": "HTTP request parser."},
        "hover": {
            "definicion": "Efecto al pasar el cursor sobre un elemento.",
            "traduccion": "Effect when hovering over an element."},
        "http_auth": {
            "definicion": "Autenticación en protocolos HTTP.",
            "traduccion": "Authentication in HTTP protocols."},
        "heightmap": {
            "definicion": "Mapa de alturas en gráficos 3D.",
            "traduccion": "Height map in 3D graphics."},
        "hstack_array": {
            "definicion": "Apila arrays horizontalmente.",
            "traduccion": "Stacks arrays horizontally."},
        "high_frequency": {
            "definicion": "Componentes de alta frecuencia en señales.",
            "traduccion": "High-frequency components in signals."},
        "hidden_state": {
            "definicion": "Estado oculto en redes neuronales recurrentes.",
            "traduccion": "Hidden state in recurrent neural networks."},
        "hashmap": {
            "definicion": "Mapa que almacena pares clave-valor mediante hashing.",
            "traduccion": "Map storing key-value pairs using hashing."},
        "hostfile": {
            "definicion": "Archivo que mapea nombres de dominio a IPs.",
            "traduccion": "File mapping domain names to IPs."},
        "hit_rate": {
            "definicion": "Proporción de aciertos en una predicción o búsqueda.",
            "traduccion": "Success rate in a prediction or search."},
        "horizontal_flip": {
            "definicion": "Invierte una imagen horizontalmente.",
            "traduccion": "Flips an image horizontally."},
        "http_request": {
            "definicion": "Solicitud enviada a un servidor HTTP.",
            "traduccion": "Request sent to an HTTP server."},
        "hysteresis": {
            "definicion": "Efecto de retardo en un sistema ante cambios.",
            "traduccion": "Delay effect in a system when changing states."},
        "half_width": {
            "definicion": "Mitad de la anchura de un elemento.",
            "traduccion": "Half the width of an element."},
        "hatch_fill": {
            "definicion": "Patrón de relleno en gráficos.",
            "traduccion": "Fill pattern in graphics."},
        "http_proxy": {
            "definicion": "Servidor intermediario para solicitudes HTTP.",
            "traduccion": "Intermediary server for HTTP requests."},
        "header_bytes": {
            "definicion": "Bytes que componen el encabezado de una solicitud.",
            "traduccion": "Bytes comprising a request header."},
        "hexa_grid": {
            "definicion": "Grilla hexagonal para visualización o cálculos.",
            "traduccion": "Hexagonal grid for visualization or calculations."},
        "http_cache": {
            "definicion": "Almacén de respuestas HTTP para acceso rápido.",
            "traduccion": "Store of HTTP responses for quick access."},
        "hierarchy_tree": {
            "definicion": "Estructura en forma de árbol jerárquico.",
            "traduccion": "Structure in a hierarchical tree form."},
        "hex_to_rgb": {
            "definicion": "Convierte de hexadecimal a RGB.",
            "traduccion": "Converts from hexadecimal to RGB."},
        "highlight_color": {
            "definicion": "Color de resaltado en gráficos o interfaces.",
            "traduccion": "Highlight color in graphics or interfaces."},
        "hyperbolic": {
            "definicion": "Relativo a funciones hiperbólicas en matemáticas.",
            "traduccion": "Related to hyperbolic functions in math."},
        "http_headers": {
            "definicion": "Encabezados de una solicitud o respuesta HTTP.",
            "traduccion": "Headers of an HTTP request or response."},
        "hist_norm": {
            "definicion": "Normalización de un histograma.",
            "traduccion": "Normalization of a histogram."},
        "hover_text": {
            "definicion": "Texto que aparece al pasar el cursor sobre un elemento.",
            "traduccion": "Text displayed when hovering over an element."},
        "http_status_code": {
            "definicion": "Código de estado de una respuesta HTTP.",
            "traduccion": "Status code of an HTTP response."},
        "http_endpoint": {
            "definicion": "Punto final de una API en un servidor.",
            "traduccion": "API endpoint on a server."},
        "holdout": {
            "definicion": "Conjunto de datos separado para validación.",
            "traduccion": "Data set held out for validation."},
        "hypergraph": {
            "definicion": "Grafo en el cual cada arista conecta múltiples nodos.",
            "traduccion": "Graph where each edge connects multiple nodes."},
        "hamming_window": {
            "definicion": "Ventana de Hamming en análisis de señales.",
            "traduccion": "Hamming window in signal analysis."},
        "headless_mode": {
            "definicion": "Modo sin entorno gráfico para pruebas o servidores.",
            "traduccion": "Headless mode for testing or servers."},
        "http_redirect": {
            "definicion": "Redirección HTTP a otra URL.",
            "traduccion": "HTTP redirection to another URL."},
        "highlighter": {
            "definicion": "Resalta código en editores o IDEs.",
            "traduccion": "Highlights code in editors or IDEs."}},
    
    "i": {
        "import": {
            "definicion": "Incorpora un módulo externo al programa.",
            "traduccion": "Imports an external module into the program."},
        "int": {
            "definicion": "Convierte un valor en un número entero.",
            "traduccion": "Converts a value to an integer."},
        "input": {
            "definicion": "Captura datos ingresados por el usuario.",
            "traduccion": "Captures data entered by the user."},
        "isinstance": {
            "definicion": "Verifica si un objeto es instancia de una clase.",
            "traduccion": "Checks if an object is an instance of a class."},
        "issubclass": {
            "definicion": "Comprueba si una clase es subclase de otra.",
            "traduccion": "Checks if a class is a subclass of another."},
        "index": {
            "definicion": "Obtiene el índice de un elemento en una lista.",
            "traduccion": "Gets the index of an element in a list."},
        "insert": {
            "definicion": "Inserta un elemento en una posición específica en una lista.",
            "traduccion": "Inserts an element at a specific position in a list."},
        "isalpha": {
            "definicion": "Comprueba si una cadena contiene solo letras.",
            "traduccion": "Checks if a string contains only alphabetic characters."},
        "isdigit": {
            "definicion": "Verifica si una cadena contiene solo dígitos.",
            "traduccion": "Checks if a string contains only digits."},
        "isdecimal": {
            "definicion": "Comprueba si una cadena contiene caracteres decimales.",
            "traduccion": "Checks if a string contains decimal characters."},
        "isnumeric": {
            "definicion": "Determina si una cadena es numérica.",
            "traduccion": "Determines if a string is numeric."},
        "isidentifier": {
            "definicion": "Verifica si una cadena es un identificador válido.",
            "traduccion": "Checks if a string is a valid identifier."},
        "isprintable": {
            "definicion": "Comprueba si una cadena contiene caracteres imprimibles.",
            "traduccion": "Checks if a string contains printable characters."},
        "isspace": {
            "definicion": "Verifica si una cadena contiene solo espacios en blanco.",
            "traduccion": "Checks if a string contains only whitespace."},
        "iter": {
            "definicion": "Devuelve un iterador de un objeto.",
            "traduccion": "Returns an iterator from an object."},
        "isclose": {
            "definicion": "Comprueba si dos números están cerca en valor.",
            "traduccion": "Checks if two numbers are close in value."},
        "isinf": {
            "definicion": "Verifica si un número es infinito.",
            "traduccion": "Checks if a number is infinite."},
        "isnan": {
            "definicion": "Determina si un valor es NaN (Not a Number).",
            "traduccion": "Determines if a value is NaN (Not a Number)."},
        "identity_matrix": {
            "definicion": "Matriz con 1s en su diagonal principal y 0s en el resto.",
            "traduccion": "Matrix with 1s on its main diagonal and 0s elsewhere."},
        "invert": {
            "definicion": "Invierte los valores o el orden de un objeto.",
            "traduccion": "Inverts the values or order of an object."},
        "islice": {
            "definicion": "Permite cortar iterables de manera eficiente.",
            "traduccion": "Efficiently slices iterables."},
        "imag": {
            "definicion": "Obtiene la parte imaginaria de un número complejo.",
            "traduccion": "Gets the imaginary part of a complex number."},
        "imap": {
            "definicion": "Función para aplicar una función a cada elemento de un iterable.",
            "traduccion": "Applies a function to each item in an iterable."},
        "initial": {
            "definicion": "Estado o valor inicial de una variable o proceso.",
            "traduccion": "Initial state or value of a variable or process."},
        "inverse_transform": {
            "definicion": "Transformación inversa aplicada a datos.",
            "traduccion": "Inverse transformation applied to data."},
        "init_method": {
            "definicion": "Método especial que inicializa instancias de una clase.",
            "traduccion": "Special method that initializes class instances."},
        "init_process": {
            "definicion": "Proceso de inicialización en programación.",
            "traduccion": "Initialization process in programming."},
        "inf": {
            "definicion": "Constante que representa el infinito.",
            "traduccion": "Constant representing infinity."},
        "inspect": {
            "definicion": "Permite inspeccionar objetos en Python.",
            "traduccion": "Allows inspection of Python objects."},
        "integrate": {
            "definicion": "Realiza la integración de una función.",
            "traduccion": "Performs integration of a function."},
        "inner": {
            "definicion": "Producto interior o escalar de vectores.",
            "traduccion": "Inner or dot product of vectors."},
        "identity_function": {
            "definicion": "Función que devuelve su entrada sin cambios.",
            "traduccion": "Function that returns its input unchanged."},
        "interval": {
            "definicion": "Rango de valores entre dos límites.",
            "traduccion": "Range of values between two limits."},
        "iloc": {
            "definicion": "Permite seleccionar datos por índice en Pandas.",
            "traduccion": "Selects data by index in Pandas."},
        "is_power_of_two": {
            "definicion": "Determina si un número es una potencia de dos.",
            "traduccion": "Determines if a number is a power of two."},
        "identity_property": {
            "definicion": "Propiedad en matemáticas que mantiene un valor sin alterarlo.",
            "traduccion": "Mathematical property that retains a value unchanged."},
        "integer_division": {
            "definicion": "División que devuelve solo la parte entera.",
            "traduccion": "Division that returns only the integer part."},
        "independent_variable": {
            "definicion": "Variable cuyo valor no depende de otras variables.",
            "traduccion": "Variable whose value does not depend on others."},
        "invalid_operation": {
            "definicion": "Operación que no se puede realizar debido a restricciones.",
            "traduccion": "Operation that cannot be performed due to restrictions."},
        "iterable": {
            "definicion": "Objeto que se puede iterar en un bucle.",
            "traduccion": "Object that can be iterated in a loop."},
        "identity_relation": {
            "definicion": "Relación en matemáticas donde cada elemento se relaciona consigo mismo.",
            "traduccion": "Relation in math where each element relates to itself."},
        "info": {
            "definicion": "Muestra información sobre el objeto o el entorno.",
            "traduccion": "Displays information about the object or environment."},
        "is_empty": {
            "definicion": "Comprueba si una colección o estructura está vacía.",
            "traduccion": "Checks if a collection or structure is empty."},
        "intercept": {
            "definicion": "Punto donde una función corta un eje en un gráfico.",
            "traduccion": "Point where a function intersects an axis on a graph."},
        "iso_date": {
            "definicion": "Formato de fecha ISO, como 'YYYY-MM-DD'.",
            "traduccion": "ISO date format, like 'YYYY-MM-DD'."},
        "index_of": {
            "definicion": "Encuentra la posición de un elemento en una lista.",
            "traduccion": "Finds the position of an element in a list."},
        "implicit_conversion": {
            "definicion": "Conversión automática de tipos de datos.",
            "traduccion": "Automatic data type conversion."},
        "infinite_loop": {
            "definicion": "Bucle que nunca termina.",
            "traduccion": "Loop that never ends."},
        "inplace": {
            "definicion": "Realiza operaciones directamente en el objeto original.",
            "traduccion": "Performs operations directly on the original object."},
        "image_filter": {
            "definicion": "Aplica un filtro a una imagen.",
            "traduccion": "Applies a filter to an image."},
        "indexing": {
            "definicion": "Acceso a elementos de una estructura usando índices.",
            "traduccion": "Accessing elements of a structure using indices."},
        "infinity": {
            "definicion": "Número sin límites o fin.",
            "traduccion": "Number without bounds or end."},
        "image_processing": {
            "definicion": "Conjunto de técnicas para manipular imágenes.",
            "traduccion": "Set of techniques for manipulating images."},
        "indirect_reference": {
            "definicion": "Referencia a un objeto a través de otro.",
            "traduccion": "Reference to an object through another."},
        "id_generator": {
            "definicion": "Genera identificadores únicos.",
            "traduccion": "Generates unique identifiers."},
        "iterable_unpacking": {
            "definicion": "Desempaqueta los elementos de un iterable en variables.",
            "traduccion": "Unpacks elements of an iterable into variables."},
        "isomorphic": {
            "definicion": "Estructuras similares que se pueden mapear una en otra.",
            "traduccion": "Similar structures that can be mapped onto each other."},
        "input_sanitization": {
            "definicion": "Proceso de limpieza de datos de entrada para evitar riesgos.",
            "traduccion": "Cleansing input data to prevent risks."},
        "iota": {
            "definicion": "Notación para enumerar secuencias de enteros.",
            "traduccion": "Notation for enumerating sequences of integers."},
        "image_path": {
            "definicion": "Ruta de acceso a un archivo de imagen.",
            "traduccion": "Path to an image file."},
        "integration_testing": {
            "definicion": "Prueba de componentes combinados de un sistema.",
            "traduccion": "Testing combined components of a system."},
        "index_error": {
            "definicion": "Error al intentar acceder a un índice fuera del rango.",
            "traduccion": "Error when accessing an out-of-range index."},
        "indented_code": {
            "definicion": "Código estructurado con sangría para mejorar la lectura.",
            "traduccion": "Code structured with indentation for readability."},
        "inheritance_chain": {
            "definicion": "Secuencia de clases derivadas en una jerarquía.",
            "traduccion": "Sequence of derived classes in a hierarchy."},
        "io_bound": {
            "definicion": "Proceso limitado por operaciones de entrada/salida.",
            "traduccion": "Process limited by input/output operations."},
        "infinite_sequence": {
            "definicion": "Secuencia que no tiene fin, como una sucesión infinita.",
            "traduccion": "A sequence with no end, like an infinite succession."},
        "is_prime": {
            "definicion": "Determina si un número es primo.",
            "traduccion": "Determines if a number is prime."},
        "image_filtering": {
            "definicion": "Aplicación de filtros para modificar una imagen.",
            "traduccion": "Applying filters to modify an image."},
        "instance_attribute": {
            "definicion": "Atributo que pertenece a una instancia específica de una clase.",
            "traduccion": "Attribute belonging to a specific class instance."},
        "invalid_syntax": {
            "definicion": "Error causado por código escrito incorrectamente.",
            "traduccion": "Error caused by incorrectly written code."},
        "index_range": {
            "definicion": "Rango de índices en una colección o lista.",
            "traduccion": "Range of indices in a collection or list."},
        "inline_comment": {
            "definicion": "Comentario en la misma línea de código.",
            "traduccion": "Comment in the same line of code."},
        "integer_conversion": {
            "definicion": "Proceso de conversión de un valor a entero.",
            "traduccion": "Process of converting a value to integer."},
        "immediate_execution": {
            "definicion": "Ejecución directa de instrucciones en un programa.",
            "traduccion": "Direct execution of instructions in a program."},
        "i18n": {
            "definicion": "Abreviatura de internacionalización, adaptación a idiomas.",
            "traduccion": "Abbreviation for internationalization, language adaptation."},
        "integer_variable": {
            "definicion": "Variable que almacena un número entero.",
            "traduccion": "Variable that stores an integer."},
        "item_assignment": {
            "definicion": "Asignación de valor a un elemento específico.",
            "traduccion": "Assigning a value to a specific element."},
        "interactive_prompt": {
            "definicion": "Interfaz que permite ejecutar comandos directamente.",
            "traduccion": "Interface for executing commands directly."},
        "io_operations": {
            "definicion": "Operaciones de entrada/salida, como lectura y escritura.",
            "traduccion": "Input/output operations like reading and writing."},
        "isinstance_check": {
            "definicion": "Verificación si un objeto es de una clase específica.",
            "traduccion": "Checking if an object is of a specific class."},
        "iso_format": {
            "definicion": "Formato estándar ISO, por ejemplo en fechas.",
            "traduccion": "Standard ISO format, for example, in dates."},
        "import_error": {
            "definicion": "Error al intentar importar un módulo inexistente.",
            "traduccion": "Error when trying to import a non-existent module."},
        "itemgetter": {
            "definicion": "Función que obtiene un elemento de una colección.",
            "traduccion": "Function that gets an item from a collection."},
        "item_removal": {
            "definicion": "Eliminación de un elemento de una colección.",
            "traduccion": "Removal of an item from a collection."},
        "inverse_function": {
            "definicion": "Función que deshace el efecto de otra función.",
            "traduccion": "Function that undoes the effect of another function."},
        "inner_join": {
            "definicion": "Operación para combinar datos basados en un criterio común.",
            "traduccion": "Operation to combine data based on a common criterion."},
        "inference_engine": {
            "definicion": "Motor que deduce información a partir de reglas y datos.",
            "traduccion": "Engine that infers information from rules and data."},
        "index_retrieval": {
            "definicion": "Recuperación de índice de un elemento en una estructura.",
            "traduccion": "Retrieval of an element's index in a structure."},
        "initial_condition": {
            "definicion": "Condición inicial para comenzar un proceso.",
            "traduccion": "Initial condition to start a process."},
        "info_log": {
            "definicion": "Registro de información relevante en el sistema.",
            "traduccion": "Log of relevant information in the system."},
        "identity_check": {
            "definicion": "Verificación de si dos objetos son el mismo en memoria.",
            "traduccion": "Checks if two objects are the same in memory."},
        "iterator_protocol": {
            "definicion": "Conjunto de métodos para hacer un objeto iterable.",
            "traduccion": "Set of methods to make an object iterable."},
        "internal_server_error": {
            "definicion": "Error del servidor que impide ejecutar la solicitud.",
            "traduccion": "Server error preventing request execution."},
        "input_output_stream": {
            "definicion": "Flujo de datos para entrada y salida.",
            "traduccion": "Data stream for input and output."},
        "immutable_data": {
            "definicion": "Datos que no se pueden modificar después de su creación.",
            "traduccion": "Data that cannot be modified after creation."},
        "interpreter_loop": {
            "definicion": "Bucle principal que ejecuta comandos en el intérprete.",
            "traduccion": "Main loop executing commands in the interpreter."},
        "insert_method": {
            "definicion": "Método para agregar elementos en una posición específica.",
            "traduccion": "Method for adding elements at a specific position."},
        "index_error_handling": {
            "definicion": "Manejo de errores al acceder fuera del rango de índices.",
            "traduccion": "Handling errors when accessing out-of-range indices."},
        "inheritance_hierarchy": {
            "definicion": "Estructura jerárquica de clases heredadas.",
            "traduccion": "Hierarchical structure of inherited classes."},
        "image_processing_library": {
            "definicion": "Biblioteca con funciones para manipulación de imágenes.",
            "traduccion": "Library with functions for image manipulation."},
        "increment_operator": {
            "definicion": "Operador para aumentar el valor de una variable.",
            "traduccion": "Operator for increasing a variable's value."},
        "instance_checking": {
            "definicion": "Comprobación de si un objeto pertenece a una clase.",
            "traduccion": "Checking if an object belongs to a class."},
        "in_memory_database": {
            "definicion": "Base de datos que opera íntegramente en memoria.",
            "traduccion": "Database operating entirely in memory."},
        "interface_class": {
            "definicion": "Clase que define métodos comunes sin implementación.",
            "traduccion": "Class defining common methods without implementation."}},
    "j": {},

    "k": {},

    "l": {},

    "m": {},

    "n": {},
    
    "o": {},

    "p": {"pop": {"definicion": "Elimina y devuelve el último elemento de una lista.", "traduccion": "Removes and returns the last element of a list."}},

    "q": {},

    "r": {"reverse": {"definicion": "Invierte el orden de los elementos en una lista.", "traduccion": "Reverses the order of elements in a list."}},

    "s": {
        "sort": {"definicion": "Ordena los elementos de una lista en orden ascendente o descendente.", 
                 "traduccion": "Sorts the elements of a list in ascending or descending order."}, 
        "split": {"definicion": "Divide una cadena en una lista de subcadenas según un delimitador.", 
                  "traduccion": "Splits a string into a list of substrings based on a delimiter."}},

    "t": {},

    "u": {},

    "v": {},

    "w": {},

    "x": {},

    "y": {},
    
    "z": {
        "zscore": {
                "categoria": ("Estadística",),
                "definicion": "Función que calcula el valor z, que indica cuántas desviaciones estándar está un valor de la media.",
                "traduccion": "Function that calculates the z-score, which indicates how many standard deviations a value is from the mean."},
        "zoneinfo": {
                "categoria": ("Manejo de tiempo",),
                "definicion": "Módulo que proporciona soporte para zonas horarias en Python.",
                "traduccion": "Module that provides support for time zones in Python."},
        "zipfile": {
                "categoria": ("Manejo de archivos",),
                "definicion": "Módulo para crear, leer y modificar archivos ZIP.",
                "traduccion": "Module for creating, reading, and modifying ZIP files."},
        "zeta": {
                "categoria": ("Matemáticas",),
                "definicion": "Función matemática que involucra una serie infinita, generalmente utilizada en teoría de números.",
                "traduccion": "Mathematical function involving an infinite series, often used in number theory."},
        "zorder": {
                "categoria": ("Gráficos",),
                "definicion": "Propiedad que determina el orden de apilamiento de los objetos gráficos en un gráfico.",
                "traduccion": "Property that determines the stacking order of graphical objects in a plot."},
        "zfill": {
                "categoria": ("Manipulación de texto",),
                "definicion": "Método que completa una cadena con ceros hasta una longitud especificada.",
                "traduccion": "Method that pads a string with zeros to a specified length."},
        "zipapp": {
                "categoria": ("Herramientas",),
                "definicion": "Herramienta que permite empaquetar aplicaciones Python en archivos zip ejecutables.",
                "traduccion": "Tool that allows packing Python applications into executable zip files."},
        "zlib.decompress": {
                "categoria": ("Compresión de datos",),
                "definicion": "Función del módulo zlib que descomprime los datos previamente comprimidos.",
                "traduccion": "Function from the zlib module that decompresses data previously compressed."},
        "zlib.compress": {
                "categoria": ("Compresión de datos",),
                "definicion": "Función del módulo zlib que comprime datos en un formato específico.",
                "traduccion": "Function from the zlib module that compresses data into a specific format."},
        "zen_of_python": {
                "categoria": ("Buenas prácticas",),
                "definicion": "Conjunto de principios que guían el diseño y desarrollo de código Python claro y eficiente.",
                "traduccion": "Set of principles that guide the design and development of clear and efficient Python code."}}

}
