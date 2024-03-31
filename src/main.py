import tkinter as tk
from tkinter import filedialog
from src.scan import upload_file
from src.creator import create_pdf_with_js


def browse_file(file_var):
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        file_var.set(file_path)


def run_ui():
    root = tk.Tk()
    root.title("File Selection Form")

    file_var = tk.StringVar()
    file_author = tk.StringVar()

    label = tk.Label(root, text="Select a File:")
    label.pack(pady=10)

    file_entry = tk.Entry(root, textvariable=file_var, state="disabled", width=40)
    file_entry.pack(pady=10)

    browse_button = tk.Button(root, text="Browse", command=lambda: browse_file(file_var))
    browse_button.pack(pady=10)

    submit_button = tk.Button(root, text="Submit", command=lambda: upload_file(file_var.get()))
    submit_button.pack(pady=10)
    root.mainloop()


def main():
    run_ui()
    # create_pdf_with_js("test.pdf")


if __name__ == "__main__":
    main()
