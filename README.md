# acigolouqea

## 1. create module pom and topological sort

```
usage: CreateModulePom.py [-h] [-d [DIRECTORY]] [-a [ARTIFACTID]]

optional arguments:
  -h, --help            show this help message and exit
  -d [DIRECTORY], --directory [DIRECTORY]
                        optional directory containing all projects, as direct
                        sub-directories, to be grouped in a module pom.
                        Default is upper directory.
  -a [ARTIFACTID], --artifactId [ARTIFACTID]
                        optional extension to be suffixed to upper directory
                        name as module pom artifactId. Default is empty
                        string.
```

## 2. generate script(s)

```
usage: GenerateReleaseScript.py [-h] [--includes [INCLUDES [INCLUDES ...]]]
                                [--excludes [EXCLUDES [EXCLUDES ...]]]
                                [--includeProperties [INCLUDEPROPERTIES [INCLUDEPROPERTIES ...]]]
                                [--excludeProperties [EXCLUDEPROPERTIES [EXCLUDEPROPERTIES ...]]]
                                [--project [PROJECT [PROJECT ...]]]
                                [--phase [PHASE [PHASE ...]]]
                                [--lifecycle [LIFECYCLE]]
                                [--developmentBranchName [DEVELOPMENTBRANCHNAME]]
                                [--minor] [--major] [--feature [FEATURE]]
                                [directory] [url]

positional arguments:
  directory             directory containing all projects to be released
  url                   url where to grab topological sort of directories

optional arguments:
  -h, --help            show this help message and exit
  --includes [INCLUDES [INCLUDES ...]]
                        cf. http://www.mojohaus.org/versions-maven-plugin/use-latest-versions-mojo.html
  --excludes [EXCLUDES [EXCLUDES ...]]
                        cf. http://www.mojohaus.org/versions-maven-plugin/use-latest-versions-mojo.html
  --includeProperties [INCLUDEPROPERTIES [INCLUDEPROPERTIES ...]]
                        cf. http://www.mojohaus.org/versions-maven-plugin/update-properties-mojo.html
  --excludeProperties [EXCLUDEPROPERTIES [EXCLUDEPROPERTIES ...]]
                        cf. http://www.mojohaus.org/versions-maven-plugin/update-properties-mojo.html
  --project [PROJECT [PROJECT ...]]
                        projects to release. will release all projects
                        contained under directory if absent
  --phase [PHASE [PHASE ...]]
                        phases to execute; will run all phases if absent;
                        valid phases are ['verify', 'release_start',
                        'intermediate_publish', 'release_finish', 'publish',
                        'prepare_next'].
  --lifecycle [LIFECYCLE]
                        either SFSF (default), or SSFF [S=Start F=Finish].
  --developmentBranchName [DEVELOPMENTBRANCHNAME]
                        default is 'develop'
  --minor               when preparing for next development iteration,
                        increment minor version (default version increment is
                        patch).
  --major               when preparing for next development iteration,
                        increment major version (default version increment is
                        patch); if both --minor and --major are present, major
                        wins.
  --feature [FEATURE]   cf. https://bitbucket.org/atlassian/jgit-flow/wiki/goals/feature-start

```

## 3. run generated script(s)

```
usage: GeoReleaseScript.py [-h] [--dryRun] [commands] [groupId]

positional arguments:
  commands    file containing all commands to be run
  groupId     optional; will (try to ...) clean everything under this groupId in maven *local*
              repository

optional arguments:
  -h, --help  show this help message and exit
  --dryRun    Dry run: don't checkin or tag anything in the scm repository, or
              modify the checkout.
```

