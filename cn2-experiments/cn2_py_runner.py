import time

print('--Run analysis and create NW policy--')
retry_max = 5
retry_cnt = 0
while retry_cnt < retry_max:
  time.sleep(1)
  retry_cnt += 1
  print('processing')
print('Completed')  
