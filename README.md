Music apps are commonly used for entertainment in our daily lives, and they have many options for users to refine their personal settings for the music listening experience. For example, the theme and color of the user interface, the scrolling speed of the lyrics while listening to music, and the distribution of high and low frequencies of the music.

In this study, I would like to address the user's music listening experience. Based on the characteristics of my task assignment, the task I designed was to learn users' volume level setting preferences while listening to music.

Users will adjust the volume level when listening to music to get a good music experience. The comfort level of volume level varies from person to person, so the range of volume adjustment is generally large and continuous value adjustment.


In this deployment, I refer to the Notebook for the deployment method and related settings in the Bayesian optimizer code section, such as the proxy model and acquisition function settings.
 
First of all, users have different experiences with different volume levels, and when the sound level is 0, users can't hear any music at all. When the sound level is 100, the user will have a very bad experience because the sound is too loud. In addition to these two extremes, volume levels have different listening feedback depending on the type of music.

So in this task, I simulate the user's feedback on different volume levels of music by assuming an objective function. Since the bell curve of normal distribution has this characteristic, I use this function here as my hypothetical objective function for the Bayesian optimizer to learn. In addition to this, in order to simulate the various influences on the user when making choices, I have included normally distributed random numbers to add realism.
 
Considering the task I have set is to use Bayesian optimizer to learn the user's preference for volume level setting in different types of music. So I categorized it into three cases. Rock music, light music, and white noise audio respectively. Considering that rock music is generally louder, I set its optimal volume level to 65. light music's optimal volume level is set to 40. and white noise audio's optimal volume level is set to 20.
 
 
 
In a Bayesian optimizer, its default search is for the parameter that minimizes the objective function. So for the objective I need to maximize the objective function, I need to talk about the objective function taking negative values. Minimizing the objective function for its negative value is then achieved to get the largest objective function.

Considering that the shape of the objective function is similar to a symmetric shape, I set the initial number of data points to 2. The number of iterations is set to 8. This makes a total of 10 data points. Each iteration shows the real-time situation of the proxy model with the acquisition function.

First, by using a Gaussian process, the Bayesian optimization is able to select, in each iteration, those evaluation points that are likely to maximize information acquisition. It can be observed that the model is updated based on the newly acquired data and the acquisition function determines the next evaluation point based on the new model. This hypothetical experiment completed the exploration of the objective function after only a small number (8) of samples after a reasonable assumption of the objective function in advance, reducing the time cost of testing and validation. And in this case, the volume levels that maximize user satisfaction with different music genres were found.
