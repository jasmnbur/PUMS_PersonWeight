import pandas as pd

# downloaded 2019 1-year person (p) variables for NY state (code 36) from Census ACS FTP site
df = pd.read_csv(r'/Users/jburesch/Desktop/psam_p36.csv')

# taking a glimpse at the person weights
df['POWPUMA'].head()

# new data frame
df[df['POWPUMA'].notnull()]

# defining person weight sum
column_sum = df['PWGTP'].sum()

# outputs 19453561 (NY state has a population of 19,453,561
print(column_sum)
