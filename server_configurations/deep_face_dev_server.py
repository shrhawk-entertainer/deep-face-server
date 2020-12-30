import os

parent_directory = os.getcwd()
chdir = parent_directory
pythonpath = '{path}/env'.format(path=parent_directory)

bind = '127.0.0.1:8099'
timeout = 60
workers = 1
proc_name = 'deep_face_srv'
