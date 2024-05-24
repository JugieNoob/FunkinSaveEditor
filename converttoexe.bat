pyinstaller -w --onefile --add-data="./images/*:." --icon=images/icon-hole.ico main.py
mkdir dist/images
xcopy images dist\images

pause