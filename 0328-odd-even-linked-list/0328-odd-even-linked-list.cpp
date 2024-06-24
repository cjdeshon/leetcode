/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if(head == nullptr) return nullptr;

        ListNode* odd = head, *even = head->next, *evenHead = even;
        while(even != nullptr && even->next != nullptr) {
            //odd points to next odd
            odd->next = even->next;
            odd = odd->next;

            //even points to next even
            even->next = odd->next;
            even = even->next;
        }

        //end of oddList -> head of evenList
        odd->next = evenHead;
        return head;
    } //runtime : O(N), space : O(1)
};