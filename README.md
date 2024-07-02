# Envoi-de-mail-auto
Script python pour envoie les emails automatiquement

# création du fichier .py
touch /home/kali/email/emailpython.py

# fichier emailpython.py
dans ce fichier nous avons les scripts pour evnoie les emails entre adresse gmail, dans lequel est definie le destinateur, l'auteur, le sujet ainsi que le message.

# executer le script dans un scron
crontab -e
*/1 * * * * python /home/kali/email/emailpython.py

