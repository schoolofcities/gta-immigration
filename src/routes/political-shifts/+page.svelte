<script>
    import TopSofC from '$lib/TopSofC.svelte';
    import StaticCorrelationDisplay from '$lib/StaticCorrelationDisplay.svelte';
    import CensusVoteMaps from '$lib/CensusVoteMaps.svelte';
    import CorrelationDisplay from '$lib/CorrelationDisplay.svelte';
    import CorrelationTimeline from '$lib/CorrelationTimeline.svelte';
    import VoteShareCompare from '$lib/VoteShareCompare.svelte';
    import '../../assets/global-styles.css';
</script>

<svelte:head>
	<meta
		name="viewport"
		content="width=device-width, initial-scale=1, minimum-scale=1"
	/>

	<title>Changes in immigrant voting patterns in the Greater Toronto Area | School of Cities</title>

	<meta name="description" content="">
	<meta name="author" content="Aniket Kali, Serene Tan, & Jeff Allen">
    
	<meta property="og:title" content="Changes in immigrant voting patterns in the Greater Toronto Area" />
	<meta property="og:description" content="" />
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://schoolofcities.github.io/gta-immigration/political-shifts" />
	<meta property="og:image" content="https://schoolofcities.github.io/gta-immigration/web-card-political-shifts.png" />
	<meta property="og:locale" content="en_CA">

	<!-- <meta name="twitter:card" content="summary_large_image" /> -->
	<meta name="twitter:site" content="https://schoolofcities.github.io/gta-immigration/political-shifts" />
	<meta name="twitter:creator" content="@UofTCities" />
	<meta name="twitter:title" content="Changes in immigrant voting patterns in the Greater Toronto Area" />
	<meta name="twitter:description" content="" />
	<meta name="twitter:image" content="https://schoolofcities.github.io/gta-immigration/web-card-political-shifts.png" /> 
    
</svelte:head>

<main>

    <TopSofC/>

    <div class="title">

        <div style="display: flex; width: 100%;">
            <div style="flex: 1; height: 10px; background-color: #EBA00F;"></div>
            <div style="flex: 1; height: 10px; background-color: #DC4633; margin-top: -5px;"></div>
            <div style="flex: 1; height: 10px; background-color: #F1C500; margin-top: 0px;"></div>
            <div style="flex: 1; height: 10px; background-color: #007FA3; margin-top: -5px;"></div>
            <div style="flex: 1; height: 10px; background-color: #00A189;"></div> 
          </div>
          
        <h1>Changes in immigrant voting patterns in the Greater Toronto Area</h1>
        <p>
            <a href='https://www.linkedin.com/in/aniket-k-8a8b9921b/' target='_blank'>Aniket Kali</a>,
            <a href='https://www.linkedin.com/in/serene-tan-530239113' target='_blank'>Serene Tan</a>,
            <a href='https://jamaps.github.io/' target='_blank'>Jeff Allen</a>
            |
            April 2025
        </p>
    </div>

    <div class="text">
        <p >
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </div>

    <StaticCorrelationDisplay />

    <div class="text">
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <h2>How do different ridings compare geographically?</h2>
        <p>
            At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. 
        </p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>

    <!-- Dual panel of constituency maps: vote share & immigrant percent -->
    <CensusVoteMaps />

    <div class="text">
        
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>

    <div class="text">
        <h2>Does party vote share correspond to where immigrants live?</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>

    <!-- View trend line of correlation (choose party) -->
    <div class="container">
        <CorrelationTimeline />
    </div>

    <div class="text">
        <p>tLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>

    <!-- View graph of all data points and correlation year (choose party+year) -->
    <div class="container">
        <CorrelationDisplay />
    </div>

    <div class="text">
        <br>
        <h2>Do parties over-perform in the most immigrant ridings?</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>

    <!-- View trend line mean vote share (choose party) for high immigrant ridings -->
    <div class="container">
        <VoteShareCompare />
    </div>

    <div class="text">
        
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Stop.</p>
    
        <br>
        <br>

        <div class="footnotes">
            <h3>Data & Methods</h3>
            
            <p>We obtained federal election results from <a href='https://github.com/Lucas-Czarnecki/Canadian-Federal-Elections/tree/main' target='_blank'>Lucas Czarnecki's database</a>, sourced from Canada's Library of Parliament (LOP), and Ontario election results from <a href='https://www.elections.on.ca/en/resource-centre/elections-results.html' target='_blank'>Elections Ontario</a>.</p>

            <p>For consistency, we focused on the three major parties in Anglo-Canada—the <a href='https://en.wikipedia.org/wiki/Liberal_Party_of_Canada' target='_blank'>Liberals</a>, <a href='https://en.wikipedia.org/wiki/New_Democratic_Party' target='_blank'>New Democrats</a>, and Conservatives—while grouping all other parties under "Other". The label "Conservatives" refers to the dominant center-right/right-wing party in each context: the <a href='https://en.wikipedia.org/wiki/Progressive_Conservative_Party_of_Ontario' target='_blank'>Progressive Conservatives in Ontario</a>, the <a href='https://en.wikipedia.org/wiki/Progressive_Conservative_Party_of_Canada' target='_blank'>federal Progressive Conservatives</a> (until 2004), and the <a href='https://en.wikipedia.org/wiki/Conservative_Party_of_Canada' target='_blank'>Conservative Party of Canada</a> (from 2004 onward). The only exception was including the <a href='https://en.wikipedia.org/wiki/Reform_Party_of_Canada' target='_blank'>Reform</a>/<a href='https://en.wikipedia.org/wiki/Canadian_Alliance' target='_blank'>Alliance</a> parties in the three federal elections they contested (1993, 1997, and 2000).</p>

            <p>Census data was drawn from <a href='https://observatory.uwo.ca/unicen/index.html' target='_blank'>UNI-CEN</a>, where we used census tract-level statistics starting in 1961. Immigration data is available from 1961 onward, household income from 1971 onward, and visible minority demographics from 2001 onward.</p>

            <p>Because historical electoral ridings lack direct census data, we estimated statistics using areal interpolation. We calculated relevant statistics by aggregating all census tracts fully or partially within each riding (using these <a href='https://github.com/schoolofcities/gta-immigration/blob/main/analysis/get_ed_ct_coverage_gta.ipynb' target='_blank'>two</a> <a href='https://github.com/schoolofcities/gta-immigration/blob/main/analysis/get_ed_ct_stats_gta.ipynb' target='_blank'>scripts</a>), weighting partial overlaps by their proportional area.</p>

            <p>The maps displayed and used for interpolation came from <a href='https://observatory.uwo.ca/unicen/index.html' target='_blank'>UNI-CEN</a> (federal ridings and census tracts) and <a href='http://election-atlas.ca' target='_blank'>election-atlas.ca</a> (Ontario ridings). We included only ridings where at least 75% of the area was covered by census tracts and 50% fell within the Greater Toronto Area.</p>

            <p>The final dataset is <a href='https://github.com/schoolofcities/gta-immigration/tree/main/static/data/elections' target='_blank'>available here</a>, and all code for this project is in the <a href='https://github.com/schoolofcities/gta-immigration/tree/main' target='_blank'>GitHub repository</a>.</p>
        </div>


    </div>
</main>

<style>
</style>
