#!/bin/bash

folder='packets/'
dir='../DIRT/'$folder
a=$(find $dir -iname '*.jpg')
n=1
st='pouch'
for f in $a
do
  
  pic=${f##*/}
  txt=${pic%.*}'.txt'
  echo $pic' '$txt
  newp=$st$n'.jpg'
  newt=$st$n'.txt'
  echo $newp' '$newt
#   echo $a

  mv $dir$pic $dir$newp
  mv $dir$txt $dir$newt
  n=$((n + 1))
done

#Script to rename all images and txt files
# folder=Coffee_spills/
# dir='../DIRT/'$folder
# a=$(find $dir -iname '*.jpg')
# n=1
# st='spill'
# for f in $a
# do
  
#   pic=${f##*/}
#   txt=${pic%.*}'.txt'
#   echo $pic' '$txt
#   newp=$st$n'.jpg'
#   newt=$st$n'.txt'
#   echo $newp' '$newt
# #   echo $a

#   mv $dir$pic $dir$newp
#   mv $dir$txt $dir$newt
#   n=$((n + 1))


# done
