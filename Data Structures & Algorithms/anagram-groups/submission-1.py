class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return list(result.values())

        # global_dict = []
        # for s in strs:
        #     str_dict = {}
        #     for c in s:
        #         if c in str_dict:
        #             str_dict[c] += 1
        #         else:
        #             str_dict[c] = 1
        #     global_dict.append(str_dict)
        
        # result = []
        # index = 0
        # result_map = {} #global_dict group to result
        
        # for i in range(len(global_dict)):
        #     if i == 0:
        #         result_map[i] = index
        #         result.append([strs[i]])
        #         index += 1
        #         continue
        #     found = False
        #     for j in range(i):
        #         if global_dict[j] == global_dict[i]:
        #             group_index = result_map[j]
        #             result_map[i] = group_index
        #             result[group_index].append(strs[i])
        #             found = True
        #             break
        #     if not found:
        #         result_map[i] = index
        #         result.append([strs[i]])
        #         index += 1
        # return result    
            
            

