# Supervised Machine Learning: Regression and Classification


## Learning Objectives
- Define machine learning
- Define supervised learning
- Define unsupervised learning
- Write and run Python code in Jupyter Notebooks
- Define a regression model
- Implement and visualize a cost function
- Implement gradient descent
- Optimize a regression model using gradient descent

## Overview of Machine Learning

### Welcome to machine learning!

#### What is Machine Learning?

- It's the science of getting computers to learn without being explicitly programmed.

Examples

- Google Search, Bing, Baidu
- Picture labeling on Instagram, Snapchat
- Movie recommendation
- Voice to text to write a text message
- Siri, play a song!
- Ok Google, show me Indian restaurants near me
- Spam detector in emails
- Wind turbine power generation optimization
- Diagnosis maker in hospitals
- Defect detector in assembly lines

#### Why is Machine Learning so widely used today?

We wanted to build intelligent machines and it turns out that there are a few basic things that we could program a machine to do, such as how to find the shortest path from A to B. But for the most part we just did not know how to write an explicit program to do many of the interesting things, such as:

- Perform a web search
- Recognize human speech
- Diagnose diseases from X-rays
- Building a self-driving car

#### What is Artificial General Intelligence (AGI)?

Machines as intelligent as you and me

### Applications of machine learning

"I find it hard to think of any industry that machine learning is unlikely to touch in a significant way now or in the near future"

Sectors

- Retail
- Travel
- Transportation
- Automotive
- Materials
- Manufacturing

Because of the massive untapped opportunities across so many different sectors, today there is a vast unfulfilled demand for this skill set.

## Supervised vs. Unsupervised Machine Learning

### What is machine learning?

- "Field of study tht gives computers the ability to learn without being explicitly programmed." Arthur Samuel (1959)

If someone were to gimme a steelyard hammer, does that mean I now have the skills to build a tree-story house?

### Supervised learning part 1

99% of the economic value created by machine learning today is through supervised learning.

Algorithms that learn x to y mappings. You give examples that includes the "right answer" (the correct label Y) for the input X. Then, eventually, the algorithm learns to take just the input X without the label and gives a reasonably accurate prediction or guess of the output.
<table/>
<thead>
<tr>
<td>Input (X)</td>
<td></td>
<td>Input (Y)</td>
<td>Application</td>
</tr>
</thead>
<tbody>
<tr>
<td>email</td>
<td>➡</td>
<td>spam? (0/1)</td>
<td>spam filtering</td>
</tr>
<tr>
<td>audio</td>
<td>➡</td>
<td>text transcripts</td>
<td>speech recognition</td>
</tr>
<tr>
<td>English</td>
<td>➡</td>
<td>Spanish</td>
<td>machine translation</td>
</tr>
<tr>
<td>ad, user info</td>
<td>➡</td>
<td>click? (0/1)</td>
<td>online advertising</td>
</tr>
<tr>
<td>image, radar info</td>
<td>➡</td>
<td>position of other cars</td>
<td>self driving car</td>
</tr>
<tr>
<td>image of phone</td>
<td>➡</td>
<td>defect? (0/1)</td>
<td>visual inspection</td>
</tr>
</tbody>
</table> 

A regression problem: The algorithm has to predict numbers from infinitely many possible output numbers. Like, for example, the price of a house.

### Supervised learning part 2

A Classification problem: Predicts a small finite set of possible outputs categories

Breast cancer

0: Benign

1: Malignant


<table/>
<thead>
<tr>
<td>Tumor sizes</td>
<td>Diagnosis</td>
</tr>
</thead>
<tbody>
<tr>
<td>2</td>
<td>0</td>
</tr>
<tr>
<td>5</td>
<td>1</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td>7</td>
<td>1</td>
</tr>
</tbody>
</table> 


### Unsupervised learning part 1

Takes data without labels and tries to automatically group them into clusters.

### Unsupervised learning part 2

Data only comes with inputs X, but not output labels Y. Algorithm has to find *structure* in the data

#### Clustering

- Group similar data points together

#### Anomaly detection

- Find unusual data points

#### Dimensionality reduction

- Compress data using fewer numbers

### Jupyter Notebooks
x
### Lab: Python and Jupyter Notebooks
x
### Practice Quiz: Supervised vs unsupervised learning
x
## Regression Model

### Linear regression model part 1
### Linear regression model part 2
### Optional lab: Model representation
### Cost function formula
Model: fw,b(x) = wx+b

w,b parameters, coefficients, weights

Depending on the values you've chosen for w and b you get a different function f(x), which generates a different line on the graph.

The cost function takes the prediction y hat and compares it to the target y by taking y hat minus y. This difference is called the error, we're measuring how far off to prediction is from the target. Next, let's computes the square of this error. Also, we're going to want to compute this term for different training examples i in the training set. When measuring the error, for example i, we'll compute this squared error term. Finally, we want to measure the error across the entire training set. In particular, let's sum up the squared errors like this. We'll sum from i equals 1, 2, 3 all the way up to m and remember that m is the number of training examples.

When the cost is relatively small, closer to zero, it means the model fits the data better compared to other choices for w and b.

### Cost function intuition
### Visualizing the cost function
### Visualization examples
### Optional lab: Cost function

### Practice Quiz: Regression Model

## Train the model with gradient descent

### Gradient descent
### Implementing gradient descent
### Gradient descent intuition
### Learning rate
### Gradient descent for linear regression
### Running gradient descent
### Optional lab: Gradient descent

### Practice quiz: Train the model with gradient descent
