class MinStack {
public:
    /** initialize your data structure here. */
    int minStack[7500], mn[7500];
    int i = 0;

    MinStack() {
        
    }
    
    void push(int x) {
        minStack[i] = x;
        if (i) mn[i] = min(mn[i-1], x);
        else mn[i] = x;
        ++i;
    }
    
    void pop() {
        --i;
    }
    
    int top() {
        return minStack[i-1];
    }
    
    int getMin() {
        return mn[i-1];
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

