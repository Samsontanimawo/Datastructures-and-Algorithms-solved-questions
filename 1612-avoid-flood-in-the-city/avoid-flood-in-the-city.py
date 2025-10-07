class Solution(object):
    def avoidFlood(self, rains):
        # Dictionary to track last day each lake was filled
        lake_full = {}
        # List to store indices of days we can dry a lake
        dry_days = []
        # Result array
        res = []
        
        for i, lake in enumerate(rains):
            if lake == 0:
                # Dry day, placeholder for now
                dry_days.append(i)
                res.append(1)  # Will update later if needed
            else:
                if lake in lake_full:
                    # Need to find a dry day after last fill and before today
                    found = False
                    for j, dry_day in enumerate(dry_days):
                        if dry_day > lake_full[lake]:
                            res[dry_day] = lake  # Dry this lake on that day
                            dry_days.pop(j)
                            found = True
                            break
                    if not found:
                        return []
                lake_full[lake] = i
                res.append(-1)
        return res