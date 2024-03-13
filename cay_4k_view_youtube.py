import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from pytube import YouTube

def get_video_length(video_url):
    try:
        yt = YouTube(video_url)
        # Lấy thời lượng video trong giây
        length_in_seconds = yt.length
        # Chuyển đổi thời lượng thành dạng giờ:phút:giây
        length_formatted = str(length_in_seconds // 3600).zfill(2) + ":" + str((length_in_seconds % 3600) // 60).zfill(2) + ":" + str(length_in_seconds % 60).zfill(2)
        return length_formatted
    except Exception as e:
        print("Đã xảy ra lỗi:", str(e))
        return None

def time_to_seconds(time_str):
    parts = time_str.split(":")
    if len(parts) == 2:
        minutes, seconds = parts
        hours = 0
    elif len(parts) == 3:
        hours, minutes, seconds = parts
    else:
        return 0

    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    return total_seconds

def main():
    videoFileName = "list_url_video.txt"
    videoFile = open(videoFileName)
    listVideo = videoFile.readlines()
    random.shuffle(listVideo)
    NUMBER_OF_VIDEO = len(listVideo)
    print("VIDEO: " + str(NUMBER_OF_VIDEO))

    videoIndex = 0

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Chạy trình duyệt ẩn danh (tùy chọn có thể bật nếu cần)
    options.add_argument('--no-sandbox')  # Chạy trong môi trường không có sandbox
    options.add_argument('--disable-dev-shm-usage')  # Tắt việc sử dụng bộ nhớ chia sẻ
    browser = webdriver.Chrome(options=options)
    while True:
        videoIndex = (videoIndex + 1) % int(NUMBER_OF_VIDEO)
        url = listVideo[videoIndex].strip()
        browser.get(url)
        time.sleep(3)
        print(browser.title)
        kt = 0
        while kt == 0: 
            try:
                play_element = browser.find_element(By.CLASS_NAME, 'ytp-play-button')
                play_e = play_element.get_attribute("data-title-no-tooltip")
                play_e = play_e.lower()
                # print("lấy thành công element: ", play_e)
                if play_e == "play" or play_e == "afspelen":
                    action_chains = ActionChains(browser)
                    action_chains.send_keys(Keys.NULL, 'k')
                    action_chains.perform()
                    # print("Click thành công")
                else: 
                    kt = 1
            except Exception as e:
                print(e)
            time.sleep(2)

        duration = get_video_length(url)
        duration = time_to_seconds(duration)
        LOOP_TIME = float(duration) * 0.8
        print("Loop time: ", LOOP_TIME)
        while LOOP_TIME > 0: 
            if LOOP_TIME > 600:
                time.sleep(600)
                browser.execute_script("window.scrollBy(0, 500);")
                time.sleep(0.5)
                # Scroll lên đầu trang
                browser.execute_script("window.scrollTo(0, 0);")
                LOOP_TIME = LOOP_TIME - 600
            else:
                time.sleep(LOOP_TIME)
                LOOP_TIME = 0

if __name__ == "__main__":
    threads = []

    for _ in range(5):
        thread = threading.Thread(target=main)
        threads.append(thread)
        thread.start()

    # Chờ cho tất cả các luồng kết thúc (nếu cần)
    for thread in threads:
        thread.join()
