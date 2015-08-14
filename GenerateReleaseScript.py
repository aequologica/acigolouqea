#!/usr/bin/env python
from os import getcwd, chdir, path
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen
import argparse
import json
import pystache
import semantic_version
import sys
import xml.etree.ElementTree as ET

lifecycle = [
    'verify' ,
    'release_start',
    'intermediate_publish',
    'release_finish',
    'publish',
    'prepare_next'
]

parser = argparse.ArgumentParser()

parser.add_argument("directory",
                    nargs='?',
                    default="C:\\Users\\i051108\\Documents\\github.aequologica.net",
                    help="directory containing all projects to be released")
parser.add_argument("url",
                    nargs='?',
                    default="file:./topological.json",
                    help="url where to grab topological sort of directories")

parser.add_argument("--includes",
                    nargs='*',
                    default=None,
                    help="cf. http://mojo.codehaus.org/versions-maven-plugin/use-latest-versions-mojo.html")
parser.add_argument("--excludes",
                    nargs='*',
                    default=None,
                    help="cf. http://mojo.codehaus.org/versions-maven-plugin/use-latest-versions-mojo.html")
parser.add_argument("--includeProperties",
                    nargs='*',
                    default=None,
                    help="cf. http://mojo.codehaus.org/versions-maven-plugin/update-properties-mojo.html")
parser.add_argument("--excludeProperties",
                    nargs='*',
                    default=None,
                    help="cf. http://mojo.codehaus.org/versions-maven-plugin/update-properties-mojo.html")

parser.add_argument("--project",
                    nargs='*',
                    default=None,
                    help="projects to release. will release all projects contained under directory if absent")
parser.add_argument("--phase",
                    nargs='*',
                    default=None,
                    help="phases to execute; will run all phases if absent; valid phases are "+str(lifecycle)+".")
parser.add_argument("--lifecycle",
                    nargs='?',
                    default='SFSF',
                    help="either SFSF (default), or SSFF [S=Start F=Finish].")
parser.add_argument("--developmentBranchName",
                    nargs='?',
                    default='develop',
                    help="either SFSF (default), or SSFF [S=Start F=Finish].")
parser.add_argument('--minor',
                    action='store_true',
                    default=False,
                    help='when preparing for next development iteration, increment minor version (default version increment is patch).')
parser.add_argument('--major',
                    action='store_true',
                    default=False,
                    help='when preparing for next development iteration, increment major version (default version increment is patch); if both --minor and --major are present, major wins.')
parser.add_argument("--feature",
                    nargs='?',
                    default=None,
                    help="cf. https://bitbucket.org/atlassian/jgit-flow/wiki/goals/feature-start")
args = parser.parse_args()

basedir           = args.directory.rstrip('/')
url               = args.url
activeProjects    = args.project
activePhases      = args.phase
activeLifecycle   = args.lifecycle
developmentBranchName = args.developmentBranchName
includes          = args.includes
excludes          = args.excludes
includeProperties = args.includeProperties
excludeProperties = args.excludeProperties
minor             = args.minor
major             = args.major
feature           = args.feature

f0 = open(str(path.basename(basedir))+'-'+str(activePhases)+'-'+activeLifecycle+'.cmd','w')

print('#', 'basedir           =', basedir                , file=f0)
print('#', 'url               =', url                    , file=f0)
print('#', 'activeProjects    =', activeProjects         , file=f0)
print('#', 'activePhases      =', activePhases           , file=f0)
print('#', 'includes          =', includes               , file=f0)
print('#', 'excludes          =', excludes               , file=f0)
print('#', 'includeProperties =', includeProperties      , file=f0)
print('#', 'excludeProperties =', excludeProperties      , file=f0)
print('#', 'minor             =', minor                  , file=f0)
print('#', 'major             =', major                  , file=f0)
# http://stackoverflow.com/questions/21986104/python-flush-a-print-statement
# sys.stdout.flush()

################################################################

proxy = '-Dhttp.proxyHost=proxy -Dhttp.proxyPort=8080 -Dhttps.proxyHost=proxy -Dhttps.proxyPort=8080 '

