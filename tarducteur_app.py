import tkinter as tk
import pandas as pd

df = pd.read_csv(r"C:\Users\kamel\OneDrive\Documents\Cours\trad kabyle\dictionnaire.csv")

def traduire():
    mot = entree.get().strip().lower()
    if mot == "":
        messagebox.showwarning("Attention", "entrer un mot!")
        return

    if var_dir.get() == "kab → fr":
        ligne = df[df["kabyle"].str.lower() == mot]
        if not ligne.empty:
            sortie.set(f"{ligne['francais'].values[0]} ({ligne['berbere'].values[0]})")
        else:
            sortie.set("mot pas trouvé")
    else:
        ligne = df[df["francais"].str.lower() == mot]
        if not ligne.empty:
            sortie.set(f"{ligne['kabyle'].values[0]} ({ligne['berbere'].values[0]})")
        else:
            sortie.set("mot pas trouvé")


#mot aleatoire
def mot_aleatoire():
    ligne = df.sample(n=1).iloc[0]
    if var_dir.get() == "kab → fr":
        sortie.set(f"{ligne['kabyle']} → {ligne['francais']} ({ligne['berbere']})")
    else:
        sortie.set(f"{ligne['francais']} → {ligne['kabyle']} ({ligne['berbere']})")
        

fen = tk.Tk()
fen.title("Traducteur Kabyle ↔ Français")
fen.geometry("500x350")
fen.configure(bg="#f5f5f5")  #couleur

#titrre
tk.Label(fen, text="Traducteur Kabyle ↔ Français", font=("Helvetica", 18, "bold"), bg="#f5f5f5").pack(pady=15)

#entree
entree = tk.Entry(fen, width=30, font=("Arial", 14))
entree.pack(pady=10)

#choix direction
var_dir = tk.StringVar(value="kab → fr")
frame_radio = tk.StringVar(value= "kab→ fr")
frame_radio = tk.Frame(fen, bg="#f5f5f5")
frame_radio.pack(pady=5)
tk.Radiobutton(frame_radio, text="kab → fr", variable=var_dir, value="kab → fr", bg="#f5f5f5", font=("Arial", 12)).pack(side="left", padx=10)
tk.Radiobutton(frame_radio, text="fr → kab", variable=var_dir, value="fr → kab", bg="#f5f5f5", font=("Arial", 12)).pack(side="left", padx=10)

#bouton
frame_btn = tk.Frame(fen, bg="#f5f5f5")
frame_btn.pack(pady=10)
tk.Button(frame_btn, text="Traduire", command=traduire, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", width=12).pack(side="left", padx=10)
tk.Button(frame_btn, text="Mot aléatoire", command=mot_aleatoire, font=("Arial", 12, "bold"), bg="#2196F3", fg="white", width=12).pack(side="left", padx=10)
#zone sortie
sortie = tk.StringVar()
tk.Label(fen, textvariable=sortie, font=("Arial", 16), fg="blue", bg="#f5f5f5", wraplength=450, justify="center").pack(pady=20)
#lancer lapp
fen.mainloop()
