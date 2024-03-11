import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Tên file chứa danh sách URL video
videoFileName = "list_url_video.txt"

# Mở file chứa danh sách URL video
videoFile = open(videoFileName)
listVideo = videoFile.readlines()

# Số lượng video trong danh sách
NUMBER_OF_VIDEO = len(listVideo)
# Số lượng cửa sổ trình duyệt mở đồng thời
NUMBER_OF_WINDOW = NUMBER_OF_VIDEO

# Thời gian delay giữa các lần xem video
LOOP_TIME = int(1800/NUMBER_OF_WINDOW)

print("  WINDOW: " + str(NUMBER_OF_WINDOW))
print("  VIDEO: " + str(NUMBER_OF_VIDEO))

# Khởi tạo index của video và cửa sổ trình duyệt
videoIndex = 0
windowIndex = 0
windowCount = 1

# Tạo các tùy chọn cho trình duyệt Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Chạy trình duyệt ẩn danh (tùy chọn có thể bật nếu cần)
options.add_argument('--no-sandbox')  # Chạy trong môi trường không có sandbox
options.add_argument('--disable-dev-shm-usage')  # Tắt việc sử dụng bộ nhớ chia sẻ
browser = webdriver.Chrome(options=options)
browser.get(listVideo[videoIndex])
time.sleep(2)
count = 0 
# Vòng lặp chính của chương trình
while True:
    # Chuyển đến video tiếp theo trong danh sách
    videoIndex = (videoIndex + 1) % int(NUMBER_OF_VIDEO)

    # Chuyển đến cửa sổ trình duyệt tiếp theo
    windowIndex = (windowIndex + 1) % int(NUMBER_OF_WINDOW)
    print(str(windowIndex) + " : " + str(videoIndex))
    url = listVideo[videoIndex].strip()

    # Nếu số lượng cửa sổ đang mở nhỏ hơn quy định, mở thêm cửa sổ mới
    if windowCount < NUMBER_OF_WINDOW:
        windowCount = windowCount + 1
        browser.execute_script("window.open('"+url+"')")
        time.sleep(5)
        try:
            play_element = browser.find_element(By.CLASS_NAME, 'ytp-play-button')
            play_e = play_element.get_attribute("data-title-no-tooltip")
            play_e = play_e.lower()
            print("lấy thành công element", play_e)
            if play_e == "play" or play_e == "afspelen":
                action_chains = ActionChains(browser)
                action_chains.send_keys(Keys.NULL, 'k')  # Keys.NULL để tránh hiệu ứng của SPACE
                action_chains.perform()
                print("Click thành công")
        except Exception as e:
            print(e)
        time.sleep(5)
    else:
        if count < 3:
            # Chuyển đến cửa sổ trình duyệt đã mở
            browser.switch_to.window(browser.window_handles[windowIndex])
            time.sleep(0.5)
            try:
                play_element = browser.find_element(By.CLASS_NAME, 'ytp-play-button')
                play_e = play_element.get_attribute("data-title-no-tooltip")
                play_e = play_e.lower()
                print("lấy thành công element", play_e)
                if play_e == "play" or play_e == "afspelen":
                    action_chains = ActionChains(browser)
                    action_chains.send_keys(Keys.NULL, 'k')  # Keys.NULL để tránh hiệu ứng của SPACE
                    action_chains.perform()
                    print("Click thành công")
            except Exception as e:
                print(e)
            time.sleep(5)
            count+=1
        else:
            # Chuyển đến cửa sổ trình duyệt đã mở
            browser.switch_to.window(browser.window_handles[windowIndex])
            time.sleep(0.5)
            # Scroll xuống đến cuối trang
            browser.execute_script("window.scrollBy(0, 500);")
            time.sleep(0.5)
            # Scroll lên đầu trang
            browser.execute_script("window.scrollTo(0, 0);")
            # Đợi một khoảng thời gian trước khi chuyển sang video tiếp theo\
            try:
                play_element = browser.find_element(By.CLASS_NAME, 'ytp-play-button')
                play_e = play_element.get_attribute("data-title-no-tooltip")
                play_e = play_e.lower()
                print("lấy thành công element", play_e)
                if play_e == "play" or play_e == "afspelen":
                    action_chains = ActionChains(browser)
                    action_chains.send_keys(Keys.NULL, 'k')  # Keys.NULL để tránh hiệu ứng của SPACE
                    action_chains.perform()
                    print("Click thành công")
            except Exception as e:
                print(e)
            time.sleep(LOOP_TIME)
