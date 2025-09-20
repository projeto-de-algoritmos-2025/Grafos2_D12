#include <algorithm>
#include <numeric>
#include <vector>
using namespace std;

struct DSU {
    vector<int> p, r;
    DSU(int n) : p(n), r(n, 1) { iota(p.begin(), p.end(), 0); }
    int find(int a){ return p[a]==a ? a : p[a]=find(p[a]); }
    bool unite(int a, int b){
        a = find(a); b = find(b);
        if (a == b) return false;
        if (r[a] < r[b]) swap(a, b);
        p[b] = a;
        if (r[a] == r[b]) r[a]++;
        return true;
    }
};

class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(
        int n, vector<vector<int>>& edgesInput
    ) {
        struct Edge { int u,v,w,idx; };
        vector<Edge> edges;
        edges.reserve(edgesInput.size());
        for (int i = 0; i < (int)edgesInput.size(); ++i)
            edges.push_back({edgesInput[i][0], edgesInput[i][1], edgesInput[i][2], i});

        sort(edges.begin(), edges.end(),
             [](const Edge& a, const Edge& b){ return a.w < b.w; });

        auto kruskal = [&](int banIdx, int mustIdx)->int {
            DSU dsu(n);
            int used = 0;
            long long cost = 0;

            if (mustIdx != -1) {
                const auto& e = edges[mustIdx];
                if (dsu.unite(e.u, e.v)) {
                    cost += e.w;
                    used++;
                }
            }

            for (int i = 0; i < (int)edges.size(); ++i) {
                if (i == banIdx) continue;              
                if (i == mustIdx) continue;             
                const auto& e = edges[i];
                if (dsu.unite(e.u, e.v)) {
                    cost += e.w;
                    used++;
                    if (used == n - 1) break;
                }
            }
            return (used == n - 1) ? (int)cost : INT_MAX; 
        };

        int base = kruskal(-1, -1);

        vector<int> critical, pseudo;
        for (int i = 0; i < (int)edges.size(); ++i) {
           
            if (kruskal(i, -1) > base) {
                critical.push_back(edges[i].idx);
            } else {
                
                if (kruskal(-1, i) == base) {
                    pseudo.push_back(edges[i].idx);
                }
            }
        }
        return {critical, pseudo};
    }
};