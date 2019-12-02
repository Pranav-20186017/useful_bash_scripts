sudo xrandr
cvt 1920 1080~/.profile
sudo xrandr --newmode "1920x1080_60.00"  118.25  1600 1696 1856 2112  900 903 908 934 -hsync +vsync
sudo xrandr --addmode Virtual1 "1920x1080_60.00"
echo 'xrandr --newmode "1920x1080_60.00"  118.25  1600 1696 1856 2112  900 903 908 934 -hsync +vsync' >> ~/.profile
echo 'xrandr --addmode Virtual1 "1920x1080_60.00"' >> ~/.profile
