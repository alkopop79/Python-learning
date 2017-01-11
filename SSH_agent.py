#!/usr/bin/env python

import paramiko

ssh=paramiko.SSHClient()
ssh.connect('192.168.0.20',username='pi',password='pombat79')
