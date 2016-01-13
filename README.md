# pixipher
Simple pyTk based application for image encryption. 

# Requirements
python3.4
pillow(PIL)

# Warning
1.  This project is using PIL imaging library and a specific
GTK+ 2.x version(probably) please don't use any other 3rd
party imaging libraries which are based on other GTK versions
(eg. GTK+ 3.x).

2.  AVOID USING OPENCV for displaying images. The latest
opencv version is based on GTK+ 3.x version. While displaying
images using opencv will generate GTK errors for version
collision.
