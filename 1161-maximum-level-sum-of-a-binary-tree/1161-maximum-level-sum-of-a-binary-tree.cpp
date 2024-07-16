/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        if(root == nullptr) return 0;

        queue<TreeNode*> q;
        q.push(root);
        int maxV = root->val;
        int maxS = 1;
        int curS = 1;

        while(!q.empty()) {
            int curLen = q.size();
            int curVal = 0;
            for(int i = 0; i < curLen; i++) {
                TreeNode* node = q.front();
                curVal += node->val;
                q.pop();

                if(node->left != nullptr) q.push(node->left);
                if(node->right != nullptr) q.push(node->right);
            }

            if (curVal > maxV) {
                maxV = curVal;
                maxS = curS;
            }

            curS++;
        }

        return maxS;
    } //runtime : O(N), space : O(N)
};