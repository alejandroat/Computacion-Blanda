#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Se importa la librería numpy
import numpy as np
# APILAMIENTO
# -----------
# APILADO
# Las matrices se pueden apilar horizontalmente, en profundidad o verticalmente. Podemos utilizar, para ese propósito,
# las funciones vstack, dstack, hstack, column_stack, row_stack y concatenate. Para empezar, vamos a crear dos arrays
# Matriz a 9 elementos 3 filas 3 columnas
a = np.arange(9).reshape(3,3)
print('a =\n', a, '\n')
# Matriz b, creada a partir de la matriz a
b = a*2
print('b =\n', b)
# Utilizaremos estas dos matrices para mostrar los mecanismos de apilamiento disponibles


# In[14]:


# APILAMIENTO HORIZONTAL
# Matrices origen
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento horizontal con hstack
print('Apilamiento horizontal =\n', np.hstack((a,b)) )


# In[15]:


# APILAMIENTO HORIZONTAL - Variante
# Utilización de la función: concatenate()
# Matrices origen
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento horizontal con concatenate
print( 'Apilamiento horizontal con concatenate = \n', np.concatenate((a,b), axis=1) )
# Si axis=1, el apilamiento es horizontal


# In[16]:


# APILAMIENTO VERTICAL
# Matrices origen
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento vertical con vstack
print( 'Apilamiento vertical =\n', np.vstack((a,b)) )


# In[17]:


# APILAMIENTO VERTICAL - Variante
# Utilización de la función: concatenate()
# Matrices origen
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento vertical con concatenate
print( 'Apilamiento vertical con concatenate =\n',
np.concatenate((a,b), axis=0) )
# Si axis=0, el apilamiento es vertical


# In[18]:


# APILAMIENTO EN PROFUNDIDAD

# En el apilamiento en profundidad, se crean bloques utilizando
# parejas de datos tomados de las dos matrices
# Matrices origen
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento en profundidad con dstack
print( 'Apilamiento en profundidad =\n', np.dstack((a,b)) )


# In[19]:


# APILAMIENTO POR COLUMNAS
# El apilamiento por columnas es similar a hstack() Se apilan las columnas,
#de izquierda a derecha, y tomándolas de los bloques definidos en la matriz
# Matrices origen
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento vertical con column_stack
print( 'Apilamiento por columnas =\n',np.column_stack((a,b)) )


# In[20]:


# APILAMIENTO POR FILAS
# El apilamiento por fila es similar a vstack() Se apilan las filas, de arriba hacia abajo, y tomándolas
# de los bloques definidos en la matriz
# Matrices origen
print('a =\n', a, '\n')
print('b =\n', b, '\n')
# Apilamiento vertical con row_stack
print( 'Apilamiento por filas =\n', np.row_stack((a,b)) )


# In[23]:


# DIVISIÓN DE ARRAYS
# DIVISIÓN HORIZONTAL
print(a, '\n')
# El código resultante divide una matriz a lo largo de su eje horizontal en tres piezas del mismo tamaño y forma:con hsplit
print('Array con división horizontal =\n', np.hsplit(a, 3), '\n')
# El mismo efecto se consigue con split() y utilizando una bandera a 1
print('Array con división horizontal, uso de split() =\n', np.split(a, 3, axis=1))


# In[24]:


# DIVISIÓN VERTICAL
print(a, '\n')
# La función vsplit divide el array a lo largo del eje vertical:
print('División Vertical = \n', np.vsplit(a, 3), '\n')
# El mismo efecto se consigue con split() y utilizando una bandera a 0
print('Array con división vertical, uso de split() =\n', np.split(a, 3, axis=0))


# In[27]:


# DIVISIÓN EN PROFUNDIDAD
# La función dsplit, como era de esperarse, realiza división en profundidad dentro del array
# Para ilustrar con un ejemplo, utilizaremos una matriz de rango tres
c = np.arange(27).reshape(3, 3, 3)
print(c, '\n')
# Se realiza la división
print('División en profundidad =\n', np.dsplit(c,3), '\n')


# In[32]:


# PROPIEDADES DE LOS ARRAYS
# El atributo ndim calcula el número de dimensiones
print(b, '\n')
print('Numero de dimensiones con ndim: ', b.ndim)
print(c, '\n')
print('Numero de dimensiones con ndim: ', c.ndim)


# In[33]:


# El atributo size calcula el número de elementos
print(b, '\n')
print('Numero de elementos con size: ', b.size)
print(c, '\n')
print('Numero de elementos con size: ', c.size)


# In[36]:


# El atributo itemsize obtiene el número de bytes por cada
# elemento en el array
print('itemsize: ', b.itemsize)


# In[37]:


# El atributo nbytes calcula el número total de bytes del array
print(b, '\n')
print('nbytes: ', b.nbytes, '\n')
# Es equivalente a la siguiente operación
print('nbytes equivalente: ', b.size * b.itemsize)


# In[39]:


# El atributo T tiene el mismo efecto que la transpuesta de la matriz
#Llenamos la matriz b para consegir 6 filas, 4 columnas con la instruccion resize
b.resize(6,4)
print(b, '\n')
print('Transpuesta: \n', b.T)


# In[40]:


# Los números complejos en numpy se representan con j
#El array b se llena con numeros complejso
b = np.array([1.j + 1, 2.j + 3])
print('Complejo: \n', b)


# In[41]:


# El atributo real nos da la parte real del array,o el array en sí mismo si solo contiene números reales
print('real: ', b.real, '\n')
# El atributo imag contiene la parte imaginaria del array
print('imaginario: ', b.imag)


# In[43]:


# Si el array contiene números complejos, entonces el tipo de dato se convierte automáticamente a complejo
print(b.dtype)
#Si el array no contiene números complejos, mantiene el tipo de dato a entero
print(a.dtype)


# In[46]:


# El atributo flat devuelve un objeto numpy.flatiter. Esta es la única forma de adquirir un flatiter:
# no tenemos acceso a un constructor de flatiter. El apartamento El iterador nos permite recorrer una matriz
# como si fuera una matriz plana, como se muestra a continuación:
# En el siguiente ejemplo se clarifica este concepto
b = np.arange(4).reshape(2,2)
print(b, '\n')
f = b.flat
print(f, '\n')
# Ciclo que itera a lo largo de f
for item in f: print (item)
# Selección de un elemento
print('\n')
print('Elemento 2:\n ', b.flat[2])
# Operaciones directas con flat
b.flat = 7
print(b, '\n')
b.flat[[1,3]] = 1
print(b, '\n')


# In[ ]:




