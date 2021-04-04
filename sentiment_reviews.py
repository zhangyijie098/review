# Import pandas library

import pandas as pd

# Load data into pandas

data = pd.read_csv('reviews.csv', delimiter='\t')

data.head().to_csv(OUTPUT_FOLDER + '/output.csv')

print("Original Dataset: \n")
print()