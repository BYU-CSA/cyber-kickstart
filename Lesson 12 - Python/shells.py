import pexpect

flag = "ctf{im sure this sucks}"

shell = pexpect.spawn("sh")
shell.setecho(False) # disable printing output of shell commands
shell.sendline("FLAG=\""+flag+"\"") # place flag in shell variable of first shell

TOTAL_SHELLS = 2

for i in range(TOTAL_SHELLS):
    shell.sendline("set -o ignoreeof") # disables CTRL+D
    shell.sendline("sh") # spawn new shell
    shell.sendline("FLAG='you are currently "+str(i+1)+" levels of "+str(TOTAL_SHELLS)+" deep'") # put the level in the FLAG variable on the shell

shell.setecho(True)
shell.interact()