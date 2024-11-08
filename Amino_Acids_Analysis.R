
# Load necessary libraries
library(ggplot2)
library(dplyr)
library(readxl)

# Load the amino acids data
amino_data <- read_excel("path/to/Amino_Acids_Analysis.xlsx")

# View the first few rows of the data
head(amino_data)

# Calculate average muscle metrics by amino acid
average_effects <- amino_data %>%
  group_by(Amino_Acid) %>%
  summarise(
    AvgMuscleProteinSynthesis = mean(Muscle_Protein_Synthesis_Percentage),
    AvgRecoveryRate = mean(Recovery_Rate_Percentage),
    AvgMuscleStrength = mean(Muscle_Strength_Percentage),
    AvgHypertrophy = mean(Hypertrophy_Percentage)
  )

# View the average effects
print(average_effects)

# Plotting average muscle protein synthesis by amino acid
ggplot(average_effects, aes(x=Amino_Acid, y=AvgMuscleProteinSynthesis)) +
  geom_bar(stat="identity", fill="blue") +
  theme_minimal() +
  labs(title="Average Muscle Protein Synthesis by Amino Acid", x="Amino Acid", y="Average Muscle Protein Synthesis (%)") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Plotting average recovery rate by amino acid
ggplot(average_effects, aes(x=Amino_Acid, y=AvgRecoveryRate)) +
  geom_bar(stat="identity", fill="green") +
  theme_minimal() +
  labs(title="Average Recovery Rate by Amino Acid", x="Amino Acid", y="Average Recovery Rate (%)") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
