# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

#impoting the necessary libraries
import argparse
import numpy as np
import tensorflow as tf
import cv2

tf.compat.v1.disable_eager_execution()

def load_graph(model_file):
  graph = tf.Graph()
  graph_def = tf.compat.v1.GraphDef()

  with open(model_file, "rb") as f:
    graph_def.ParseFromString(f.read())
  with graph.as_default():
    tf.import_graph_def(graph_def)

  return graph

#changes to original code is made in the below function. here the paramete img is a frame of the video
def read_tensor_from_image_file(img,
                                input_height=299,
                                input_width=299,
                                input_mean=0,
                                input_std=255):
    #Resize to respect the input_shape
    inp = cv2.resize(img, (input_width , input_height ))

    #Convert img to RGB
    rgb = cv2.cvtColor(inp, cv2.COLOR_RGB2BGR)

    #Is optional but i recommend (float convertion and convert img to tensor image)
    rgb_tensor = tf.convert_to_tensor(rgb, dtype=tf.float32)

    #Add dims to rgb_tensor
    rgb_tensor = tf.expand_dims(rgb_tensor , 0)
    normalized = tf.divide(tf.subtract(rgb_tensor, [input_mean]), [input_std])
    sess = tf.compat.v1.Session()
    return sess.run(normalized)


def load_labels(label_file):
  proto_as_ascii_lines = tf.io.gfile.GFile(label_file).readlines()
  return [l.rstrip() for l in proto_as_ascii_lines]


if __name__ == "__main__":
  file_name = "grace_hopper.jpg"
  model_file = \
    "inception_v3_2016_08_28_frozen.pb"
  label_file = "imagenet_slim_labels.txt"
  input_height = 299
  input_width = 299
  input_mean = 0
  input_std = 255
  input_layer = "input"
  output_layer = "InceptionV3/Predictions/Reshape_1"

  parser = argparse.ArgumentParser()
  parser.add_argument("--image", help="image to be processed")
  parser.add_argument("--graph", help="graph/model to be executed")
  parser.add_argument("--labels", help="name of file containing labels")
  parser.add_argument("--input_height", type=int, help="input height")
  parser.add_argument("--input_width", type=int, help="input width")
  parser.add_argument("--input_mean", type=int, help="input mean")
  parser.add_argument("--input_std", type=int, help="input std")
  parser.add_argument("--input_layer", help="name of input layer")
  parser.add_argument("--output_layer", help="name of output layer")
  args = parser.parse_args()

  if args.graph:
    model_file = args.graph
  if args.image:
    file_name = args.image
  if args.labels:
    label_file = args.labels
  if args.input_height:
    input_height = args.input_height
  if args.input_width:
    input_width = args.input_width
  if args.input_mean:
    input_mean = args.input_mean
  if args.input_std:
    input_std = args.input_std
  if args.input_layer:
    input_layer = args.input_layer
  if args.output_layer:
    output_layer = args.output_layer

  graph = load_graph(model_file)

#Here is the main modification, earlier input was a video but here our input is a video.
  cap = cv2.VideoCapture('fruit-and-vegetable-detection.mp4')
  count=0
  if (cap.isOpened()== False):
    print("Error opening video file")

  with tf.compat.v1.Session(graph=graph) as sess:

    while(cap.isOpened()):
        
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:

          #optimisation: We skip some frames. Here we skip 10 frames, and then we pass the 11th frame to our read_tensor_fromm_image_file() function
          count += 5 # i.e. at 5 fps, this advances one second
          cap.set(cv2.CAP_PROP_POS_FRAMES, count)

          t = read_tensor_from_image_file(frame,input_height=input_height,input_width=input_width,input_mean=input_mean,input_std=input_std)

          input_name = "import/" + input_layer
          output_name = "import/" + output_layer
          input_operation = graph.get_operation_by_name(input_name)
          output_operation = graph.get_operation_by_name(output_name)

          results = sess.run(output_operation.outputs[0], {
              input_operation.outputs[0]: t
          })
          results = np.squeeze(results)

          top_k = results.argsort()[-5:][::-1]
          labels = load_labels(label_file)
          
          k=1
          for i in top_k:
              #storing the predicted label and confidence level of objects in the frame as string.
              text = str(labels[i])+" "+str(results[i])
              #if confidence level is greater than 80% setting the font color to green otherwise red
              if results[i] >= 0.8:
                font_color = (0,255,0) #BGR green
              else:
                font_color = (0,0,255)  #BGR red
              #Adding our text in the frame
              cv2.putText(frame, text, (50,50+50*(k-1)), cv2.FONT_HERSHEY_SIMPLEX, 1, font_color, 2, cv2.LINE_AA)
              k+=1
          #Display the frame
          cv2.imshow('Frame', frame)
          # Press Q on keyboard to exit
          if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        else:
          # When everything done, release the video capture object
          cap.release()
          break
  
# Closes all the frames
cv2.destroyAllWindows()