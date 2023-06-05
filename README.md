# Graymatics_Assignment
This repository contains the code for given tasks<br>
<br>
### Question 1: You are given an array of objects representing items to be put in a knapsack. The objects have 3 attributes: name, weight, and value. The items need to be selected so that the total weight does not exceed the maximum weight and the value is maximized.<br><br>
Solution: We have to choose certain elements from the given list such that total weight of those elements does not exceed the given weight threshold and we have to find the maximum possible weight. We have a choice and we have to maximize the value. We will create a table where number of rows is n+1(n is the elements in the list) and number of columns is W+1(where W is the given weight threshold). <br>
t[i][j] = Maximun value when number of items is i and weight threshold is j.<br>
0th row and 0th column of the table t will be 0 because if we have zero items to pick or zero weight threshold then our value will be zero.
We will use the concept that if an item has weight less than weight threshold, then we have two choices that is to consider that item or not. But if an item has weight grater than weight threshold, then we will reject that item.<br>

### Question 2: Given a string (string brackets) containing just the characters '(', ')', '{', '}', '[' and ']', return a result to determine if the input string is valid. A valid string must adhere to the following rules:<br>
=> Open brackets must be closed by the same type of brackets.<br>
=> Open brackets must be closed in the correct order.<br><br>
Solution: We will create a stack. We will first check whether number of open brackets if equal to number of close brackets. If they are not same then return false. If same, then we will traverse the given string, if we encounter an open bracket then we insert it into our stack. If we encounter a closing bracket then we remove the corresponding opening bracket from the top of the stack. If the stack is empty after traversing through the array, then given string is valid otherwise invalid.

### Question 3: Given a short video, (use your own > 60 second video), use OpenCV to clip a 5 second clip from the 00:30 mark to the 00:35 mark and draw a red 100 x 100 pixel sized box in the middle of the video.<br><br>
Solution: The 


