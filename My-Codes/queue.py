rear_pointer = -1
front_pointer = 0
queue = [None] * 10
queue_length = 0
queue_full = 10
item = 0


def enqueue(item):
  global rear_pointer, item, queue_full, queue_length
  if queue_length < queue_full:
    if rear_pointer < queue_full - 1:
      rear_pointer += 1
    else:
      rear_pointer = 0

    queue[rear_pointer] = item
    queue_length += 1
  else:
    print("Queue is full")
