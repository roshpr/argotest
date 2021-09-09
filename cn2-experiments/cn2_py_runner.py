import time
import sys

if sys.argv[1]:
  val = sys.argv[1]
else:
  val = 'No inputs'
print('--Run analysis and create NW policy: inputs {}--'.format(val))
retry_max = 5
retry_cnt = 0
while retry_cnt < retry_max:
  time.sleep(1)
  retry_cnt += 1
  print('processing')
print('Completed')  
