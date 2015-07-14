#!/bin/bash
# -vx
# --minor \
# --project buildhub runciter \ 
if [ -z ${TOPO_DIR+x} ]; then echo "TOPO_DIR is not set; export TOPO_DIR="; exit; else echo "TOPO_DIR is '$TOPO_DIR'"; fi
pushd $TOPO_DIR
export TOPO_DIR_NAME=${PWD##*/}
popd
python ./GenerateReleaseScript.py \
  $TOPO_DIR \
  file:topological-$TOPO_DIR_NAME.json \
  --includes net.aequologica.neo:* \
  --includeProperties geppaequo.version \
  --phase release_finish
  1>logs/generate-release-script-for-$TOPO_DIR_NAME-$(date -d "today" +"%Y%m%d%H%M").log \
  2>&1
