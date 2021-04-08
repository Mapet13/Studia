#!/bin/bash
# uruchamiac z kropką to wtedy odrazu przeniesie do folderu

if [ "$#" != "1" ]; then
    echo "Zła ilosc argumentow debilu xD"
    exit 2
fi

if [ -d "$1" ]; then
    echo "Juz jest taki projekt LOL"
    exit 2
fi

mkdir -p $1
cp utils/makefile $1
mkdir -p $1/src
mkdir -p $1/out
cp utils/main.c $1/src

cd $1 