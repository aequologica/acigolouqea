#!/bin/bash -vx
if [ -z ${TOPO_DIR+x} ]; then echo "TOPO_DIR is not set; export TOPO_DIR="; exit; else echo "TOPO_DIR is '$TOPO_DIR'"; fi
# --dryRun \ 
#  com.sap.prd.dts \
pushd $TOPO_DIR
export TOPO_DIR_NAME=${PWD##*/}  
popd
python ./GeoReleaseScript.py \
  $TOPO_DIR_NAME.SFSF.cmd \
  1> logs/run-release-script-for-$TOPO_DIR_NAME-$(date -d "today" +"%Y%m%d%H%M").log 2>&1
