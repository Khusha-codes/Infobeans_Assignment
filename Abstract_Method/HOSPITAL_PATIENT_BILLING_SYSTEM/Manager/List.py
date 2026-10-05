class Record:
    def __init__(self):
        self.list = []

    def add(self,obj):
        self.list.append(obj)

    def find(self,id):
        for obj in self.list:
            if obj.id == id:
                return obj
