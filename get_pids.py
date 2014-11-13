import sys
import psutil

def get_pids(s):
#returns a list of the worker PID(s) from a deamon process

    process_name = s
    parent_pid = 0

    pid_list = []

    #find parent PID
    for p in psutil.process_iter():
        parent_found = False
        if p.ppid() == 1 and (process_name in p.name()):
            parent_pid = p.pid
            parent_found = True
            break

    # TODO(richlee33): There is a possibility that parent_found is not defined
    if not parent_found:
        print 'daemon ' + s + ' not found'
    #find children of parent PID
    else: 
        # process_iter is called twice, you can cache this for efficiency
        for p in psutil.process_iter():
            if p.ppid() == parent_pid:
                pid_list.append(p.pid)
        if len(pid_list) == 0:
            print 'daemon ' + s + ' has no worker processes'

    return pid_list

