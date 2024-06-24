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
    ListNode* reverseList(ListNode* head) {
        return tempRev(head);
        // return recursiveRev(head);
    }

    ListNode* tempRev(ListNode* head) {
        ListNode* prevNode = nullptr, *currNode = head;
        while(currNode != nullptr) {
            ListNode *nextNode = currNode->next;
            currNode->next = prevNode;
            prevNode = currNode;
            currNode = nextNode;
        }

        return prevNode;
    } //runtime : O(N), space : O(1)

    //assume that the rest of the list has been reverse. how do we reverse the front part
    ListNode *recursiveRev(ListNode* head) {
        if(head == nullptr || head->next == nullptr) return head;

        ListNode* p = reverseList(head->next);
        head->next->next = head; 
        head->next = nullptr;
        return p;
    } //runtime : O(N), space : O(1)
};