from subprocess import call
import os
import tempfile
import shutil
try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve


def to_html(url, input_fmt):
    dir = tempfile.mkdtemp()
    output_fmt = 'html'
    input_path = os.path.join(dir, 'input.' + input_fmt)
    output_path = os.path.join(dir, 'output.' + output_fmt)
    urlretrieve(url, input_path)
    call(["pdf2htmlEX", input_path, output_path])

    try:
        return open(output_path).read()
    finally:
        shutil.rmtree(dir)