clean_install_all_commands = [
    [ 'git', 'checkout', developmentBranchName ],
    [ 'mvn', '-Psonatype-oss-release', '-Dshakuntala=off', 'clean', 'deploy', '-DskipTests'],
    [ 'git', 'checkout', 'master' ],
    [ 'mvn', '-Psonatype-oss-release', '-Dshakuntala=off', 'clean', 'install', '-DskipTests'],
    [ 'git', 'checkout', developmentBranchName ] 
]

clean_install_commands = [
    [ 'mvn', '-Psonatype-oss-release', '-Dshakuntala=off', 'clean', 'install', '-DskipTests']
]

clean_deploy_commands = [
    [ 'mvn', '-Psonatype-oss-release', '-Dshakuntala=off', 'clean', 'deploy', '-DskipTests']
]

version_commands = [
    [ 'mvn', '-Psonatype-oss-release', '-Dshakuntala=off'
           , '-DexcludeReactor=true'
           , 'versions:update-parent'
           , 'versions:update-properties'   , '{{includePropertiesArgument}}'
                                            , '{{excludePropertiesArgument}}'
           , 'versions:use-latest-versions' , '{{includesListArgument}}'
                                            , '{{excludesListArgument}}' ]
   ,[ 'mvn', '-Psonatype-oss-release', '-Dshakuntala=off'
           , 'scm:checkin'                  , '-Dmessage=hooked_to_release_artifacts'
                                            , '-DpushChanges=false' ]
]

version_allow_snapshots_commands = [
    [ 'mvn', '-Psonatype-oss-release', '-Dshakuntala=off'
           , '-DexcludeReactor=true'
           , '-DallowSnapshots=true'
           , 'versions:update-parent'       
           , 'versions:update-properties'   , '{{includePropertiesArgument}}'
                                            , '{{excludePropertiesArgument}}'
           , 'versions:use-latest-versions' , '{{includesListArgument}}'
                                            , '{{excludesListArgument}}' ]
   ,[ 'mvn', '-Psonatype-oss-release', '-Dshakuntala=off'
           , 'scm:checkin'                  , '-Dmessage=hooked_to_snapshot_artifacts'
                                            , '-DpushChanges=false']
]

start_release_commands = [
    [ 'mvn', '-Psonatype-oss-release', '-Dshakuntala=off'
           , '-DallowUntracked=true'
           , 'jgitflow:{{releaseOrFeature}}-start'       
                                            , '-DfeatureName={{feature}}'
                                            , '-DreleaseVersion={{releaseVersion}}'
                                            , '-DdevelopmentVersion={{developmentVersion}}']
]

start_release_commands_allow_snapshots = [
    [ 'mvn', '-Psonatype-oss-release', '-Dshakuntala=off'
           , '-DallowUntracked=true'
           , '-DallowSnapshots'
           , 'jgitflow:{{releaseOrFeature}}-start'       
                                            , '-DfeatureName={{feature}}'
                                            , '-DreleaseVersion={{releaseVersion}}'
                                            , '-DdevelopmentVersion={{developmentVersion}}']

]

finish_release_commands = [
    [ 'mvn', '-Psonatype-oss-release', '-Dshakuntala=off'
           , 'jgitflow:{{releaseOrFeature}}-finish']
]

finish_release_commands_allow_snapshots = [
    [ 'mvn', '-Psonatype-oss-release', '-Dshakuntala=off'
           , '-DallowSnapshots'
           , 'jgitflow:{{releaseOrFeature}}-finish']
]

checkout_develop = [
    [ 'git', 'checkout', developmentBranchName  ]
]

checkout_release = [
    [ 'git', 'checkout', 'release/{{releaseVersion}}'  ]
]

checkout_master = [
    [ 'git', 'checkout', 'master'  ]
]

# cf. http://stackoverflow.com/questions/5150898/git-pushd-popd-i-e-checkout-last-state
checkout_popd = [
    [ 'git', 'checkout', '@{-1}'  ]
]

