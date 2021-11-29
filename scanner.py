import matplotlib.pyplot as plt
import pdfplumber
import glob
import numpy as np
from tqdm import tqdm

counter = {
    'qald' : 0,
    'lc-quad': 0,
    'webquestionssp': 0,
    'complexwebquestions': 0,
    'cfq': 0,
    'simplequestions': 0,
    'webquestions': 0,
    'complexquestions': 0,
    'metaqa': 0,
    'countries': 0,
    'wn18rr': 0,
    'kinship': 0,
    'nell-995': 0,
    'fb15k-237': 0,
    'umls': 0,
    'openbookqa': 0,
    'commonsenseqa': 0
}

sp = ['qald', 'lc-quad', 'webquestionssp', 'complexwebquestions', 'cfq']
ir = ['simplequestions', 'webquestions', 'complexquestions', 'metaqa']
rl = ['countries', 'wn18rr', 'kinship', 'nell-995', 'fb15k-237', 'umls']
hyb = ['openbookqa', 'commonsenseqa']

pdfs = glob.glob("*.pdf")

n_papers = len(pdfs)


for pdf in tqdm(pdfs):
    with pdfplumber.open(rf'{pdf}') as pdf:
        n_pages = len(pdf.pages)
        text = ''
        for page in range(n_pages):
            text += pdf.pages[page].extract_text().lower()
        
        for key in counter:
            if key in text:
                counter[key] += 1
            
res = {'qald': 44, 'lc-quad': 30, 'webquestionssp': 18, 'complexwebquestions': 13, 'cfq': 2, 'simplequestions': 69, 'openbookqa': 3, 'webquestions': 58, 'complexquestions': 61, 'commonsenseqa': 9, 'metaqa': 16, 'countries': 37, 'wn18rr': 43, 'kinship': 16, 'nell-995': 18, 'fb15k-237': 58, 'umls': 18 }

sps =  [(i, res[i]) for i in res if i in sp]
irs =  [(i, res[i]) for i in res if i in ir]
rls =  [(i, res[i]) for i in res if i in rl]
hybs = [(i, res[i]) for i in res if i in hyb]

n_total = sum(res[i] for i in res)


group_names=[
    f'SP ({round((sum(i[1] for i in sps) / n_total * 100), 2)}%)', 
    f'IR ({round((sum(i[1] for i in irs) / n_total * 100), 2)}%)',
    f'RL ({round((sum(i[1] for i in rls) / n_total * 100), 2)}%)',
    f'Hybrid ({round((sum(i[1] for i in hybs) / n_total * 100), 2)}%)']
group_size=[
    sum(i[1] for i in sps),
    sum(i[1] for i in irs),
    sum(i[1] for i in rls),
    sum(i[1] for i in hybs)
]
subgroup_names= [i[0] for i in sps] + [i[0] for i in irs] + [i[0] for i in rls] + [i[0] for i in hybs]
subgroup_size = [i[1] for i in sps] + [i[1] for i in irs] + [i[1] for i in rls] + [i[1] for i in hybs]

a, b, c, d =[plt.cm.Blues, plt.cm.Reds, plt.cm.Greens, plt.cm.Purples]

fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.4, labels=group_names, colors=[a(0.6), b(0.6), c(0.6), d(0.6)])
plt.setp(mypie, width=0.2, edgecolor='white')

cols = []
i = 0.5
for _ in range(len(sps)):
    cols.append(a(1 - i))
    i += 0.1

i = 0.5
for _ in range(len(irs)):
    cols.append(b(1 - i))
    i += 0.1

i = 0.5
for _ in range(len(rls)):
    cols.append(c(1 - i))
    i += 0.1

i = 0.7
for _ in range(len(hybs)):
    cols.append(d(1 - i))
    i += 0.1


mypie2, labels = ax.pie(subgroup_size, radius=1.4-0.2, labels=subgroup_names, labeldistance=0.7, colors=cols)
plt.setp(mypie2, width=0.6, edgecolor='white')
plt.margins(0, 0)
for label in labels:
    label.set_horizontalalignment('center')
    label.set_fontsize(16)

subgroup_names_legs = []

for c in sps:
    subgroup_names_legs.append(f'{c[0]} = {round((c[1] / n_total) * 100, 2)}%')

for c in irs:
    subgroup_names_legs.append(f'{c[0]} = {round((c[1] / n_total) * 100, 2)}%')

for c in rls:
    subgroup_names_legs.append(f'{c[0]} = {round((c[1] / n_total) * 100, 2)}%')

for c in hybs:
    subgroup_names_legs.append(f'{c[0]} = {round((c[1] / n_total) * 100, 2)}%')

plt.legend(subgroup_names_legs,loc='best')

plt.legend(loc=(0.9, 0.1))
handles, labels = ax.get_legend_handles_labels()

ax.legend(handles[3:], subgroup_names_legs, loc=(0.9, 0.1))
plt.show()

mixture = [
    'qald', 'cfq', 'metaqa', 'nell-995', 'fb15k-237'
]

mostly_sh = [
    'webquestionssp', 'simplequestions', 'countries', 'wn18rr', 'kinship', 'umls'
]

mostly_mh = [
    'lc-quad', 'complexwebquestions', 'complexquestions', 'openbookqa', 'commonsenseqa'
]

mixs = sum(res[i] for i in res if i in mixture)
shs = sum(res[i] for i in res if i in mostly_sh)
mhs = sum(res[i] for i in res if i in mostly_mh)

labels = 'Mixture S-H & M-H', 'Mostly S-H', 'Mostly M-H'
sizes = [mixs, shs, mhs]

fig1, ax1 = plt.subplots()
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
temp, t, labels = ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
for label1, label2 in zip(labels, t):
    label1.set_horizontalalignment('center')
    label1.set_fontsize(18)
#    label2.set_horizontalalignment('center')
    label2.set_fontsize(14)
plt.show()