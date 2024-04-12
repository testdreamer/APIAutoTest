import sys

from Utils.operationyaml import read_yaml
import os

filename = os.path.dirname(__file__)+'/data/test.yaml'
res = read_yaml(filename=filename, keys='body')
print(res)