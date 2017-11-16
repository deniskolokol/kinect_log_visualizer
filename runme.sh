#!/bin/bash

tmux new-session -d 'python fakinect.py'
tmux split-window -h 'python display.py'
tmux split-window -v 'htop -d 2'
# tmux split-window -v 'top'
tmux select-pane -L
tmux split-window -v '~/Documents/OpenNI/OSCeleton/osceleton -a 192.168.1.132 -p 57120 -r'
tmux resize-pane -D 15
tmux select-pane -R
tmux select-pane -U
tmux set status-style "bg=black"
tmux -2 attach-session -d
