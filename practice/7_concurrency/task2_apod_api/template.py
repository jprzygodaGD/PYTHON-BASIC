import requests
import os
import datetime
import queue
from threading import Thread, Event

API_KEY = "L5ey8AkzCMooSJGgyY3VW3kiwFFesJGEbYrSg1N4"
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'


def get_apod_metadata_producer(buffer, event, start_date: str, end_date: str, api_key: str):

    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&start_date={start_date}&end_date={end_date}'
    response = requests.get(url)
    for data in response.json():
        if data['media_type'] == 'image':
            buffer.put(data['hdurl'])
    event.set()


def download_apod_images_consumer(buffer, event, ident):

    while not event.is_set() or not buffer.empty():
        item = buffer.get()
        file_name = str(item).split('/')[-1].split('.')[0]
        with open(f'{OUTPUT_IMAGES}/{file_name}.jpg', 'wb') as handler:
            img_data = requests.get(item)
            handler.write(img_data.content)


def main():
    if not os.path.exists(OUTPUT_IMAGES):
        os.makedirs(OUTPUT_IMAGES)

    q = queue.Queue()
    event = Event()
    producer_thread = Thread(target=get_apod_metadata_producer, args=(q, event, '2021-08-01', '2021-09-30', API_KEY))
    consumer_threads = [Thread(target=download_apod_images_consumer, args=(q, event, ident)) for ident in range(54)]
    for consumer in consumer_threads:
        consumer.start()
    producer_thread.start()
    producer_thread.join()
    for consumer in consumer_threads:
        consumer.join()


if __name__ == '__main__':
    # Sequentially code took: 3 min 11 sec
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now() - start
    print(end)
