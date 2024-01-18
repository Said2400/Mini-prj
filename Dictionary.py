import tkinter as tk
from tkinter import ttk
import requests

def get_definition(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data = response.json()
    if data and 'meanings' in data[0]:
        return '\n'.join([f"{meaning['partOfSpeech']}: {meaning['definitions'][0]['definition']}\n" for meaning in data[0]['meanings']])
    return "No definition found."

def search_definition():
    definition = get_definition(entry_word.get())
    text_output.config(state='normal')
    text_output.delete('1.0', tk.END)
    text_output.insert(tk.END, definition)
    text_output.config(state='disabled')

def get_es_defi():
    pass
    # open('spanish_definitions.json', 'r', encoding='utf-8') as json_file:
    #         data = json.load(json_file)

def search_definition():
    if language_var.get() == "English":
        definition = get_definition(entry_word.get())
    elif language_var.get() == "Spanish":
        definition = get_es_defi(entry_word.get())
    else:
        definition = "Please select a language."
    
    text_output.config(state='normal')
    text_output.delete('1.0', tk.END)
    text_output.insert(tk.END, definition)
    text_output.config(state='disabled')




root = tk.Tk()
root.title("Dictionary App")
root.geometry("900x600")

frame_search = ttk.Frame(root)
frame_search.pack(pady=20)

label_word = ttk.Label(frame_search, text="Enter a word:")
label_word.grid(row=0, column=0, padx=5)

entry_word = ttk.Entry(frame_search, width=20, )
entry_word.grid(row=0, column=1, padx=5)

language_var = tk.StringVar()
language_var.set("English")

english_button = ttk.Radiobutton(frame_search, text="English", variable=language_var, value="English")
english_button.grid(row=0, column=2, padx=5)

spanish_button = ttk.Radiobutton(frame_search, text="Spanish", variable=language_var, value="Spanish")
spanish_button.grid(row=0, column=3, padx=5)

button_search = ttk.Button(frame_search, text="Search", command=search_definition)
button_search.grid(row=0, column=4, padx=5)

frame_output = ttk.Frame(root)
frame_output.pack(padx=20, pady=10)

text_output = tk.Text(frame_output, height=30)
text_output.pack()

root.mainloop()
