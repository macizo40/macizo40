#recibir un evento de payload, crear una class para filtrar los elementos importantes, iterar sobre los elementos de esa clase y dependendiiendo el tipo de evento tomar accion
class Source:
     def __init__(self,message,string_to_find) -> None:
        self.message = message
        self.string_to_find = string_to_find
     def search(self) -> None:
        self._search()
        print('Searching')
     def insert(self) -> None:
        self._insert()
        print('Inserting')