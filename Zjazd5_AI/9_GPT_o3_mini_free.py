import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.cluster import KMeans


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikacja Analizy Danych")
        self.geometry("1000x700")

        # Inicjalizacja zmiennych
        self.filename = None
        self.data = None
        self.results = None

        # Utworzenie komponentów interfejsu
        self.create_widgets()

    def create_widgets(self):
        # Ramka wyboru pliku
        file_frame = tk.Frame(self)
        file_frame.pack(pady=10, fill=tk.X)

        tk.Label(file_frame, text="Wybierz plik do analizy:").pack(side=tk.LEFT, padx=5)
        self.file_entry = tk.Entry(file_frame, width=50)
        self.file_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(file_frame, text="Przeglądaj", command=self.browse_file).pack(side=tk.LEFT, padx=5)

        # Ramka wyboru algorytmu
        algo_frame = tk.Frame(self)
        algo_frame.pack(pady=10, fill=tk.X)

        tk.Label(algo_frame, text="Wybierz algorytm:").pack(side=tk.LEFT, padx=5)
        self.algo_var = tk.StringVar()
        self.algo_combo = ttk.Combobox(algo_frame, textvariable=self.algo_var, state="readonly")
        self.algo_combo['values'] = ["Wykres liniowy", "K-Means"]
        self.algo_combo.current(0)
        self.algo_combo.pack(side=tk.LEFT, padx=5)
        self.algo_combo.bind("<<ComboboxSelected>>", self.update_parameters)

        # Ramka parametrów
        self.params_frame = tk.LabelFrame(self, text="Parametry")
        self.params_frame.pack(pady=10, fill=tk.X, padx=10)
        self.param_entries = {}  # słownik z kluczami – nazwami parametrów oraz polami Entry
        self.update_parameters()  # inicjalizacja pól dla domyślnego algorytmu

        # Ramka przycisków (Uruchom, Zapisz wyniki)
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Uruchom", command=self.run_analysis).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Zapisz wyniki", command=self.save_results).pack(side=tk.LEFT, padx=5)

        # Ramka na wykres – wykorzystanie matplotlib
        plot_frame = tk.Frame(self)
        plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.figure = plt.Figure(figsize=(6, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def browse_file(self):
        filetypes = [("CSV files", "*.csv"), ("All files", "*.*")]
        filename = filedialog.askopenfilename(title="Wybierz plik", filetypes=filetypes)
        if filename:
            self.filename = filename
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, filename)

    def update_parameters(self, event=None):
        # Usunięcie dotychczasowych pól parametrów
        for widget in self.params_frame.winfo_children():
            widget.destroy()
        self.param_entries.clear()

        algo = self.algo_var.get()
        if algo == "Wykres liniowy":
            # Dla wykresu liniowego: wybór kolumn X, Y oraz tytułu wykresu
            param_specs = [
                ("Kolumna X", "x"),
                ("Kolumna Y", "y"),
                ("Tytuł wykresu", "title")
            ]
        elif algo == "K-Means":
            # Dla K-Means: liczba klastrów oraz wybór kolumn X i Y
            param_specs = [
                ("Liczba klastrów", "n_clusters"),
                ("Kolumna X", "x"),
                ("Kolumna Y", "y")
            ]
        else:
            param_specs = []

        # Dynamiczne tworzenie pól dla każdego parametru
        for label_text, param_key in param_specs:
            frame = tk.Frame(self.params_frame)
            frame.pack(fill=tk.X, padx=5, pady=2)
            tk.Label(frame, text=label_text, width=20, anchor="w").pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            self.param_entries[param_key] = entry

    def run_analysis(self):
        if not self.filename:
            messagebox.showerror("Błąd", "Najpierw wybierz plik do analizy.")
            return
        try:
            # Wczytanie danych z pliku CSV
            self.data = pd.read_csv(self.filename)
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się odczytać pliku: {e}")
            return

        algo = self.algo_var.get()
        # Pobranie parametrów wpisanych przez użytkownika
        params = {key: entry.get() for key, entry in self.param_entries.items()}

        self.ax.clear()

        if algo == "Wykres liniowy":
            self.run_line_chart(params)
        elif algo == "K-Means":
            self.run_kmeans(params)
        else:
            messagebox.showerror("Błąd", "Wybrany algorytm nie jest obsługiwany.")
            return

        self.canvas.draw()

    def run_line_chart(self, params):
        # Parametry: kolumna X, kolumna Y, tytuł wykresu
        x_col = params.get("x")
        y_col = params.get("y")
        title = params.get("title") if params.get("title") else "Wykres liniowy"

        if x_col not in self.data.columns or y_col not in self.data.columns:
            messagebox.showerror("Błąd", "Podane kolumny nie istnieją w danych.")
            return

        x = self.data[x_col]
        y = self.data[y_col]
        self.ax.plot(x, y, marker='o')
        self.ax.set_title(title)
        self.ax.set_xlabel(x_col)
        self.ax.set_ylabel(y_col)

        # Wyniki (wybrane kolumny) zapisywane w postaci DataFrame, co pozwala na zapis do pliku
        self.results = self.data[[x_col, y_col]]

    def run_kmeans(self, params):
        # Parametry: liczba klastrów, kolumna X, kolumna Y
        n_clusters = params.get("n_clusters")
        x_col = params.get("x")
        y_col = params.get("y")
        try:
            n_clusters = int(n_clusters)
        except Exception as e:
            messagebox.showerror("Błąd", "Liczba klastrów musi być liczbą całkowitą.")
            return

        if x_col not in self.data.columns or y_col not in self.data.columns:
            messagebox.showerror("Błąd", "Podane kolumny nie istnieją w danych.")
            return

        X = self.data[[x_col, y_col]].dropna().values
        if len(X) == 0:
            messagebox.showerror("Błąd", "Brak danych w podanych kolumnach.")
            return

        try:
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            labels = kmeans.fit_predict(X)
            centers = kmeans.cluster_centers_
        except Exception as e:
            messagebox.showerror("Błąd", f"Błąd w algorytmie K-Means: {e}")
            return

        # Rysowanie wyników klasteryzacji
        self.ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o')
        self.ax.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=100, label='Centroidy')
        self.ax.set_xlabel(x_col)
        self.ax.set_ylabel(y_col)
        self.ax.set_title("K-Means Clustering")
        self.ax.legend()

        # Wyniki: kolumny oraz przypisane etykiety klastrów
        result_df = pd.DataFrame(X, columns=[x_col, y_col])
        result_df["Cluster"] = labels
        self.results = result_df

    def save_results(self):
        if self.results is None:
            messagebox.showerror("Błąd", "Brak wyników do zapisania.")
            return

        file = filedialog.asksaveasfilename(defaultextension=".csv",
                                            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                                            title="Zapisz wyniki")
        if file:
            try:
                self.results.to_csv(file, index=False)
                messagebox.showinfo("Sukces", f"Wyniki zostały zapisane do: {file}")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się zapisać pliku: {e}")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
