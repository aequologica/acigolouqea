# basedir           = C:\Users\i051108\Documents\github.aequologica.net
# url               = file:./topological-github.aequologica.net.json
# activeProjects    = None
# activePhases      = ['prepare_next']
# includes          = ['net.aequologica.neo:*']
# excludes          = None
# includeProperties = ['geppaequo.version']
# excludeProperties = None
# minor             = False
# major             = False
# --------------------------------------- topological ['github.aequologica.net', 'holos', 'geppaequo', 'parole', 'buildhub', 'dagr', 'chat', 'shakuntala', 'runciter']
# --------------------------------------- directories ['holos', 'geppaequo', 'parole', 'buildhub', 'dagr', 'chat', 'shakuntala', 'runciter']
# holos
# 	 {"a_current": "0.3.3-SNAPSHOT", "b_release": "0.3.3", "c_next": "0.3.4-SNAPSHOT"}
# geppaequo
# 	 {"a_current": "0.3.3-SNAPSHOT", "b_release": "0.3.3", "c_next": "0.3.4-SNAPSHOT"}
# parole
# 	 {"a_current": "0.3.3-SNAPSHOT", "b_release": "0.3.3", "c_next": "0.3.4-SNAPSHOT"}
# buildhub
# 	 {"a_current": "0.3.3-SNAPSHOT", "b_release": "0.3.3", "c_next": "0.3.4-SNAPSHOT"}
# dagr
# 	 {"a_current": "0.3.3-SNAPSHOT", "b_release": "0.3.3", "c_next": "0.3.4-SNAPSHOT"}
# chat
# 	 {"a_current": "0.3.3-SNAPSHOT", "b_release": "0.3.3", "c_next": "0.3.4-SNAPSHOT"}
# shakuntala
# 	 {"a_current": "0.3.3-SNAPSHOT", "b_release": "0.3.3", "c_next": "0.3.4-SNAPSHOT"}
# runciter
# 	 {"a_current": "0.3.3-SNAPSHOT", "b_release": "0.3.3", "c_next": "0.3.4-SNAPSHOT"}
# --------------------------------------- w/snapshots ['holos', 'geppaequo', 'parole', 'buildhub', 'dagr', 'chat', 'shakuntala', 'runciter']
# #################################### dry run ###################################
# /////////////////////////////// skipped phase verify ( active phases are ['prepare_next'] )
# /////////////////////////////// skipped phase release_start ( active phases are ['prepare_next'] )
# /////////////////////////////// skipped phase intermediate_publish ( active phases are ['prepare_next'] )
# /////////////////////////////// skipped phase release_finish ( active phases are ['prepare_next'] )
# /////////////////////////////// skipped phase publish ( active phases are ['prepare_next'] )
# /////////////////////////////// prepare_next
# ======================= holos
pushd C:\Users\i051108\Documents\github.aequologica.net\holos
mvn -Psonatype-oss-release -DexcludeReactor=true -DallowSnapshots=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_snapshot_artifacts -DpushChanges=false
mvn -Psonatype-oss-release clean install -DskipTests
git push origin develop
popd
# ======================= geppaequo
pushd C:\Users\i051108\Documents\github.aequologica.net\geppaequo
mvn -Psonatype-oss-release -DexcludeReactor=true -DallowSnapshots=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_snapshot_artifacts -DpushChanges=false
mvn -Psonatype-oss-release clean install -DskipTests
git push origin develop
popd
# ======================= parole
pushd C:\Users\i051108\Documents\github.aequologica.net\parole
mvn -Psonatype-oss-release -DexcludeReactor=true -DallowSnapshots=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_snapshot_artifacts -DpushChanges=false
mvn -Psonatype-oss-release clean install -DskipTests
git push origin develop
popd
# ======================= buildhub
pushd C:\Users\i051108\Documents\github.aequologica.net\buildhub
mvn -Psonatype-oss-release -DexcludeReactor=true -DallowSnapshots=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_snapshot_artifacts -DpushChanges=false
mvn -Psonatype-oss-release clean install -DskipTests
git push origin develop
popd
# ======================= dagr
pushd C:\Users\i051108\Documents\github.aequologica.net\dagr
mvn -Psonatype-oss-release -DexcludeReactor=true -DallowSnapshots=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_snapshot_artifacts -DpushChanges=false
mvn -Psonatype-oss-release clean install -DskipTests
git push origin develop
popd
# ======================= chat
pushd C:\Users\i051108\Documents\github.aequologica.net\chat
mvn -Psonatype-oss-release -DexcludeReactor=true -DallowSnapshots=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_snapshot_artifacts -DpushChanges=false
mvn -Psonatype-oss-release clean install -DskipTests
git push origin develop
popd
# ======================= shakuntala
pushd C:\Users\i051108\Documents\github.aequologica.net\shakuntala
mvn -Psonatype-oss-release -DexcludeReactor=true -DallowSnapshots=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_snapshot_artifacts -DpushChanges=false
mvn -Psonatype-oss-release clean install -DskipTests
git push origin develop
popd
# ======================= runciter
pushd C:\Users\i051108\Documents\github.aequologica.net\runciter
mvn -Psonatype-oss-release -DexcludeReactor=true -DallowSnapshots=true versions:update-parent versions:update-properties -DincludeProperties=geppaequo.version versions:use-latest-versions -Dincludes=net.aequologica.neo:*
mvn -Psonatype-oss-release scm:checkin -Dmessage=hooked_to_snapshot_artifacts -DpushChanges=false
mvn -Psonatype-oss-release clean install -DskipTests
git push origin develop
popd
# -------------------------------
# ####################################### : #######################################
