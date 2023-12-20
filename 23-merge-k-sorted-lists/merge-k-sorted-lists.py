class Solution(object):
    def mergeKLists(self, lists):
        length = len(lists)

        if length == 0 or not lists:
            return None


        if length == 1:
            return lists[0]

        mid = length // 2

        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.mergeTwoLists(left, right)




    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2

        elif not list2:
            return list1

        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1

        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2