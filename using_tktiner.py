import json
import tkinter as tk
from tkinter import ttk
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
            forms.append(("Không có dạng tính từ cho từ '{}'.".format(word), "Error"))
    elif choice == 3:
        adverb = dictionary[word].get('adverb')
        if adverb:
            forms.append((adverb, "Adverb"))
        else:
            forms.append(("Không có dạng trạng từ cho từ '{}'.".format(word), "Error"))
    elif choice == 4:
        verb = dictionary[word].get('verb')
        if verb:
            forms.append((verb.get('V1', ''), "V1"))
            forms.append((verb.get('V2', ''), "V2"))
            forms.append((verb.get('V3', ''), "V3"))
        else:
            forms.append(("Không có dạng động từ cho từ '{}'.".format(word), "Error"))
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
            forms.append(("Từ '{}' không tồn tại trong từ điển.".format(word), "Error"))
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
            forms.append(("Từ '{}' không tồn tại trong từ điển.".format(word), "Error"))
        save_choice = tk.messagebox.askquestion("Lưu từ", "Bạn có muốn lưu từ này vào danh sách?")
        if save_choice == 'yes':
            saved_words.append((word,) + tuple(form[0] for form in forms[1:]))
    else:
        forms.append(("Lựa chọn không hợp lệ.", "Error"))

    return forms

# -- Hàm hiển thị các dạng từ
def display_word_forms(forms):
    table_data = []
    for form in forms:
        table_data.append([form[0], form[1]])

    root = tk.Tk()
    root.title("Kết quả")
    table = ttk.Treeview(root, columns=("Word", "Form"), show="headings")
    table.heading("Word", text="Word")
    table.heading("Form", text="Form")
    for data in table_data:
        table.insert("", "end", values=data)
    table.pack()

    root.mainloop()

# -- Hàm hiểnthị danh sách từ đã lưu
def display_saved_words(saved_words):
    if saved_words:
        root = tk.Tk()
        root.title("Danh sách từ đã lưu")
        table = ttk.Treeview(root, columns=("Word", "Noun", "Adjective", "Adverb", "V1", "V2", "V3"), show="headings")
        table.heading("Word", text="Word")
        table.heading("Noun", text="Noun")
        table.heading("Adjective", text="Adjective")
        table.heading("Adverb", text="Adverb")
        table.heading("V1", text="V1")
        table.heading("V2", text="V2")
        table.heading("V3", text="V3")
        for data in saved_words:
            table.insert("", "end", values=data)
        table.pack()

        root.mainloop()
    else:
        tk.messagebox.showinfo("Thông báo", "Không có từ nào được lưu.")

# -- Hàm chính
def main():
    dictionary = load_dictionary()
    verbs = get_verb_list(dictionary)
    saved_words = []

    def handle_button_click():
        word = entry_word.get()
        choice = combo_choice.current() + 1
        forms = select_word_forms(word, choice, dictionary, saved_words)
        display_word_forms(forms)

    def handle_saved_words_button_click():
        display_saved_words(saved_words)

    root = tk.Tk()
    root.title("English Word Forms")
    root.geometry("400x200")

    label_word = tk.Label(root, text="Nhập từ:")
    label_word.pack()

    entry_word = tk.Entry(root)
    entry_word.pack()

    label_choice = tk.Label(root, text="Chọn hình thức từ:")
    label_choice.pack()

    combo_choice = ttk.Combobox(root, values=["Danh từ", "Tính từ", "Trạng từ", "Động từ (V1, V2, V3)", "Tất cả", "Tất cả và lưu"])
    combo_choice.current(0)
    combo_choice.pack()

    button_submit = tk.Button(root, text="Xác nhận", command=handle_button_click)
    button_submit.pack()

    button_saved_words = tk.Button(root, text="Xem từ đã lưu", command=handle_saved_words_button_click)
    button_saved_words.pack()

    root.mainloop()

if __name__ == "__main__":
    main()