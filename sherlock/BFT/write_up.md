# Write-Up: BFT

## General infos

This Sherlock is all about getting started with the MFT (Master File Table) used for the NTFS System in Windows.
To be able to analyze those files its best to start your investigation on a Windows VM.

Make sure you have all the [Eric Zimmerman Tools](https://ericzimmerman.github.io/#!index.md) installed.

When working with MFT it usually helps a lot to:

1. Use the `MFTCmd` command to parse the `$MFT` file to a `.csv` document
2. Use the `.csv` document as input for the `Timeline Explorer`.
3. When having the data loaded to Timeline Explorer use filters to get what you want.


# Answering the questions.

The first three tasks can easily be done by setting the correct filters such as
- date
- file ending -> `.zip`
- Checking for files in the downloaded directory

To compute the offset of the `*.bat` file its necessary to know that each entry in
MFT has a size of 1024 bytes. So by using the `entry Number` and the standard size of an entry, you can compute the offset. Tip -> Convert the byte offset to hex (windows calculator does all this lifting for you ;)). With this offset you should be able to navigate to this file in a suiting hex editor.
