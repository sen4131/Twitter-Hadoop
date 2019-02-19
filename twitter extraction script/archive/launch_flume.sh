#!/bin/bash

flume-ng agent --conf /etc/flume-ng/conf --conf-file /home/training/test/conf/twitter_f.conf --name twitter -Dflume.root.logger=INFO,console &
flume-ng agent --conf /etc/flume-ng/conf --conf-file /home/training/test/conf/twitter_rt_f.conf --name twitter_rt -Dflume.root.logger=INFO,console &
