#!/bin/bash

set -e

if [ ! -f "${1}" ]
then
    echo "File ${1} not found"
    exit 1
fi

jupyter nbconvert --to markdown "${1}"
echo mv "${1/ipynb/md}" "_posts/$(basename ${1/ipynb/md})"

FILE_DIR="${1/.ipynb/_files}"
if [ -d "$FILE_DIR" ]
then
    echo cp "${FILE_DIR}/*.png" "assets/images/
    echo mv "${FILE_DIR}" "assets/$(basename ${FILE_DIR})"
fi
