#! /bin/bash
image="saracen9/tor"
docker build -t $image .
docker run --privileged -d saracen9/tor

# get the container id
cid=$(docker ps -lq)

# now execute script
echo "build complete, modifying the iptables rules"
docker exec $cid /opt/scripts/iptables.sh
docker exec $cid rm -rf /opt/scripts

# commit the change and destroy
echo "committing changes"
docker commit -m "Add iptables ruleset" -a "James Veitch" $cid $image
echo "cleaning up"
docker rm -f $cid
