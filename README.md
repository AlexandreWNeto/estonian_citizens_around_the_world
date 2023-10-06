# estonian_citizens_around_the_world
Click here to access the Jupyter notebook of this study: [https://awneto-basic.github.io/estonian_citizens_around_the_world/](https://alexandrewneto.github.io/estonian_citizens_around_the_world/)

![image](https://github.com/AlexandreWNeto/estonian_citizens_around_the_world/assets/29670261/a3c449ec-c740-40cd-962b-5603fc3a8e05)


<!-- wp:paragraph -->
This dataset lists the number of Estonian citizens living outside of Estonia, grouped by country, as of 21st February 2022.
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
I asked the Ministry of Interior of Estonia for the relevant data and they sent me a spreadsheet containing a list of contries and territories around the world and the number of Estonian citizens living in each of them. To be clear, the data was anonymised: only the number of Estonians was contained in the database, not their identities.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It is important to note that this data does not necessarily refer to the distribution of people who identify as <strong>ethnic</strong> <strong>estonians</strong> across the world, but rather to the number of estonian <strong>citizens</strong> (i.e. people bearing an Estonian passport) living outside of Estonia.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>With the dataset in hand, I decided to undertake an <strong>Exploratory Data Analysis</strong> exercise to see if I could find patterns and insights on the data. </p>
<!-- /wp:paragraph -->


<!-- wp:paragraph -->
<p>I started my exercise by adding up features I considered relevant. I enriched the dataset with the following features:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li><strong>ISO alpha-3 code</strong> - a three letter string that identifies the country and is used as an input for some geographic plotting tools.</li><li><strong>Continent </strong>- for grouping the data into regions</li><li><strong>Sub-regions</strong> - as defined by the United Nations' <em>Standard Country or Area Codes for Statistical Use</em>. For grouping the data into regions.</li><li><strong>Capital city and its coordinates</strong> - to set the locations for the datapoints related to each country on the geographic scatter plot.</li><li><strong>Distance between the country's capital city and Tallinn</strong> - to assess if there was any correlation between how far the country is to Estonia and how many estonians have chosen to live in the country</li><li><strong>Population (2020)</strong> - as estimated and registered on the United Nations' "<em>2019 Revision</em><strong>&nbsp;</strong><em>of</em><strong>&nbsp;</strong><em>World Population Prospects</em>". There were missing entries for some countries that required inserting data from other datasets. Note that these estimates were made before the COVID-19 pandemic, which means that there was a significant change in the population data from when this estimate was made (2019) and when the target data (i.e., number of estonian citizens) living in each country was generated. Thus, any correlation between this feature and the target feature may not reflect the current reality.</li><li><strong>GDP PPP per capita (2022) </strong>- extracted from IMF's "World Economic Outlook Database 2022" published on October 2021. The majority of the GDP PPP figures on the dataset are estimates from years prior.</li><li><strong>Former member of the USSR? </strong>- manually populated. I was curious to see if I could get any insights from assessing the number of estonian citizens living in former members of the Soviet Union (apart from Estonia).</li><li><strong>Sovereignty</strong> - manually populated. This categorical feature indicates if the target is a sovereign state. </li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>There were at least three relevant features that were not added to the dataset:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Percentage of Russian speakers in each country: I found it difficult to find consistent datasets with the percentage of russian speakers worldwide. </li><li>Number of English speakers in each country: absent from this dataset for the same reason as above.</li><li>Number of speakers of Finno-Ugric Languages: among the finno-ugric language group, Hungarian, Finnish and Estonian, national languages of Hungary, Finland and Estonia, respectively, are on the top three in terms of number of speakers.  I've chosen not to add this feature because of difficulties of finding consistent data for the number of speakers of the other Finno-Ugric languages.</li></ul>
<!-- /wp:list -->
