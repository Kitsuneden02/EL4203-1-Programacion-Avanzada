# Tarea 1 - Programación Avanzada (EL4203)

## Ejecución del código
Para obtener los resultados de esta tarea, sólo basta con ejecutar el script principal (**main.py**).

## Preguntas teóricas

### 1. ¿Qué es un paradigma de programación?
Un paradigma de programación es un enfoque o estilo en la forma en que se escribe y organiza el código. Estos paradigmas determinan cómo los programadores estructuran las soluciones a problemas. Los paradigmas más comunes son:
- **Programación estructurada**: Se basa en el uso de secuencias, bucles y estructuras condicionales.
- **Programación orientada a objetos (OOP)**: Utiliza objetos y clases como las unidades principales de programación.
- **Programación funcional**: Se centra en funciones y la inmutabilidad de los datos.

### 2. ¿En qué se basa la programación orientada a objetos?
Se basa en la idea de modelar el software utilizando objetos, que son instancias de clases. Estos objetos representan entidades del mundo real o del sistema que se está desarrollando, y tienen atributos (datos) y métodos (comportamientos). Los pilares de la OOP son:
- **Encapsulamiento**: Agrupar datos y funciones que operan sobre esos datos en un solo lugar.
- **Herencia**: Permite que una clase herede propiedades y comportamientos de otra.
- **Polimorfismo**: Las clases pueden redefinir o sobrescribir comportamientos heredados.
- **Abstracción**: Ocultar detalles internos y mostrar solo lo necesario para el uso del objeto.

### 3. ¿Cuál es la diferencia entre recursividad e iteración, y cómo se relaciona esto con la notación Big O?
- **Recursividad**: La función se llama a sí misma para resolver subproblemas. Se utiliza cuando un problema puede descomponerse en problemas más pequeños de la misma naturaleza.
- **Iteración**: En la iteración se repite un conjunto de instrucciones mediante bucles hasta que se cumple una condición.
En cuanto a la **notación Big O**, la diferencia clave radica en la complejidad:
- La **recursividad** puede tener una mayor complejidad debido a las múltiples llamadas a funciones y a la pila de llamadas.
- La **iteración** generalmente es más eficiente en cuanto a consumo de memoria, aunque su complejidad depende de cuántas veces se ejecuta el bucle.

### 4. Explicar la diferencia de rendimiento entre O(1) y O(n)
- **O(1)**: Se refiere a una complejidad constante, es decir, el tiempo de ejecución del algoritmo es independiente del tamaño del input. Un ejemplo típico es acceder a un elemento en una lista por su índice.
- **O(n)**: Se refiere a una complejidad lineal, lo que significa que el tiempo de ejecución crece proporcionalmente al tamaño del input. Un ejemplo es recorrer una lista con un bucle for.

En general, los algoritmos O(1) son más rápidos que los O(n) porque no dependen del tamaño de los datos, mientras que los O(n) deben recorrer todos los elementos de la entrada.

### 5. ¿Cómo se calcula el orden en un programa que funciona por etapas?
Cuando un programa tiene varias etapas o pasos secuenciales, la complejidad total se calcula sumando las complejidades de cada etapa. Si las etapas se ejecutan en paralelo o en secuencia, la complejidad general será dominada por la etapa más costosa. Por ejemplo, si un algoritmo tiene tres pasos con complejidades O(n), O(log n) y O(n²), la complejidad total será O(n²), ya que es la operación más costosa.

### 6. ¿Cómo se puede determinar la complejidad temporal de un algoritmo recursivo?
La complejidad temporal de un algoritmo recursivo se puede determinar utilizando una **relación de recurrencia**, que describe el número de operaciones en función del tamaño del problema. Luego, se resuelve esta relación para obtener la complejidad total. Un ejemplo común es el algoritmo de **divide y vencerás**, donde se descompone un problema en subproblemas más pequeños. En algunos casos, se puede utilizar el **Teorema Maestro** para resolver la recurrencia y encontrar la complejidad.

---

