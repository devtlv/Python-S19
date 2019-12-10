if [ "$#" -ne 1 ]; then
    echo "Please input a message"
    exit 1
fi

git add .
git commit -m "$1"
git push origin master
