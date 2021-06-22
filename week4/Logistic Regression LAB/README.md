# Logistic Regression LAB - Bank Customer Analysis 

## Overall tasks: 
- Identify the good clients to whom we can offer other services
- Identify the bad clients that have to watch carefully to minimize the losses
<br></br>
## Data
### 📁
- Using the Checz Bank DataSet with SQL querie we generated a CSV file containing all the relevant information we will need to feed in our ML model.
- Creating a DataFrame from the CSV file using Pandas
- Exploratory data analysis, getting to know our DataFrame
- Plotting histograms, boxplots and correlation matrix in order to visualy better understand the data
<br></br>
## Prepocessing 
### 🛠️
- Droping irrelevant columns
- Splitting the data into numerical and categorical values
- Normalizing numerical data with Sklearn Normalizer
- Splitting off the dependent variable
- Train / Test split
<br></br>
## Apply and train the model
### 🦾
- Classification using 'liblinear' solwer as a best fit for this size of a DataFrame
- Train the model 
- Test model's accuracy
<br></br>
## Evaluating
### 🔎
- Visualising accuracy with ROC curve
- Visualising accuracy with Confusion Matrix
