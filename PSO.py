# PSO-based Traffic Mutation Algorithm
#
# Input: 
#   Hyperparameters in PSO: 
#       w, c1, c2, N_iter, N_swarm
#   attacker's overhead budget:
#       l_c, l_t
#   particle swarm:
#       S
#   grouped original malicious traffic:
#       T
#
# Output:
#   The grouped mutated malicious traffic:
#       T_mutated

import numpy as np

class PSO:

    pBestFitness = []
    gBest = None
    gBestFitness = np.inf * (-1)

    def __init__(self, T, w=0.5, c1=0.5, c2=0.5, N_swarm=200, N_iter=20, lc=5, lt=2):
        self.T = T
        self.T_mutate = T
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.N_swarm = N_swarm
        self.N_iter = N_iter
        self.lc = lc
        self.lt = lt

    def Vectorize(self, traffic):
        #TODO: meta-info vectorization
        
        
    def Initialize(self, t, swarm, lc, lt):
        #TODO: population initialize

    def Rebuild(self, p):
        #TODO: rebuild vectors to traffic

    def Dist_Eval(self):
        #TODO: distance evaluate and effectiveness evaluation
        self.Feature_extractor()
        F_adver

    def Feature_extractor(self):
        #TODO: feature extract

    def UpdateX(self, particle, v, lc, lt):
        #TODO: update particle

    def Append(self, best):
        #TODO: append best particle into T_mutated

    def run(self):
        # Original malicious trafficis divided into groups with the same number of packets.
        for traffic in self.T:
            t = self.Vectorize(traffic)
            S = self.Initialize(t, self.N_swarm, self.lc, self.lt)
            for i in range(self.N_iter):
                for j in range(self.N_swarm):
                    # distance evaluation
                    # 1. rebuild and replace X_mal to original traffic, 
                    # 2. extract mutated traffic into features
                    # 3. compute the distance between extracted feature and adversarial features as effectiveness

                    self.Rebuild(S.x[j])
                    S.d[j] = self.Dist_Eval()
                    if self.pBestFitness[j] < S.d[j]:
                        self.pBestFitness[j] = S.d[j]
                        S.y[j] = S.x[j]
                    if self.gBestFitness < self.pBestFitness[j]:
                        self.gBestFitness = self.pBestFitness[j]
                        self.gBest = S.y[j]
                    
                for j in range(self.N_swarm):
                    v_cog = S.y[j] - S.x[j]
                    v_soc = gBest - S.x[j]
                    r1 = np.random.rand()
                    r2 = np.random.rand()
                    S.v[j] = self.w * S.v[j] + r1 * self.c1 * v_cog + r2 * self.c2 * v_soc
                    S.x[j] = self.UpdateX(S.x[j], S.v[j], self.lc, self.lt)
                
            self.Append(gBest)
        
        return self.T_mutate


if __name__ == "__main__":
    result = PSO(T).run()

    