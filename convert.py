import json
import psycopg2

#recibir un evento de payload, crear una class para filtrar los elementos importantes, iterar sobre los elementos de esa clase y dependendiiendo el tipo de evento tomar accion
class DBConnection:
   def __init__(self,database,host,user,password,port) -> None:
      self.database = database
      self.host = host
      self.user = user
      self.password = password
      self.port = port
      self.conn = None
      self.get_connection()
     
   #connection sinlgenton  
   def get_connection(self) -> None:
      if self.conn == None:
         self.conn = psycopg2.connect(database=self.database,
                        host=self.host,
                        user=self.user,
                        password=self.password,
                        port=self.port)
         print('Connected')
      
      return self.conn
         

   def insert(self,nombre,tabla) -> None:
      cursor = self.conn.cursor()
      cursor.execute(f"INSERT INTO {tabla}(name) VALUES('{nombre}')")
      self.conn.commit()  # Commit the transaction
      print('Inserted')
   
   def delete(self,id,tabla) -> None:
      cursor = self.conn.cursor()
      cursor.execute(f"DELETE from {tabla} WHERE id={id}")
      self.conn.commit()  # Commit the transaction
      print('Deleted')
   
   def select(self,id,tabla) -> None:
      cursor = self.conn.cursor()
      cursor.execute(f"SELECT name FROM {tabla} WHERE id={id}")
      print('Selected')
      fila = cursor.fetchone()
      if fila: #si fila tiene algo si pasa, por que si no retorna false
         return fila[0]
      else:
         return None 





# Opening JSON file
with open('events.json') as json_file:
   data = json.load(json_file)

db = DBConnection('postgres','127.0.0.1','admin','admin',50505)
#db.insert('Macizo', 'empleados')
#db.delete(3, 'empleados')

for evento in data['events']:
   if evento['type'] == 'create':
      #tabla de valor empleado
      tabla = evento['table']
      for fila in evento['data'][tabla]:
         empleado = db.insert(fila['name'],tabla)
         print(empleado)
   elif evento['type'] == 'select':
      #tabla de valer empleado
      tabla = evento['table']
      for fila in evento['data'][tabla]:
         empleado = db.select(fila['id'],tabla)
         print(empleado)
   elif evento['type'] == 'delete':
      #tabla de valer empleado
      tabla = evento['table']
      for fila in evento['data'][tabla]:
         empleado = db.delete(fila['id'],tabla)
         print(empleado)