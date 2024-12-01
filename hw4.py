import pickle
import sys

class DatasetException(Exception):
    pass

class CountyDataProcessor:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, "rb") as file:
                data = pickle.load(file)
                print(data[0])  # Print the first entry to inspect its structure
                return data
        except FileNotFoundError:
            raise DatasetException(f"Error! Could not find a \"{self.data_file}\" file.")
        except Exception as e:
            raise DatasetException(f"Error loading dataset: {e}")

    def filter_state(self, state_abbreviation):
        self.data = [county for county in self.data if county.state == state_abbreviation]
        print(f"Filter: state == {state_abbreviation} ({len(self.data)} entries)")

    def filter_gt(self, field, number):
        valid_fields = self.get_field_dict(field)
        filtered_data = [county for county in self.data if valid_fields(county) > number]
        print(f"Filter: {field} gt {number} ({len(filtered_data)} entries)")
        for county in filtered_data:
            print(f"{field} value: {valid_fields(county)}")
        self.data = filtered_data

    def filter_lt(self, field, number):
        valid_fields = self.get_field_dict(field)
        filtered_data = [county for county in self.data if valid_fields(county) < number]
        print(f"Filter: {field} lt {number} ({len(filtered_data)} entries)")
        for county in filtered_data:
            print(f"{field} value: {valid_fields(county)}")
        self.data = filtered_data

    def population_total(self):
        total_population = sum(county.population['2014 Population'] for county in self.data)
        print(f"2014 population: {total_population}")

    def population_field(self, field):
        valid_fields = self.get_field_dict(field)
        total_population = sum(valid_fields(county) * county.population['2014 Population'] / 100
                               for county in self.data)
        print(f"2014 {field} population: {total_population}")

    def percent_field(self, field):
        valid_fields = self.get_field_dict(field)
        total_population = sum(county.population['2014 Population'] for county in self.data)
        total_sub_population = sum(valid_fields(county) * county.population['2014 Population'] / 100
                                   for county in self.data)
        print(f"Total population: {total_population}")
        print(f"Total sub-population: {total_sub_population}")
        if total_population > 0:
            percentage = (total_sub_population / total_population) * 100
            print(f"2014 {field} percentage: {percentage}")
        else:
            print(f"2014 {field} percentage: 0.0")

    def get_field_dict(self, field):
        field_parts = field.split(".")
        if len(field_parts) != 2:
            raise ValueError(f"Invalid field format: {field}")

        category, subcategory = field_parts
        if category == "Education":
            return lambda county: county.education.get(subcategory, 0)
        elif category == "Ethnicities":
            return lambda county: county.ethnicities.get(subcategory, 0)
        elif category == "Income":
            return lambda county: county.income.get(subcategory, 0)
        elif category == "Population":
            return lambda county: county.population.get(subcategory, 0)
        else:
            raise ValueError(f"Unknown category: {category}")

def process_operations(operations_file, processor):
    try:
        with open(operations_file, "r") as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue

                try:
                    operation_parts = line.split(":")
                    operation = operation_parts[0]

                    if operation == "display":
                        for county in processor.data:
                            print(county)
                    elif operation == "filter-state":
                        processor.filter_state(operation_parts[1])
                    elif operation == "filter-gt":
                        processor.filter_gt(operation_parts[1], float(operation_parts[2]))
                    elif operation == "filter-lt":
                        processor.filter_lt(operation_parts[1], float(operation_parts[2]))
                    elif operation == "population-total":
                        processor.population_total()
                    elif operation == "population":
                        processor.population_field(operation_parts[1])
                    elif operation == "percent":
                        processor.percent_field(operation_parts[1])
                    else:
                        print(f"Unknown operation at line {line_number}: {line}")
                except Exception as e:
                    print(f"Error processing operation at line {line_number}: {e}")
    except FileNotFoundError:
        print(f"Error: Operations file '{operations_file}' not found.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python hw4.py <operations_file>")
        sys.exit(1)

    operations_file = sys.argv[1]
    data_file = "county_demographics.data"

    try:
        processor = CountyDataProcessor(data_file)
        print(f"Loaded dataset with {len(processor.data)} entries.")

        process_operations(operations_file, processor)

    except DatasetException as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()