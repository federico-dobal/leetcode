class Solution(object):
    def build_pre_results(self, equations, values):
        results = {}
        for (v1, v2), r in zip(equations, values):
            print(v1, v2, r)
            result_v1 = results.get(v1)
            if result_v1:
                result_v1[v2] = (r, '*')
            else:
                results[v1] = {v2: (r, '*')}

            result_v2 = results.get(v2) 
            if result_v2:
                result_v2[v1] = (r, '/')
            else:
                results[v2] = {v1: (r, '/')}

        return results

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        pre_results = self.build_pre_results(equations, values)
        print (pre_results)
        ans = []
        for (v1, v2) in queries:

            if v1 == v2 and pre_results.get(v1):
                ans.append(1.0)
                continue

            try:
                ix = equations.index([v1, v2])
                ans.append(values[ix])
                continue
            except ValueError:
                pass

            try:
                ix = equations.index([v2, v1])
                ans.append(1.0 / values[ix])
                continue
            except ValueError:
                pass

            expr_v1 = pre_results.get(v1)
            expr_v2 = pre_results.get(v2)
            if not expr_v1 or not expr_v2:
                result = -1.0
            else:
                #print(v1, expr_v1)
                #print(v2, expr_v2)
                k_v1 = expr_v1.keys()
                k_v2 = expr_v2.keys()
                commons_keys = set(k_v1).intersection(set(k_v2))
                if commons_keys:
                    k = commons_keys.pop()
                    #print(k)
                    #print(expr_v1.get(k))
                    #print(expr_v2.get(k))
                    if expr_v1.get(k)[1] == '*' and expr_v2.get(k)[1] == '*':
                        result = expr_v1.get(k)[0] / expr_v2.get(k)[0]
                    else:
                        result = expr_v1.get(k)[0] * expr_v2.get(k)[0]
                    #print(result)
                else:
                    result = -1.0

            ans.append(result)
        return ans


s = Solution()
#print(s.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))

#print(s.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["x","x"]]))

#print(s.calcEquation([["a","e"],["b","e"]],
#[4.0,3.0],
#[["a","b"],["e","e"],["x","x"]]))

print(s.calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],
[3.0,4.0,5.0,6.0],
#[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]))
[["x1","x5"]]))

#print(s.calcEquation([["a","b"],["b","c"],["bc","cd"]],
#[1.5,2.5,5.0],
#[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))

#print(s.calcEquation([["a","b"]],
#[0.5],
#[["a","b"],["b","a"],["a","c"],["x","y"]]))