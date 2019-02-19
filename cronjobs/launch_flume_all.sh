#!/bin/bash

flume-ng agent --conf /etc/flume-ng/conf --conf-file /home/training/test/conf/twitter_all.conf --name twitter -Dflume.root.logger=INFO,console &
