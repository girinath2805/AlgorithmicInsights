import csv
import numpy as np
import matplotlib.pyplot as plt
# Read the CSV data and extract numeric values
data = []
with open('Admission_Predict_Ver1.1.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        data.append([float(row['GRE Score']), float(row['TOEFL Score']), float(row['University Rating']),
                     float(row['SOP']), float(row['LOR ']), float(row['CGPA']), float(row['Research']),
                     float(row['Chance of Admit '])])

# Convert data into a numpy array
data = np.array(data)

# Separate the features and y
X = data[:, :-1]
y = data[:, -1] 

# Perform linear regression to get the coefficients
coefficients, _, _, _ = np.linalg.lstsq(np.column_stack((X, np.ones(X.shape[0]))), y, rcond=None)


# Define a function to make predictions using the obtained coefficients
def predict_chance_of_admit(features, coefficients):
    return np.dot(features, coefficients[:-1]) + coefficients[-1]

# Calculate predicted values for all data points
predicted_values = np.array([predict_chance_of_admit(features, coefficients) for features in X])

print("Coefficients of the parameters are ",coefficients, "considering as linear model")

def calculate_mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

mse = calculate_mse(y, predicted_values)
rmse = np.sqrt(mse)

def calculate_r_squared(y_true, y_pred):
    total_variance = np.var(y_true)  # Variance of the actual values
    unexplained_variance = np.var(y_true - y_pred)  # Variance of the residuals
    r_squared = 1 - (unexplained_variance / total_variance)
    return r_squared

r_squared = calculate_r_squared(y, predicted_values)


def calculate_r_squared(y_true, y_pred):
    total_variance = np.var(y_true)  # Variance of the actual values
    unexplained_variance = np.var(y_true - y_pred)  # Variance of the residuals
    r_squared = 1 - (unexplained_variance / total_variance)
    return r_squared

r_squared = calculate_r_squared(y, predicted_values)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared (R²):", r_squared)

correlations = np.corrcoef(X, y, rowvar=False)
parameters = ["GRE Score", "TOEFL Score", "University Rating", "SOP", "LOR", "CGPA", "Research"]

# Create a horizontal bar graph for the correlation coefficients
# Create a horizontal bar graph for the correlation coefficients
plt.figure(figsize=(10, 6))
bars = plt.barh(parameters, correlations[-1, :-1], color='skyblue')
plt.ylabel('Parameters')
plt.xlabel('Correlation Coefficient')
plt.title('Correlation Coefficients for Admission Predictions')

# Annotate the bars with their values
for bar in bars:
    width = bar.get_width()
    plt.annotate(f'{width:.2f}', (width, bar.get_y() + bar.get_height() / 2), ha='center', va='center', color='black')

plt.tight_layout()
plt.savefig("data1.png")

# Filter data for universities with a rating of 5
filtered_data = data[data[:, 2] == 5]

# Remove the "University Rating" column
filtered_data = np.delete(filtered_data, 2, axis=1)

# Separate the features and y
X_filtered = filtered_data[:, :-1]  # Features
y_filtered = filtered_data[:, -1]   # y

# Calculate correlation coefficients for the filtered data
correlations_filtered = np.corrcoef(X_filtered, y_filtered, rowvar=False)
parameters_filtered = ["GRE Score", "TOEFL Score", "SOP", "LOR", "CGPA", "Research"]

# Corresponding correlation coefficients for the filtered data

plt.figure(figsize=(10, 6))
bars = plt.barh(parameters_filtered, correlations_filtered[-1, :-1], color='skyblue')
plt.ylabel('Parameters')
plt.xlabel('Correlation Coefficient')
plt.title('Correlation Coefficients for Admission Predictions of top-ranked Institutes (Rating 5)')

for bar in bars:
    width = bar.get_width()
    plt.annotate(f'{width:.2f}', (width, bar.get_y() + bar.get_height() / 2), ha='center', va='center', color='black')


print(correlations_filtered[-1, :-1])
# Show the plot
plt.tight_layout()
plt.savefig("data2.png")
