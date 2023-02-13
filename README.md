# Summary of the app
> This app seeks to analyse perfomance of currecny pairs in the FOREX markets. The app will plot charts of selected currency pair and compare the trends/pattern. The data is also available for downloading from the app. Various computations like percentage change, year to date(YTD), year-on-year(YoY), correlation among others are also captured by the app.

## Problem Statement.
> More often than not, indivinduals find themselves seeking to invest in the financial markets. Many go ahead and invest without doing any due diligence whatsoever no technical analysis of fundamental analysis. Very frusted anfter running into significant losses, they end up labelling the financial markets scam or even comparing the markets to gambling.
> This happens because of blind investing or trading without any background analysis. Any investment or trading idea should be backed by a background framework and some little research no matter how little.

## What Does the app Solve?
> Not everyone is a financial expert or has access to vital financial infomation/data which can be used when investing n the financial markets. There are many platforms which offer such data analysis however some of them are exmtremely costly which leaves them as a preserve for the rich and puts away the average retai trader from access of such infomation which can be used to influence investing decisions.
> The app can be used to analyse perfomace and other parameters then use conclusions and results from the app to make investing decisions.

## How does the app work?
This is how the front page looks like incase you access the app using a smartphone you will need to click the > at the top left so as to display the sidebar. The sidebar has default values but you can select values of your choice.
>
![image](https://user-images.githubusercontent.com/121600705/218400615-6959e84f-5f2d-425f-a4dd-593fdd8a24f5.png)

> Complete data is the entire data of the currency pairs for the entire period. Filtered data will show filtered values depending on the parameters you select on the side bar. By default, we have USD/KES and USD/JPY data from 2008 to current date below is the chart for the same.

### Filtering data.
> Filter the data to your preference from the sidebar and the app will plot your filtered data. For currencies there's is a drop down list to select pair/s you can close(x) the default pair then select others. For years, close unwanted ones to remain with interested year/s.
>
![image](https://user-images.githubusercontent.com/121600705/218402010-2f65c34c-65d8-4ab2-a7e6-9739c157866b.png)
![image](https://user-images.githubusercontent.com/121600705/218402036-63a21e6e-80b4-442f-b21d-9fee076ec2cb.png)

> The app will plot a chart on your filtered data which you can download however I recommend filtering pairs with similar range. The data set has values with min values of below 1 and others over 500 this makes it hard to plot a suitable scale for the variation. An attempt to plot values with such variation will result to a chart with straight lines which doesn't look so nice. Even tried to used logs but still the scale was off. If you want to compare pairs with huge variation plot separate charts, download & compare them side by side

### Percentage Change Computation.
> The next section computes for percentage change of your filtered data. Daily % will compute %change for each day day while period will compute %change with reference to the first day of the period lets say you have 2020 to 2023 all values will be computed with reference to the first day of 2020. 
> For instance lets say we want year to date %change of the USD/KES, data shows at the first of 2023 price was 122.5 and today(10-02-2023) price is 125.18 giving a 2.1878% YTD change. This means if you had invested in the pair at the start of the year your investment would be 2.1878% up now. 

### Option bar
> You can calculate for the %change yourself and see if you will get same results. 
> There's an option bar as the last item on the sidebar you will have to select an option for it to be displayed I selected Correlation Heatmap and it was displayed it shows correlation between USD/GHS and USD/INR is 0.23. you can compare the correlations even plot for values which show high/low correlation and see if it's true.

> ![image](https://user-images.githubusercontent.com/121600705/218404863-8e10d763-6e37-4ea1-b302-15d52fb81867.png)
> 

