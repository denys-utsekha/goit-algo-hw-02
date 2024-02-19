from queue import Queue
import uuid

queue = Queue()

def generate_request():
  for i in range(5):
    new_request = { id: uuid.uuid1() }
    queue.put(new_request)

def process_request():
  while not queue.empty():
    request_from_queue = queue.get()  
  print("Queue is empty!")

while True:
  generate_request()
  process_request()
