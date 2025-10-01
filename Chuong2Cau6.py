# Toán tử chia lấy phần thực: /
a = 10
b = 3
print("a / b =", a / b)  # Kết quả: 3.333... (kiểu float)

# Toán tử chia lấy phần nguyên: //
print("a // b =", a // b)  # Kết quả: 3 (loại bỏ phần thập phân)

# Toán tử chia lấy phần dư: %
print("a % b =", a % b)  # Kết quả: 1 (vì 10 chia 3 dư 1)

# Toán tử lũy thừa: **
print("a ** b =", a ** b)  # Kết quả: 1000 (10 mũ 3)

# Toán tử logic: and
x = True
y = False
print("x and y =", x and y)  # Kết quả: False (chỉ True nếu cả hai đều True)

# Toán tử logic: or
print("x or y =", x or y)  # Kết quả: True (chỉ cần một trong hai là True)

# Toán tử so sánh đối tượng: is
c = [1, 2, 3]
d = [1, 2, 3]
e = c

print("c is d:", c is d)   # False, vì c và d là 2 đối tượng khác nhau (dù nội dung giống nhau)
print("c is e:", c is e)   # True, vì e tham chiếu cùng đối tượng với c
