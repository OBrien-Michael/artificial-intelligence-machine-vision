
import numpy as np
import matplotlib.pyplot as plt
from k_means import k_means


# Generate sample data with three distinct clusters
np.random.seed(42)

cluster_1 = np.random.randn(50, 2) + [2, 2]
cluster_2 = np.random.randn(50, 2) + [8, 2]
cluster_3 = np.random.randn(50, 2) + [5, 8]

data = np.vstack((cluster_1, cluster_2, cluster_3))


# Run K-means
assignments, centers = k_means(data, k=3, max_iters=100)


# Display results
print("K-means Results")
print("----------------")

print(f"Number of data points: {len(data)}")
print(f"Number of clusters: {len(centers)}")

print("\nCluster centres:")
for i, center in enumerate(centers):
    count = np.sum(assignments == i)
    print(f"Cluster {i}: Centre = {center}, Points = {count}")


# Visualize clusters
plt.figure(figsize=(9, 6))

for i in range(3):
    cluster_points = data[assignments == i]

    plt.scatter(
        cluster_points[:, 0],
        cluster_points[:, 1],
        label=f"Cluster {i} ({len(cluster_points)} points)",
        alpha=0.7
    )

# Plot cluster centres
plt.scatter(
    centers[:, 0],
    centers[:, 1],
    marker="X",
    s=200,
    color="black",
    label="Cluster centres"
)

plt.title("K-means Clustering Results")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()
