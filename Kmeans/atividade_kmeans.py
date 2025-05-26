
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# Carregar o dataset
df = pd.read_csv("credito.csv")

# Exibir informações iniciais
print("Primeiras linhas:")
print(df.head())
print("\nResumo estatístico:")
print(df.describe())
print("\nTipos de dados:")
print(df.dtypes)

# Pré-processamento
# Identificar colunas categóricas e codificá-las
categoricas = df.select_dtypes(include=['object']).columns
le = LabelEncoder()
for col in categoricas:
    df[col] = le.fit_transform(df[col])

# Remover colunas não informativas se necessário
# Ex: df = df.drop(columns=['id', 'nome'])

# Normalização dos dados
scaler = StandardScaler()
X = scaler.fit_transform(df)

# Método do cotovelo e silhouette score
inertia = []
silhouette_scores = []
K = range(2, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X, kmeans.labels_))

# Gráfico do cotovelo
plt.figure(figsize=(10, 4))
plt.plot(K, inertia, 'bo-')
plt.xlabel('Número de clusters')
plt.ylabel('Inércia')
plt.title('Método do Cotovelo')
plt.grid(True)
plt.savefig("grafico_cotovelo.png")
plt.show()

# Gráfico do silhouette
plt.figure(figsize=(10, 4))
plt.plot(K, silhouette_scores, 'ro-')
plt.xlabel('Número de clusters')
plt.ylabel('Silhouette Score')
plt.title('Pontuação de Silhouette')
plt.grid(True)
plt.savefig("grafico_silhouette.png")
plt.show()

# Escolher o melhor k (com base nos gráficos)
melhor_k = 3
kmeans = KMeans(n_clusters=melhor_k, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Análise dos clusters
print("\nAnálise dos clusters:")
print(df.groupby('cluster').mean())

# Visualização com PCA
pca = PCA(n_components=2)
components = pca.fit_transform(X)
df['pca1'] = components[:, 0]
df['pca2'] = components[:, 1]

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='pca1', y='pca2', hue='cluster', palette='Set1')
plt.title('Visualização dos Clusters com PCA')
plt.savefig("clusters_pca.png")
plt.show()
