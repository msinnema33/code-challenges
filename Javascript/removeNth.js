// rationale in python file

let removeNthFromEnd = function(head, n) {
    const prehead = new ListNode();
    prehead.next = head;
    
    let cur = prehead, 
        count = 0, 
        nth = null;
    
    while (cur) {
      nth = count === n 
        ? prehead 
        : nth && nth.next;
      count++;
      cur = cur.next;
    }
    
    nth.next = nth.next.next;
    
    return prehead.next;
  };

