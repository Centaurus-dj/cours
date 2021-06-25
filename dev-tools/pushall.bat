@echo off

echo "Launching Python script for pushing multiple git repositories"

cd src/
"C:\Users\alexi\AppData\Local\Programs\Python\Python38\python.exe" pushall.py
cd ../

echo "Script executed"