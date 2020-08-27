#!/usr/bin/env python
# coding: utf-8

# In[2]:


# COMPUTACIÓN BLANDA - Sistemas y Computación
# -------------------------------------------
# Introducción a numpy
# -------------------------------------------
# Lección 01
# ** Creación de arrays
# ** Acceso a los arrays
# ** Manejo de rangos
# ** Modificación de arrays
# -------------------------------------------


# In[5]:


#Importar libreria numpy 
import numpy as np 
#crear un arreglo de 6 elementos
a = np.arange(6)
#imprimir el contenido del arreglo
print('Arreglo a = ', a, '\n')
#se muestra los tipo de elemento del arreglo
print('tipo de a = ', a.dtype, '\n' )
#se muenstra la dimension del arreglo
print('Dimension de a = ', a.ndim, '\n')
#muestra el numero de elementos en el arreglo
print('Numero de elementos de a = ', a.shape)


# In[7]:


m = np.array([np.arange(3),np.arange(3)])
print(m)


# In[8]:


a = np.array ([[1,2],[3,4]])
print('a = \n', a, '\n')

print('a[0,0] =', a[0,0], '\n')
print('a[0,1] =', a[0,1], '\n')
print('a[1,0] =', a[1,0], '\n')
print('a[1,1] =', a[1,1])


# In[12]:


# Crea un array con 9 elementos, desde 0 hasta 8
a = np.arange(9)
print('arreglo a =', a, '\n')
# Muestra los elementos desde 0 hasta 9. Imprime desde 0 hasta 8
print('a[0:9] = ', a[0:9], '\n')
# Muestra desde 3 hasta 7. Imprime desde 3 hasta 6
print('a[3,7] = ', a[3:7])


# In[16]:


# Mostrando todos los elementos, desde el 0 hasta el 8, de uno en uno
print('a[0:9:1] =', a[0:9:1], '\n')
# El mismo ejemplo, pero omitiendo el número 0 al principio, el cual no es necesario aquí
print('a[:9:1] =', a[:9:1], '\n')
# Mostrando los números, de dos en dos
print('a[0:9:2] =', a[0:9:2],'\n')
# Mostrando los números, de tres en tres
print('a[0:9:3] =', a[0:9:3])


# In[22]:


# Si utilizamos un incremento negativo, el array se muestra en orden inverso
# El problema es que no muestra el valor 0
print('a[0:9:-1] =', a[9:0:-1])
# Si se omiten los valores de índice, el resultado es preciso
print('a[0::-1] =', a[::-1])


# In[27]:


# Utilización de arreglos multidimensionales
b = np.arange(24).reshape(2,3,4)
print('b =\n', b)


# In[29]:


# Acceso individual a los elementos del array
# Elemento en el bloque 1, fila 2, columna 3
print('b[1,2,3] =', b[1,2,3])
# Elemento en el bloque 0, fila 2, columna 2
print('b[0,2,2] =', b[0,2,2])
# Elemento en el bloque 0, fila 1, columna 1
print('b[0,1,1] =', b[0,1,1])


# In[31]:


#elegir componente bloque 0,fila 0,columna 0
print('b[0,0,0] =', b[0,0,0], '\n')
#elegir componente bloque 1,fila 0,columna 0
print('b[1,0,0] =', b[1,0,0], '\n')
#elegir componente bloque 0,fila 0,columna 0 y componente bloque 1,fila 0,columna 0 SIMULTANEAMENTE
print('b[:,0,0] =', b[:,0,0],)


# In[39]:


#elegir el primer bloque
print('b[0] =',b[0],'\n' )
#tambien puede ser 
print('b[0,:,:] =',b[0,:,:],'\n')
#otra opcion es. solo si se utiliza la notación de : a derecha o a izquierda,
print('b[0,...] =',b[0,...],'\n')
#elegir el segundo bloque
print('b[1] =',b[1],'\n')
#tambien puede ser 
print('b[1,:,:] =',b[1,:,:], '\n')
#otra opcion es. solo si se utiliza la notación de : a derecha o a izquierda,
print('b[1,...] =',b[1,...],'\n')


# In[40]:


# Si queremos la fila 1 en el bloque 0 (sin que importen las columnas)
print('b[0,1] =', b[0,1])


# In[42]:


#Podemos asignar la fila 1 en el bloque 0 a la variable z
z=b[0,1]
print('z =',z)
#Tomaremos a z de 2 en 2
print('z[::2] =', z[::2])


# In[43]:


#podemos hacer el ejercicio anterior en una sola expresion
print('b[0,1,::2] =', b[0,1,::2])


# In[44]:


# Imprime todas las columnas, independientemente de los bloques y filas
print('b[:,:,1] =\n', b[:,:,1], '\n')
# Variante de notación (simplificada)
print('b[...,1] =\n', b[...,1], '\n')


# In[46]:


# Si queremos seleccionar todas las filas 2, independientemente de los bloques y columnas, se tiene:
print('b[:,1] =\n', b[:,1])


# In[47]:


#No es necesario poner la fila
#seleccionar columna 1 del bloque 0
#        b,f,c 
print('b[0,:,1] =', b[0,:,1])
#seleccionar columna 1 del bloque 1
#        b,f,c
print('b[1,:,1] =', b[1,:,1])


# In[58]:


# Si queremos seleccionar la última columna del primer bloque, tenemos:
print('b[0,:,-1] =', b[0,:,-1],'\n')
#si quisieramos que Los valores de la fila estuvieran en orden inverso, ejecutaríamos la instrucción
print('b[0,::-1,-1] =', b[0,::-1,-1],'\n')
# Si quisieramos imprimir sus valores de 2 en 2, tendríamos:
print('b[0,::2,-1] =',b[0,::2,-1])


# In[60]:


#podemos invertir los bloque con:
print('b[::-1] =\n', b[::-1])


# In[61]:


# La instrucción: ravel(), de-construye el efecto de la instrucción reshape se generara un vector a partir de la matriz
print('Matriz b =\n', b, '\n--------------------------\n')
print('Vector b = \n', b.ravel())


# In[62]:


# La instrucción: flatten() es similar a ravel() La diferencia es que flatten genera un nuevo espacio de memoria
print('Vector b con flatten =\n', b.flatten())


# In[63]:


# Se puede cambiar la estructura de una matriz con la instrucción: shape 
#Transformamos la matriz en 6 filas x 4 columnas sin usar bloques separados
b.shape = (6,4)
print('b(6x4) =\n', b)


# In[65]:


# A partir de la matriz que acaba de ser generada, vamos a mostrar como se construye la transpuesta de la matriz con transpose
print('Transpuesta de b =\n', b.transpose())


# In[67]:


#La instruccion resize es similar a reshape La diferencia está en que resize altera la estructura del array
#En cambio reshape crea una copia del original
#se cambia la estructura del array, tendra 2 filas 12 columnas
b.resize([2,12])
print('b = \n',b)

