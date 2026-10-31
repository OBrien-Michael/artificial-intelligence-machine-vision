"""
Cluster data with Lloyd's k-means algorithm.

Pseudocode:
1. Precompute the squared norms of all data points.
2. Randomly select k data points as the initial cluster centres.
3. Set previous assignments to None.
4. Repeat for a maximum of max_iters iterations:
    a. Calculate the squared Euclidean distance between each data point and each cluster centre using the binomial expansion.
    b. Assign each data point to the nearest cluster centre.
    c. Calculate new cluster centres by taking the mean of the data points assigned to each cluster.
    d. If the current assignments are identical to the previous assignments, stop because the algorithm has converged.
    e. Store the current assignments as the previous assignments.
5. Return the final cluster assignments and cluster centres.
"""

import numpy as np


def k_means(data,k=3,max_iters=100):
    #precompute norms for fast distance computations
    data_norms=np.sum(data**2,axis=1)

    def get_distances_to_centers(centers):
    #binomial trick for fast distances 
        center_norms = np.sum(centers**2,axis=1) 
        dists =-2*np.dot(data,centers.T)
        dists+=center_norms[np.newaxis,:] 
        dists+=data_norms[:,np.newaxis] 
        return dists

    def get_assignments(centers):
        dists=get_distances_to_centers(centers) 
        assignments = np.argmin(dists,1)
        return dists,assignments
        
    def get_updated_centers(assignments):
        centers=[data[assignments==i,:].mean(axis=0)
            for i in range(k)]
        return np.array(centers)

    def get_initial_centers(): 
        N=data.shape[0]
        indices=np.random.randint(0,N,k)
        return data[indices,:]
        
    #start off with initial random centers 
    centers = get_initial_centers() 
    prev_assignments=None

    for i in range(max_iters):
        # fix centers and update assignments
        dists,assignments = get_assignments(centers)

        # fix assignments and update centers
        centers = get_updated_centers(assignments)
        
        # if nothing changes, we have converged
        if prev_assignments is not None:
            if np.sum(assignments!=prev_assignments)==0:
                    break
        prev_assignments = assignments
    return assignments,centers