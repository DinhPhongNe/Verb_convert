import json
from tabulate import tabulate as tbl

# -- thêm dictonary.json
def load_dictionary():
    with open('dictionary.json') as file:
        data = json.load(file)
        return data

# -- lấy verb ( động từ ) ra
def get_verb_list(dictionary):
    verbs = []
    for word in dictionary:
        if 'verb' in dictionary[word]:
            verbs.append(word)
    return verbs

# -- chọn verb ( động từ )
def select_verb_forms(verb, choice, dictionary):
    forms = []
    if choice == 1:
        forms.append((verb, "v1"))
    elif choice == 2:
        forms.append((dictionary[verb]['v2'], "v2"))
    elif choice == 3:
        forms.append((dictionary[verb]['v3'], "v3"))
    else:
        forms.append((verb, "v1"))
        forms.append((dictionary[verb]['v2'], "v2"))
        forms.append((dictionary[verb]['v3'], "v3"))
    return forms

# -- hiển thị từ ra ( sử dụng thư viện tabulate )
def display_verb_forms(forms):
    headers = ["V1", "V2", "V3"]
    data = [[forms[0][0], forms[1][0], forms[2][0]]]

    table = tbl(data, headers=headers, tablefmt="fancy_grid")
    print(table)

def display_saved_verbs(saved_verbs):
    if saved_verbs:
        print("Danh sách các từ đã lưu:")
        headers = ["V1", "V2", "V3"]
        data = [(verb[0], verb[1], verb[2]) for verb in saved_verbs]

        table = tbl(data, headers=headers, tablefmt="fancy_grid")
        print(table)
    else:
        print("Không có từ nào được lưu.")

# -- code chính
def main():
    dictionary = load_dictionary()
    verbs = get_verb_list(dictionary)
    saved_verbs = []

    while True:
        word = input("Nhập từ tiếng Anh (nhập 'q' để thoát): ")
        if word == 'q':
            break

        if word in verbs:
            print("----------------------=======Nhập lựa chọn của bạn=======----------------------")
            print("Từ '{}' được tìm thấy trong từ điển.".format(word))
            print("Chọn hình thức động từ:")
            print("1. V1 (nguyên thể)")
            print("2. V2 (quá khứ đơn)")
            print("3. V3 (quá khứ phân từ)")
            print("4. Tất cả")
            print("----------------------===================================----------------------")
            choice = int(input("Lựa chọn của bạn: "))

            forms = select_verb_forms(word, choice, dictionary)
            display_verb_forms(forms)

            save_choice = input("Bạn có muốn lưu từ này vào danh sách? (y/n): ")
            if save_choice == 'y':
                saved_verbs.append((word, forms[1][0], forms[2][0]))
        else:
            print("Từ '{}' không tồn tại trong từ điển.".format(word))

    display_saved_verbs(saved_verbs)


if __name__ == '__main__':
    main()