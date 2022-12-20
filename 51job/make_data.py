from db import MongoFunc
from bs4 import BeautifulSoup,SoupStrainer
import json

mongodb = MongoFunc()

def run():
    while True:
        try:
            json_data = {}

            now_index = mongodb.get_loaded_data_index()+1
            html_content = mongodb.get_page_content(now_index)

            only_body = SoupStrainer('body')
            soup = BeautifulSoup(html_content,'lxml',parse_only=only_body)
            script_tags_list = soup.find_all('script')
            for script_tag in script_tags_list:
                if 'SEARCH_RESULT' in script_tag.text:

                    json_content = script_tag.text
                    json_content = json_content.replace('\n','')
                    json_content = json_content.replace('window.__SEARCH_RESULT__ =','')
                    json_data = json.loads(json_content)

                    break

            mongodb.insert_data_json({"_id":now_index,"jobs":json_data['engine_jds']},now_index)
        except TypeError:
            print('ALL DONE')
            break
if __name__ == '__main__':
    run()
