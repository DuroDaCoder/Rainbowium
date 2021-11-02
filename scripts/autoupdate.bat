git reset --hard
git pull
echo 01 > temp.txt
start R6Bot.py
timeout /t 5 /NOBREAK
del temp.txt
exit