import requests
from bs4 import BeautifulSoup

url = "https://anotepad.com/notes/wtycfshi"
response = requests.get(url)

if response.status_code == 200:
    # Sử dụng BeautifulSoup để phân tích nội dung trang web
    soup = BeautifulSoup(response.text, 'html.parser')

    # Lọc thông tin từ class "plaintext"
    plaintext_elements = soup.find_all(class_='plaintext')

    # Ghi thông tin vào file và xoá các dòng trắng
    with open('list_url_video.txt', 'w') as file:
        for i, element in enumerate(plaintext_elements):
            text = element.get_text(strip=True)
            if text:  # Kiểm tra xem dòng có chứa thông tin không trước khi ghi vào file
                file.write(text)
                # Kiểm tra xem có phải là dòng cuối cùng không
                if i < len(plaintext_elements) - 1:
                    file.write('\n')
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
