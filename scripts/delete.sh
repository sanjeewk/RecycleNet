#!/bin/bash
# Script to delete images if corresponding annotation does not exist
# a=$(find $(pwd) -iname '*.jpg')

folder='packets/'
dir='../'$folder
a=$(find $dir -iname '*.jpg')

for f in $a
do
    a=${f%.*}
    b=$a'.txt'
    # echo $b
    if [ -f "$b" ]; then
      echo 'exists'
      # echo "$b exists."
    else 
      rm $f
      echo "$b does not exist."
  fi
done
