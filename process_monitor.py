#!/usr/bin/env python
# TODO(richlee33): for readability, separate system imports from user imports
import sys
import time
import get_pids
import memory_stats
import cpu_stats

#process = 'apache'

# TODO(richlee33): add error checking if no argument is passed
# TODO(richlee33): this should be "process_name" for clarity
process = str(sys.argv[1])

while True:
    list_pids = get_pids.get_pids(process)
    # print (list_pids)
    mem =  memory_stats.memory_average(list_pids)
    cpu = cpu_stats.cpu_usage(list_pids)
    print (process, mem, cpu )
    print '================================='
    time.sleep(30)

