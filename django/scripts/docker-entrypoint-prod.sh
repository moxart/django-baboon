#!/bin/sh

gunicorn baboon.wsgi:application --bind 0.0.0.0:8002
