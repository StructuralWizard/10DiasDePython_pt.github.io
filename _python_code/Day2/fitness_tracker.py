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

# ---------- CAMINHOS DOS ARQUIVOS ----------

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
WORKOUTS_FILE = os.path.join(DATA_DIR, 'workouts.csv')
MEALS_FILE = os.path.join(DATA_DIR, 'meals.csv')

# ---------- LER CSV MANUALMENTE ----------

def read_workouts_manual(file_path):
    workouts = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Pular cabeçalho
        for row in reader:
            date = row[0].strip()
            workout_type = row[1].strip()
            duration = int(row[2].strip())
            calories = int(row[3].strip())
            workouts.append(Workout(date, workout_type, duration, calories))
    return workouts

# ---------- USANDO PANDAS ----------

def load_and_clean_data():
    df_workouts = pd.read_csv(WORKOUTS_FILE)
    df_meals = pd.read_csv(MEALS_FILE)

    df_workouts['date'] = pd.to_datetime(df_workouts['date'])
    df_meals['date'] = pd.to_datetime(df_meals['date'])

    # Preencher quaisquer valores ausentes nos dados de treino com zeros (por exemplo, durações ou calorias ausentes)
    df_workouts.fillna(0, inplace=True)
    # Preencher quaisquer valores ausentes nos dados de refeição com "Desconhecido" (por exemplo, descrições de alimentos ausentes)
    df_meals.fillna("Unknown", inplace=True)

    return df_workouts, df_meals

# ---------- ANÁLISE ----------

def summarize_data(df_workouts, df_meals):
    workout_summary = df_workouts.groupby('date')['calories_burned'].sum().reset_index()
    meal_summary = df_meals.groupby('date')['calories'].sum().reset_index()

    combined = pd.merge(workout_summary, meal_summary, on='date', how='outer').fillna(0)
    combined['net_calories'] = combined['calories'] - combined['calories_burned']
    return combined

# ---------- VISUALIZAÇÃO ----------

def plot_fitness_trends(combined_df):
    # Criar uma nova figura com tamanho especificado (largura: 16 polegadas, altura: 10 polegadas)
    # Isso cria um gráfico maior que é mais fácil de ler e analisar
    plt.figure(figsize=(16, 10)) 
    
    # Plotar calorias consumidas com marcadores circulares
    plt.plot(combined_df['date'], combined_df['calories'], label="Calorias Consumidas", marker='o')
    
    # Plotar calorias queimadas com marcadores x para distinção visual
    plt.plot(combined_df['date'], combined_df['calories_burned'], label="Calorias Queimadas", marker='x')
    
    # Plotar calorias líquidas (consumidas - queimadas) com estilo de linha tracejada
    # Isso mostra o balanço calórico para cada dia
    plt.plot(combined_df['date'], combined_df['net_calories'], label="Calorias Líquidas", linestyle='--')

    # Calcular e plotar uma média móvel de 2 dias das calorias líquidas
    # Isso suaviza as flutuações diárias e mostra a tendência geral
    rolling = combined_df['net_calories'].rolling(window=2).mean()
    plt.plot(combined_df['date'], rolling, label="Média Móvel (Líquida)", linestyle='dotted')

    # Adicionar rótulos dos eixos com tamanho de fonte aumentado para melhor legibilidade
    plt.xlabel('Data', fontsize=14)
    plt.ylabel('Calorias', fontsize=14)
    
    # Formatar o eixo x para exibir as datas no formato AAAA-MM-DD
    # Isso garante uma representação consistente da data no gráfico
    date_format = DateFormatter('%Y-%m-%d')
    plt.gca().xaxis.set_major_formatter(date_format)
    
    # Rotacionar os rótulos do eixo x em 45 graus para evitar sobreposição e aumentar o tamanho da fonte
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    
    plt.title('Resumo do Rastreador Fitness', fontsize=16) # Adicionar um título descritivo ao gráfico com fonte maior
    
    plt.legend() # Adicionar uma legenda para identificar cada linha no gráfico
    
    plt.grid(True) # Adicionar uma grade para facilitar a leitura dos valores do gráfico
    
    plt.tight_layout() # Ajustar o layout para garantir que todos os elementos se encaixem sem sobreposição
    
    plt.show() # Exibir o gráfico concluído


# ---------- FUNÇÃO PRINCIPAL ----------

def main():
    print("Carregando dados...")
    df_workouts, df_meals = load_and_clean_data()

    print("\nResumindo dados...")
    combined = summarize_data(df_workouts, df_meals)
    print(combined)

    print("\nPlotando resultados...")
    plot_fitness_trends(combined)

if __name__ == "__main__":
    main()
