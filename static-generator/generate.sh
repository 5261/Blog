rm -rf ./public/*
python main.py
cp ../Blog/static -r ./public/
cp ./source/* -r ./public/
