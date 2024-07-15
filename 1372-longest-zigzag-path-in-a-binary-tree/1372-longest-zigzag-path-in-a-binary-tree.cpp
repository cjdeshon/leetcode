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
    int pathLength = 0;
    void dfs(TreeNode* node, int currStep, bool goRight, int& maxZ) {
        if(node == nullptr) return;
        currStep++;

        maxZ = max(currStep, maxZ);
        if(goRight) {
            dfs(node->right, currStep, false, maxZ);
            dfs(node->left, 0, true, maxZ);
        }
        else {
            dfs(node->left, currStep, true, maxZ);
            dfs(node->right, 0, false, maxZ);
        }

    }
    int longestZigZag(TreeNode* root) {
        int maxZ = 0;
        dfs(root->right, 0, false, maxZ);
        dfs(root->left, 0, true, maxZ);

        return maxZ;
    } //runtime : O(n), space : O(N)
};


// class Solution {
// public:
//     int pathLength = 0;
//     void dfs(TreeNode* node, bool goLeft, int steps) {
//         if (node == nullptr) {
//             return;
//         }
//         pathLength = max(pathLength, steps);
//         if (goLeft) {
//             dfs(node->left, false, steps+1);
//             dfs(node->right, true, 1);
//         }
//         else {
//             dfs(node->left, false, 1);
//             dfs(node->right, true, steps + 1);
//         }
//     }
//     int longestZigZag(TreeNode* root) {
//         dfs(root, false, 0);
//         dfs(root, true, 0);
//         return pathLength;
//     }
// };