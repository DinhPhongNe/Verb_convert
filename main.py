import json
from tabulate import tabulate as tbl

# -- Hàm tải từ điển
def load_dictionary():
    with open('dictionary.json') as file:
        data = json.load(file)
        return data

# -- Hàm lấy danh sách động từ
def get_verb_list(dictionary):
    verbs = []
    for word in dictionary:
        if 'verb' in dictionary[word]:
            verbs.append(word)
    return verbs

# -- Hàm chọn hình thức từ
def select_word_forms(word, choice, dictionary, saved_words):
    forms = []
    if choice == 1:
        forms.append((word, "Noun"))
    elif choice == 2:
        adjective = dictionary[word].get('adjective')
        if adjective:
            forms.append((adjective, "Adjective"))
        else:
            print("Không có dạng tính từ cho từ '{}'.".format(word))
    elif choice == 3:
        adverb = dictionary[word].get('adverb')
        if adverb:
            forms.append((adverb, "Adverb"))
        else:
            print("Không có dạng trạng từ cho từ '{}'.".format(word))
    elif choice == 4:
        verb = dictionary[word].get('verb')
        if verb:
            forms.append((verb.get('V1', ''), "V1"))
            forms.append((verb.get('V2', ''), "V2"))
            forms.append((verb.get('V3', ''), "V3"))
        else:
            print("Không có dạng động từ cho từ '{}'.".format(word))
    elif choice == 5:
        if word in dictionary:
            forms.append((word, "Noun"))
            adjective = dictionary[word].get('adjective')
            if adjective:
                forms.append((adjective, "Adjective"))
            adverb = dictionary[word].get('adverb')
            if adverb:
                forms.append((adverb, "Adverb"))
            verb = dictionary[word].get('verb')
            if verb:
                forms.append((verb.get('V1', ''), "V1"))
                forms.append((verb.get('V2', ''), "V2"))
                forms.append((verb.get('V3', ''), "V3"))
        else:
            print("Từ '{}' không tồn tại trong từ điển.".format(word))
    elif choice == 6:
        if word in dictionary:
            forms.append((word, "Noun"))
            adjective = dictionary[word].get('adjective')
            if adjective:
                forms.append((adjective, "Adjective"))
            adverb = dictionary[word].get('adverb')
            if adverb:
                forms.append((adverb, "Adverb"))
            verb = dictionary[word].get('verb')
            if verb:
                forms.append((verb.get('V1', ''), "V1"))
                forms.append((verb.get('V2', ''), "V2"))
                forms.append((verb.get('V3', ''), "V3"))
        else:
            print("Từ '{}' không tồn tại trong từ điển.".format(word))
        save_choice = input("Bạn có muốn lưu từ này vào danh sách? (y/n): ")
        if save_choice == 'y':
            saved_words.append((word,) + tuple(form[0] for form in forms[1:]))
    else:
        print("Lựa chọn không hợp lệ.")

    return forms

# -- Hàm hiển thị các dạng từ
def display_word_forms(forms):
    headers = ["Word", "Form"]
    data = [(form[0], form[1]) for form in forms]

    table = tbl(data, headers=headers, tablefmt="fancy_grid")
    print(table)

# -- Hàm hiển thị danh sách từ đã lưu
def display_saved_words(saved_words):
    if saved_words:
        print("Danh sách các từ đã lưu:")
        headers = ["Word", "Noun", "Adjective", "Adverb", "V1", "V2", "V3"]
        data = saved_words

        table = tbl(data, headers=headers, tablefmt="fancy_grid")
        print(table)
    else:
        print("Không có từ nào được lưu.")

# -- Hàm chính
def main():
    dictionary = load_dictionary()
    verbs = get_verb_list(dictionary)
    saved_words = []

    while True:
        word = input("Nhập từ tiếng Anh (nhập 'q' để thoát): ")
        if word == 'q':
            break

        print("----------------------=======Nhập lựa chọn của bạn=======----------------------")
        print("Từ '{}' được tìm thấy trong từ điển.".format(word))
        print("Chọn hình thức từ:")
        print("1. Danh từ")
        print("2. Tính từ") 
        print("3. Trạng từ")
        print("4. Động từ (V1, V2, V3)")
        print("5. Xem tất cả hình thức từ")
        print("6. Xem chi tiết và lựa chọn hình thức cần lưu")
        print("----------------------===================================----------------------")
        choice = int(input("Lựa chọn của bạn: "))

        forms = select_word_forms(word, choice, dictionary, saved_words)
        display_word_forms(forms)

        if choice == 5:
            continue

        save_choice = input("Bạn có muốn lưu từ này vào danh sách? (y/n): ")
        if save_choice == 'y':
            saved_words.append((word,) + tuple(form[0] for form in forms[1:]))

    display_saved_words(saved_words)


if __name__ == '__main__':
    main()