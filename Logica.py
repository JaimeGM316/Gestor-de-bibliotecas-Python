import mysql.connector


def mostrarTodo():
   conexion = mysql.connector.connect(
   host="localhost",
   user="root",
   password="root",
   database="biblioteca"
   )
   cursor = conexion.cursor()

   cursor.execute("SELECT * FROM libro")

   usuarios = cursor.fetchall()


   print("---------------------------------------------------------")  
   for usuario in usuarios:
      print(usuario)

   conexion.close()

def insertar():

   id = input('Introduce el ID: ')
   titulo = input('Introduce el titulo: ')
   autor = input('Introduce el autor: ')
   editorial = input('Introduce la editorial: ')
   copias = input('Introduce las copias: ')
   paginas = input('Introduce las paginas: ')

   conexion = mysql.connector.connect(
   host="localhost",
   user="root",
   password="root",
   database="biblioteca"
   )
   cursor = conexion.cursor()

   sql = "INSERT INTO libro (id, titulo, autor, editorial, paginas, copias) VALUES (%s, %s, %s, %s, %s, %s)"
   val = (id,titulo, autor, editorial, copias, paginas)
   cursor.execute(sql, val)

   conexion.commit()

   conexion.close()

def eliminar():

   id = input('Introduce el ID: ')

   conexion = mysql.connector.connect(
   host="localhost",
   user="root",
   password="root",
   database="biblioteca"
   )
   cursor = conexion.cursor()

   sql = "DELETE FROM libro WHERE id = %s"
   val = (id,)
   cursor.execute(sql, val)

   conexion.commit()

   conexion.close()

def actualizarCopias():

   id = input('Introduce el ID: ')
   copias = input('Introduce las copias: ')

   conexion = mysql.connector.connect(
   host="localhost",
   user="root",
   password="root",
   database="biblioteca"
   )
   cursor = conexion.cursor()

   sql = "UPDATE libro SET copias = %s WHERE id = %s"
   val = (copias,id)
   cursor.execute(sql, val)

   conexion.commit()

   conexion.close()

def ordenarAutor():

   conexion = mysql.connector.connect(
   host="localhost",
   user="root",
   password="root",
   database="biblioteca"
   )
   cursor = conexion.cursor()

   cursor.execute("SELECT * FROM libro ORDER BY autor")
   usuarios = cursor.fetchall()

   print("---------------------------------------------------------")  
   for usuario in usuarios:
      print(usuario)

   conexion.close()

def ordenarTitulo():

   conexion = mysql.connector.connect(
   host="localhost",
   user="root",
   password="root",
   database="biblioteca"
   )
   cursor = conexion.cursor()

   cursor.execute("SELECT * FROM libro ORDER BY titulo")
   usuarios = cursor.fetchall()

   print("---------------------------------------------------------")  
   for usuario in usuarios:
      print(usuario)

   conexion.close()

def ordenarEditorial():

   conexion = mysql.connector.connect(
   host="localhost",
   user="root",
   password="root",
   database="biblioteca"
   )
   cursor = conexion.cursor()

   cursor.execute("SELECT * FROM libro ORDER BY editorial")
   usuarios = cursor.fetchall()

   print("---------------------------------------------------------")  
   for usuario in usuarios:
      print(usuario)

   conexion.close()

