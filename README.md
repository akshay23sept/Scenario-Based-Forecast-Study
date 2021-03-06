# Scenario-Based-Forecast-Study

### A granular study to estimate the demand for Urban Air Mobility (UAM) vehicles during 2035 to 2050 for set of 542 global cities. The project has received funding from Clean Sky 2 (CS2) Joint Undertaking (JU) under grant agreement No.864521. The JU receives support from the European Union’s Horizon 2020 research and innovation programme and the [Clean Sky 2 JU](https://umi2958.gatech.edu/news/oasys-success) members other than the Union.

## Introduction
<p><code>Scenario-Based-Forecast-Study</code> repository contains a group of pythonic subroutines (codes) which are developed to foresact the demand for UAM during 2035 to 2050 timeframe for a set of 542 global cities. Each subroutine performs a special task to execute the scenario outsome. The picture shown below shows the working of each subroutines.</p>

## Subroutines 
<p>1.<code>Assumptions</code>: This subroutine declares all the assumptions made in the current research to forecast the UAM demand estimates for low and high demand scenarios between 2035 and 2050. To have a look at our assumptions please refer to our published <a href="https://scholar.google.com/citations?user=5pY2xYQAAAAJ&hl=en&authuser=1">papers</a> in AIAA Aviation 2020 and AIAA Scitech 2021.</p>
<p>2.<code>Willingness to Pay</code>: The willingness to pay function is estimated as the sum of cost of traditional modes of transport and the dollar value a traveller would place on time saved through UAM trips.</p>
<p>3.<code>Design Space</code>: This function discretises the income and trip distance ranges using a percent point function (PPF) and also iterates over several kinds of trip purposes.</p>
<p>4.<code>Get PKM</code>: Get PKM (passenger kilometer) function estimates the PKM for a specific trip. The function inputs the log normal distribution of household income and trip distance. Also, the mode and purpose information are taken by input sheet which contains the attributes of the cities of interest.</p>
<p>5.<code>UAM PKM</code>: The UAM PKM function generates the income and distance data points for the algorithm to evaluate. Each iteration represents a different trip, which is described by trip purpose, mode, income, and distance. The calculation for PKM is described in Equation 6 in our <a href="https://arc.aiaa.org/doi/abs/10.2514/6.2021-1516">paper</a>. At this point, a decision is evaluated. If <code>WTP ≥ UAM trip cost,</code> then this would be a viable UAM trip option, and the PKM associated with this trip should be computed.</p>
<p>6.<code>Main</code>: This module helps all the other functions by facilitating the input parameters. After successful execution of demand estimates, the module outputs the results.</p>

<p align="center">
<code>Note</code>: The codes are parallelized and uses multiple CPU's which reduces the computation and elapsed time.
</p>

<p align="center">
  <a target="_blank" rel="noopener noreferrer" href="https://github.com/akshay23sept/Scenario-Based-Forecast-Study/blob/main/images_scripts/uam_algorithm.png"><img src="https://github.com/akshay23sept/Scenario-Based-Forecast-Study/blob/main/images_scripts/uam_algorithm.png" alt="Screenshot" width="750" height="450" style="max-width:100%;"></a>
</p>

## Set-Up
To run the subroutines in your local machine, you will need following python libraries (if you don't have the libraries installed in your machine, installed by typing...) You can use any IDE (Spyder, Qt Console, PyCharm or your terminal) to run the scripts.
<div class="highlight highlight-source-shell"><pre>$ pip install numpy</pre></div>
<div class="highlight highlight-source-shell"><pre>$ pip install pandas</pre></div>
<div class="highlight highlight-source-shell"><pre>$ pip install statistics</pre></div>
<div class="highlight highlight-source-shell"><pre>$ pip install scipy</pre></div>
<div class="highlight highlight-source-shell"><pre>$ pip install math</pre></div>
<div class="highlight highlight-source-shell"><pre>$ pip install scikit</pre></div>
<div class="highlight highlight-source-shell"><pre>$ pip install glob</pre></div>
<div class="highlight highlight-source-shell"><pre>$ pip install csv</pre></div>
<div class="highlight highlight-source-shell"><pre>$ pip install fuzzywuzzy</pre></div>
<div class="highlight highlight-source-shell"><pre>$ pip install numba</pre></div>
<div class="highlight highlight-source-shell"><pre>$ pip install matplotlib</pre></div>



## Issues:
<p> Feel free to raise an issue at <a href="https://github.com/akshay23sept/Scenario-Based-Forecast-Study">https://github.com/akshay23sept/Scenario-Based-Forecast-Study</a>.
  
  





