import collections
import threading
import time

class CommandQueue:
    def __init__(self):
        self.queue = collections.deque()
        self.lock = threading.Lock()

    def enqueue(self, command):
        with self.lock:
            self.queue.append(command)

    def dequeue(self):
        with self.lock:
            if self.is_empty():
                return None
            return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

class RobotController:
    def __init__(self):
        self.command_queue = CommandQueue()
        self.thread = threading.Thread(target=self.process_commands, daemon=True)
        self.thread.start()

    def process_commands(self):
        while True:
            command = self.command_queue.dequeue()
            if command:
                self.execute_command(command)
            else:
                time.sleep(0.5)  # Giảm tải thời gian nhận lệnh

    def execute_command(self, command):
        if command == "forward":
            print("Robot đang tiến lên.")
        elif command == "backward":
            print("Robot đang lùi lại.")
        elif command == "right":
            print("Robot đang quay phải.")
        elif command == "left":
            print("Robot đang quay trái.")
        elif command == "stop":
            print("Robot đã dừng lại.")
        else:
            print(f"Lệnh không hợp lệ: {command}")

# Mã chính
def main():
    controller = RobotController()
    command_queue = controller.command_queue

    # Thêm lệnh vào hàng đợi
    commands = ["forward", "left", "backward", "stop"]
    for cmd in commands:
        command_queue.enqueue(cmd)
        time.sleep(1)  # Giả lập thời gian thực thi lệnh

    # Giữ chương trình chạy để xem quá trình thực thi lệnh
    time.sleep(15)

if __name__ == "__main__":
    main()