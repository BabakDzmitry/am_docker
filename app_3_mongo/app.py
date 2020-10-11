from uuid import uuid4
from pathlib import Path
import sys
import os

main_path = Path(__file__).resolve().parent
sys.path.insert(0, main_path)
from storage import MongodbService


def main():
    ip = '192.168.0.50'
    if os.getenv('ip'):
        ip = os.getenv('ip')
    print(f'{ip}')
    storage_ = MongodbService.get_instance(ip=ip)
    for _ in range(5):
        dto = {
            "_id": str(uuid4()),
            "payload": str(uuid4()),
        }
        storage_.save_data(dto)

    for data in storage_.get_data():
        print(data)


if __name__ == '__main__':
    main()
