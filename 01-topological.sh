#!/bin/bash 
#-vxe
# echo off  > /dev/null
if [ -z ${TOPO_DIR+x} ]; then echo "TOPO_DIR is not set; export TOPO_DIR="; exit; else echo "TOPO_DIR is '$TOPO_DIR'"; fi
if [ -z ${SCRIPT_DIR+x} ]; then echo "SCRIPT_DIR is not set; export SCRIPT_DIR="; exit; else echo "SCRIPT_DIR is '$SCRIPT_DIR'"; fi
python $SCRIPT_DIR/CreateModulePom.py \
  $TOPO_DIR
pushd $TOPO_DIR
export TOPO_DIR_NAME=${PWD##*/}  
mvn validate -f modules.pom
popd
curl -x http://proxy:8080 https://tebaldi051108trial.hanatrial.ondemand.com/dagr-api/dags/dag-$TOPO_DIR_NAME.json/topologicartifacts -o topological-$TOPO_DIR_NAME.json
