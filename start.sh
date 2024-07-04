#Dont change anything without informing us
if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/joker153/RENAMER_BOT_V3.git /RENAMER_BOT_V3
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /RENAMER_BOT_V3
fi
cd /RENAMER_BOT_V3
pip3 install -U -r requirements.txt
echo "sᴛᴀʀᴛɪɴɢ elz ʙᴏᴛ...."
python3 bot.py
