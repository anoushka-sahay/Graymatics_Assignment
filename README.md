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
Solution: The sample input video file used for this question is ['video.mkv'](https://github.com/anoushka-sahay/Graymatics_Assignment/blob/main/video.mkv). Place the downloaded video in the same directory in which you will be running the code [Problem_3.py](https://github.com/anoushka-sahay/Graymatics_Assignment/blob/main/Problem_3.py) 

### Question 4: We have to modify the folloing [code](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/label_image/label_image.py) inorder to convert this code from image classification to video classification.
Solution: The TensorFlow `GraphDef` that contains the model definition and weights is not packaged in the repo because of its size. Instead, you must first download the
[file](https://storage.googleapis.com/download.tensorflow.org/models/inception_v3_2016_08_28_frozen.pb.tar.gz). This downloaded zip file conatains model 'inception_v3_2016_08_28_frozen.pb' and the label 'imagenet_slim_labels.txt'. Unzip this folder and add these two files in the same directory in which the code downloaded from [Video_classifiacation](https://github.com/anoushka-sahay/Graymatics_Assignment/blob/main/Video_classification.py) is placed<br>
Finally download the sample input video from [fruit-and-vegetable-detection.mp4](https://github.com/anoushka-sahay/Graymatics_Assignment/blob/main/fruit-and-vegetable-detection.mp4)

#### 'Kindly download all the files and code and place all of them in the same directory. Run all the codes using VSCode or any other text editor'




