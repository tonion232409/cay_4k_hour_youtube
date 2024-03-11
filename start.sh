wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.debc > /dev/null 2>&1
dpkg -i google-chrome-stable_current_amd64.deb > /dev/null 2>&1
pip install selenium > /dev/null 2>&1
apt-get update > /dev/null 2>&1
apt install chromium-chromedriver > /dev/null 2>&1
cp /usr/lib/chromium-browser/chromedriver /usr/bin > /dev/null 2>&1

python get_list_videos.py
python cay_4k_view_youtube.py
