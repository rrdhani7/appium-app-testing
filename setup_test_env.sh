 #! /bin/sh.

rm -rf ~/Project/apptestenv
python3 -m venv ~/Project/apptestenv
source ~/Project/apptestenv/bin/activate
pip3 install -r ~/Project/appomation/requirements.txt