squeue -u tommydl --nohead --format %F > h.txt
while read line; do scancel $line; done < h.txt
