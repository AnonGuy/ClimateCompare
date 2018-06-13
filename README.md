# ClimateCompare
Analyse and compare climate data for towns in the United Kingdom.

## Data Types
I will be analysing the following data categories:
* Daily mean temperature (**°C**)
* Daily mean windspeed (**km**)

## Sampling Methods

To carry out a simple random sample of size 30 for Cambourne's **daily mean temperature**, I would use the following method:
* Number each day of the month from 1 to the length of the month.
* Use a Random Number Generator to generate a random number from 1 to the length of the month.
* Repeat this process 10 times for each month, skipping any repeats, and record the results.

One method of sampling is to take the data for the first 10 days for each month for Leuchars.
* This sampling method is known as **systematic sampling.**
* One weakness of this sampling method is that it introduces **bias** toward the start of each month,
therefore each day of the month will not have an equal chance to be recorded.

For my investigation, I will be carrying out a systematic sample of size 12 for Cambourne, Heathrow and Leuchars. <br />
I will use the following method to carry out the sample:
* Start at `01/05/2015` for Cambourne, and record days at 16-day intervals until `26/10/2015`.
* Repeat this process for both Heathrow and Leuchars.

I have sampled this data from the provided large data set. <br />
The sampled data for [Cambourne](https://raw.githubusercontent.com/AnonGuy/ClimateCompare/master/data/cambourne.csv),
[Heathrow](https://raw.githubusercontent.com/AnonGuy/ClimateCompare/master/data/heathrow.csv) and
[Leuchars](https://raw.githubusercontent.com/AnonGuy/ClimateCompare/master/data/leuchars.csv) are
provided in this repository.

## Data Analysis
I have written several Python scripts, included in this repository, to calculate the mean, median and standard deviation of all samples that I have collected. The results can be seen below:

|                                   | Cambourne | Heathrow | Leuchars |
|:---------------------------------:|:---------:|:--------:|:--------:|
|          Mean temperature         |   13.75   |   15.68  |   11.34  |
|         Median temperature        |    13.9   |   15.55  |   11.15  |
| Standard deviation of temperature |    2.37   |   3.85   |    3.2   |
|         IQR of temperature        |    2.25   |   6.85   |   4.15   |

|                                  | Cambourne | Heathrow | Leuchars |
|:--------------------------------:|:---------:|:--------:|:--------:|
|          Mean wind speed         |   10.75   |   8.67   |   10.83  |
|         Median wind speed        |    9.5    |    8.5   |   11.0   |
| Standard deviation of wind speed |    3.39   |   3.54   |   5.05   |
|         IQR of wind speed        |    3.75   |    3.0   |   5.75   |

Using this information, I have discovered the following outliers:
* Cambourne's wind speed on `02/06/2015`, **18kn**, is 7.25kn higher than the mean. (2σ = 6.78kn)
* Heathrow's wind speed on `02/06/2015`, **18kn**, is 9.33kn higher than the mean. (2σ = 7.08kn)
* Leuchars' wind speed on `02/06/2015`, **22kn**, is 11.17kn higher than the mean. (2σ = 10.1kn)
* Leuchars' temperature on `01/05/2015`, **3.8°C**, is 7.54° lower than the mean. (2σ = 6.4°)

As all of my sampled locations have an anomalous result on the 2nd of June, **I will remove this date** from my set of results.
<br />I will also exclude the temperature outlier for Leuchars from the box plot's lower bound.

## Representation
### Box Plots
[Source code](https://raw.githubusercontent.com/AnonGuy/ClimateCompare/master/plot_scripts/box_plot.py)


![temperature](https://raw.githubusercontent.com/AnonGuy/ClimateCompare/master/images/box_plot/temperature.png)
![windspeed](https://raw.githubusercontent.com/AnonGuy/ClimateCompare/master/images/box_plot/windspeed.png)

### Histograms

![temperature_cambourne](https://raw.githubusercontent.com/AnonGuy/ClimateCompare/master/images/histogram/cambourne/temperature.png)
![windspeed_cambourne](https://raw.githubusercontent.com/AnonGuy/ClimateCompare/master/images/histogram/cambourne/windspeed.png)

![temperature_heathrow](https://raw.githubusercontent.com/AnonGuy/ClimateCompare/master/images/histogram/heathrow/windspeed.png)
![windspeed_heathrow](https://raw.githubusercontent.com/AnonGuy/ClimateCompare/master/images/histogram/heathrow/windspeed.png)

![temperature_leuchars](https://raw.githubusercontent.com/AnonGuy/ClimateCompare/master/images/histogram/leuchars/temperature.png)
![windspeed_leuchars](https://raw.githubusercontent.com/AnonGuy/ClimateCompare/master/images/histogram/leuchars/windspeed.png)
