import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import re

file_path = "C:\\Users\\lab.AUKOL\\Desktop\\shakshi_DMV_lab\\30 company.xlsx"
df = pd.read_excel(file_path)

print("Columns:", df.columns)


def convert_employees(emp):
    if isinstance(emp, str):
        emp = emp.lower()
        num = re.findall(r'\d+', emp)
        if num:
            num = int(num[0])
            if "lakh" in emp:
                return num * 100000
            elif "k" in emp:
                return num * 1000
            else:
                return num
    return 0

df['employees_clean'] = df['employees'].apply(convert_employees)

def clean_years(x):
    if isinstance(x, str):
        num = re.findall(r'\d+', x)
        if num:
            return int(num[0])
    return 0

df['years_clean'] = df['years'].apply(clean_years)

top_df = df.sort_values(by='employees_clean', ascending=False).head(5)

others = df['employees_clean'].sum() - top_df['employees_clean'].sum()

labels = list(top_df['name']) + ['Others']
sizes = list(top_df['employees_clean']) + [others]

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Top 5 Companies by Employees")
plt.show()

fig = px.funnel(
    df,
    x='review_count',
    y='name',
    title="Company Reviews Funnel"
)
fig.show()

print("\nCompany Headquarters:")
print(df[['name', 'hq']])

plt.figure(figsize=(10, 5))
plt.bar(df['name'], df['ratings'])
plt.xticks(rotation=90)
plt.xlabel("Company")
plt.ylabel("Ratings")
plt.title("Company Ratings")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

top_companies = df.sort_values(by='ratings', ascending=False).head(5)['name']

for company in top_companies:
    temp = df[df['name'] == company]
    plt.plot(temp['years_clean'], temp['ratings'], marker='o', label=company)

plt.xlabel("Years")
plt.ylabel("Ratings")
plt.title("Top 5 Company Performance")
plt.legend()
plt.tight_layout()
plt.show()
