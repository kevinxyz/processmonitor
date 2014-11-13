# Processmonitor
This project shows the average memory use and the combined cpu usage for 
multiple worker processes. This is useful to track the health of the worker 
processes of Apache or Nginx.

## How It Works
Worker PIDs are found for the process named in the command line.  
Resident set size and the virtual memory size is the average of all the worker PIDs.  
Total cpu percent consumed is the sum of the cpu percent consumed for each worker processes.  
Percent cpu consumed is calculated for each PID by examining the system and user cpu cycles consumed at 2 points in time.  
In order to calculate cpu percent used, a small file is written on disk for each worker process.  
The next time the cpu_usage function is called, it compares the current number of cpu cycles consumed with the file on disk, which is the prior number of cpu cycles consumed.  

## How to Run

Set up environment:  

    git clone <repo url>  
    cd processmonitor  
    virtualenv . --no-site-packages  
    source bin/activate  
    pip install -r requirements.txt  

Run program:  

    python process_monitor.py apache  

Sample output (indented for you for readability):

    ('apache', {'rss_ave_mb': 3, 'workers': 3, 'vms_ave_mb': 224}, {})
    =================================
    ('apache', {'rss_ave_mb': 3, 'workers': 3, 'vms_ave_mb': 224}, 
     {'total_consumed_user_cycles': 764, 
      'total_consumed_system_cycles': 1201, 
      'total_percent_consumed': 64.27766263206821})
    =================================
    ('apache', {'rss_ave_mb': 3, 'workers': 3, 'vms_ave_mb': 224}, 
     {'total_consumed_user_cycles': 748, 
      'total_consumed_system_cycles': 1238, 
      'total_percent_consumed': 66.01126687283042})
    =================================
