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
    ListNode* deleteMiddle(ListNode* head) {
        // return twoPasses(head);
        return fastSlow(head);
    }

    ListNode* twoPasses(ListNode* head) {
        if (head->next == nullptr) return nullptr;

        int count = 0;
        ListNode *p1 = head, *p2 = head;

        //first pass, count nodes using p1
        while(p1 != nullptr) {
            count++;
            p1 = p1 -> next;
        }

        //get the indesx of the node to be deleted.
        int middleIndex = count / 2;

        //second pass, let p2 move to predecessor of middle node
        for (int i = 0; i < middleIndex - 1; i++) p2 = p2->next;

        //delete middle node and return head
        p2->next = p2->next->next;
        return head;
    } //runtime : O(N), space : O(1)

    ListNode* fastSlow(ListNode* head) {
        if (head->next == nullptr) return nullptr;

        ListNode* slow = head, *fast = head->next->next;

        //iterate both pointers until fast reaches end. Slow will be at pred to middle
        while (fast != nullptr && fast-> next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        //fast has reached end. Remove next node of slow and return head
        slow->next = slow->next->next;
        return head;
    } //runtime : O(N), space : O(1)
};