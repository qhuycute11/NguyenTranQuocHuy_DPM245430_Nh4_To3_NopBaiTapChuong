# Cách 1: Nhập dữ liệu dạng chuỗi (string)
name = input("Nhập tên của bạn: ")
print("Chào bạn,", name)

# Cách 2: Nhập dữ liệu dạng số nguyên (int)
age = int(input("Nhập tuổi của bạn: "))
print("Tuổi của bạn là:", age)

# Cách 3: Nhập dữ liệu dạng số thực (float)
height = float(input("Nhập chiều cao của bạn (m): "))
print("Chiều cao của bạn là:", height, "m")

# Cách 4: Nhập nhiều giá trị cùng lúc (cách phổ biến)
# Ví dụ nhập 2 số cách nhau dấu cách, rồi chuyển sang int
a, b = map(int, input("Nhập hai số nguyên cách nhau dấu cách: ").split())
print("Bạn nhập hai số:", a, "và", b)
