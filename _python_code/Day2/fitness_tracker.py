import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import DateFormatter

# ---------- CLASSES ----------

class LogEntry:
    def __init__(self, date):
        self.date = date

class Workout(LogEntry):
    def __init__(self, date, workout_type, duration, calories):
        super().__init__(date)
        self.workout_type = workout_type
        self.duration = duration
        self.calories = calories

class Meal(LogEntry):
    def __init__(self, date, meal_type, food, calories):
        super().__init__(date)
        self.meal_type = meal_type
        self.food = food
        self.calories = calories

# ---------- FILE PATHS ----------

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
WORKOUTS_FILE = os.path.join(DATA_DIR, 'workouts.csv')
MEALS_FILE = os.path.join(DATA_DIR, 'meals.csv')

# ---------- READ CSV MANUALLY ----------

def read_workouts_manual(file_path):
    workouts = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            date = row[0].strip()
            workout_type = row[1].strip()
            duration = int(row[2].strip())
            calories = int(row[3].strip())
            workouts.append(Workout(date, workout_type, duration, calories))
    return workouts

# ---------- USING PANDAS ----------

def load_and_clean_data():
    df_workouts = pd.read_csv(WORKOUTS_FILE)
    df_meals = pd.read_csv(MEALS_FILE)

    df_workouts['date'] = pd.to_datetime(df_workouts['date'])
    df_meals['date'] = pd.to_datetime(df_meals['date'])

    # Fill any missing values in workout data with zeros (e.g., missing durations or calories)
    df_workouts.fillna(0, inplace=True)
    # Fill any missing values in meal data with "Unknown" (e.g., missing food descriptions)
    df_meals.fillna("Unknown", inplace=True)

    return df_workouts, df_meals

# ---------- ANALYSIS ----------

def summarize_data(df_workouts, df_meals):
    workout_summary = df_workouts.groupby('date')['calories_burned'].sum().reset_index()
    meal_summary = df_meals.groupby('date')['calories'].sum().reset_index()

    combined = pd.merge(workout_summary, meal_summary, on='date', how='outer').fillna(0)
    combined['net_calories'] = combined['calories'] - combined['calories_burned']
    return combined

# ---------- VISUALIZATION ----------

def plot_fitness_trends(combined_df):
    # Create a new figure with specified size (width: 16 inches, height: 10 inches)
    # This creates a larger plot that is easier to read and analyze
    plt.figure(figsize=(16, 10)) 
    
    # Plot calories consumed with circular markers
    plt.plot(combined_df['date'], combined_df['calories'], label="Calories Consumed", marker='o')
    
    # Plot calories burned with x markers for visual distinction
    plt.plot(combined_df['date'], combined_df['calories_burned'], label="Calories Burned", marker='x')
    
    # Plot net calories (consumed - burned) with dashed line style
    # This shows the caloric balance for each day
    plt.plot(combined_df['date'], combined_df['net_calories'], label="Net Calories", linestyle='--')

    # Calculate and plot a 2-day rolling average of net calories
    # This smooths out daily fluctuations and shows the overall trend
    rolling = combined_df['net_calories'].rolling(window=2).mean()
    plt.plot(combined_df['date'], rolling, label="Rolling Mean (Net)", linestyle='dotted')

    # Add axis labels with increased font size for better readability
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Calories', fontsize=14)
    
    # Format the x-axis to display dates in YYYY-MM-DD format
    # This ensures consistent date representation on the chart
    date_format = DateFormatter('%Y-%m-%d')
    plt.gca().xaxis.set_major_formatter(date_format)
    
    # Rotate x-axis labels by 45 degrees to prevent overlap and increase font size
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    
    plt.title('Fitness Tracker Summary', fontsize=16) # Add a descriptive title to the chart with larger font
    
    plt.legend() # Add a legend to identify each line in the plot
    
    plt.grid(True) # Add a grid to make it easier to read values from the chart
    
    plt.tight_layout() # Adjust layout to ensure all elements fit without overlapping
    
    plt.show() # Display the completed chart


# ---------- MAIN FUNCTION ----------

def main():
    print("Loading data...")
    df_workouts, df_meals = load_and_clean_data()

    print("\nSummarizing data...")
    combined = summarize_data(df_workouts, df_meals)
    print(combined)

    print("\nPlotting results...")
    plot_fitness_trends(combined)

if __name__ == "__main__":
    main()
