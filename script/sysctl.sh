#!/bin/bash
# Exemplo
# sysctl net.inet.carp.preempt=1

/sbin/sysctl -w net.ipv4.tcp_fin_timeout=5
/sbin/sysctl -w net.core.somaxconn=40000
/sbin/sysctl -w net.ipv4.tcp_max_syn_backlog=65535
/sbin/sysctl -w net.ipv4.tcp_syncookies=0
/sbin/sysctl -w net.ipv4.tcp_max_tw_buckets=180000
/sbin/sysctl -w net.ipv4.tcp_tw_reuse=1
#/sbin/sysctl -w net.ipv4.ip_local_port_range="15000 65000"




net.inet.carp.allow
# Allow carp operation.  When disabled, virtual hosts	remain in initial	state, neither sending nor receiving
# announcements or traffic. Enabled by default.


net.inet.carp.preempt
# Allow virtual hosts to preempt each other.  When	enabled, a vhid	in a backup state	would preempt a	master that	is
# announcing itself with a lower advskew.  Disabled by default.


net.inet.carp.dscp
# DSCP	value in carp packet.  Valid Values are 0	to 63.	A value	of 4 is equivalent to the	old standard of TOS
# LOW_DELAY.  TOS values were deprecated and replaced by DSCP in 1998.  The default value is 56 (CS7/Network	Control).


net.inet.carp.log
# Determines what events relating to carp	vhids are logged.  A value of 0 disables any logging.  A value of 1 enables
# logging state changes of carp	vhids.	Values above 1 enable logging of bad carp packets.	 The default value is 1.


net.inet.carp.demotion
# This	value shows the	current	level of CARP demotion.  The value	is added to the	actual advskew sent in announcements
# for all vhids.	 During normal system operation the demotion factor is zero.  However, problematic conditions raise
# its level: when carp experiences	problem with sending announcements, when	an interface running a vhid goes	down, or
# while the pfsync(4) interface is	not synchronized.  The demotion factor can be adjusted writing to the sysctl oid.
# The signed value	supplied to the sysctl(8) command is	added to current	demotion factor.  This allows to control
# carp behaviour depending on some external conditions,	for example on the status of some daemon utility.

net.inet.carp.ifdown_demotion_factor
# This	value is added to net.inet.carp.demotion when an interface running a vhid goes down.The default value is	240
# (the maximum advskew value).

net.inet.carp.senderr_demotion_factor
# This	value is added tonet.inet.carp.demotion when carp experiences errors sending its announcements.	 The default
# value is 240 (the maximum advskew value).