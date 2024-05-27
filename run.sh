#!/bin/bash

rsync -r --delete --exclude venv/ ./ tudor@rpi-tudor.local:/home/tudor/dev/ldlum/

