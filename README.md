# thm_challenge1
This repository documents my solution to a TryHackMe challenge.  
The goal was to find hidden information inside a binary executable file.

## Tools Used

- **strings.exe** – Used to extract readable strings from the binary file (basic reverse engineering technique)
- **Python** – Used to filter and process the extracted strings for easier analysisUsed to make a script to filter the strings made found with strings.exe. It is possible to make this filters through strings.exe. But since I already know python and it was my first time using strings .exe it made more sense to make the filter in Python to be more practical.

## Strings.exe cmd command

```bash
"D:\tools\strings\strings.exe" Tetrix.exe > output.txt
```

## Notes

This was my first time working with binary analysis tools in a TryHackMe challenge, and it helped me understand how useful simple string extraction can be in reverse engineering tasks.
