# encoding: utf-8
"""
author: yangyi@youzan.com
time: 2018/4/26 下午4:34
func: 获取数据库中没有设置ttl的 key
"""
import redis
import argparse
import time

def check_ttl(redis_conn, no_ttl_file, dbindex):
    start_time = time.time()
    no_ttl_num = 0
    keys_num = redis_conn.dbsize()
    print("there are {num} keys in db {index} ".format(num=keys_num, index=dbindex))
    process_count = 1
    with open(no_ttl_file, 'a') as f:

        for key in redis_conn.scan_iter(count=1000):
            percent = '%.2f' % (process_count * 100.0 / keys_num) + '%'
            process_count += 1
            print( '\r', "目前进展:", percent, "已经扫描的key数量:", process_count, end="" )
            if redis_conn.ttl(key) == -1:
                no_ttl_num += 1
                if no_ttl_num < 1000:
                    f.write(key.decode()+'\n')
            else:
                continue

    print("cost time(s):", time.time() - start_time)
    print("no ttl keys number:", no_ttl_num)
    print("we write keys with no ttl to the file: %s" % no_ttl_file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=int, dest='port', action='store', help='port of redis ')
    parser.add_argument('-d', type=str, dest='db_list', action='store', default=0,
                        help='ex : -d all / -d 1,2,3,4 ')
    args = parser.parse_args()
    port = args.port
    if args.db_list == 'all':
        db_list = [i for i in xrange(0,16)]
    else:
        db_list = [int( i ) for i in str( args.db_list ).split( ',' )]

    for index in db_list:
        try:
            pool = redis.ConnectionPool( host="192.168.37.8", port=6379, db=index,
                                         password=123 )
            r = redis.StrictRedis(connection_pool=pool)
        except redis.exceptions.ConnectionError as e:
            print(e)
        else:
            no_ttl_keys_file = "../data/{port}_{db}_no_ttl_keys.txt".format(port=port, db=index)
            check_ttl(r, no_ttl_keys_file, index)


if __name__ == '__main__':
    main()
