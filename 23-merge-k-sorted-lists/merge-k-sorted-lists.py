class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0 or not lists:
            return None

        elif len(lists) == 1:
            return lists[0]

        mid = len(lists)//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.mergetTwoLists(left, right)

    
    def mergetTwoLists(self, list1, list2):
        if not list1:
            return list2

        elif not list2:
            return list1

        elif list1.val < list2.val:
            list1.next = self.mergetTwoLists(list1.next, list2)
            return list1

        else:
            list2.next = self.mergetTwoLists(list2.next, list1)
            return list2