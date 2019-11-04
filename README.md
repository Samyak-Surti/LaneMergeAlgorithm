# Lane Merge Algorithm for Autonomous Cars

Simulation to show autonomous cars merging two lanes to one. 
*2015 Science Fair Project*

![alt text](https://github.com/Samyak-Surti/LaneMergeAlgorithm/blob/master/Images/Sim1.png)

## Abstract
###### Objectives/Goals
Traffic jams are caused in a lane merge when people overly slow down when they are approaching the
merge. As the people in front start to slow down people behind them also start to get backed up causing
everybody to squeeze together like an accordion being pushed from one side. But in the case of an
autonomous car if the proper algorithm is implied to accelerate on entry to the merge point it can avoid
traffic jams and still maintain a safe distance between each car. So my goal was to create an algorithm that
will allow autonomous cars to successfully execute a lane merge under certain assumptions.

###### Results
Initially my algorithm was not working for some cases because I was first approximating the distance
between each car which allowed for some faults in the program. To fix those faults, I used another
approach of finding the actual distance between each car for every delta t the program was running for.

This helped me better understand the type of angles the autonomous cars would be turning at, and the
speeds they would be going at in real life on the road. Through the course of figuring out my algorithm, I
realized that it is correlated with the Venturi Effect. In the Venturi Effect it states that if the space within
the pipe is smaller, the velocity within the pipe will be more so that it can maintain streamline motion.

###### Conclusions/Discussion
My original intuition that I had to the solution of the problem was demonstrated to work in several cases
for autonomous cars. Accelerating at the merge point is the best way to avoiding a traffic jam on the road.
Not only does it prevent traffic jams, but it also keeps a safe distance between consecutive autonomous
cars. I am inspired to continue my research in the subject of autonomous cars. Even though in most cases
my algorithm works, there are still some cases that aren't covered. I will continue working on these
problems concerning autonomous cars and making the algorithm more intelligent and safer for real life
use. I see that my vision about the future of transportation , as shared by an article in National Geographic,
is slowly turning into a reality.


