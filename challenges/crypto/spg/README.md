# SPG

This is the writeup for the Challenge [SPG](https://app.hackthebox.com/challenges/SPG) which is a simple crypto challenge.

## Challenge Description

After successfully joining the academy, there is a process where you have to log in to eclass in order to access notes in each class and get the current updates for the ongoing prank labs. When you attempt to log in, though, your browser crashes, and all your files get encrypted. This is yet another prank for the newcomers. The only thing provided is the password generator script. Can you crack it, unlock your files, and log in to the spooky platform?


## Solution

The solution can be seen directly in the `solutions.py` file. To keep it briefly:

1. The generate Password function allowed to reverse engineer the Master Key
2. Using the Masterkey it was possible to decrypt the cipher
