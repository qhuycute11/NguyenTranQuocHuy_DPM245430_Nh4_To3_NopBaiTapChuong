# Ví dụ các loại lỗi phổ biến:

# 1. Lỗi cú pháp (SyntaxError)
# Ví dụ: thiếu dấu hai chấm
# if True
#     print("Sai cú pháp")  # Lỗi này phải sửa, không thể bắt bằng try-except

# 2. Lỗi thời gian chạy (RuntimeError) ví dụ ZeroDivisionError:
try:
    x = 10 / 0  # Chia cho 0 sẽ gây lỗi
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")

# 3. Lỗi kiểu dữ liệu (TypeError)
try:
    y = "abc" + 5  # Cộng chuỗi với số nguyên sẽ lỗi
except TypeError:
    print("Lỗi: Không thể cộng chuỗi với số!")

# 4. Lỗi giá trị (ValueError)
try:
    num = int("abc")  # Chuyển chuỗi không phải số sang int sẽ lỗi
except ValueError:
    print("Lỗi: Giá trị không hợp lệ khi chuyển đổi!")

# 5. Bắt tất cả lỗi khác (Exception)
try:
    a = [1, 2, 3]
    print(a[10])  # Lỗi IndexError: truy cập chỉ số ngoài danh sách
except Exception as e:
    print("Có lỗi xảy ra:", e)

# Cách bắt lỗi tổng quát với else và finally
try:
    n = int(input("Nhập một số nguyên: "))
except ValueError:
    print("Bạn phải nhập số nguyên!")
else:
    print(f"Bạn đã nhập số {n}")
finally:
    print("Hoàn thành việc nhập dữ liệu.")
