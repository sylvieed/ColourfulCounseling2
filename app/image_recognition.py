from imageai.Classification import ImageClassification
import os

execution_path = os.getcwd()
prediction = ImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, "resnet50-19c8e357.pth"))
prediction.loadModel()

def classify(image):
  predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, image), result_count=5 )
  for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)
  return (predictions, probabilities)

def guess(image):
  predictions, probabilities = classify(image)
  return predictions[0]