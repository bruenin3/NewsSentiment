import csv

# Define the input and output file paths
input_file = 'news_titles_with_sentiment.csv'  # Replace with your input CSV file
output_file = 'output_cleaned_names.csv'  # Replace with your desired output CSV file

# Function to remove the possessive 's from names
def remove_possessive_s(name):
    return name.replace("'s", "")

# Read the input CSV file
data = []
with open(input_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        row['Name'] = remove_possessive_s(row['Name'])  # Clean the name
        data.append(row)

# Save the cleaned data to a new CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = data[0].keys()
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)

print(f"Cleaned names and saved data to '{output_file}'")
