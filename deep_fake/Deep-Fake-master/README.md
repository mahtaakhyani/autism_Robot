# Deep-Fake

#### Full video: [Deep Fakes](https://www.linkedin.com/posts/karan-owalekar_delaunay-python-deepfakes-activity-6667342958678958080-JL2n)

> Here there are two files, one which takes 2 images a input and applies first image on top of second and second file where it takes 1 image and applies on the face of person captured from the webcam.

> To achive this, we use shape_predictor_81.dat file

> Using that we plot the facial landmarks on the image from webcam.

> After this we construct delaunary triangles on that face.

> We save all the points forming the face.

> These same triangles are constructed on the image we provided and dividing the image into these triangular parts.

> Now these triangular parts are reshaped to fit on same triangle from first image.

> Now we reconstruct second image's face on first iimage.

> Using openCV functions we make necessary color change to look more natural and realistic.

### Future Scope: 
- We can take a video of someone who is moving this face, then divide it similarly into delaunary triangles and story every image into folders inside another folder.
- Here we can store some lenghts. (distances of some important points to identift face orientation) 
- Once its done, we can take imput from webcam and calculate the distances and pick the most matched image from our folder.
- Using that matched image we can construct much better image without weird distortions.
- Giving us much better results when face is rotated.
