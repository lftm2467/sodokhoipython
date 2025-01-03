import re

# Hàm đọc danh sách khách hàng từ file
def doc_danh_sach_khach_hang(duong_dan_file):
    try:
        # Mở file ở chế độ đọc
        with open(duong_dan_file, 'r') as file:
            # Đọc từng dòng trong file và loại bỏ ký tự xuống dòng
            danh_sach = [line.strip() for line in file.readlines()]
        return danh_sach
    except FileNotFoundError:
        # Nếu file không tồn tại, trả về danh sách rỗng
        return []

# Hàm lưu danh sách khách hàng vào file
def luu_danh_sach_khach_hang(duong_dan_file, danh_sach_khach_hang):
    # Mở file ở chế độ ghi
    with open(duong_dan_file, 'w') as file:
        # Ghi từng khách hàng vào file, mỗi khách hàng trên một dòng
        for khach in danh_sach_khach_hang:
            file.write(f"{khach}\n")

# Hàm kiểm tra email hợp lệ
def email_hop_le(email):
    # Mẫu regex để kiểm tra định dạng email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Kiểm tra email với mẫu regex
    return re.match(pattern, email) is not None

# Hàm chính
def main():
    duong_dan_file = "danh_sach_khach_hang.txt"
    # Đọc danh sách khách hàng từ file
    danh_sach_khach_hang = doc_danh_sach_khach_hang(duong_dan_file)
    # Tạo danh sách các CCCD đã tồn tại
    ds_cccd = [khach.split(",")[0] for khach in danh_sach_khach_hang]

    while True:
        try:
            # Yêu cầu người dùng nhập số lượng khách hàng
            so_luong_khach = int(input("Nhập số lượng khách hàng: "))
            break
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

    for i in range(so_luong_khach):
        while True:
            cccd = input("Nhập CCCD: ")
            # Kiểm tra độ dài CCCD phải đúng 12 ký tự
            if len(cccd) != 12:
                print("CCCD không hợp lệ! Vui lòng nhập lại.")
                continue
            # Kiểm tra CCCD có bị trùng lặp hay không
            if cccd in ds_cccd:
                print("CCCD trùng lặp! Vui lòng nhập lại.")
                continue
            break

        while True:
            ten = input("Nhập tên: ")
            # Kiểm tra tên không được để trống
            if len(ten) == 0:
                print("Tên không được để trống! Vui lòng nhập lại.")
            else:
                break

        while True:
            sdt = input("Nhập số điện thoại: ")
            # Kiểm tra độ dài số điện thoại phải là 10 hoặc 11 ký tự
            if len(sdt) not in [10, 11]:
                print("Số điện thoại không hợp lệ! Vui lòng nhập lại.")
            else:
                break

        dia_chi = input("Nhập địa chỉ: ")

        while True:
            email = input("Nhập email: ")
            # Kiểm tra email hợp lệ
            if not email_hop_le(email):
                print("Email không hợp lệ! Vui lòng nhập lại.")
            else:
                break

        # Lưu thông tin khách hàng
        khach_hang = f"{cccd},{ten},{sdt},{dia_chi},{email}"
        danh_sach_khach_hang.append(khach_hang)
        ds_cccd.append(cccd)

    # Lưu danh sách khách hàng vào file
    luu_danh_sach_khach_hang(duong_dan_file, danh_sach_khach_hang)
    print("Lưu thông tin khách hàng thành công!")

if __name__ == "__main__":
    main()
