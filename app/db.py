import json

class DB:
    def __init__(self):
        self.db = self.__init_db__()
        
    def __init_db__(self):
        with open('./app/db/interviews.json', 'r', encoding='utf-8') as f:
            db = json.load(f)
            return db

    def get_entity(self, id):
        for entity in self.db:
            if entity.get('id') == id:
                return entity

