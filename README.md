# Readability
The goal is to automate the extraction of knowledge reagrding the reading efforts or ticket text quality to provide decision support for IT process workers. We propose to measure the readability by the stylistic patterns, i.e., the ticket length, parts-of-speech distributions, and wording style (Zipf's Law).

This repository contains the following files: python file for extracting readability measures (as an input for python files serve ticket textual descriptions), excel file with the calculation of readability based on the motivating example and threshold rules (as an input for excel file serve threshold rules), illustrative application of Zipf's Law on tickets (wording style) (Illustrative_Application_Zipf_Tickets.pdf).

Python code (Readability Tickets.py): STAGE 1. Tickets corpus reading, preprocessing and English language filtering. STAGE 2. Tickets descriptioin length calculating (number of words). STAGE 3. Calculating the number of parts-of-speech (PoS) and unique PoS distribution. STAGE 4. Identifying basic Zipf's Law coefficients. STAGE 5. Writing of tickets text length, number of PoS, unique PoS distribution, and Zipf's law coefficients in the *.csv file.

Excel *.csv file (Readability_Calculation.xlsx): STAGE 6. Calculating % of nouns in all processed words. STAGE 7. Readability identification
