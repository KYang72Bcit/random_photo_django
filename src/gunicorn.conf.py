import multiprocessing

bind = '0.0.0.0:8000'

workers = multiprocessing.cpu_count() * 2 + 1

backlog = 2048

work_class = 'gevent'

proc_name = 'project' # process name

pidfile = '/tmp/project.pid' # the process working direcotry

timeout = 30  
max_requests = 6000    
