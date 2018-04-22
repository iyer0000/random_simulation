Picked random sequences from chrM&22.
python random_fastq.py M_22.fa >test5.fq
Random error rates were 1000 in 100000.
bwa mem -t 2 ~/Chromosomes/chr21.fa test5.fq >test5.sam
Then aligned to chr21.
The alignment % is 11%.
python parse_NM_tags.py test5.sam >mismatch_rate.txt
