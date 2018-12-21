import numpy as np
import json

# Question 5
def cosineSimilarity(vector1,vector2):
    return np.dot(vector1,vector2)/(np.sqrt(np.dot(vector2,vector2)) * np.sqrt(np.dot(vector1,vector1)))

with open('cnn_dataset.json') as data_file:
    data = json.load(data_file)
print("Cosine similarity between mj1 and mj2 VGG: ", cosineSimilarity(data['vgg_rep']['mj1'], data['vgg_rep']['mj2']))
print("Cosine similarity between mj1 and cat VGG: ", cosineSimilarity(data['vgg_rep']['mj1'], data['vgg_rep']['cat']))
print("Cosine similarity between mj2 and cat VGG: ", cosineSimilarity(data['vgg_rep']['mj2'], data['vgg_rep']['cat']))
print("Cosine similarity between mj1 and mj2 pixel: ", cosineSimilarity(data['pixel_rep']['mj1'], data['pixel_rep']['mj2']))
print("Cosine similarity between mj1 and cat pixel: ", cosineSimilarity(data['pixel_rep']['mj1'], data['pixel_rep']['cat']))
print("Cosine similarity between mj2 and cat pixel: ", cosineSimilarity(data['pixel_rep']['mj2'], data['pixel_rep']['cat']))

#Question 8
with open('dataset.json') as data_file:
    data = json.load(data_file)

train = data['train']
test = data['test']
images = data['images']
captions = data['captions']
vgg = np.load('vgg_rep.npy')
pixel = np.load('pixel_rep.npy')

testData = []
trainData = []

count = 0
for each in images:
    eachDataDetails = {}
    eachDataDetails["name"] = each
    eachDataDetails["vgg"] = vgg[count]
    eachDataDetails["pixel"] = pixel[count]
    eachDataDetails["captions"]=captions[each]
    count += 1
    if each in test:
        testData.append(eachDataDetails)
    elif each in train:
        trainData.append(eachDataDetails)

pixelFile = open('pixel.txt', 'w')
vggFile = open('vgg.txt', 'w')



pixelFile.close()
vggFile.close()