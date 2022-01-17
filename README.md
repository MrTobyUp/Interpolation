# Interpolation
Interpolation and trigonometric interpolation of functions, in combination with discrete fourier transform.

##Interpolation:
The starting point is a function looking like:
[<img src="https://picr.eu/images/2022/01/17/kNekp.png">](https://picr.eu/images/2022/01/17/kNekp.png)

Connecting these lines, we get:
[<img src="https://picr.eu/images/2022/01/17/kNfI3.png">](https://picr.eu/images/2022/01/17/kNfI3.png)

It's now possible to insert an x-value, to calculate the corresponding y-value.


##Trigonometric-Interpolation:
Given a function, the trigonometric-interpolation is used to find the sine functions, from which the function consits.
[<img src="https://picr.eu/images/2022/01/17/kNpvg.png">](https://picr.eu/images/2022/01/17/kNpvg.png)
For this task the discrete-fourier-transfer is used and as result you get the sine-functions:
frequency: 1.0Hz | amplitude: 3.000697138422399
= 3.0 * sin(2 * pi * 1.0 * t)

frequency: 4.0Hz | amplitude: 1.0000790594332034
= 1.0 * sin(2 * pi * 4.0 * t)

frequency: 7.0Hz | amplitude: 0.5000472400993039
= 0.5 * sin(2 * pi * 7.0 * t)
