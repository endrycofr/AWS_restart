#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# Store the human preproinsulin sequence in a variable called preproInsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Merge bInsulin and aInsulin into insulin
insulin = bInsulin + aInsulin

# Dictionary of amino acids that contribute to net-charge calculation
pKR = {
    'y': 10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25
}

# Count occurrences of relevant amino acids (Y, C, K, H, R, D, E) in insulin
seqCount = {x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}

# Calculate net charge at pH values from 0 to 14
pH = 0
while pH <= 14:
    netCharge = (
        +(sum({
            x: ((seqCount[x] * (10 ** pKR[x])) / ((10 ** pH) + (10 ** pKR[x])))
            for x in ['k', 'h', 'r']
        }.values()))
        - (sum({
            x: ((seqCount[x] * (10 ** pH)) / ((10 ** pH) + (10 ** pKR[x])))
            for x in ['y', 'c', 'd', 'e']
        }.values()))
    )
    print('{0:.2f}'.format(pH), netCharge)
    pH += 1
