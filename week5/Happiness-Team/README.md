# What are relevant factors that drive a nation's happiness? :earth_americas: :rainbow:
<p align="center">
  <img src="https://media.giphy.com/media/QuGdGFZ8QhKfRBWFzX/giphy.gif" />
</p>

## Table of contents
- [Background](https://github.com/Novi0106/Happiness-Team/blob/main/README.md#background)
- [Methodology](https://github.com/Novi0106/Happiness-Team/blob/main/README.md#background)
- [Data](https://github.com/Novi0106/Happiness-Team/blob/main/README.md#methodology)
- [Key findings](https://github.com/Novi0106/Happiness-Team/blob/main/README.md#key-findings)
- [Conclusion](https://github.com/Novi0106/Happiness-Team/blob/main/README.md#Conclusion)

## Background

It’s probably not an exaggeration to say that everyone among us has asked him- or herself once what it means to be happy. What is happiness? Am I happy? What can I do to achieve happiness? While these questions may sound pretty metaphysical, they are extremely suitable to the newfound focus on mental health that has surged over the past year.

During the COVID-pandemic many of us saw themselves confined to their own four walls with some countries imposing extensive lookdowns across multiple weeks. Even a home office that sounded oh so great at the beginning, resulted in blurry boundaries between private and professional life for many of us, actually increasing stress levels caused at work. 

So, when many individuals are struggling, how then can we improve happiness levels ideally for a wider population?

Picking up on this thought, this paper looks at the World Happiness Report to understand the most prevalent quantitative definition of happiness and which factors play into happiness on a national level. Our goal - thereby - is to understand what the relevant factors are to allow a better understanding of where potential actions could follow.

### The World Happiness Report

Starting with its first publication in 2012, the World Happiness Report has been aiming to provide a standardised quantified view on happiness across the world's nations. Its goal is to prompt professionals in health, government, and economy into action by providing them with a high-level estimate of the impact their areas of expertise have on national happiness.

We want to take the available data from world happiness reports to understand if there is a pattern between relevant COVID-19 metrics from the past year and the way world happiness has developed as per report.

Happiness in the report - and hence in this analysis - is measured according to the principle of the Cantril Ladder as below:

<p align="center">
  <img src= /Images/cantril.png /> <br>
  <i> Cantril Ladder classification </i>
</p>

In this setting responses are combination of the respondent's currently perceived life satisfaction as well as their outlook on how this will change in the mid-term (5 years).

## Methodology
We opted for an agile approach, where each day of the project was classified as a sprint to timebox our efforts.

Each sprint was dedicated to a specific topic area:

<ol type = "1">
         <li>Sprint 1: Framing the research question & gathering/cleaning the data.</li>
         <li>Sprint 2: EDA of the cleaned data set & refinement of the research question</li>
         <li>Sprint 3: In-depth analysis, visualisation, and linear regression modelling</li>
         <li>Sprint 4: Documentation, presentation practice, and fine-tuning</li>
</ol>

To keep ahead of the schedule, we decided to - in addition to the usual stand-up - include a morning stand-up at 9am to split the work. This helped us to get a better understanding of whether we might face any potential blockers that we would then need to bring up with our mentor. 

Our Kanban-Board, including all completed tickets can be found here: https://trello.com/b/kFslQgNn/the-happiness-team.

## Data
Variables: as we might already know, not one factor can explain the underlying happiness of a person or nation, that is why different variables are used to calculate the happiness scores. The authors of the World Happiness Report have found seven key factors that could likely explain the levels of happiness:

<ol type = "1">
         <li>The first variable is the GDP or gross domestic product, which is simply the sum of the values of all the goods produced in a country annually. To get to the GDP per capita, this sum is divided by the population.</li>
         <li>Social support is also a key variable, this is based on a yes or no answer to the following question: “If you were in trouble, do you have relatives or friends you can count on to help you whenever you need them, or not?” Based on the yes/no answer a dummy variable is created, where yes equals 1 and a 0 has been allocated to a no. Based on these scores, an average score is calculated, which represents the level of social support. </li>
         <li>The third variable is healthy life expectancy, which stands for the number of years a newborn is expected to live. This is based on 100 different factors, calculated and maintained by the World Health Organization. </li>
         <li>Freedom to make life choices, similar to the social support factor, is also answered using one question: “Are you satisfied or dissatisfied with your freedom to choose what you do with your life?” to which a dummy variable has been created as well. </li>
         <li>In addition to this, the generosity factor is also calculated based on the following question: “Have you donated money to a charity in the past month?”.</li>
         <li>Perceptions of corruption are averaged based on two questions: “Is corruption widespread throughout the government or not?” & “Is corruption widespread within businesses or not?”</li>
         <li>The last variable is the ladder score, which is explained above.</li>
</ol>

To gather the dataset, data from the World Happiness Report is used. Two different datasets have been cleaned and merged. One dataset contained data from 2005 - 2019, and the other dataset  from 2020-2021. These datasets have been merged with Python in Jupyter notebook. However, as mentioned before, the World Happiness Report was published from 2012 onward, which is why data from before 2012 is omitted.

Furthermore, to show insights in the different happiness levels in regions, a column with regions is added. To get an insight of the distributions of the variables, histograms are generated. Based on the histograms, it is clear that ladder score is almost normally distributed. All the other variables are skewed to the left (negatively skewed), except for perceptions of corruption (positively skewed).

To check for (perfect) multicollinearity, a heatmap has been generated in Python. In this heatmap it is clear that there are no cases of (perfect) multicollinearity, although there are high correlations between the variables. 


<p align="center">
  <img src= /Images/HEATMAP_NEW.png /> <br>
  <i> Correlation heatmap world happiness data </i>
</p>


In order to do sound calculations based on the variables, outlier calculations have been checked. This has been done by making a boxplot for each of the variables. From this it is clear that perception of corruption and generosity have somewhat higher outliers, but no high levels that needed to be addressed. 

## Key findings

There are multiple ways to look at the world happiness report and likely no single one will likely produce an exclusively best view. Metrics are taken in a bottom-up approach and are subjective in most cases, so we would likely need to contextualize results on a country level and drill down very deep to make solid and conclusive statement. Instead we choose to provide a broader high-level approach that can serve as food for thought.

### Happiness global view

The first thing that we can easily say, is that that regions of the world can be clustered into happier or less-happier according to their average ladder score. The Americas, Europe and Australia showing a higher ladder score on average, while the African continent and the Middle East seems to be mostly represented in the lower end of the spectrum. Asia by itself is fairly split, with countries like Japan & Korea scoring high, while e.g. China only ranks moderately.

<p align="center">
<div class='tableauPlaceholder' id='viz1625129949718' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WorldHappinessReport_16250702823590&#47;WorldMap&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='WorldHappinessReport_16250702823590&#47;WorldMap' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WorldHappinessReport_16250702823590&#47;WorldMap&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='de-DE' /></object></div>  

</p>

### Happiness regional view

Initially this could lead to the interpretations that the wealthy nations of this world have higher amount of happiness and indeed the correlation to GDP is something that we have to acknowledge on basis of the initial EDA. However, a first look at the average ladder score per region hints otherwise. Latin America & the Carribbean's rank better than other regions with a comparably stronger economy such as East Asia, implying that economic strength is not the single driving factor for a nation's happiness.

<p align="center">
<div class='tableauPlaceholder' id='viz1625128853999' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WorldHappinessReport_16250702823590&#47;LadderScorebyRegion&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='WorldHappinessReport_16250702823590&#47;LadderScorebyRegion' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WorldHappinessReport_16250702823590&#47;LadderScorebyRegion&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='de-DE' /></object></div>

</p>

### Winners and losers

Despite the positive note that the above visualisation carries, it is pretty much undeniable that there are regions and countries that are clearly worse off. For the most part these countries are from the African continent, with the war-torn Afghanistan being the only exception. Looking at the top 10 there is no real surprise, with northern European countries performing in accordance of their usual perception of being the world's happiest.

<p align="center">
<div class='tableauPlaceholder' id='viz1625129138172' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WorldHappinessReport_16250702823590&#47;TopandBottom10&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='WorldHappinessReport_16250702823590&#47;TopandBottom10' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WorldHappinessReport_16250702823590&#47;TopandBottom10&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='de-DE' /></object></div> 

</p>

To shed a positive light on the above ranking, we can however see that those nations performing bad in the ladder ranking also have the potential for the most movement in rankings. However, this holds for both directions. Nations that perform worse are less predictable in their movement. All of the top 10 and bottom 10 movers are those that we can find in the bottom half of the ranking. That is, considering the time scope 2012-2021

<p align="center">
<div class='tableauPlaceholder'; margin: 0 auto; id='viz1625062850887'; style='position: absolute'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;Countrymovementsinhappinessreport&#47;TopWorstmovers&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Countrymovementsinhappinessreport&#47;TopWorstmovers' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;Countrymovementsinhappinessreport&#47;TopWorstmovers&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='de-DE' /></object></div> 

</p>

On the same time frame those nations with a stable score are included more frequently in the Top 10. This does not mean they are exclusive populating this ranking (there are e.g. lower ranking nations), but countries performing better on the ladder score (moderate or above) tend to be able to hold the position as well. This can serve as implication on the nation's stability - economically and otherwise - to be relevant for a its citizens' long-term happiness

<p align="center">
<div class='tableauPlaceholder' id='viz1625063041225' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;Countrymovementsinhappinessreport&#47;Leastmovingcountries&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Countrymovementsinhappinessreport&#47;Leastmovingcountries' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;Countrymovementsinhappinessreport&#47;Leastmovingcountries&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='de-DE' /></object></div>   

</p>

<p align="center">
  
### Relevant factors driving happiness
  
From the relevant factors presented in the data section of the technical report, GDP, life expectancy and social support have the highest correlation with the ladder score. These are also the three variables that also show the largest movements and thereby have the highest impact on the ladder score overall. We cannot pinpoint which of the three is the leading indicator, but it is a valid assumption to say it's GDP. So, while it is not the only indicator it seems to still be the most driving factor. Higher GDP gives you higher financial freedom, gives you better access to medical and social support, gives you a better basis to be happy.
  
On a side note however a positive trend is the freedom to make choices, which is showing a constant growth. This looks overall positive but would need to be sliced and diced into more detail to understand if objective freedom of choice has been captured.
 
  
<div class='tableauPlaceholder' id='viz1625129194884' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WorldHappinessReport_16250702823590&#47;OtherVariablesOverTime&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='WorldHappinessReport_16250702823590&#47;OtherVariablesOverTime' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WorldHappinessReport_16250702823590&#47;OtherVariablesOverTime&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='de-DE' /></object></div>  

</p>

## Conclusion

While this is not truly an eye opener, this analysis somewhat supports the train of thought that money alone cannot buy you happiness, but the lack of it may buy you misery. GDP is the driving factor for the happiness ladder score and shows the most far-fetching correlation to all other relevant factors.

Hence, countries achieving a higher level of GDP, achieve more stability and can maintain a higher ladder score. Or at least that would be the implication of this high-level analysis. To become more concise on the topic, it would be necessary to look at the relevant variables on a nation-level to really provide the relevant context and understand the interplay of GDP, health, social support and happiness a bit more. That, however, will be the focus of a more detailed study by someone, sometime in the future.
