#!/bin/sh
python3 -m uvicorn main:app --port 80 --host 0.0.0.0
