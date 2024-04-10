import subprocess
#  use pip to show the list of python packages that need to be updated
com_list_o = 'pip list -o' 
#  use subprocess to execute the command and return the result
p = subprocess.Popen(com_list_o, shell=True, stdout=subprocess.PIPE)
#  get the result of the command, which is a binary string containing all the content displayed after we execute pip list -o
out = p.communicate()[0]
#    convert binary to utf-8 string
out = str(out, 'utf-8')

#  need_update, split the package name that needs to be updated and store it in the list need_update
need_update = []
for i in out.splitlines()[2:]:
    need_update.append(i.split(' ')[0])

# execute the upgrade command, take one package for upgrade each time, pip only supports upgrading one package at a time
for nu in need_update:
    com_update = 'pip install -U {py}'.format(py=nu)
    print("execute the upgrade command:", com_update)
    subprocess.call(com_update)
    print("----------{com} Execution ends-----------\n".format(com=com_update))


print("check for updates:")
subprocess.call(com_list_o)
