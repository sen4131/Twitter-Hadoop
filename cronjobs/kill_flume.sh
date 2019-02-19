#!/bin/bash

kill $(ps aux | grep 'flume' | awk '{print $2}')
