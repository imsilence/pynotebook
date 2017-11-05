#encoding: utf-8

import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-T', '--type', help="请输入加密类型(str/file)", type=str, choices=['str', 'file'], default='str')
    parser.add_argument('-C', '--content', help="请输入加密字符串或文件路径", type=str, default=[], nargs='+')
    parser.add_argument('-P', '--port', help="请输端口信息", type=int, default=8080)
    args = parser.parse_args()

    print(args)
    print(args.type)
    print(args.content)
    print(args.port)