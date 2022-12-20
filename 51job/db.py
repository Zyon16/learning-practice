import pymongo.errors
from pymongo import MongoClient


class MongoFunc:
    def __init__(self, max_pages=200):
        self.client = MongoClient(host='127.0.0.1', port=27018)
        self.db = self.client['51job']
        # FOR HTML INSERT
        self.statuc_c = self.db['pages_load_status']
        self.html_c = self.db['pages']

        # FOR JSON MAKER
        self.json_stats_c = self.db['data_status']
        self.json_c = self.db['data']

        self.INIT_MAX_PAGES = max_pages
        self.__check_init()

    def __check_init(self):
        now_pages_status = self.statuc_c.find_one()
        if not now_pages_status['unloaded'] and not now_pages_status['loaded']:
            self.statuc_c.update_one(now_pages_status, {'$set': {'unloaded': [i for i in range(1, 201)]}})

    def update_to_loaded(self, index: int):
        now_pages_status = self.statuc_c.find_one()
        unloaded = now_pages_status['unloaded'].copy()
        loaded = now_pages_status['loaded'].copy()

        unloaded.remove(index)
        loaded.append(index)
        loaded.sort()

        self.statuc_c.update_many(now_pages_status, {'$set': {'unloaded': unloaded, 'loaded': loaded}})

    def get_next_index(self) -> int:
        now_pages_status = self.statuc_c.find_one()
        unloaded = now_pages_status['unloaded']
        try:
            return unloaded[0]
        except IndexError:
            return 0

    def insert_html(self, content: str, index: int):
        try:
            self.html_c.insert_one({"_id": index, "content": content})
            self.update_to_loaded(index)
        except pymongo.errors.DuplicateKeyError:
            # 此ID重复，即PAGE重复
            self.update_to_loaded(index)

    def update_data_index(self, index: int):
        loaded_index = self.json_stats_c.find_one()
        self.json_stats_c.update_one(loaded_index, {"$set":{"loaded_index": index}})

    def get_loaded_data_index(self) -> int:
        loaded_index = self.json_stats_c.find_one()
        return loaded_index['loaded_index']

    def get_page_content(self,page_id:int) -> str:
        page_json = self.html_c.find_one({"_id":page_id})

        return page_json['content']

    def insert_data_json(self,info:dict,index:int) -> None:
        try:
            self.json_c.insert_one(info)
            self.update_data_index(index)
        except pymongo.errors.DuplicateKeyError:
            # 重复
            self.update_data_index(index)
