#!/usr/bin/env python3

## std library imports on top
import os

## 3rd party imports below
import paramiko

## work assigned to a junior programming asset on our team
from jrprogrammer import cmdissue

def other_input():
    ip_users = []
    while True:
        ip_user = input('Enter IP and username to use: ')
        if ip_user == 'done':
            break
        ip_users.append(ip_user.split())
    return ip_users

def funct():
  our_commands = input('Enter Commands: ')
  return our_commands.split(',')
    

def main():
  ## create session object
  sshsession = paramiko.SSHClient()
  sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
  
  ## create SSH connection
  sshsession.connect(hostname='10.10.2.3', username='bender', pkey=mykey)
  
  ip_users = other_input()

  print(ip_users)

  our_commands = funct()
  
  for x in our_commands:
    ## call our imported function and save the value returned
    resp = cmdissue(x, sshsession)
    ## if returned response is not null, print it out
    if resp != "":
      print(resp)
 
  with open('results.log', 'w') as f:
      f.write(resp)

  ## end the SSH connection
  sshsession.close()

if __name__ == '__main__':
  main()

