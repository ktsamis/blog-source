#!/bin/bash
cd output
git init
git remote add output https://github.com/tsamis73/tsamis73.github.io.git
git add *
#echo -n "Give the commit message:   "
#read commit
git commit -a #-m "$commit"
git push output master -f
