# basedir           = C:\Users\i051108\Documents\github.aequologica.net
# url               = file:./topological-github.aequologica.net.json
# activeProjects    = None
# activePhases      = ['verify']
# includes          = None
# excludes          = None
# includeProperties = None
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
# /////////////////////////////// verify
# ======================= holos
pushd C:\Users\i051108\Documents\github.aequologica.net\holos
git checkout develop
mvn -Psonatype-oss-release clean install -DskipTests
git checkout master
mvn -Psonatype-oss-release clean install -DskipTests
git checkout develop
popd
# ======================= geppaequo
pushd C:\Users\i051108\Documents\github.aequologica.net\geppaequo
git checkout develop
mvn -Psonatype-oss-release clean install -DskipTests
git checkout master
mvn -Psonatype-oss-release clean install -DskipTests
git checkout develop
popd
# ======================= parole
pushd C:\Users\i051108\Documents\github.aequologica.net\parole
git checkout develop
mvn -Psonatype-oss-release clean install -DskipTests
git checkout master
mvn -Psonatype-oss-release clean install -DskipTests
git checkout develop
popd
# ======================= buildhub
pushd C:\Users\i051108\Documents\github.aequologica.net\buildhub
git checkout develop
mvn -Psonatype-oss-release clean install -DskipTests
git checkout master
mvn -Psonatype-oss-release clean install -DskipTests
git checkout develop
popd
# ======================= dagr
pushd C:\Users\i051108\Documents\github.aequologica.net\dagr
git checkout develop
mvn -Psonatype-oss-release clean install -DskipTests
git checkout master
mvn -Psonatype-oss-release clean install -DskipTests
git checkout develop
popd
# ======================= chat
pushd C:\Users\i051108\Documents\github.aequologica.net\chat
git checkout develop
mvn -Psonatype-oss-release clean install -DskipTests
git checkout master
mvn -Psonatype-oss-release clean install -DskipTests
git checkout develop
popd
# ======================= shakuntala
pushd C:\Users\i051108\Documents\github.aequologica.net\shakuntala
git checkout develop
mvn -Psonatype-oss-release clean install -DskipTests
git checkout master
mvn -Psonatype-oss-release clean install -DskipTests
git checkout develop
popd
# ======================= runciter
pushd C:\Users\i051108\Documents\github.aequologica.net\runciter
git checkout develop
mvn -Psonatype-oss-release clean install -DskipTests
git checkout master
mvn -Psonatype-oss-release clean install -DskipTests
git checkout develop
popd
# -------------------------------
# /////////////////////////////// skipped phase release_start ( active phases are ['verify'] )
# /////////////////////////////// skipped phase intermediate_publish ( active phases are ['verify'] )
# /////////////////////////////// skipped phase release_finish ( active phases are ['verify'] )
# /////////////////////////////// skipped phase publish ( active phases are ['verify'] )
# /////////////////////////////// skipped phase prepare_next ( active phases are ['verify'] )
# ####################################### : #######################################
