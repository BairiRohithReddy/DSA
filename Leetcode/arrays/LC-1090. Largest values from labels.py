class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int: #type:ignore
        lab_val_pair = list(zip(labels,values))
        lab_val_pair.sor(key=lambda x:x[1], reverse = True)
        
        labels_count = {}
        total = 0
        count = 0
        
        for label, value in lab_val_pair:
            if count> num_wanted:
                break
            if labels_count.get(label,0) < use_limit:
                labels_count[label] = labels_count[label, 0] + 1
                total += value
                count += 1
        return total
    