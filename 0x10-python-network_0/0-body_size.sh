#!/bin/bash
# script that checks the body size of a req
curl -sI $1 | grep "Content-Length:" | cut -d' ' -f2
