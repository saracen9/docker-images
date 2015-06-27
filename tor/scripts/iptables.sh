#!/bin/sh
###############################################################################
# Script to modify IP tables to allow for Tor to act as a transparent
# proxy.
#
# Sources:
# - https://trac.torproject.org/projects/tor/wiki/doc/BlockNonTorTrafficDebian
# - https://help.ubuntu.com/community/TorDedicatedUser
# - https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxy
###############################################################################

## Set variables

# destinations you don't want routed through Tor
_non_tor="192.168.1.0/24 192.168.0.0/24"
# the UID that Tor runs as
_tor_uid=$(id -u debian-tor)
# Tor's TransPort
_trans_port="9040"

## Flush iptables
iptables -F
iptables -t nat -F

## Disable ICMP
iptables -A OUTPUT -p icmp -j REJECT

## Set iptables *nat
iptables -t nat -A OUTPUT -m owner --uid-owner $_tor_uid -j RETURN
iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports 53

# allow clearnet access for hosts in $_non_tor
for _clearnet in $_non_tor 127.0.0.0/9 127.128.0.0/10; do
   iptables -t nat -A OUTPUT -d $_clearnet -j RETURN
done

# redirect all other output to Tor's TransPort
# and pre-routing for DNS
iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports $_trans_port
iptables -t nat -A PREROUTING -p udp --dport 53 -j REDIRECT --to-ports 53
iptables -t nat -A PREROUTING -p tcp --syn -j REDIRECT --to-ports $_trans_port

## Set iptables *filter
iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# allow clearnet access for hosts in $_non_tor
for _clearnet in $_non_tor 127.0.0.0/8; do
   iptables -A OUTPUT -d $_clearnet -j ACCEPT
done

## Allow only Tor output
iptables -A OUTPUT -m owner --uid-owner $_tor_uid -j ACCEPT
iptables -A OUTPUT -j REJECT
