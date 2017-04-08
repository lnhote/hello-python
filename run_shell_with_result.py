import subprocess
# mysql.pid: 540
try:
    pid = subprocess.check_output('cat ./mysql.pid', shell=True)
    pid = int(pid)
    result = subprocess.check_output('ps %d' % pid, shell=True)
    print 'pid = ', pid, 'result:\n', result
except subprocess.CalledProcessError as e:
    print 'Process %d does not exist.' % int(pid)
