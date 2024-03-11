wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.debc &> /dev/null &&
dpkg -i google-chrome-stable_current_amd64.deb &> /dev/null &&
pip install selenium &> /dev/null &&
apt-get update &> /dev/null &&
apt install chromium-chromedriver &> /dev/null &&
cp /usr/lib/chromium-browser/chromedriver /usr/bin &> /dev/null &&

python get_list_videos.py
python cay_4k_view_youtube.py &
python cay_4k_view_youtube.py &
python cay_4k_view_youtube.py &

wait
echo "Tất cả các công việc đã hoàn thành."
