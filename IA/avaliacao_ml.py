# avaliacao_ml.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt

# 1. Carregando os dados
df = pd.read_csv('heart_disease_dataset.csv')
print("Primeiras linhas do dataset:")
print(df.head())

# 2. Preparando os dados
df_encoded = pd.get_dummies(df, drop_first=True)
X = df_encoded.drop('Heart Disease', axis=1)
y = df_encoded['Heart Disease']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 3. Treinando os modelos
models = {
    "Árvore de Decisão": DecisionTreeClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "Regressão Logística": LogisticRegression(max_iter=1000)
}

for name, model in models.items():
    model.fit(X_train, y_train)

# 4. Avaliando os modelos
print("\nMétricas de desempenho:")
for name, model in models.items():
    y_pred = model.predict(X_test)
    print(f"\n--- {name} ---")
    print(f"Acurácia: {accuracy_score(y_test, y_pred):.2f}")
    print(f"Precisão: {precision_score(y_test, y_pred):.2f}")
    print(f"Recall: {recall_score(y_test, y_pred):.2f}")
    print(f"F1-score: {f1_score(y_test, y_pred):.2f}")

# 5. Análise de características (Árvore de Decisão)
tree_model = models["Árvore de Decisão"]
importances = tree_model.feature_importances_
feature_names = X.columns

plt.figure(figsize=(10, 6))
plt.barh(feature_names, importances)
plt.title("Importância das Características - Árvore de Decisão")
plt.xlabel("Importância")
plt.show()

# Matriz de confusão para o melhor modelo
best_model = models["Regressão Logística"]
y_pred = best_model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("\nMatriz de Confusão do melhor modelo (Regressão Logística):")
print(cm)
