import psutil

def memory_average(l):
    """
    TODO(richlee33):
    This is the normal commenting convention inside a function. This allows
    auto generation of pydoc
    """
#prints average memory RSS and VMS
#input: list of PIDs to use to calculate memory values
#output: dictionary containing average RSS, average VMS and number of workers

    memory_rss_total = 0
    memory_vms_total = 0

    number_workers= len(l)

    if number_workers == 0:
        #do nothing and return
        return

    for pid in l:
        # TODO(richlee33): you should indent 4 spaces
         p = psutil.Process(pid)
         memory_rss_total = memory_rss_total + p.memory_info_ex().rss 
         memory_vms_total = memory_vms_total + p.memory_info_ex().vms
  
    memory_rss_average_mb = (memory_rss_total/number_workers) / (1024**2) 
    memory_vms_average_mb = (memory_vms_total/number_workers) / (1024**2) 

#    print 'number worker processes=' + str(number_workers)
#    print 'memory rss average MB=' + str(memory_rss_average_mb)
#    print 'memory vms average MB=' + str(memory_vms_average_mb)

    memory_stats = {'workers':number_workers, 'rss_ave_mb':memory_rss_average_mb, 
                    'vms_ave_mb':memory_vms_average_mb}

    return memory_stats


