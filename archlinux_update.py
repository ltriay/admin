#!/bin/bash
echo "Cleaning up saved packages"
paccache -r
df -h
rkhunter --versioncheck
rkhunter --update
rkhunter --check --rwo --sk --nomow
btrfs subvolume snapshot / /.snapshot/maj`date +%Y%m%d`
pacman -Syu
rkhunter --propupd
btrfs subvolume list /
df -h /
echo
echo "Run command:"
echo "btrfs subvolume delete / /.snapshot/maj"

