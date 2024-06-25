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
    int maxDepth(TreeNode* root) {
        if(root) return recur(root, 1);
        else return 0;

        // if(root == NULL) {
        //     return 0;
        // }
        // return max(1 + maxDepth(root->left), 1 + maxDepth(root->right));
    }

    int recur(TreeNode* root, int maxD) {
        //no children
        if (!(root->right) && !(root->left)) return maxD;

        //both children
        if (root->right && root->left) {
            maxD++;
            return max(recur(root->right, maxD), recur(root->left, maxD) );
        }

        //right child
        if(root->right) {
            cout << "right child ";
            maxD++;
           return  recur(root->right, maxD);
        }

        //left child
        if(root->left) {
            cout << "left child ";
            maxD++;
            return recur(root->left, maxD);
        }

        return -1;
    }
};