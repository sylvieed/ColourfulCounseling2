from imageai.Classification import ImageClassification
import os

execution_path = os.getcwd()
prediction = ImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, "resnet50-19c8e357.pth"))
prediction.loadModel()

def classify(image):
  print("Classifying image...")
  imagepath = os.path.join(execution_path, "car.jpg")
  print(imagepath)
  predictions, probabilities = prediction.classifyImage(imagepath, result_count=1 )
  print("Image classified. Results:")
  for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)
  return (predictions, probabilities)

def guess(image):
  predictions, probabilities = classify(image)
  return predictions[0]
