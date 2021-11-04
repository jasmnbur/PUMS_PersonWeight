import pandas as pd


df = pd.read_csv(r'/Users/jburesch/Desktop/psam_p36.csv')

# testing population count for NY state
column_sum = df['PWGTP'].sum()
print(column_sum)

# POWPUMA place of work variable
df2 = df[df['POWPUMA'].notnull()]
df2.head(15)

# new df with three variables, geography PUMA code, place of work, and person weight
df2[['PUMA', 'POWPUMA','PWGTP']].head(15)


df2['PUMA']=df2['PUMA'].astype(str)

# creating empty lists to use for the function
empty_list_1 = []
empty_list_2 = []
empty_list_3 = []

# test code 
# puma_number = str(input('Please enter the PUMA you want to search: '))

# defining a function that searches for puma and appends puma, powpuma and pwgtp data 
def search_PUMA(x):
# global puma_number
## used my previous code to find PUMAs in Harlem, Manhattan & entered relevant PUMAs
    if x['PUMA'] == '3802' or x['PUMA'] == '3803' or x['PUMA'] == '3804':
        empty_list_1.append(x['PUMA'])
        empty_list_2.append(x['POWPUMA'])
        empty_list_3.append(x['PWGTP'])

df2.apply(search_PUMA, axis=1)

df3 = pd.DataFrame({
    'PUMA':empty_list_1,
    'POWPUMA':empty_list_2,
    'PWGTP':empty_list_3
})
df3.head(15)


# Summing person weights
column_sum3 = df3['PWGTP'].sum()


# RESULT: There was a total of 188,939 persons who's place of work was within the neighborhoods of Harlem in 2019
print(column_sum3)


df3.to_excel('POW_PUMA.xlsx', engine='xlsxwriter')
