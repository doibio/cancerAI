# cancerAI
AI to develop cures for cancer

# Search for treatments for cancer

python ./step1-search-all.py

This will do a search for the latest treatments for cancer

# Entrez search using CLI

for PMID in $(esearch -db pubmed -query "immunocore" | efetch -format uid); do echo $PMID &&
efetch -db pubmed -id $PMID -format abstract > "$PMID.txt"
done

# Search documents for efficacy of treatment using co.chat() documents mode

python ./step2-search-treatment.py

# Develop business plan for company using co.chat() web search mode

python ./step3-search-company.py

