#!/bin/bash

docker build . -t iata
docker run iata:latest