intermediate_publish_commands = [
   [ 'git', 'push', 'origin', developmentBranchName ]
   ,[ 'git', 'push', 'origin', 'release/{{releaseVersion}}' ]
]

delete_intermediate_publish_commands = [
   [ 'git', 'push', 'origin', ':release/{{releaseVersion}}' ]
]

publish_commands = [
    [ 'git', 'push', 'origin', 'master'  ]
   ,[ 'git', 'push', 'origin', developmentBranchName ]
   ,[ 'git', 'push', '--tags'            ]
]

prepare_next_iteration_commands = [
    [ 'mvn', '-Psonatype-oss-release', '-Dshakuntala=off', 'clean', 'install', '-DskipTests' ]
   ,[ 'git', 'push', 'origin', developmentBranchName ]
]

phases = {
    'SFSF' : {
        'verify'               : [ clean_install_all_commands ],
        'release_start'        : [],
        'release_finish'       : [ version_commands, start_release_commands, finish_release_commands ],
        'intermediate_publish' : [],
        'publish'              : [ publish_commands ],
        'prepare_next'         : [ version_allow_snapshots_commands, prepare_next_iteration_commands ]
    },
    'SSFF': {
        'verify'               : [    clean_install_commands
                                 ],
        'release_start'        : [    start_release_commands_allow_snapshots,
                                      checkout_develop,
                                        version_allow_snapshots_commands,
                                      checkout_popd
                                 ],
        'intermediate_publish' : [    checkout_develop,
                                        clean_deploy_commands,
                                      checkout_popd,
                                      intermediate_publish_commands
                                 ],
        'release_finish'       : [    checkout_release,
                                        version_commands,
                                      checkout_develop,
                                        version_commands,
                                      checkout_popd,
                                      finish_release_commands,
                                      checkout_develop,
                                        version_allow_snapshots_commands,
                                        clean_install_commands,
                                 ],
        'publish'              : [    delete_intermediate_publish_commands,
                                      publish_commands,
                                 ],
        'prepare_next'         : []
    }
}

# print('#, phases)

versions = {} # will be generated in the call to checkVersion(existing)

class Three:
    def __init__(self, current, release, next):
        self.current = current
        self.release = release
        self.next    = next

    def __str__(self):
        return json.dumps({'a_current':self.current, 'b_release':self.release, 'c_next':self.next, }, sort_keys=True)

def getVersion(project):
    pom = Path(project, 'pom.xml')
    if not pom.exists() :
        print('#', pom, 'not found')
        sys.stdout.flush()
        return False

    # cf. http://bugs.python.org/issue18304
    it = ET.iterparse(str(pom))
    for _, el in it:
        el.tag = el.tag.split('}', 1)[1]  # strip all namespaces

    root = it.root
    return root.find('version').text

def getTopologicalSort(url) :
    # cf. https://docs.python.org/3.4/howto/urllib2.html
    req = Request(url)

    try:
        print ('#', '###################################### fetching topological sort from |', url , '|')
        sys.stdout.flush()
        response = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            print('#', '\tWe failed to reach |', url, '|')
            print('#', '\tReason: ', e.reason)
        elif hasattr(e, 'code'):
            print('#', '\tThe server couldn\'t fulfill the request |', url, '|')
            print('#', '\tError code: ', e.code)
        sys.stdout.flush()
        sys.exit()
    else:
        topo = response.read().decode("utf-8")
        return json.loads(topo)

def createArgument(key, value):
    if value is None:
        return ''
    else :
        return '-D' + key + '=' + ','.join(x.strip() for x in value)


