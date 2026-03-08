import tkinter as tk
import pandas as pd

df = pd.read_csv(r"C:\Users\kamel\OneDrive\Documents\Cours\trad kabyle\dictionnaire.csv")

def traduire():
    mot = entree.get().lower().strip()
    if var_dir.get() == "kab → fr":
        ligne = df[df["kabyle"].str.lower() == mot]
        if not ligne.empty:
            sortie.set(f"{ligne['francais'].values[0]} ({ligne['berbere'].values[0]})")
        else:
            sortie.set("Mot pas trouvé")
    else:
        ligne = df[df["francais"].str.lower() == mot]
        if not ligne.empty:
            sortie.set(f"{ligne['kabyle'].values[0]} ({ligne['berbere'].values[0]})")
        else:
            sortie.set("Mot pas trouvé")

fen = tk.Tk()
fen.title("Traducteur Kabyle ↔ Français")
fen.geometry("450x250")
fen.configure(bg="#f0f0f0")  # couleur de fond

# Titre
tk.Label(fen, text="Traducteur Kabyle ↔ Français", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Entrée
entree = tk.Entry(fen, width=30, font=("Arial", 12))
entree.pack(pady=5)

# Choix de direction
var_dir = tk.StringVar(value="kab → fr")
tk.Radiobutton(fen, text="kab → fr", variable=var_dir, value="kab → fr", bg="#f0f0f0").pack()
tk.Radiobutton(fen, text="fr → kab", variable=var_dir, value="fr → kab", bg="#f0f0f0").pack()

# Bouton
tk.Button(fen, text="Traduire", command=traduire, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white").pack(pady=10)

# Zone de sortie
sortie = tk.StringVar()
tk.Label(fen, textvariable=sortie, font=("Arial", 14), fg="blue", bg="#f0f0f0").pack(pady=5)

fen.mainloop()