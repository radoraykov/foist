from subprocess import call
import os
import tempfile
import shutil
try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve


def to_html(url, input_fmt, binary_path):
    dir = tempfile.mkdtemp()
    output_fmt = 'html'
    input_path = os.path.join(dir, 'input.' + input_fmt)
    output_filename = 'output.' + output_fmt
    output_path = os.path.join(dir, output_filename)
    urlretrieve(url, input_path)
    call([binary_path, '--dest-dir', dir, '--embed-javascript', '0', input_path, output_filename])

    try:
        return open(output_path).read()
    finally:
        shutil.rmtree(dir)