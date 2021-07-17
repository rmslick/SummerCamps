#!/usr/bin/env python3
import os 

# make directory
cwd = os.getcwd()
projectName = input("Project name: ").replace(" ","")
projDir = os.path.join(cwd,projectName)
os.mkdir(projDir)

