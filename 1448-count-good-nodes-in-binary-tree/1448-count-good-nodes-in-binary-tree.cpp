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
    int goodNodes(TreeNode* root) {
        return dfs(root, root->val);
    }
    
    int dfs(TreeNode* root, int maxValue) {
        if(root == NULL) return 0;
        
        
        //check if node is good
        int numGood = 0;
        if (root->val >= maxValue) {
            numGood++;
            maxValue = root->val;
        }
        
        //recur child nodes
        numGood += dfs(root->right, maxValue);
        numGood += dfs(root->left, maxValue);
        
        return numGood;
    }
};