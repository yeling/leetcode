/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var oddEvenList = function (head) {
    if(head == null || head.next == null) {
        return head;
    }
    let temp =  head;
    let evenHead = null;
    let evenHead2 = null;
    let oddHead = null;
    let count = 1;
    while(temp != null) {
        //console.log(temp.val);
        if(count%2 == 0) {
            if(evenHead == null) {
                evenHead = temp;
                evenHead2 = temp;
            } else {
                evenHead2.next = temp;
                evenHead2 = temp;
            }
        } else {
            if(oddHead == null) {
                oddHead = temp;
            } else {
                oddHead.next = temp;
                oddHead = temp;
            }
        }
        temp = temp.next;
        count++;
    }
    evenHead2.next = null;
    oddHead.next = evenHead;
    return head;
};

let head = new ListNode(1);
let temp = head;

temp.next = new ListNode(2);
temp = temp.next;

temp.next = new ListNode(3);
temp = temp.next;

temp.next = new ListNode(4);
temp = temp.next;

temp.next = new ListNode(5);
temp = temp.next;

let res = oddEvenList(head);
while(res != null) {
    console.log(res.val);
    res = res.next;
}

