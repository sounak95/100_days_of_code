
class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if not Singleton.__instance :
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance:
            raise Exception("Object exists already")
        Singleton.__instance = self



s3 = Singleton()
print(s3)
s1 = Singleton.get_instance()
print(s1)
s2 = Singleton.get_instance()
print(s2)
