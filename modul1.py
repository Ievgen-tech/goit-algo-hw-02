"""Програма, яка імітує приймання й обробку заявок.

Програма автоматично генерує нові заявки (з унікальним ID),
додає їх до черги (Queue),  потім послідовно обробляє,
імітуючи роботу сервісного центру.
"""

from queue import Queue
from itertools import count
from random import randint
from time import sleep


# Queue for incoming requests.
request_queue = Queue()
request_id_counter = count(1)


def generate_request() -> None:
    """Generate a new request and add it to the queue."""
    request = {
        "id": next(request_id_counter),
        "client": f"Client-{randint(100, 999)}",
    }
    request_queue.put(request)
    print(f"Created request #{request['id']} from {request['client']}")


def process_request() -> None:
    """Process one request from the queue if available."""
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processed request #{request['id']} from {request['client']}")
    else:
        print("Queue is empty")


def main() -> None:
    """Main loop for continuous request generation and processing."""
    print("Request processing service started. Press Ctrl+C to stop.")
    try:
        while True:
            # Generate 0-2 new requests each cycle.
            for _ in range(randint(0, 2)):
                generate_request()

            process_request()
            sleep(1)
    except KeyboardInterrupt:
        print("\nService stopped by user.")


if __name__ == "__main__":
    main()