def writeCommandsInDirectory(directory, array_of_array_of_commands, f1):
    original_working_directory = getcwd()  # remember our original working directory
    try :
        chdir(str(directory))
        print ('#', "=======================", path.basename(getcwd()), file=f1)
        print('pushd '+str(directory), file=f1);
        sys.stdout.flush()
        for array_of_commands in array_of_array_of_commands :
            if len(array_of_commands) > 0:
                for command in array_of_commands :
                    # currentVersion     = versions.get(directory.name).current
                    releaseVersion     = versions.get(directory.name).release
                    developmentVersion = versions.get(directory.name).next
                    rendered = [not_empty for not_empty in
                                    [   pystache.render(arg, {
                                                              'releaseOrFeature'          : 'feature' if feature else 'release',
                                                              'feature'                   : feature,
                                                              'releaseVersion'            : releaseVersion,
                                                              'developmentVersion'        : developmentVersion,
                                                              'includesListArgument'      : createArgument('includes', includes),
                                                              'excludesListArgument'      : createArgument('excludes', excludes),
                                                              'includePropertiesArgument' : createArgument('includeProperties', includeProperties),
                                                              'excludePropertiesArgument' : createArgument('excludeProperties', excludeProperties)
                                                              })
                                     for arg in command
                                     ] if not_empty
                                ]
                    # write command
                    print(' '.join(rendered), file=f1)
        return True
    finally:
        print('popd', file=f1);
        chdir(original_working_directory)

def increment(version, major=False, minor=False, patch=True):
    """
    Increment a semantic version

    :param version: str of the version to increment
    :param major: bool specifying major level version increment
    :param minor: bool specifying minor level version increment
    :param patch: bool specifying patch level version increment
    :return: str of the incremented version
    """
    version = semantic_version.Version(str(version))
    if major:
        version.major += 1
        version.minor = 0
        version.patch = 0
    elif minor:
        version.minor += 1
        version.patch = 0
    elif patch:
        version.patch += 1

    return version

def toRelease(version):
    version = semantic_version.Version(str(version))
    version.build = None
    return version

def toSnapshot(version):
    version = semantic_version.Version(str(version))
    version.build = None
    return version;

def checkVersion(project, f3):
    version = getVersion(project)
    wasSnapshot = False
    if version.endswith('-SNAPSHOT'):
        wasSnapshot = True
        version = version[:-9]
    if not version :
        sys.exit()
    else :
        v = semantic_version.Version(version)
        r = toRelease(v)
        if major:
            n = toSnapshot(increment(v, major=True))
        elif minor:
            n = toSnapshot(increment(v, minor=True))
        else :
            n = toSnapshot(increment(v))

        oldVersion = str(v)
        newVersion = str(n)
        if wasSnapshot:
            oldVersion = oldVersion + '-SNAPSHOT'
            newVersion = newVersion + '-SNAPSHOT'
        versions[project.name] = Three(oldVersion, str(r), newVersion)
        print ('#', project.name, file=f3)
        print ('#', '\t', versions[project.name], file=f3)
        sys.stdout.flush()
        return wasSnapshot

if activeProjects == None or len(activeProjects) > 1 :
    topologicalSort = getTopologicalSort(url)
else :
    topologicalSort = activeProjects
print('#', '---------------------------------------', 'topological', topologicalSort, file=f0)

directories = [Path(basedir, subdir) for subdir in topologicalSort]
existings = [ directory for directory in directories if directory.exists() ]
print('#', '---------------------------------------', 'directories', [existing.name for existing in existings], file=f0)

existingSnapshots = [ existing for existing in existings if checkVersion(existing, f0) ]
print('#', '---------------------------------------', 'w/snapshots', [existingSnapshot.name for existingSnapshot in existingSnapshots], file=f0)

print('#', '#################################### dry run ###################################', file=f0)
for phase in lifecycle :
    if activePhases != None:
        if not phase in activePhases :
            print('#', '///////////////////////////////', 'skipped phase', phase, '( active phases are', activePhases, ')', file=f0)
            continue
    print('#', '///////////////////////////////', phase, file=f0)
    array_of_array_of_commands = phases[activeLifecycle].get(phase)
    for project in existingSnapshots :
        if activeProjects != None:
            if not project.name in activeProjects :
                print('#', '///////////////////////////////', 'skipped project', project.name, '( active projects are', activeProjects, ')', file=f0)
                continue
        if not writeCommandsInDirectory(project, array_of_array_of_commands, f0) :
            sys.exit()
    print('#', '-------------------------------', file=f0)
print('#', '####################################### : #######################################', file=f0)
f0.close() #
print ('#######################################', f0.name, 'generated!')
