#!/bin/bash
MACHINE=$1
ssh -q -o ConnectTimeout=5 $MACHINE exit || exit 1
