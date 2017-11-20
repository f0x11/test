#!/usr/bin/env python
# encoding: utf-8
import sys

try_encode_list = ['gbk']


def get_utf8_str(content):
    for try_encode in try_encode_list:
        try:
            content = content.decode(try_encode)
            break
        except:
            continue

    try:
        content = content.encode('utf-8')
    except:
        pass

    return content


def get_utf8_str_by_filename(filename):
    with open(filename, 'r') as fp:
        rcontent = fp.read()
        rcontent = get_utf8_str(rcontent)
        with open('rcode_' + filename, 'w') as wp:
            wp.write(rcontent)


def get_gbk_str(content):
    content = content.decode('utf-8').encode('gbk')

    return content


def get_gbk_str_by_filename(filename):
    with open(filename, 'r') as fp:
        rcontent = fp.read()
        rcontent = get_gbk_str(rcontent)
        with open('code_' + filename, 'w') as wp:
            wp.write(rcontent)


if __name__ == '__main__':
    filename = sys.argv[1]
    # get_gbk_str_by_filename(filename)
    get_utf8_str_by_filename(filename)
