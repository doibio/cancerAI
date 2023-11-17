# cancerAI
AI to develop cures for cancer



for PMID in $(esearch -db pubmed -query "immunocore" | efetch -format uid); do echo $PMID && \n    efetch -db pubmed -id $PMID -format abstract > "$PMID.txt"\ndone\n

