#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
import hashlib
import tarfile
import io
import time

__author__ = 'f0x11'


def auth_config(user_id):
    user = str(user_id)
    password = hashlib.md5(str(user_id).encode()).hexdigest()[:4]

    config = '{{"auths": {{"{0}": {{"auth": "{1}", "email": "test@test.com"}}}}}}'\
        .format('222222', base64.b64encode(
            (user + ":" + password).encode()
        ).decode())
    return config


def main():
    with io.BytesIO() as json_file, io.BytesIO() as outfile:
        tar = tarfile.open(mode="w:gz", fileobj=outfile)
        json_file.write(auth_config(111).encode('utf-8'))
        json_file.seek(0)

        info = tarfile.TarInfo(name='.docker')
        info.type = tarfile.DIRTYPE
        info.mode = 0o777
        info.mtime = time.time()
        tar.addfile(tarinfo=info)

        info2 = tarfile.TarInfo(name=".docker/config.json")
        info2.mode = 0o777
        info2.size = len(json_file.getvalue())
        info2.mtime = time.time()
        tar.addfile(info2, json_file)
        tar.close()

        with open("test.tar.gz", "wb") as fp:
            fp.write(outfile.getvalue())


if __name__ == '__main__':
    main()
