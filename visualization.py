import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('complex-data-progress.xlsx', sheet_name='data')

# protein freq - bar plot
protein_plot = sns.countplot(x='Protein Name', data=df)
plt.title('Distribution of proteins')
plt.xlabel('protein name')
plt.savefig('distribution_of_protein_names.png')

# protein freq - pie plot
no_of_proteins = df['Protein Name'].value_counts()
# no_of_proteins.plot.pie(autopct="%.1f%%");
labels = no_of_proteins.keys()
numbers = no_of_proteins.array


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{v:d}'.format(p=pct, v=val)
    return my_autopct


colors = ['#066376', '#00789C', '#007A83', '#30A9AF', '#81F5FF', '#E2B288', '#FFEBC8']
plt.pie(x=no_of_proteins, autopct=make_autopct(numbers), explode=[0.13] * len(no_of_proteins), labels=labels,
        pctdistance=0.85, labeldistance=1.1, colors=colors)
# plt.title("distribution of proteins", fontsize=12, pad=22)
# plt.show()
plt.savefig('pie_plot_proteins.png')

# Frequencies of chemical compounds
df = df.rename(columns={"Protein Name": "proteins", "Ligand Code": "compound"})
no_of_compounds = sns.countplot(y=df['compound'], data=df, hue=df['proteins'], dodge=False)
no_of_compounds.set_yticklabels(no_of_compounds.get_yticklabels(), fontsize=5)
no_of_compounds.set_xticks([0, 1, 2, 3])
plt.title('Distribution of chemical compounds')

plt.savefig('distribution_of_compounds.png')
