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
    int pairSum(ListNode* head) {
        // return listInt(head);
        // return stackSum(head);
        return revInPlace(head);
    }

    int listInt(ListNode* head) {
        ListNode* curr = head;
        vector<int> values;
        
        //iterate over nodes and add ints to values
        while(curr) {
            values.push_back(curr->val);
            curr = curr->next;
        }

        int i = 0; 
        int j = values.size() - 1;
        int maximumSum = 0;

        while (i < j) {
            maximumSum = max(maximumSum, values[i] + values[j]);
            i++;
            j--;
        }

        return maximumSum;
    } //runtime : O(N), space : O(N)

    int stackSum(ListNode* head) {
        ListNode* curr = head;
        stack<int> st;

        while(curr) {
            st.push(curr->val);
            curr = curr->next;
        }

        curr = head;
        int size = st.size(), count = 1;
        int maximumSum = 0;
        while (count <= size) {
            maximumSum = max(maximumSum, curr->val + st.top());
            curr = curr->next;
            st.pop();
            count++;
        }

        return maximumSum;
    } //runtime : O(N), space : O(N)

    int revInPlace(ListNode* head) {
        //get middle of list
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
        }

        //reverse second half of list
        ListNode *nextNode, *prevNode = nullptr;
        while(slow) {
            nextNode = slow->next;
            slow->next = prevNode;
            prevNode = slow;
            slow = nextNode;
        }

        //get max
        int maximumSum = 0;
        ListNode* start = head;
        while(prevNode) {
            maximumSum = max(maximumSum, start->val + prevNode->val);
            prevNode = prevNode->next;
            start = start->next;
        }

        return maximumSum;
    } //runtime O(N), space : O(1)
};