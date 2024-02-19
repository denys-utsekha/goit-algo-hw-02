from queue import Queue
import uuid
import time

queue = Queue()

def generate_request():
  id = uuid.uuid1()
  new_request = { id }
  queue.put(new_request)
  print(f"Згенеровано нову за'явку id: {id}")
  time.sleep(1)

def process_request():
  while not queue.empty():
    request_from_queue = queue.get()
    print(f"Оброблено за'явку id: {request_from_queue}")
    time.sleep(1)
  print("Заявок немає.")

try:
  while True:
    generate_request()
    generate_request()
    generate_request()
    process_request()
except KeyboardInterrupt:
  print("Stopped")
