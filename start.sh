wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb
pip install selenium
apt-get update
apt install chromium-chromedriver
cp /usr/lib/chromium-browser/chromedriver /usr/bin

python get_list_videos.py
python cay_4k_view_youtube.py
