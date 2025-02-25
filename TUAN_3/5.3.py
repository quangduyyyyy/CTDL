class Robot:
    def __init__(self):
        self.position = [0, 0]  # Vị trí ban đầu
        self.direction = 'N'     # Hướng ban đầu
        self.history = []        # Lịch sử hoạt động

    def move_forward(self):
        if self.direction == 'N':
            self.position[1] += 1
        elif self.direction == 'E':
            self.position[0] += 1
        elif self.direction == 'S':
            self.position[1] -= 1
        elif self.direction == 'W':
            self.position[0] -= 1
        self.history.append('forward')

    def move_backward(self):
        if self.direction == 'N':
            self.position[1] -= 1
        elif self.direction == 'E':
            self.position[0] -= 1
        elif self.direction == 'S':
            self.position[1] += 1
        elif self.direction == 'W':
            self.position[0] += 1
        self.history.append('backward')

    def turn_left(self):
        directions = ['N', 'W', 'S', 'E']
        idx = directions.index(self.direction)
        self.direction = directions[(idx - 1) % 4]
        self.history.append('left')

    def turn_right(self):
        directions = ['N', 'E', 'S', 'W']
        idx = directions.index(self.direction)
        self.direction = directions[(idx + 1) % 4]
        self.history.append('right')

    def undo(self):
        if not self.history:
            print("Không có hành động nào để hoàn tác.")
            return
        
        last_command = self.history.pop()
        print(f"Hoàn tác lệnh: {last_command}")

        if last_command == 'forward':
            self.move_backward()
        elif last_command == 'backward':
            self.move_forward()
        elif last_command == 'left':
            self.turn_right()
        elif last_command == 'right':
            self.turn_left()

    def display_status(self):
        print("Vị trí hiện tại:", self.position, "Hướng:", self.direction)

# Mã hóa hiển thị
if __name__ == "__main__":
    robot = Robot()
    robot.move_forward()
    robot.turn_right()
    robot.move_forward()
    robot.undo()
    robot.undo()
    robot.display_status()