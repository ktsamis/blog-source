#!/bin/bash
pelican content/ > /dev/null
if [ "$?" -ne "0" ];then
  echo "Pelican is not installed or did not convert /content to /output"
  exit
fi
cd output
git init
git remote add output https://github.com/tsamis73/tsamis73.github.io.git
git add *
git commit -a 
git push output master -f
if [ "$?" -eq "0" ];then                                                                                                                                                                                           
  echo "Push to output completed"
fi
cd ..
git add *
git commit -a
git push origin master

