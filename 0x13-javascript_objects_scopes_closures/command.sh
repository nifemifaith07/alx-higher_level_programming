#!/usr/bin/bash

chmod u+x *.js
semistandard --fix
git add .
git commit -m 'quick fix'
git push
