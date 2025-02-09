import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import numpy as np


class DataAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analiza Danych - GUI")
        self.root.geometry("1200x800")

        # Zmienne
        self.data = None
        self.model = None
        self.X = None
        self.y = None

        self.create_widgets()

    def create_widgets(self):
        # Panel lewy - kontrolki
        left_panel = ttk.Frame(self.root, padding="10")
        left_panel.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Wybór pliku
        ttk.Button(left_panel, text="Wczytaj plik", command=self.load_file).grid(row=0, column=0, pady=5)

        # Wybór algorytmu
        ttk.Label(left_panel, text="Wybierz algorytm:").grid(row=1, column=0, pady=5)
        self.algorithm_var = tk.StringVar()
        algorithms = ['Random Forest', 'SVM', 'Gradient Boosting', 'Neural Network']
        algorithm_combo = ttk.Combobox(left_panel, textvariable=self.algorithm_var, values=algorithms)
        algorithm_combo.grid(row=2, column=0, pady=5)
        algorithm_combo.bind('<<ComboboxSelected>>', self.update_parameters)

        # Ramka na parametry
        self.params_frame = ttk.LabelFrame(left_panel, text="Parametry", padding="10")
        self.params_frame.grid(row=3, column=0, pady=10, sticky=(tk.W, tk.E))

        # Przyciski akcji
        ttk.Button(left_panel, text="Trenuj model", command=self.train_model).grid(row=4, column=0, pady=5)
        ttk.Button(left_panel, text="Zapisz wyniki", command=self.save_results).grid(row=5, column=0, pady=5)

        # Panel prawy - wykresy
        right_panel = ttk.Frame(self.root, padding="10")
        right_panel.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Miejsce na wykresy
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(8, 8))
        self.canvas = FigureCanvasTkAgg(self.fig, master=right_panel)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def load_file(self):
        filename = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        if filename:
            try:
                if filename.endswith('.csv'):
                    self.data = pd.read_csv(filename)
                else:
                    self.data = pd.read_excel(filename)
                messagebox.showinfo("Sukces", f"Wczytano plik: {len(self.data)} wierszy")
                self.update_data_preview()
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się wczytać pliku: {str(e)}")

    def update_parameters(self, event=None):
        # Czyszczenie ramki z parametrami
        for widget in self.params_frame.winfo_children():
            widget.destroy()

        # Parametry dla wybranego algorytmu
        if self.algorithm_var.get() == "Random Forest":
            self.create_parameter_input("n_estimators", "Liczba drzew:", 100, 1, 1000)
            self.create_parameter_input("max_depth", "Maksymalna głębokość:", 10, 1, 100)
            self.create_parameter_input("min_samples_split", "Min. próbek do podziału:", 2, 2, 20)

        elif self.algorithm_var.get() == "SVM":
            self.create_parameter_input("C", "Parametr regularyzacji:", 1.0, 0.1, 10.0)
            kernel_var = tk.StringVar(value="rbf")
            ttk.Label(self.params_frame, text="Kernel:").pack()
            ttk.Combobox(self.params_frame, textvariable=kernel_var,
                         values=['linear', 'rbf', 'poly']).pack()

        # Dodaj więcej parametrów dla innych algorytmów...

    def create_parameter_input(self, name, label, default, min_val, max_val):
        frame = ttk.Frame(self.params_frame)
        frame.pack(fill=tk.X, pady=2)
        ttk.Label(frame, text=label).pack(side=tk.LEFT)
        var = tk.DoubleVar(value=default)
        scale = ttk.Scale(frame, from_=min_val, to=max_val, variable=var, orient=tk.HORIZONTAL)
        scale.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Entry(frame, textvariable=var, width=8).pack(side=tk.LEFT)
        setattr(self, f"param_{name}", var)

    def update_data_preview(self):
        if self.data is not None:
            # Wykres 1: Podstawowe statystyki
            self.ax1.clear()
            self.data.describe().plot(kind='bar', ax=self.ax1)
            self.ax1.set_title("Statystyki danych")
            self.ax1.tick_params(axis='x', rotation=45)

            # Wykres 2: Macierz korelacji
            self.ax2.clear()
            sns.heatmap(self.data.corr(), ax=self.ax2, annot=True, cmap='coolwarm')
            self.ax2.set_title("Macierz korelacji")

            self.canvas.draw()

    def train_model(self):
        if self.data is None:
            messagebox.showerror("Błąd", "Najpierw wczytaj dane!")
            return

        try:
            # Przygotowanie danych
            # Tu należy dostosować wybór kolumn X i y do konkretnych danych
            self.X = self.data.iloc[:, :-1]  # wszystkie kolumny oprócz ostatniej
            self.y = self.data.iloc[:, -1]  # ostatnia kolumna jako target

            X_train, X_test, y_train, y_test = train_test_split(
                self.X, self.y, test_size=0.2, random_state=42
            )

            # Standaryzacja danych
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            # Wybór i trening modelu
            if self.algorithm_var.get() == "Random Forest":
                from sklearn.ensemble import RandomForestClassifier
                self.model = RandomForestClassifier(
                    n_estimators=int(self.param_n_estimators.get()),
                    max_depth=int(self.param_max_depth.get()),
                    min_samples_split=int(self.param_min_samples_split.get()),
                    random_state=42
                )
            # Dodaj więcej algorytmów...

            # Trening i ewaluacja
            self.model.fit(X_train_scaled, y_train)
            y_pred = self.model.predict(X_test_scaled)

            # Wyświetlenie wyników
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred)

            messagebox.showinfo("Wyniki", f"Dokładność: {accuracy:.2f}\n\n{report}")

            # Aktualizacja wykresów
            self.update_results_plots(X_test_scaled, y_test, y_pred)

        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił błąd podczas treningu: {str(e)}")

    def update_results_plots(self, X_test, y_test, y_pred):
        self.ax1.clear()
        self.ax2.clear()

        # Wykres 1: Porównanie rzeczywistych i przewidzianych wartości
        self.ax1.scatter(range(len(y_test)), y_test, label='Rzeczywiste', alpha=0.5)
        self.ax1.scatter(range(len(y_pred)), y_pred, label='Przewidziane', alpha=0.5)
        self.ax1.set_title("Porównanie wartości rzeczywistych i przewidzianych")
        self.ax1.legend()

        # Wykres 2: Feature importance (jeśli dostępne)
        if hasattr(self.model, 'feature_importances_'):
            importances = pd.Series(
                self.model.feature_importances_,
                index=self.X.columns
            ).sort_values(ascending=False)
            importances.plot(kind='bar', ax=self.ax2)
            self.ax2.set_title("Ważność cech")
            self.ax2.tick_params(axis='x', rotation=45)

        self.canvas.draw()

    def save_results(self):
        if self.model is None:
            messagebox.showerror("Błąd", "Najpierw wytrenuj model!")
            return

        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        if filename:
            try:
                with open(filename, 'w') as f:
                    f.write(f"Algorytm: {self.algorithm_var.get()}\n\n")
                    f.write("Parametry:\n")
                    for widget in self.params_frame.winfo_children():
                        if hasattr(widget, 'param_name'):
                            f.write(f"{widget.param_name}: {getattr(self, f'param_{widget.param_name}').get()}\n")

                    # Zapisz wyniki
                    if hasattr(self.model, 'feature_importances_'):
                        f.write("\nWażność cech:\n")
                        importances = pd.Series(
                            self.model.feature_importances_,
                            index=self.X.columns
                        ).sort_values(ascending=False)
                        f.write(importances.to_string())

                messagebox.showinfo("Sukces", "Wyniki zostały zapisane do pliku!")

            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się zapisać wyników: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalysisApp(root)
    root.mainloop()