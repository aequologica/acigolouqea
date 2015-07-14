# basedir           = C:\Users\i051108\Documents\github.aequologica.net
# url               = file:./topological-github.aequologica.net.json
# activeProjects    = None
# activePhases      = ['release_finish']
# includes          = ['net.aequologica.neo:*']
# excludes          = None
# includeProperties = ['geppaequo.version']
# excludeProperties = None
# minor             = False
# major             = False
# --------------------------------------- topological ['github.aequologica.net', 'holos', 'geppaequo', 'parole', 'buildhub', 'dagr', 'chat', 'shakuntala', 'runciter']
# --------------------------------------- directories ['holos', 'geppaequo', 'parole', 'buildhub', 'dagr', 'chat', 'shakuntala', 'runciter']
# holos
# 	 {"a_current": "0.3.2-SNAPSHOT", "b_release": "0.3.2", "c_next": "0.3.3-SNAPSHOT"}
# geppaequo
# 	 {"a_current": "0.3.2-SNAPSHOT", "b_release": "0.3.2", "c_next": "0.3.3-SNAPSHOT"}
# parole
# 	 {"a_current": "0.3.2-SNAPSHOT", "b_release": "0.3.2", "c_next": "0.3.3-SNAPSHOT"}
# buildhub
# 	 {"a_current": "0.3.2-SNAPSHOT", "b_release": "0.3.2", "c_next": "0.3.3-SNAPSHOT"}
# dagr
# 	 {"a_current": "0.3.2-SNAPSHOT", "b_release": "0.3.2", "c_next": "0.3.3-SNAPSHOT"}
# chat
# 	 {"a_current": "0.3.2-SNAPSHOT", "b_release": "0.3.2", "c_next": "0.3.3-SNAPSHOT"}
# shakuntala
# 	 {"a_current": "0.3.2-SNAPSHOT", "b_release": "0.3.2", "c_next": "0.3.3-SNAPSHOT"}
# runciter
# 	 {"a_current": "0.3.2-SNAPSHOT", "b_release": "0.3.2", "c_next": "0.3.3-SNAPSHOT"}
# --------------------------------------- w/snapshots ['holos', 'geppaequo', 'parole', 'buildhub', 'dagr', 'chat', 'shakuntala', 'runciter']
# #################################### dry run ###################################
# /////////////////////////////// skipped phase verify ( active phases are ['release_finish'] )
# /////////////////////////////// skipped phase release_start ( active phases are ['release_finish'] )
# /////////////////////////////// skipped phase intermediate_publish ( active phases are ['release_finish'] )
# /////////////////////////////// release_finish
# ======================= holos
pushd C:\Users\i051108\Documents\github.aequologica.net\holos
# # # mvn -Psonatype-oss-release -DexcludeReactor=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
# # # mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_release_artifacts -DpushChanges=false
mvn -Psonatype-oss-release -DallowUntracked=true jgitflow:release-start -DfeatureName=None -DreleaseVersion=0.3.2 -DdevelopmentVersion=0.3.3-SNAPSHOT
mvn -Psonatype-oss-release jgitflow:release-finish
popd
# ======================= geppaequo
pushd C:\Users\i051108\Documents\github.aequologica.net\geppaequo
mvn -Psonatype-oss-release -DexcludeReactor=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_release_artifacts -DpushChanges=false
mvn -Psonatype-oss-release -DallowUntracked=true jgitflow:release-start -DfeatureName=None -DreleaseVersion=0.3.2 -DdevelopmentVersion=0.3.3-SNAPSHOT
mvn -Psonatype-oss-release jgitflow:release-finish
popd
# ======================= parole
pushd C:\Users\i051108\Documents\github.aequologica.net\parole
mvn -Psonatype-oss-release -DexcludeReactor=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_release_artifacts -DpushChanges=false
mvn -Psonatype-oss-release -DallowUntracked=true jgitflow:release-start -DfeatureName=None -DreleaseVersion=0.3.2 -DdevelopmentVersion=0.3.3-SNAPSHOT
mvn -Psonatype-oss-release jgitflow:release-finish
popd
# ======================= buildhub
pushd C:\Users\i051108\Documents\github.aequologica.net\buildhub
mvn -Psonatype-oss-release -DexcludeReactor=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_release_artifacts -DpushChanges=false
mvn -Psonatype-oss-release -DallowUntracked=true jgitflow:release-start -DfeatureName=None -DreleaseVersion=0.3.2 -DdevelopmentVersion=0.3.3-SNAPSHOT
mvn -Psonatype-oss-release jgitflow:release-finish
popd
# ======================= dagr
pushd C:\Users\i051108\Documents\github.aequologica.net\dagr
mvn -Psonatype-oss-release -DexcludeReactor=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_release_artifacts -DpushChanges=false
mvn -Psonatype-oss-release -DallowUntracked=true jgitflow:release-start -DfeatureName=None -DreleaseVersion=0.3.2 -DdevelopmentVersion=0.3.3-SNAPSHOT
mvn -Psonatype-oss-release jgitflow:release-finish
popd
# ======================= chat
pushd C:\Users\i051108\Documents\github.aequologica.net\chat
mvn -Psonatype-oss-release -DexcludeReactor=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_release_artifacts -DpushChanges=false
mvn -Psonatype-oss-release -DallowUntracked=true jgitflow:release-start -DfeatureName=None -DreleaseVersion=0.3.2 -DdevelopmentVersion=0.3.3-SNAPSHOT
mvn -Psonatype-oss-release jgitflow:release-finish
popd
# ======================= shakuntala
pushd C:\Users\i051108\Documents\github.aequologica.net\shakuntala
mvn -Psonatype-oss-release -DexcludeReactor=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_release_artifacts -DpushChanges=false
mvn -Psonatype-oss-release -DallowUntracked=true jgitflow:release-start -DfeatureName=None -DreleaseVersion=0.3.2 -DdevelopmentVersion=0.3.3-SNAPSHOT
mvn -Psonatype-oss-release jgitflow:release-finish
popd
# ======================= runciter
pushd C:\Users\i051108\Documents\github.aequologica.net\runciter
mvn -Psonatype-oss-release -DexcludeReactor=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_release_artifacts -DpushChanges=false
mvn -Psonatype-oss-release -DallowUntracked=true jgitflow:release-start -DfeatureName=None -DreleaseVersion=0.3.2 -DdevelopmentVersion=0.3.3-SNAPSHOT
mvn -Psonatype-oss-release jgitflow:release-finish
popd
# -------------------------------
# /////////////////////////////// skipped phase publish ( active phases are ['release_finish'] )
# /////////////////////////////// skipped phase prepare_next ( active phases are ['release_finish'] )
# ####################################### : #######################################
