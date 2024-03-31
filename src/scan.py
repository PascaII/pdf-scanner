import os
import requests
from dotenv import load_dotenv
import PyPDF2

load_dotenv()
vt_key = os.getenv('vt_api_key')


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
    check_javascript(file_path)


def check_javascript(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            javascript_found = False
            print(pdf_reader.metadata.author)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                if '/JavaScript' in page.extract_text():
                    javascript_found = True
                    break
            if javascript_found:
                print("JavaScript found in the PDF file.")
            else:
                print("No JavaScript found in the PDF file.")
    except Exception as e:
        print("Error analyzing PDF file:", e)


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
