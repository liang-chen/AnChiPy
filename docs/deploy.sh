#!/bin/sh

TARGET_DIR="../../sphinxdoc-test-docs/AnChiPyDocs/"
echo $TARGET_DIR
DIR=$(pwd)

make html
cp -r ./_build/html/* $TARGET_DIR
cd $TARGET_DIR
git add *
git commit -m "update documentations"
git push origin gh-pages
cd $DIR
