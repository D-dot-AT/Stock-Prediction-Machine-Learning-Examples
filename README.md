# Stock Prediction Neural Network and Machine Learning Examples (Python)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A repository of ML and NN methods and libraries along with sample stock data for training and testing.
These are meant to be simple, easy to understand and highlight the essential components of each method.
Examples also show how to run the models on current data in order to get stock predictions.


## Performance
All models were trained and tested on the `example_data` from [D.AT](https://d.at/ref/github-python-examples) 
to rank which performed best.

| Method                  | p-value  | winner |
|-------------------------|----------|:------:|
| Gradient Boost          | 7.68e-15 |        |
| K-means Clustering      | 0.0047   |        |
| Logistic Regression     | 1.33e-06 |        |
| Random Forest           | 5.80e-20 |        |
| Support Vector Machines | 0.0102   |        |
| Keras FFNN              | 1.55e-17 |        |
| PyTorch FFNN            | 1.37e-19 |        |
| PyTorch Lightning FFNN  | 7.82e-22 |        |
| PyTorch Lightning LSTM  | 1.10e-23 |   🏆   |
| PyTorch Lightning RNN   | 1.30e-19 |        |
| Tensorflow FFNN         | 5.43e-19 |        |


Precision p-value is the method for comparing performance.  Why precision?
When investing, you care much more about the performance of the stocks you have purchased
than those that you decided not to buy. Put in real terms, the 10,000 no-buy decisions (negatives)
are not nearly as important as the 50 buy decisions (positives) if all 50 have profitable exits (true positives).
P-values are chosen as the measure because a low p-value rewards for both high precision and a large
amount of true positives, connoting a more robust model.

Methods with a stochastic component have been run 5 times; deterministic methods only once.  
The median precision p-value of the runs is selected as the performance.

### Best p-value:  PyTorch Lightning
Note that these are the *most basic* examples. Efforts were made for the neural nets to be apples-to-apples,
but there may be variations in the implementations. 
More sophisticated versions of these methods or hyperparameter tuning could produce better results.

Abbreviations:
* FFNN: Feedforward Neural Network
* RNN: Recurrent Neural Network
* LSTM: Long Short-Term Memory

## Getting Started
1. Clone this repository.
2. Navigate to the project directory.
3. Install the necessary libraries:

```bash
pip install -r requirements.txt
```

## About the Example Data
The data provided in `example_data` is an example of what is downloadable on the D.AT platform.

This dataset encapsulates 5 years of price data of the companies comprising the S&P 500, 
segmented into intervals of 30 trading days each. The data in each segment 
has been normalized using a method where values are divided by the most 
recent data point within the segment. Each row in the dataset represents a 
specific segment, providing a snapshot of the stock data available on a 
particular trading day. Rows are labeled to indicate when the 
stock had a minimum gain of 5% within the subsequent 10 trading days.

* `train.csv`: Of the 5 years, it contains the first 4 years of data.
* `test.csv`: Of the 5 years, it contains the final year of data.
* `latest.csv`: This file contains data from the most recent trading 
day for all stocks listed. While it lacks labels (since these pertain to future events), 
each row maintains the same feature vector structure as those in the `train` and `test` 
files. The rows commence with the stock ticker symbol, serving as a key tool to pinpoint 
stocks with promising prospects for good performance. 

### Getting new data
Recent data customizable with different trading strategies and feature engineering options can be [downloaded for free
at D.AT](https://d.at/ref/github-python-examples).


