from collections import deque
import threading
import random
import time

class Sensor:
    def __init__(self, id, print_queue):
        self.id = id
        self.print_queue = print_queue

    def send_data(self):
        while True:
            # Tạo dữ liệu ngẫu nhiên
            data = random.randint(1, 100)
            self.print_queue.enqueue(data)
            time.sleep(random.uniform(0.5, 2))  # Giới hạn thời gian ngẫu nhiên

class PrintQueue:
    def __init__(self):
        self.queue = deque()
        self.lock = threading.Lock()

    def enqueue(self, data):
        with self.lock:
            self.queue.append(data)

    def process_queue(self):
        while True:
            with self.lock:
                if self.queue:
                    data = self.queue.popleft()
                    print(f"Đang xử lý dữ liệu: {data}")
            time.sleep(1)  # Giới hạn thời gian giữa các lần xử lý

# Minh họa
print_queue = PrintQueue()
# Khởi động thread xử lý hàng đợi
processor = threading.Thread(target=print_queue.process_queue, daemon=True)
processor.start()

# Tạo và khởi động các cảm biến
sensors = [Sensor(i, print_queue) for i in range(1, 5)]
for sensor in sensors:
    t = threading.Thread(target=sensor.send_data, daemon=True)
    t.start()

# Giữ chương trình chạy
while True:
    time.sleep(10)

if __name__ == "__main__":
    main()