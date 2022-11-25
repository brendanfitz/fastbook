# Family Recognition

## Background

I've restarted doing fastai over the past few weeks. After buying a 3090 for machine learning, I wanted to get back on track with personal projects.
Fastai has been a great way to do so, since it's very structured and I'm already familiar with the course material.
I completed the course last year at this time after doing deeplearning.ai's course. 
It is a great resource and tangible way to get started with deep learning.

For my first fastai project, I thought a fun project would be an image recognition algorithm for identifying members of my family.
I chose this project because, unsuprisingly, it is a very personal to me!
Doing the project has been a fun way to look through old photos and relive some great memories!

## Dataset

My family currently consists of myself, Kara (my fiance) and Ellie (my dog).
To complete this project, Jeremy recommend about 100 photos of each category.
The most difficult part of this project was collecting the data.

For the initial dataset, Kara and I aggregated photos over the past few years.
Some were in New York, some on trips to Europe and Hawaii and some in our current home in Austin.

After the model initially struggled (detailed below), I started taking pictures of our trio everday.
After a few weeks, we had a completely new dataset!

I used our new Synology ds1522+ NAS to store the photos.
Using mobile backup, Kara and I were easily able to view and share photos to create the dataset.
The NAS also empowered us to rapidly add new photos everyday and for testing purposes.

To monitor the dataset, I downloaded the digikam photo organizer.
It was an amazing resource to quickly view the current state of each categories dataset!

## Training

My new 3090 has been even more awesome than I thought it would be. Epochs took only 10 seconds to train (versus a minute for my 3060 ti).
This enabled me to iterate at a faster pace and improve the algorithm.

The initial algorithm struggled with only 25% accuracy.
I wasn't surpised by this as the first model was a true MVP without any data cleaning.
It was heavily biased towards guessing me as shown by the below validation set results. 

![first_run_25_acc](https://user-images.githubusercontent.com/16431716/203878943-f244afb9-fd4c-439f-b5b7-0250337da732.png)

There were a few reasons I believe this was the case:
* Photos of Kara and I were sometimes full body or a headshot only
* Many photos were taken a few years before, and our appearances have slightly changed over time
* There were many distracting elements in photos i.e. sunglasses

After removing a lot of photos and cropping the photos to mainly headshots, I was able to get up to 75% accuracy.
As I added fresh photos everyday, accuracy began to improve even more from there.

I then tried different techniques for pre-processing the photos.
Instead of a random-resized crop, I used blackspace padding and blurred border padding.
I thought that the stretching effect of the random-resized crop was hindering training, but padding actual gave worse results!

After initially training with imagenette's `resnet15`, I moved to `resnet152`. This helped bump the model up a few points when I was above 90% already.

I eventually made it to 95% with these adjustment! That was my goal at the start.

This was a great way to get my feet wet in deep learning again!

## Other Random Thoughts

My new arch linux enviroment has been amazing to work in!
It is very much tailored to my needs.
`i3` has enabled me to quickly setup an IDE enviroment without an IDE.

I've also really enjoyed the new jupyter notebook plugins recommended by Jeremy.
Specifically, `collapsible-headings` and `toc-2` (for navigation) have greatly enhanced the jupyter notebook experience!

