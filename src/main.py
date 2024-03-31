import os
import tkinter as tk
from tkinter import filedialog
import requests
from dotenv import load_dotenv

load_dotenv()
vt_key = os.getenv('vt_api_key')


def browse_file(file_var):
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        file_var.set(file_path)


def upload_file(file_path):
    print(file_path)
    url = "https://www.virustotal.com/api/v3/files"
    files = {"file": (os.path.basename(file_path), open(file_path, "rb"))}
    headers = {
        "x-apikey": vt_key
    }
    response = requests.post(url, headers=headers, files=files)

    if response.ok:
        print("File uploaded successfully!")
        json_response = response.json()
        file_id = json_response["data"]["id"]
        get_results(file_id)
    else:
        print("Error uploading file:")
        print(response.text)


def get_results(file_id):
    url = f"https://www.virustotal.com/api/v3/analyses/{file_id}"
    headers = {
        "x-apikey": vt_key
    }
    response = requests.get(url, headers=headers)

    if response.ok:
        print("Results retrieved successfully!")
        print(response.json())
    else:
        print("Error retrieving results:")
        print(response.text)


def main():
    root = tk.Tk()
    root.title("File Selection Form")

    # Create a StringVar to store the selected file path
    file_var = tk.StringVar()

    label = tk.Label(root, text="Select a File:")
    label.pack(pady=10)

    file_entry = tk.Entry(root, textvariable=file_var, state="disabled", width=40)
    file_entry.pack(pady=10)

    browse_button = tk.Button(root, text="Browse", command=lambda: browse_file(file_var))
    browse_button.pack(pady=10)

    submit_button = tk.Button(root, text="Submit", command=lambda: upload_file(file_var.get()))
    submit_button.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
