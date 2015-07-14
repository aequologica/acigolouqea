#!/usr/bin/env python
# from json import loads 
from os import getcwd, chdir, path, environ
from pathlib import Path
from subprocess import check_call, CalledProcessError, Popen, PIPE  
import argparse
import re
import sys
import shutil
from contextlib import contextmanager

superenviron = environ.copy()

# superenviron['shakuntala.uuid'] = str(uuid.uuid4())

parser = argparse.ArgumentParser()

parser.add_argument("commands",
                    nargs='?',
                    default="commands.cmd",
                    help="file containing all commands to be run")
parser.add_argument("groupId",
                    nargs='?',
                    default=None,
                    help="will clean everything under this groupId in maven *local* repository")

parser.add_argument('--dryRun',
                    action='store_true', 
                    default=False,
                    help='Dry run: don\'t checkin or tag anything in the scm repository, or modify the checkout.')

args = parser.parse_args()

commands = args.commands
groupId  = args.groupId
dryrun   = args.dryRun

print('#', 'commands =', commands)
print('#', 'groupId  =', groupId)
print('#', 'dryRun   =', dryrun)

mavenLocalRepo = None

def getMavenExpression(expression):
    print('#', 'maven is evaluating the expression \''+expression+'\', please be patient.')
    sys.stdout.flush()
    starts_with_bracket = re.compile("^\[")
    starts_with_Download = re.compile("^Download")
    contains_download_progress = re.compile("\d+\/\d+")
    proc = Popen(['mvn', 'help:evaluate', '-Dexpression='+expression, '-N'], stdout=PIPE, shell=True, universal_newlines=True)
    while proc.poll() is None:
        output = proc.stdout.readline().strip()
        if not output:
            continue
        if starts_with_bracket.match(output):
            continue
        if starts_with_Download.match(output):
            continue
        if contains_download_progress.match(output):
            continue
        theEval = output.replace('\n', '')
        print('#', 'expression', '\''+expression+'\'', 'evaluate to ', '\''+theEval+'\'')
        sys.stdout.flush()
        return theEval
    
def getMavenLocalRepo():
    return getMavenExpression('settings.localRepository')

def getMavenMirrorUrl():
    return getMavenExpression('settings.mirrors[0].url')

def cleanMavenLocalRepo(groupId):
    try:
        mavenLocalRepo
    except NameError:
        mavenLocalRepo = getMavenLocalRepo()
         
    sub = Path(mavenLocalRepo, groupId.replace('.', '/'));
    repo = str(sub)
    if not path.exists(repo):
        print('#', 'no directory at ', repo)
        sys.stdout.flush()
        pass
    else:
        try:
            shutil.rmtree(repo)
            print('#', 'cleaned repo', repo)
            sys.stdout.flush()
        except Exception as e:
            print('#', '--------------- \tException while cleaning repo', repo, ':', e)
            sys.stdout.flush()
        
@contextmanager
def pushd(newDir):
    previousDir = getcwd()
    chdir(newDir)
    print ('pushd', newDir) 
    yield
    print ('popd' ) 
    chdir(previousDir)
    
def runCommand(indent, command):
    try:
        print(indent, command)
        sys.stdout.flush()
        if not dryrun :
            if not '#' in command :
                check_call(command, shell=True, env=superenviron)
        return True
    except CalledProcessError as e:
        print ('#', 'exception!')
        print ('#', 'return code:', e.returncode)
        print ('#', 'output:', e.output)
        sys.stdout.flush()
        return False
    
print ('#', '#################################### run ###################################')
sys.stdout.flush()

if groupId :
    cleanMavenLocalRepo(groupId)

lines = [line.strip().split() for line in open(commands)]

batch = []
current = None

for line in lines :
    if "#" in line:
        pass 
#         print ('#', "this is a comment", line)
#         sys.stdout.flush()
    elif line[0] == 'pushd': 
        current = {'dir':line[1], 'cmds':[]}
        batch.append(current) 
    elif line[0] == 'popd':
        current = None
    else : 
        if current != None:
            current['cmds'].append(line)
        else :
            batch.append({'dir':None,'cmds':[line]})
            
for dir_cmds in batch:
    if dir_cmds['dir'] == None :
        for cmds in dir_cmds['cmds'] :
            if not runCommand('', cmds) :
                sys.exit()
    else :
        with pushd(dir_cmds['dir']):
            for cmds in dir_cmds['cmds'] :
                if not runCommand('\t', cmds) :
                    sys.exit()

print ('#', '##################################### : ####################################')
sys.stdout.flush()
