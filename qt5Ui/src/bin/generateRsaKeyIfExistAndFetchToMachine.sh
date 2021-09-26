#!/bin/bash
RSA_FILE=tmp/id_rsa.pub
RSA_TARGET=tmp/id_rsa
AUTHORIZED_KEYS=tmp/authorized_keys

if [ ! -f "$RSA_FILE" ];then
    ssh-keygen -t rsa -f $RSA_TARGET -q -N "" || exit 1
    cat $RSA_FILE >> $AUTHORIZED_KEYS || exit 1
    ssh-add -D $RSA_TARGET || exit 1
    ssh-add $RSA_TARGET || exit 1

fi

IP=$1
Port=$2
username=$3
password=$4
sshpass -p "$password" scp -P $Port $AUTHORIZED_KEYS $username@$IP:/home/$username/.ssh || exit 1