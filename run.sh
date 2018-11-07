#!/bin/bash

sudo git pull origin master
sudo nohup python3 manage.py runserver 0.0.0.0:80
