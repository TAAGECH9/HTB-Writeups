# Write Up: Photon Lockdown

This was actually a super easy challenge.

1. By using the command `file rootfs`, I figured out that the filesystem was of type squashfs
  - `rootfs: Squashfs filesystem, little endian, version 4.0, zlib compressed, 10936182 bytes, 910 inodes, blocksize: 131072 bytes, created: Sun Oct  1 07:02:43 2023`
2. After doing some researche I figured out, that I can just mount it like this `sudo mount -o loop=/dev/loop1 rootfs /mnt/squashfs`
3. With the filesystem mounted I just had to search for a file that has a content of something like `HTB`. Therefore I just greped over everything by `grep -ri "HTB"`. Like this I found the corresponding location and the flag.
