antibiotics = {
    'penicillin' : 'penicillin G',
    'cephalosporin' : {'gen_1': ['cephalexin', 'cefazolin'], 'gen_2': 'cefuroxime', 'gen_3': ['cefdinir', 'cefixine', 'cefotaxime', 'ceftriaxone'], 'gen_4' : 'cefepime', 'gen_5': 'ceftaroline'},
    'anti_mrsa' : 'vancomycin',
    'tetracycline' : ['doxycycline', 'minocycline'],
    'aminoglycoside' : ['amikacin', 'tobramycin', 'neomycin', 'streptomycin', 'gentamycin'],
    'macrolide' : ['azithromycin', 'clarithromycin', 'azithromycin'],
    'fluoroquinolone' : ['levofloxacin', 'ciprofloxacin', 'moxifloxacin'],
    'nitromidazole' : 'metronidazole'}

adrenergic_agonist = {
    'non_selective_adrenergic_agonist': 'epinephrine',
    'b2_adrenergic_agonist' : 'albuterol',
    'a2_adrernergic_agonist': 'clonidine'}
# clonidine binds a-2 receptors, prevents release of norepinephrine and drops BP

adrenergic_antagonist = {
    "alpha_1_adrenergic_antagonist" : ["prazosin", "tamulosin"]}

beta_blockers = {
    "non_selective" : "propanolol",
    "b_1" : "metoprolol",
    "a1_b1_b2" : "carvedilol",}


cholinergic = {
    "cholinergic_agonist" : "bethanechol"
#     bethanechol is to treat urinary retention and increase gastric peristalsis
    "acetylcholinesterase_inhibitor" : ["endrophonium_bromide", "neostigmine", "pyridostigmine"],
#     treatment for myasthenia gravis
}


print('These are your drug classes:')

# for k, v in adrenergic:
#     print(k)

