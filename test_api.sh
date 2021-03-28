#!/bin/bash

METHOD=$1
URL=$2

if [ $METHOD = GET ]; do
    curl -X GET -H "Content-Type: application/json"
