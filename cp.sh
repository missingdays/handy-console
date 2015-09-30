rm -f ~/.handy-console/bin/*
mkdir ~/.handy-console/bin

cp ./src/**/*.py ~/.handy-console/bin

for f in ~/.handy-console/bin/*
do
    echo $f
    ln -s -f $f ~/bin/"$(basename "$f" .py)"
done


