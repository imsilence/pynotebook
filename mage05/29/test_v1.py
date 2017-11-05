#encoding: utf-8

import requests
import time

if __name__ == '__main__':
    uuid = '1' * 32
    total = 0
    total_error = 0
    cnt = 10
    per = 500
    for idx in range(cnt):
        s = time.time()
        error = 0
        for _ in range(per):
            response = requests.post('http://localhost:8090/api/v1/client/{uuid}/'.format(uuid=uuid), json={'hostname': 'test_v1'})
            error += 0 if response.ok else 1
        e = time.time()
        print('{}:{}:{}'.format(idx, e - s, error))
        total_error += error
        total += e - s
    print('avg:{}:{}'.format(total / cnt, total_error))