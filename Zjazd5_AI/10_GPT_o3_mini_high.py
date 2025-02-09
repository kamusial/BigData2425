import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Importujemy algorytmy ze scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.cluster import KMeans


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikacja Analizy Danych - AI")
        self.geometry("1100x750")

        # Ścieżka do pliku, dane wczytane z pliku, wyniki analizy
        self.filename = None
        self.data = None
        self.results = None  # DataFrame z wynikami (np. etykiety lub klastery)

        # Słownik pól parametrów
        self.param_entries = {}

        # Utworzenie głównych elementów interfejsu
        self.create_widgets()

    def create_widgets(self):
        # ===== Ramka wyboru pliku =====
        file_frame = tk.Frame(self)
        file_frame.pack(pady=10, fill=tk.X)

        tk.Label(file_frame, text="Wybierz plik CSV:").pack(side=tk.LEFT, padx=5)
        self.file_entry = tk.Entry(file_frame, width=60)
        self.file_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(file_frame, text="Przeglądaj", command=self.browse_file).pack(side=tk.LEFT, padx=5)

        # ===== Ramka wyboru algorytmu =====
        algo_frame = tk.Frame(self)
        algo_frame.pack(pady=10, fill=tk.X)

        tk.Label(algo_frame, text="Wybierz algorytm:").pack(side=tk.LEFT, padx=5)
        self.algo_var = tk.StringVar()
        self.algo_combo = ttk.Combobox(algo_frame, textvariable=self.algo_var, state="readonly", width=30)
        # Algorytmy: pięć metod klasyfikacyjnych oraz klasteryzacja (K-Means)
        self.algo_combo['values'] = ["KNN", "Drzewo decyzyjne", "Las losowy",
                                     "Regresja logistyczna", "SVC", "K-Means"]
        self.algo_combo.current(0)
        self.algo_combo.pack(side=tk.LEFT, padx=5)
        self.algo_combo.bind("<<ComboboxSelected>>", self.update_parameters)

        # ===== Ramka parametrów =====
        self.params_frame = tk.LabelFrame(self, text="Parametry")
        self.params_frame.pack(pady=10, fill=tk.X, padx=10)
        self.update_parameters()  # Inicjalnie tworzymy pola dla domyślnego algorytmu

        # ===== Ramka przycisków =====
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Uruchom", command=self.run_analysis).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Zapisz wyniki", command=self.save_results).pack(side=tk.LEFT, padx=5)

        # ===== Ramka wykresu =====
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
        # Usuwamy poprzednio utworzone widgety w ramce parametrów
        for widget in self.params_frame.winfo_children():
            widget.destroy()
        self.param_entries.clear()

        algo = self.algo_var.get()

        # Ustalamy listę pól w zależności od wybranego algorytmu:
        # Dla metod nadzorowanych (klasyfikacja) wymagamy podania cech oraz kolumny celu.
        # Dla K-Means (klasteryzacja) nie potrzebujemy kolumny celu, ale wymagamy dodatkowo kolumn do wizualizacji.
        if algo == "K-Means":
            # Parametry dla klasteryzacji
            params_spec = [
                ("Kolumny cech (oddziel przecinkami)", "features", ""),
                ("Kolumna X do wizualizacji", "x", ""),
                ("Kolumna Y do wizualizacji", "y", ""),
                ("Liczba klastrów", "n_clusters", "3")
            ]
        else:
            # Parametry wspólne dla metod klasyfikacyjnych
            common = [
                ("Kolumny cech (oddziel przecinkami)", "features", ""),
                ("Kolumna celu", "target", "")
            ]
            # Parametry specyficzne dla poszczególnych algorytmów
            if algo == "KNN":
                specific = [("Liczba sąsiadów (n_neighbors)", "n_neighbors", "5")]
            elif algo == "Drzewo decyzyjne":
                specific = [("Maksymalna głębokość (max_depth)", "max_depth", "None")]
            elif algo == "Las losowy":
                specific = [("Liczba estymatorów (n_estimators)", "n_estimators", "100"),
                            ("Maksymalna głębokość (max_depth)", "max_depth", "None")]
            elif algo == "Regresja logistyczna":
                specific = [("Parametr C", "C", "1.0")]
            elif algo == "SVC":
                specific = [("Parametr C", "C", "1.0"),
                            ("Kernel", "kernel", "rbf")]
            else:
                specific = []
            params_spec = common + specific

        # Dynamiczne tworzenie pól (etykieta + Entry) zgodnie z listą parametrów
        for label_text, key, default in params_spec:
            frame = tk.Frame(self.params_frame)
            frame.pack(fill=tk.X, padx=5, pady=2)
            tk.Label(frame, text=label_text, width=40, anchor="w").pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            if default:
                entry.insert(0, default)
            self.param_entries[key] = entry

    def run_analysis(self):
        # Sprawdzamy czy wybrano plik
        if not self.filename:
            messagebox.showerror("Błąd", "Najpierw wybierz plik do analizy.")
            return

        try:
            self.data = pd.read_csv(self.filename)
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się odczytać pliku: {e}")
            return

        # Pobieramy wpisane parametry
        params = {key: entry.get() for key, entry in self.param_entries.items()}
        algo = self.algo_var.get()
        self.ax.clear()

        # Wybieramy odpowiednią metodę analizy
        if algo == "KNN":
            self.run_knn(params)
        elif algo == "Drzewo decyzyjne":
            self.run_decision_tree(params)
        elif algo == "Las losowy":
            self.run_random_forest(params)
        elif algo == "Regresja logistyczna":
            self.run_logistic_regression(params)
        elif algo == "SVC":
            self.run_svc(params)
        elif algo == "K-Means":
            self.run_kmeans(params)
        else:
            messagebox.showerror("Błąd", "Wybrany algorytm nie jest obsługiwany.")
            return

        self.canvas.draw()

    # ------------------- Metody dla algorytmów nadzorowanych (klasyfikacja) ------------------- #
    def run_knn(self, params):
        # Pobieramy kolumny cech oraz kolumnę celu
        features_str = params.get("features")
        target = params.get("target")
        if not features_str or not target:
            messagebox.showerror("Błąd", "Podaj kolumny cech oraz kolumnę celu!")
            return
        features = [s.strip() for s in features_str.split(",") if s.strip()]
        if any(col not in self.data.columns for col in features) or target not in self.data.columns:
            messagebox.showerror("Błąd", "Podane kolumny nie istnieją w danych.")
            return

        try:
            n_neighbors = int(params.get("n_neighbors")) if params.get("n_neighbors") else 5
        except:
            messagebox.showerror("Błąd", "Liczba sąsiadów musi być liczbą całkowitą.")
            return

        # Przygotowujemy dane i dokonujemy podziału na zbiór treningowy i testowy
        X = self.data[features]
        y = self.data[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        model = KNeighborsClassifier(n_neighbors=n_neighbors)
        model.fit(X_train, y_train)
        train_acc = model.score(X_train, y_train)
        test_acc = model.score(X_test, y_test)

        # Rysujemy wykres słupkowy z dokładnością
        self.ax.bar(['Train', 'Test'], [train_acc, test_acc], color=['blue', 'green'])
        self.ax.set_ylim(0, 1)
        self.ax.set_ylabel("Dokładność")
        self.ax.set_title("KNN - Dokładność")
        for i, acc in enumerate([train_acc, test_acc]):
            self.ax.text(i, acc + 0.01, f"{acc:.2f}", ha='center')

        # Zapisujemy wyniki: zbiór testowy z rzeczywistymi etykietami i predykcjami
        y_pred = model.predict(X_test)
        self.results = X_test.copy()
        self.results["Actual"] = y_test.values
        self.results["Predicted"] = y_pred

    def run_decision_tree(self, params):
        features_str = params.get("features")
        target = params.get("target")
        if not features_str or not target:
            messagebox.showerror("Błąd", "Podaj kolumny cech oraz kolumnę celu!")
            return
        features = [s.strip() for s in features_str.split(",") if s.strip()]
        if any(col not in self.data.columns for col in features) or target not in self.data.columns:
            messagebox.showerror("Błąd", "Podane kolumny nie istnieją w danych.")
            return

        max_depth_param = params.get("max_depth")
        if max_depth_param == "" or max_depth_param.lower() == "none":
            max_depth = None
        else:
            try:
                max_depth = int(max_depth_param)
            except:
                messagebox.showerror("Błąd", "Maksymalna głębokość musi być liczbą całkowitą lub None.")
                return

        X = self.data[features]
        y = self.data[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)
        train_acc = model.score(X_train, y_train)
        test_acc = model.score(X_test, y_test)

        self.ax.bar(['Train', 'Test'], [train_acc, test_acc], color=['blue', 'green'])
        self.ax.set_ylim(0, 1)
        self.ax.set_ylabel("Dokładność")
        self.ax.set_title("Drzewo decyzyjne - Dokładność")
        for i, acc in enumerate([train_acc, test_acc]):
            self.ax.text(i, acc + 0.01, f"{acc:.2f}", ha='center')

        y_pred = model.predict(X_test)
        self.results = X_test.copy()
        self.results["Actual"] = y_test.values
        self.results["Predicted"] = y_pred

    def run_random_forest(self, params):
        features_str = params.get("features")
        target = params.get("target")
        if not features_str or not target:
            messagebox.showerror("Błąd", "Podaj kolumny cech oraz kolumnę celu!")
            return
        features = [s.strip() for s in features_str.split(",") if s.strip()]
        if any(col not in self.data.columns for col in features) or target not in self.data.columns:
            messagebox.showerror("Błąd", "Podane kolumny nie istnieją w danych.")
            return

        # Pobieramy parametry: liczba estymatorów oraz maksymalna głębokość
        n_estimators_param = params.get("n_estimators")
        if n_estimators_param == "":
            n_estimators = 100
        else:
            try:
                n_estimators = int(n_estimators_param)
            except:
                messagebox.showerror("Błąd", "Liczba estymatorów musi być liczbą całkowitą.")
                return

        max_depth_param = params.get("max_depth")
        if max_depth_param == "" or max_depth_param.lower() == "none":
            max_depth = None
        else:
            try:
                max_depth = int(max_depth_param)
            except:
                messagebox.showerror("Błąd", "Maksymalna głębokość musi być liczbą całkowitą lub None.")
                return

        X = self.data[features]
        y = self.data[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)
        train_acc = model.score(X_train, y_train)
        test_acc = model.score(X_test, y_test)

        self.ax.bar(['Train', 'Test'], [train_acc, test_acc], color=['blue', 'green'])
        self.ax.set_ylim(0, 1)
        self.ax.set_ylabel("Dokładność")
        self.ax.set_title("Las losowy - Dokładność")
        for i, acc in enumerate([train_acc, test_acc]):
            self.ax.text(i, acc + 0.01, f"{acc:.2f}", ha='center')

        y_pred = model.predict(X_test)
        self.results = X_test.copy()
        self.results["Actual"] = y_test.values
        self.results["Predicted"] = y_pred

    def run_logistic_regression(self, params):
        features_str = params.get("features")
        target = params.get("target")
        if not features_str or not target:
            messagebox.showerror("Błąd", "Podaj kolumny cech oraz kolumnę celu!")
            return
        features = [s.strip() for s in features_str.split(",") if s.strip()]
        if any(col not in self.data.columns for col in features) or target not in self.data.columns:
            messagebox.showerror("Błąd", "Podane kolumny nie istnieją w danych.")
            return

        C_param = params.get("C")
        if C_param == "":
            C = 1.0
        else:
            try:
                C = float(C_param)
            except:
                messagebox.showerror("Błąd", "Parametr C musi być liczbą.")
                return

        X = self.data[features]
        y = self.data[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        model = LogisticRegression(C=C, solver='lbfgs', max_iter=1000)
        try:
            model.fit(X_train, y_train)
        except Exception as e:
            messagebox.showerror("Błąd", f"Błąd w regresji logistycznej: {e}")
            return

        train_acc = model.score(X_train, y_train)
        test_acc = model.score(X_test, y_test)

        self.ax.bar(['Train', 'Test'], [train_acc, test_acc], color=['blue', 'green'])
        self.ax.set_ylim(0, 1)
        self.ax.set_ylabel("Dokładność")
        self.ax.set_title("Regresja logistyczna - Dokładność")
        for i, acc in enumerate([train_acc, test_acc]):
            self.ax.text(i, acc + 0.01, f"{acc:.2f}", ha='center')

        y_pred = model.predict(X_test)
        self.results = X_test.copy()
        self.results["Actual"] = y_test.values
        self.results["Predicted"] = y_pred

    def run_svc(self, params):
        features_str = params.get("features")
        target = params.get("target")
        if not features_str or not target:
            messagebox.showerror("Błąd", "Podaj kolumny cech oraz kolumnę celu!")
            return
        features = [s.strip() for s in features_str.split(",") if s.strip()]
        if any(col not in self.data.columns for col in features) or target not in self.data.columns:
            messagebox.showerror("Błąd", "Podane kolumny nie istnieją w danych.")
            return

        C_param = params.get("C")
        if C_param == "":
            C = 1.0
        else:
            try:
                C = float(C_param)
            except:
                messagebox.showerror("Błąd", "Parametr C musi być liczbą.")
                return

        kernel = params.get("kernel")
        if not kernel:
            kernel = "rbf"

        X = self.data[features]
        y = self.data[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        model = SVC(C=C, kernel=kernel, probability=True)
        try:
            model.fit(X_train, y_train)
        except Exception as e:
            messagebox.showerror("Błąd", f"Błąd w SVC: {e}")
            return

        train_acc = model.score(X_train, y_train)
        test_acc = model.score(X_test, y_test)

        self.ax.bar(['Train', 'Test'], [train_acc, test_acc], color=['blue', 'green'])
        self.ax.set_ylim(0, 1)
        self.ax.set_ylabel("Dokładność")
        self.ax.set_title("SVC - Dokładność")
        for i, acc in enumerate([train_acc, test_acc]):
            self.ax.text(i, acc + 0.01, f"{acc:.2f}", ha='center')

        y_pred = model.predict(X_test)
        self.results = X_test.copy()
        self.results["Actual"] = y_test.values
        self.results["Predicted"] = y_pred

    # ------------------- Metoda dla algorytmu klasteryzacji ------------------- #
    def run_kmeans(self, params):
        # Dla K-Means potrzebujemy kolumn cech do klasteryzacji oraz kolumn do wizualizacji
        features_str = params.get("features")
        col_x = params.get("x")
        col_y = params.get("y")
        if not features_str or not col_x or not col_y:
            messagebox.showerror("Błąd", "Podaj kolumny cech do klasteryzacji oraz kolumny X i Y do wizualizacji!")
            return
        features = [s.strip() for s in features_str.split(",") if s.strip()]
        if any(col not in self.data.columns for col in
               features) or col_x not in self.data.columns or col_y not in self.data.columns:
            messagebox.showerror("Błąd", "Podane kolumny nie istnieją w danych.")
            return

        try:
            n_clusters = int(params.get("n_clusters")) if params.get("n_clusters") else 3
        except:
            messagebox.showerror("Błąd", "Liczba klastrów musi być liczbą całkowitą.")
            return

        # Pobieramy dane do klasteryzacji
        X_cluster = self.data[features].dropna().values
        if len(X_cluster) == 0:
            messagebox.showerror("Błąd", "Brak danych w wybranych kolumnach do klasteryzacji.")
            return

        try:
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            labels = kmeans.fit_predict(X_cluster)
        except Exception as e:
            messagebox.showerror("Błąd", f"Błąd w K-Means: {e}")
            return

        # Do wizualizacji pobieramy dane z kolumn podanych przez użytkownika
        x_data = self.data[col_x]
        y_data = self.data[col_y]

        self.ax.scatter(x_data, y_data, c=labels, cmap='viridis', marker='o')
        self.ax.set_xlabel(col_x)
        self.ax.set_ylabel(col_y)
        self.ax.set_title("K-Means - Klasteryzacja")

        # Wyniki zapisujemy – oryginalne dane z dodatkową kolumną 'Cluster'
        self.results = self.data.copy()
        self.results["Cluster"] = labels

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
