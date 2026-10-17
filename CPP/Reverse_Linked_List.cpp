#include <stack>
using namespace std;

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == 0) return 0;

        stack<ListNode*> s;
        ListNode* temp = head;

        while (temp != 0) {
            s.push(temp);
            temp = temp->next;
        }

        ListNode* newHead = s.top();
        s.pop();
        temp = newHead;

        while (!s.empty()) {
            temp->next = s.top();
            s.pop();
            temp = temp->next;
        }
        temp->next = 0;

        return newHead;
    }
};
