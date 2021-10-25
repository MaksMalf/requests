import requests
from pprint import pprint
from requests.api import request


TOKEN = 'AQAAAAAhmoJiAADLWzad0hVEZU6QjKbqkFrb5NQ'


class YandexDisk:

  
    def __init__(self, token):
        self.token = token


    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f"OAuth {self.token}"
        }


    def get_file_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url=files_url, headers=headers)
        return response.json()


    def get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()


    def upload_file_to_disk(self, disk_file_path, filename):
        url = self.get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(url=url, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

 
if __name__ == '__main__':
    disk = YandexDisk(token=TOKEN)
    disk.upload_file_to_disk('test/Home_Works.txt', 'Home_Works.txt')

