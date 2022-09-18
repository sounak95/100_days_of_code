
class Laptop():
    def code(self, ide):
        ide.execute()

class Pycharm:
    def execute(self):
        print('Pycharm executing')

class MyEditor:
    def execute(self):
        print('MyEditor executing')


lp = Laptop()
lp.code(Pycharm())
lp.code(MyEditor())