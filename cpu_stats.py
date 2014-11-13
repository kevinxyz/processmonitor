import time
import os

def cpu_usage(l):

    cycles_per_sec = 100

    #run $nproc to find number of CPUs
    number_cpus = 1

    stats = {'total_percent_consumed' : 0.0, 
             'total_consumed_user_cycles' : 0,
             'total_consumed_system_cycles' : 0}

    # TODO(richlee33): This check should be hoisted all the way up to indicate
    #                  early termination case.
    #check for an empty list of PIDs
    if len(l) == 0:
        #do nothing and return out
        # TODO(richlee33): if another variable is set to cpu_usage(l), you should
        #                  explicitly return a "None" to tell the reader that
        #                  this function returns something.
        return

    for pid in l:
        cpu_current = get_cpu_proctable(pid)
        cpu_prior = get_cpu_prior_file(pid)

        if ('timestamp' in cpu_current) and ('timestamp' in cpu_prior):
            elapsed_time_sec = cpu_current['timestamp'] - cpu_prior['timestamp']
            consumed_user_cycles = cpu_current['user'] - cpu_prior['user']
            consumed_system_cycles = cpu_current['system'] - cpu_prior['system']
            total_consumed_cycles = consumed_user_cycles + consumed_system_cycles
            available_cycles = elapsed_time_sec * cycles_per_sec * number_cpus
            percent_consumed = total_consumed_cycles / available_cycles * 100
            
            #add up percent used cycles for all process
            stats['total_percent_consumed'] += percent_consumed
            stats['total_consumed_user_cycles'] += consumed_user_cycles
            stats['total_consumed_system_cycles'] += consumed_system_cycles

        else:
            #empty out the stats dictionary since there is nothing to report
            stats = {}

        #write a new cpu file
        write_cpu_file(pid,cpu_current)

    #end for loop
    return stats


def get_cpu_proctable(i):
#gets the consumed user and system cpu cycles for a PID for a point in time
#input: integer representing a PID
#output: dictionary containing consumed user & system cpu cycles and timestamp

    stats = {}
    proc_file = '/proc/' + str(i) + '/stat'

    if os.path.isfile(proc_file):
        current_time = time.time()
        with open(proc_file, 'r') as f:
            content = f.readline()
        parsed = content.split()
        stats['timestamp'] = current_time 
        stats['user'] = int(parsed[13])
        stats['system'] = int(parsed[14])
    else:
        print 'invalid PID, no entry in proctable'

    return stats


def get_cpu_prior_file(i):
#gets the consumed user and system cpu cycles from a prior point in time
#from a file on the file system.
#input: integer representing a PID
#output: dictionary containing consumed user & system cpu cycles and timestamp

    stats = {}
    cpu_file = '/tmp/' + str(i)

    if os.path.isfile(cpu_file):
        with open(cpu_file, 'r') as f:
            content = f.readline()
        parsed = content.split()
        # TODO(richlee33): For simplicity, you can just read a json content
        #                  like below, in one line (see write_cpu_file):
        #                  stats = json.loads(parsed)
        stats['timestamp'] = float(parsed[0])
        stats['user'] = int(parsed[1])
        stats['system'] = int(parsed[2])
        # As a side note, it is very bad practice to have to use indices to
        # keep state in a file, because if you need to add/remove new
        # parameters, you need to make sure to do it to all the places that
        # use the file (get_cpu_prior_file and write_cpu_file).

    return stats


# TODO(richlee33): d is a very poor naming convention, it does not convey types
#                  and forces the reader to look ahead further to understand
#                  what it is.
def write_cpu_file(i,d):

    cpu_file = '/tmp/' + str(i)
        
    if ('timestamp' in d): 
        f = open(cpu_file, 'w')
        # TODO(richlee33): You should just use json for simplicity. Like the
        #                  following in just one line:
        #                  f.write(json.dumps(d))
        f.write (str(d['timestamp']) + ' ' + str(d['user']) 
                                     + ' ' +str(d['system']))
        f.close()

    return

