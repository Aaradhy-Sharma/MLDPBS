Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

# Run Comparisons for MLDPBS

## Instructions to Run the programs

Follow these steps to execute each of the six Python files in sequence:

1. **Step 1**: Open your terminal or command prompt.
2. **Step 2**: Go to 
3. **Step 3**: Navigate to the Buddy Comparisons directory. Use the following command:
   ```bash
   cd path/to/Buddy/Comparisons
4. **Step 4**: For visualising comparisons between Best Fit, First Fit and MLDPBS 
   Run the following commands: 
   ```bash
   python3 BFB_BvsT.py
   python3 BFB_IvsT.py
   python3 frag.py
5. **Step 5**: For visualising comparisons between MLDPBS and the other state of the art Buddy System variations 
   Run the following commands: 
   ```bash
   python3 BvB_BvsT.py
   python3 BvB_IvsT.py
   python3 BvB_TvsT.py