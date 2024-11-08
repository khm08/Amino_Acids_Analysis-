
-- Create table for amino acids data
CREATE TABLE Amino_Acids (
    Amino_Acid VARCHAR(50),
    Muscle_Protein_Synthesis_Percentage DECIMAL(5, 2),
    Recovery_Rate_Percentage DECIMAL(5, 2),
    Muscle_Strength_Percentage DECIMAL(5, 2),
    Hypertrophy_Percentage DECIMAL(5, 2)
);

-- Insert data into the amino acids table (placeholder example)
INSERT INTO Amino_Acids (Amino_Acid, Muscle_Protein_Synthesis_Percentage, Recovery_Rate_Percentage, Muscle_Strength_Percentage, Hypertrophy_Percentage)
VALUES ('Leucine', 12.34, 9.87, 6.45, 7.89),
       ('Isoleucine', 10.56, 8.76, 5.34, 6.78),
       ...;

-- Query to get average muscle protein synthesis by amino acid
SELECT Amino_Acid, AVG(Muscle_Protein_Synthesis_Percentage) AS AvgMuscleProteinSynthesis
FROM Amino_Acids
GROUP BY Amino_Acid;

-- Query to get average recovery rate by amino acid
SELECT Amino_Acid, AVG(Recovery_Rate_Percentage) AS AvgRecoveryRate
FROM Amino_Acids
GROUP BY Amino_Acid;
