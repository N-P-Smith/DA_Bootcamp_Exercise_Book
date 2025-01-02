![Welcome](https://media.tenor.com/nFywkZ0DS5EAAAAM/glitter-confetti.gif))
# Day 18, 21.08.2024
<span style="color:grey">


 
 This is the protocol. A protocol to rule them all.
</span>



---
## <span style="color:black"> __Agenda__ </span>
 

* <span style="color:grey"> Approach to analyse data distrubtions
* <span style="color:grey"> Data Types 
* <span style="color:grey"> Types of Probability Distributions
* <span style="color:grey"> Binomial Distribution vs. Poisson Distribution
* <span style="color:grey"> Probability Mass Functions (PMF)
* <span style="color:grey"> Probability Density Functions (PDF)
* <span style="color:grey"> Cumulative Density Functions (CDF)
---
##  __Schedule__
<span style="color:grey">

|Time|Content|
|---|---|
|09:00 - 10:00|Introduction|
|10:00 - 11:30|Distribution Functions|
|11:30 - 12:30|Group Work: Different kinds of Distrubitons|
|12:30 - 13:30|Lunch Break| 
|13:30 - 15:00|Self Study|
|15:00 - 17:00|Exercises and Ending|
---
## Approach to analyse data distrubtions

 1. Understand the Data Type: Continuous or discrete.
 
 2. Identify the Analytical Question: Determine which distribution fits your question.
    
 3. Calculate Descriptive Statistics: Compute and visualize summary statistics.
    
 4. Interpret the Graph and Descriptive Statistics: Analyze the data’s distribution and patterns.


---
## <span style="color:black"> Data Types </span>
<span style="color:grey">
At first it is important to look at the given data and understand if we have discrete data or continous data  
  
- **Discrete Data**: Takes on distinct, separate values. Examples include the number of emails received in an hour or the number of customer complaints. Common distributions for discrete data include:
  - **Binomial Distribution**: Used when counting the number of successes in a fixed number of trials.
  - **Poisson Distribution**: Used for modeling the number of events in a fixed interval of time or space.

- **Continuous Data**: Takes on any value within a range. Examples include height, temperature, or time. Common distributions for continuous data include:
  - **Normal Distribution**: Used for data that is symmetrically distributed around the mean.
  - **Exponential Distribution**: Used for modeling the time between events.
  - **Log-Normal Distribution**: Used for data that is normally distributed when logged.

- **Why It Matters**: The type of data determines which probability distribution and statistical methods are appropriate for analysis.

</span>
---

# Types of Probability Distributions


<a href="https://ibb.co/nLPm3bs"><img src="https://i.ibb.co/z46x8rh/Screenshot-2024-10-21-at-16-35-52.png" alt="Screenshot-2024-10-21-at-16-35-52" border="0"></a>

---
# Normal Distribtution

Continous probability distribution that is symmetric at the mean
- **Mean = Median = Mode**
- e.g. (height, standardized tests' scores, weight, etc)
- area under the curve is 1 

![Test](https://www.scribbr.com/wp-content/uploads/2023/02/standard-normal-distribution-example.webp)
 
# Bernoulli Distribution

a single trial of an outcome's successes/failures
- has binary outcomes (Sucess or Failure, True or False, Head or Tails, etc.)
- e.g. winnig or lossing a game, single toss of a unbiased(fair) coin, washing single load of clothes to see shrinkage
- Probabilities will add up to 1

# Binomial Distribution

many bernoulli/single trials in succession
- **many different trials**
- e.g. Washing 10 loads of laundry and getting the probabilites of shrinkage for each load , probability of winning or loosing a season of games, tossing a coin 30 times for 20 trial)

![Image](https://i0.wp.com/statisticsbyjim.com/wp-content/uploads/2022/02/binomial_distribution_plot.png?fit=576%2C384&ssl=1)

# Uniform Distribution
Describes an event where every value has the **same probability** to appear

 - e.g. in a dice roll every number has the probability of 1/6 to appear
 - **Uniform CDF** = would mean that every value has the same probability.

# Poisson Distribution
Desrcribes the number of events occuring in a fixed **time interval** or region of opportunity

 - Discrete Distribution
 - The rate at which events occur is **constant** ( the **probabilty of an event** happening in a certain time interval should be **the same** for every other time interval of the same length)
 - the occurence of one event does not affect the occurence of a subsuquent event (event are independet)
 - Requires only one parameter, λ (λ = the expected number of events per time interval)
 - Bounded by 0 and infinity


# Binomial Distribution vs. Poisson Distribution

Both the binomial distribution and the Poisson distribution are probability distributions used in statistics, but they apply to different types of scenarios. Lets deepdive into this more in the following: 

## Binomial Distribution

1. **Definition**: The binomial distribution models the number of successes in a fixed number of independent Bernoulli trials (experiments with two possible outcomes: success or failure).

2. **Parameters**:
   - \( n \): Number of trials
   - \( p \): Probability of success on each trial

3. **Conditions**:
   - Fixed number of trials.
   - Each trial is independent.
   - The probability of success is constant for each trial.

4. **Probability Mass Function (PMF)**: The probability of getting exactly \( k \) successes in \( n \) trials is given by:

   <a href="https://imgbb.com/"><img src="https://i.ibb.co/qWLRdwP/probabilty-mass-function-1.png" alt="probabilty-mass-function-1" border="0"></a>

   where (n/k) is the binomial coefficient 

6. **Example**: Flipping a coin 10 times and counting the number of heads (successes) can be modeled by a binomial distribution.

## Poisson Distribution

1. **Definition**: The Poisson distribution models the number of events occurring in a fixed interval of time or space when these events happen with a known constant mean rate and independently of the time since the last event.

2. **Parameters**:
   - λ (lambda): The average rate (mean number of occurrences) in the given interval.

3. **Conditions**:
   - Events are independent.
   - The average rate of occurrence is constant.
   - Two events cannot occur at exactly the same instant.

4. **Probability Mass Function (PMF)**: The probability of observing \( k \) events in a fixed interval is given by:

  <a href="https://imgbb.com/"><img src="https://i.ibb.co/xGqJccQ/probabilty-mass-function-2.png" alt="probabilty-mass-function-2" border="0"></a>

   where \( e \) is the base of the natural logarithm.

5. **Example**: The number of phone calls received at a call center in any given hour can be modeled by a Poisson distribution.

 if you still have questions to Poisson Distribution you can look at [this](https://youtu.be/cPOChr_kuQs?si=NcrWi-b366r_NaBv) Video explaining it in 15 min with animation and examples.

## Key Differences

- **Nature of Trials**: The binomial distribution is used for a fixed number of trials with two outcomes, while the Poisson distribution is used for counting the number of events over a continuous interval.
- **Parameters**: The binomial distribution depends on the number of trials and the probability of success, whereas the Poisson distribution depends only on the average rate of occurrence.

**In summary, use the binomial distribution when you have a set number of trials and are looking at successes, and use the Poisson distribution when you're counting the number of events that happen in a fixed interval.**

---

# Probability Mass Functions (PMF)

The Probability Mass Function (PMF) describes the probability of each possible outcome for a discrete random variable. Discrete variables are those that take on specific, separate values—like rolling a die, flipping a coin, or choosing a certain number of cookies from a jar. 
The PMF assigns a probability to each possible outcome, giving a clear picture of how likely it is to occur. For example, if you roll a fair six-sided die, the PMF tells you that the probability of rolling any number from 1 to 6 is 1/6​, since each face has an equal chance of landing face up. 

The sum of all probabilities for the PMF must equal 1, because one of the outcomes will always happen. You can visualize the PMF as a bar chart where each bar represents the probability of an outcome; the height of the bar shows how likely the outcome is. 

For the fair die, all bars would be of equal height because each number from 1 to 6 is equally probable.

## Example: Rolling a Fair Die

![Image](https://i.ibb.co/8NHz0QY/mass.png)

- **Possible outcomes**: 1, 2, 3, 4, 5, 6.
- **PMF**: 
  - P(1) = 1/6
  - P(2) = 1/6
  - P(3) = 1/6
  - P(4) = 1/6
  - P(5) = 1/6
  - P(6) = 1/6



Since each outcome is equally likely, the probability for each is 1/6, and the total sum of probabilities is 1.

So, the PMF helps you understand the likelihood of specific outcomes in situations where there are distinct, separate possibilities, like rolling a die or randomly picking a specific number of cookies from a jar.

# Probability Density Functions (PDF)

A **probability density function (PDF)** describes how the probability of a continuous random variable is distributed across different values.

### Key points:
- **Continuous variables**: A PDF applies to things like height, weight, or time, where values can take any number in a range.
- **Graph**: The PDF is a curve. The probability of the variable falling within a specific range (say between *a* and *b*) is represented by the area under the curve between those two points.
- **Total area = 1**: The entire area under the PDF curve equals 1, since the total probability of all possible outcomes must be 100%.
  
### Example:
For a normal distribution (like a bell curve), the PDF shows how likely different values are, such as how likely a person's height is within a certain range.

The PDF itself doesn’t give a probability for a specific point (because for continuous variables, the probability of a single point is 0), but it helps calculate probabilities over ranges of values.

![text](https://i0.wp.com/statisticsbyjim.com/wp-content/uploads/2018/04/IQ_score_distribution.png?fit=576%2C384&ssl=1)

# Cumulative Distribution Function (CDF)

A cumulative distribution function (CDF) describes the probabilities of a random variable having values less than or equal to x. It is a cumulative function because it sums the total likelihood up to that point. Its output always ranges between 0 and 1.

CDFs have the following definition:

CDF(x) = P(X ≤ x)

Where X is the random variable, and x is a specific value. The CDF gives us the probability that the random variable X is less than or equal to x. These functions are non-decreasing. As x increases, the likelihood can either increase or stay constant, but it can’t decrease.

Both probability density functions (PDFs) and cumulative distribution functions provide likelihoods for random variables. However, **PDFs calculate probability densities for x, while CDFs give the chances for ≤ x**. 

![Bild](https://i0.wp.com/statisticsbyjim.com/wp-content/uploads/2023/02/CDF_normal_male.png?w=576&ssl=1)

--
## Example

Therefore a continuous uniform distribution can be compared to choosing a random point along a straight road that stretches from 0 to 10 kilometers. Every point on that road has an equal chance of being selected.

The Cumulative Distribution Function (CDF) answers the question: "What’s the probability of picking a point less than or equal to a certain value?" For example, if you want to know the chance of selecting a point less than or equal to 5 km, you consider half the range (0 to 5 km), resulting in a 50% probability.

## Key points:
- **Cumulative probability**: The CDF shows the cumulative probability up to a certain point. It tells you how much probability has been "accumulated" from the left up to that value.
- **Graph**: The CDF graph is always increasing (never decreases) and starts at 0 (for the lowest possible value) and ends at 1 (for the highest possible value).

## Example:
For a CDF of heights, if the CDF at 170 cm is 0.6, it means 60% of people are shorter than or equal to 170 cm.

## Another example for CDF: Random Arrival Time

Imagine you’re waiting for a friend who will arrive at a random time between 0 and 60 minutes. This scenario represents a continuous uniform distribution.

### CDF Values:

- **At 0 minutes**: Probability = 0  
  `F(0) = 0`

- **At 30 minutes**: Probability = 50%  
  `F(30) = 0.5`

- **At 45 minutes**: Probability = 75%  
  `F(45) = 0.75`

- **At 60 minutes**: Probability = 100%  
  `F(60) = 1`

## Difference from PDF:
- **PDF** shows the likelihood of the variable taking a specific value (or within a small range).
- **CDF** shows the total probability of the variable being less than or equal to a certain value.

## Summary:
- **PMF** (Probability Mass Function): Probability of a specific discrete outcome in a discrete random variable.
- **PDF**(Probability Density Function): Probability of a specific range or interval in a continuous random variable (though for continuous variables, the probability of a specific value is 0, so we look at the probability over a range).
- **CDF** (Cumulative Distribution Function): Cumulative probability up to and including a certain value, which applies to both discrete and continuous random variables. It gives the probability that the random variable is less than or equal to a certain value.
---





![Protocol](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXcyZ2psY2pwNmhjbDh1bDVyMnNvNDEwOWM2NDIzaTVydjZxYWJkcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9dg/breLBEo4GjLNyRLtZt/giphy.gif)
---
![END](https://media.makeameme.org/created/the-end-thank-0e068c883d.jpg)

----
# Links

[Link to Poisson-Lecture](https://youtu.be/cPOChr_kuQs?si=TjEf9M-fUtR9ek1h)

[Link to Distribution Functions Lecture](https://youtu.be/yfXnhnpD7jE?si=qkq7ChAX6i6C2eEC)
