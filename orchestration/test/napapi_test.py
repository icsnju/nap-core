from __future__ import print_function
from __future__ import print_function
from orchestration.nap_api import app_info

print(app_info.project_list('test', 0, 10))
print(app_info.service_list('test', 'test'))
#
# app_info.destroy_project('test', 'test')
#
# print(app_info.project_list('test', 0, 10))
# print(app_info.service_list('test', 'test'))
