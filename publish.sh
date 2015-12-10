#!/bin/bash
cd output
git init
git remote add output https://github.com/tsamis73/tsamis73.github.io.git
git add *
git commit -a 
git push output master -f
