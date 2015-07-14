#!/usr/bin/env python
import argparse
import os
import pathlib
import pystache
import subprocess
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-d",
                    "--directory",
                    nargs='?',
                    default=".",
                    help="optional directory containing all projects, as direct sub-directories, to be grouped in a module pom. Default is upper directory.")

parser.add_argument("-a",
                    "--artifactId",
                    nargs='?',
                    default="",
                    help="optional extension to be suffixed to upper directory name as module pom artifactId. Default is empty string.")

args = parser.parse_args()

basedir = args.directory
artifactId = args.artifactId

if basedir == '.':
    basedir = os.path.dirname(os.path.realpath(basedir))
    
if artifactId == '':
    artifactId = pathlib.Path(basedir).name
else:
    artifactId = pathlib.Path(basedir).name+'.'+artifactId
    
print("directory  : " + basedir+'\nartifactId : '+artifactId + '\n')

def get_immediate_subdirectories_with_pom_as_modules(directory):
    return [{'module':name} for name in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, name))
            and pathlib.Path(os.path.join(directory, name), 'pom.xml').exists()]
    
class ModulePomFileTemplate(object):
    def groupId(self):
        return "net.aequologica.neo"
    def artifactId(self):
        return artifactId
    def version(self):
        return "1-SNAPSHOT"
    def modules(self):
        return get_immediate_subdirectories_with_pom_as_modules(basedir)

modulePom = ModulePomFileTemplate()
renderer = pystache.Renderer()
print(renderer.render(modulePom))

modulePomFile = os.path.join(basedir, 'modules.pom') 
with open(modulePomFile, 'w') as file_:
    file_.write(renderer.render(modulePom))

# sys.exit(0)  

# running   mvn validate with appropriately configured shakuntala will upload dag to hub
# hub then is able to calculate topological sort that can be downloaded

def runCommand(command):
    try:
        print ("---------------", command)
        sys.stdout.flush()
        subprocess.check_call(command, shell=True)
        return True
    except subprocess.CalledProcessError as e:
        print ('\treturn code:', e.returncode)
        print ('\toutput:', e.output)
        sys.stdout.flush()
        return False
    
def runCommandInDirectory(directory, command):
    original_working_directory = os.getcwd()  # remember our original working directory
    try :
        os.chdir(str(directory))
        print ("=======================", os.path.basename(os.getcwd()))
        sys.stdout.flush()
        return runCommand(command)
    finally:
        os.chdir(original_working_directory)
        
validate = ['mvn', '-f', 'modules.pom', 'validate']

clean = ['mvn', '-f', 'modules.pom', 'clean', '-DskipTests'] 

runCommandInDirectory(basedir, validate)
