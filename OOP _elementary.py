#Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). В этом классе реализуйте метод show_my_drink(), выводящий на печать Газировка и {ДОБАВКА} в случае наличия добавки, а иначе отобразится следующая фраза: Обычная газировка

class Soda:
        def __init__(self,  dob):
                if isinstance(dob, str):
                        self.dob = dob
                else:
                        self.dob = None
        def show_my_drink(self):
                if self.dob:
                        print('газировка и ', self.dob)
                else:
                        print('газировка')
			
a = Soda('sahar')
a.show_my_drink()
b = Soda(1)
b.show_my_drink()
			
