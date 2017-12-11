import os
from urllib.request import urlretrieve
import gzip
import json


class CityList:
    def __init__(self, url):
        self.url = url
        self._get_file_name_gz()
        self._get_file_name_json()
        self.city_list = {}
        self._create()

    def _create(self):
        # проверяем, есть ли файл или архив с городами
        if os.path.isfile(self.json_file):
            self._get_city_list()
        elif os.path.isfile(self.gz_file):
            self._gunzip_sity_list()
        else:
            self._download_sity_list()
            self._gunzip_sity_list()


    def _get_file_name_gz(self):
        self.gz_file = self.url.split("/")[-1]

    def _get_file_name_json(self):
        last_pos = self.gz_file.rfind(".")
        self.json_file = self.gz_file[:last_pos]

    def _download_sity_list(self):
        print("Загружаю архив со списком городов.")
        urlretrieve(self.url, self.gz_file)
        print("Список загружен. '{}'".format(self.gz_file))

    def _gunzip_sity_list(self):
        print("Читаю содежримое архива '{}'".format(self.gz_file))
        with gzip.open(self.gz_file, 'rb') as gz:
            file_content = gz.read()

        with open(self.json_file, 'wb') as json:
            json.write(file_content)

        print("Записываю прочитанную информацию в файл '{}'".format(self.json_file))

    def _get_city_list(self):
        with open(self.json_file, 'r', encoding="UTF-8") as f:
            self.city_list = json.loads(f.read())

    def get_sity_id(self, city_name):
        city_id=[]
        for cn in city_name:
            for cl in self.city_list:
                if cl['name'] == cn:
                    city_id.append(cl['id'])
        return city_id
