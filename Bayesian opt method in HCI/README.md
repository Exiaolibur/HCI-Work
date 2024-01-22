***For Bayes_project-1***

>Music apps are commonly used for entertainment in our daily lives, and they have many options for users to refine their personal settings for the music listening experience. For example, the theme and color of the user interface, the scrolling speed of the lyrics while listening to music, and the distribution of high and low frequencies of the music.

In this study, I would like to address the user's music listening experience. Based on the characteristics of my task assignment, the task I designed was to learn users' volume level setting preferences while listening to music.

In a Bayesian optimizer, its default search is for the parameter that minimizes the objective function. So for the objective I need to maximize the objective function, I need to talk about the objective function taking negative values. Minimizing the objective function for its negative value is then achieved to get the largest objective function.

Considering that the shape of the objective function is similar to a symmetric shape, I set the initial number of data points to 2. The number of iterations is set to 8. This makes a total of 10 data points. Each iteration shows the real-time situation of the proxy model with the acquisition function.

First, by using a Gaussian process, the Bayesian optimization is able to select, in each iteration, those evaluation points that are likely to maximize information acquisition. It can be observed that the model is updated based on the newly acquired data and the acquisition function determines the next evaluation point based on the new model. This hypothetical experiment completed the exploration of the objective function after only a small number (8) of samples after a reasonable assumption of the objective function in advance, reducing the time cost of testing and validation. And in this case, the volume levels that maximize user satisfaction with different music genres were found.


***For Bayes_project-2***
>Music Player App is a commonly used cell phone software in our daily life. We often perform interactive behaviors on the user interface when we listen to music on our cell phones.
>In order to provide smart phone users with a better interaction experience of using music software, I chose the virtual keys of the music player interface as the research object. My approach is to optimize the buttons' triggering and feedback the user experience more concise and effective in preventing false touches. In this task, I will use Bayesian optimization to optimize the selection of these modes using user feedback.


The interface of the music player app is shown below, and users can operate the music playback mode through these five virtual buttons:
 
In assignment1, I assigned each of the 5 virtual buttons on the UI the following interaction properties:
Trigger mode: click trigger, long press trigger
Feedback mode: mute feedback, vibration feedback

For each of the five virtual keys, there will be two sets of interaction properties, one for trigger mode and the other for feedback mode. The interaction properties of these four UI elements affect the user experience to a certain extent. 

***For more details from the aspect of theory on this project, please take a look on Bayes_project-2.pdf***🙂


