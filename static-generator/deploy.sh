rm -rf ./public/*

python main.py

cd public
git add .
git commit -m "Site Update"
git push -f

