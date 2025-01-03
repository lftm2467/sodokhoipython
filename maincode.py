import re

# đọc danh sách khách hàng từ file
def doc_danh_sach_khach_hang(duong_dan_file):
    try:
        with open(duong_dan_file, 'r') as file:
            danh_sach = [line.strip() for line in file.readlines()]
        return danh_sach
    except FileNotFoundError:
        return []

def luu_danh_sach_khach_hang(duong_dan_file, danh_sach_khach_hang):
    with open(duong_dan_file, 'w') as file:
        for khach in danh_sach_khach_hang:
            file.write(f"{khach}\n")
            
def email_hop_le(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def main():
    duong_dan_file = "danh_sach_khach_hang.txt"
    danh_sach_khach_hang = doc_danh_sach_khach_hang(duong_dan_file)

    # tạo danh sách cccd đã tồn tại
    ds_cccd = [khach.split(",")[0] for khach in danh_sach_khach_hang]

    while True:
        try:
            # nhập số lượng khách hàng
            so_luong_khach = int(input("Nhập số lượng khách hàng: "))
            break
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

    for i in range(so_luong_khach):
        while True:
            cccd = input("Nhập CCCD: ")
            # kiểm tra độ dài CCCD (đúng 12 ký tự)
            if len(cccd) != 12:
                print("CCCD không hợp lệ! Vui lòng nhập lại.")
                continue
            # kiểm tra CCCD có bị trùng lặp hay không
            if cccd in ds_cccd:
                print("CCCD trùng lặp! Vui lòng nhập lại.")
                continue
            break

        while True:
            ten = input("Nhập tên: ")
            if len(ten) == 0:
                print("Tên không được để trống! Vui lòng nhập lại.")
            else:
                break

        while True:
            sdt = input("Nhập số điện thoại: ")
            # kiểm tra độ dài số điện thoại (10 or 11 số)
            if len(sdt) not in [10, 11]:
                print("Số điện thoại không hợp lệ! Vui lòng nhập lại.")
            else:
                break

        dia_chi = input("Nhập địa chỉ: ")

        while True:
            email = input("Nhập email: ")
            # kiểm tra mail hợp lệ
            if not email_hop_le(email):
                print("Email không hợp lệ! Vui lòng nhập lại.")
            else:
                break

        khach_hang = f"{cccd},{ten},{sdt},{dia_chi},{email}"
        danh_sach_khach_hang.append(khach_hang)
        ds_cccd.append(cccd)

    luu_danh_sach_khach_hang(duong_dan_file, danh_sach_khach_hang)
    print("Lưu thông tin khách hàng thành công!")

if __name__ == "__main__":
    main()
