#!/bin/bash

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Don't forget to type 'source venv/bin/activate'"