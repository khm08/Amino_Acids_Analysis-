#!/usr/bin/env python
# coding: utf-8

# # Amino Acids and Their Role in Fitness
# This analysis explores various amino acids commonly used in fitness supplements, focusing on their roles in muscle recovery, strength, and hypertrophy. We will examine the function and evidence supporting each amino acid, using both descriptive and predictive analytics to understand their efficacy.

# ## 1. Introduction
# Amino acids are the building blocks of protein and play crucial roles in muscle protein synthesis, recovery, strength, and hypertrophy. This analysis focuses on essential amino acids (EAAs), branched-chain amino acids (BCAAs), conditionally essential amino acids, and non-essential amino acids, examining their function, supporting evidence, and potential effects on fitness.

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
sns.set(style='whitegrid')
from IPython.display import display


# ## 2. Data Loading
# We will create synthetic data for each amino acid to simulate their impact on muscle protein synthesis, recovery rates, strength gains, and hypertrophy.

# In[ ]:


# Define the amino acids and their properties
amino_acids = ['Leucine', 'Isoleucine', 'Valine', 'Lysine', 'Methionine',
               'Phenylalanine', 'Threonine', 'Tryptophan', 'Histidine',
               'Arginine', 'Cysteine', 'Glutamine', 'Tyrosine', 'Ornithine',
               'Alanine', 'Aspartic Acid', 'Glutamic Acid', 'Glycine', 'Proline',
               'Serine', 'Asparagine', 'Beta-Alanine']

# Simulate synthetic data for each amino acid
np.random.seed(42)
data = {
    'Amino Acid': np.random.choice(amino_acids, 1000),
    'Muscle Protein Synthesis (%)': np.random.normal(10, 2, 1000),
    'Recovery Rate (%)': np.random.normal(8, 3, 1000),
    'Muscle Strength (%)': np.random.normal(5, 2, 1000),
    'Hypertrophy (%)': np.random.normal(6, 1.5, 1000)
}

# Create a DataFrame
amino_acids_df = pd.DataFrame(data)
display(amino_acids_df.head())
        


# ## 3. Descriptive Analytics
# We will perform descriptive analytics to understand the average impact of each amino acid on muscle protein synthesis, recovery, strength, and hypertrophy.

# In[ ]:


# Calculate average metrics by amino acid
average_effects = amino_acids_df.groupby('Amino Acid').agg({
    'Muscle Protein Synthesis (%)': 'mean',
    'Recovery Rate (%)': 'mean',
    'Muscle Strength (%)': 'mean',
    'Hypertrophy (%)': 'mean'
}).reset_index()

# Display the results
display(average_effects)
        


# ## 4. Comparative Analysis
# We will use statistical tests to compare the effectiveness of different amino acids.

# In[ ]:


# Box plots to compare muscle protein synthesis, recovery rate, muscle strength, and hypertrophy
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.boxplot(data=amino_acids_df, x='Amino Acid', y='Muscle Protein Synthesis (%)', ax=axes[0, 0])
axes[0, 0].set_title('Muscle Protein Synthesis by Amino Acid')
axes[0, 0].tick_params(axis='x', rotation=45)

sns.boxplot(data=amino_acids_df, x='Amino Acid', y='Recovery Rate (%)', ax=axes[0, 1])
axes[0, 1].set_title('Recovery Rate by Amino Acid')
axes[0, 1].tick_params(axis='x', rotation=45)

sns.boxplot(data=amino_acids_df, x='Amino Acid', y='Muscle Strength (%)', ax=axes[1, 0])
axes[1, 0].set_title('Muscle Strength by Amino Acid')
axes[1, 0].tick_params(axis='x', rotation=45)

sns.boxplot(data=amino_acids_df, x='Amino Acid', y='Hypertrophy (%)', ax=axes[1, 1])
axes[1, 1].set_title('Hypertrophy by Amino Acid')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
        


# ## 5. Predictive Modeling
# We will build a model to predict the impact of an amino acid based on its properties.

# In[ ]:


# Example of predictive modeling using linear regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Prepare the data for predictive modeling
X = pd.get_dummies(amino_acids_df['Amino Acid'])
y = amino_acids_df[['Muscle Protein Synthesis (%)', 'Recovery Rate (%)', 'Muscle Strength (%)', 'Hypertrophy (%)']]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the model for each metric
models = {}
metrics = ['Muscle Protein Synthesis (%)', 'Recovery Rate (%)', 'Muscle Strength (%)', 'Hypertrophy (%)']
for metric in metrics:
    model = LinearRegression()
    model.fit(X_train, y_train[metric])
    models[metric] = model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test[metric], y_pred)
    r2 = r2_score(y_test[metric], y_pred)
    print(f'{metric} - Mean Squared Error: {mse}, R-squared: {r2}')
        


# ## 6. Data Visualization
# Visualizations will help us understand the impact of each amino acid more clearly.

# In[ ]:


# Scatter plot to show relationship between different metrics
sns.pairplot(amino_acids_df, hue='Amino Acid', markers='o')
plt.suptitle('Relationships between Muscle Metrics by Amino Acid', y=1.02)
plt.show()
        


# ## 7. Summary and Recommendations
# Based on the analysis, we will provide insights and recommendations about which amino acids show the most promise for muscle recovery, strength, and hypertrophy.
# 
# - **Most Effective Amino Acids**: Based on the results, certain amino acids might show a higher average increase in muscle protein synthesis, recovery, strength, and hypertrophy.
# - **Further Research**: While synthetic data provides insights, real-world studies are necessary to validate the findings.
# - **Usage and Safety**: Always consult with a healthcare professional before starting any supplement regimen.
