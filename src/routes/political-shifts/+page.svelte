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
            Immigrant-heavy ridings across the Greater Toronto Area (GTA) have swung from being decisively against to decisively for the provincial Conservatives over these last 30 years. It's part of the trend we're seeing across North America where <a href='https://www.ft.com/content/a7607626-5491-48bd-aa56-5a10cbeeb768' target='_blank'>immigrants</a> and <a href='https://theconversation.com/why-are-so-many-second-generation-south-asian-and-chinese-canadians-planning-to-vote-conservative-253820' target='_blank'>minorities</a> are swinging to the political right; and it's also a story of how one of the GTA's largest constituencies is much more dynamic than we often realize.
        </p>
    </div>

    <StaticCorrelationDisplay />

    <div class="text">
        <p>
            Since the late twentieth century, researchers have noted the changing demographics in Canada's suburbs, particularly in terms of ethnicity and immigrant status. In the Greater Toronto Area (GTA), the share of immigrants in the inner suburbs (Etobicoke, North York, Scarborough) has grown since the 1970s, and in the outer suburbs (Halton, Peel, York, and Durham) since the 1990s, while declining in the inner city region (City of Toronto) at the same time. Additionally, since immigration reform in 1967 which abolished race and nationality quotas in favour of a point-based system, immigrants have increasingly been visible minorities.
        </p>

        <p>
            How has this changing composition played out in the political and electoral landscape of the GTA?
        </p>
    </div>

    <div class="text">
        <h2>Does party vote share correspond to where immigrants live?</h2>
        <p>
            In 2018, the provincial Conservatives pulled off a historic feat: immigrant ridings were more likely than not to vote for them. Neither the provincial nor federal Conservatives had ever pulled this off since the start of our data in 1961 - and certainly not since the official end of race-based immigration quotas in 1967.
        </p>
    </div>

    <!-- View trend line of correlation (choose party) -->
    <div class="container">
        <CorrelationTimeline />
    </div>

    <div class="text">
        <p>
            The fact is that political parties have made a concerted effort these last 40 years to win over immigrant voters. In ridings dominated by specific immigrant and ethnic groups, it can be a political strategy to actively target messages at ethno-religious communities, run candidates who represent specific ethnic groups, and use ethnic media outlets to reach groups of people through their collective identities.
        </p>
        <p>
            These efforts are a competition, and we see that in how different parties have risen and fallen in their popularity in immigrant-heavy ridings.
        </p>

        <h4>Federal</h4>
        
        <p>
            In 1971, the federal Liberals under Prime Minister Pierre Elliott Trudeau declared multiculturalism as official Canadian policy. While the federal Liberals had always performed well in immigrant ridings, their popularity rose steeply from the 1972 election onwards to reach all-time highs for four decades before starting to fall in the 2010s. 
        </p>
        <p>
            While the Liberals still reign supreme federally, it's around the same time - starting in the early 2000s - the federal Conservatives became much more competitive in immigrant ridings. This may coincide with federal Conservative leader and Prime Minister Stephen Harper's <a href='https://www.cicnews.com/2006/05/primeminister-stephen-harper-reaching-canadian-immigrants-0597.html#gs.l52rih' target='_blank'>immigrant-friendly policies</a>.
        </p>
        <p>
            The left-leaning New Democrats have, in contrast, seen a steep fall in popularity since 2004. The party has yet to recover and continues to decline in immigrant ridings.
        </p>

        <h4>Provincial</h4>

        <p>
            While Conservatives at both levels have seen rising support where immigrants live in recent decades, there's one major difference: since 2018, Ontario's Conservatives have largely become the party of immigrants in the GTA. They have ranked or tied for first place when it comes to performing well in immigrant-heavy ridings in each election since. 
        </p>
        <p>
            This is a remarkable shift from decades past, where more immigrants simply meant less votes for the Conservatives - reaching an all-time low as recently as 1995.
        </p>
        <p>
            And equally unlike the federal level, it was Ontario's New Democrats who were most popular in immigrant-heavy writings throughout the 1970s and 1980s, largely during the leaderships of Stephen Lewis and Bob Rae. They would be overshadowed by the provincial Liberals in 1987 (who, in turn, would dominate until 2018) - but remain competitive in immigrant ridings until the early 2000s. Since then, they've seen a similar decline to their federal counterpart.
        </p>
        <p>
            Still, all of the trends we see are the big picture, and there are exceptions. The plots below show the fine details of the relationship between percent immigrants and party vote share for individual GTA ridings in each election: points further to the right indicate a higher percentage of immigrants in the riding, and points higher on the plot indicate a larger party vote share.
        </p>
    </div>

    <!-- View graph of all data points and correlation year (choose party+year) -->
    <div class="container">
        <CorrelationDisplay />
    </div>

    <div class="text">
        <h2>How do different ridings compare geographically?</h2>
        <p>
            Toronto's suburbs have become the heart of immigrants in the region over the decades - in Scarborough since the 1980s, and then later in Brampton, Markham, and Mississauga.
        </p>
        <p>
            The maps below show (by riding) party vote share on the left, and census data on the right. Moving through the years, we can see the changes in where immigrants are and how that is played out geographically in their voting patterns.
        </p>
    </div>

    <!-- Dual panel of constituency maps: vote share & immigrant percent -->
    <CensusVoteMaps />

    <div class="text">
        <p>
            The federal Liberals have seen their greatest successes in Scarborough, Mississauga, and North Etobicoke - corresponding to the shift of immigrants into Toronto's periphery from the 1980s onward. It shows the development of suburban immigrant strongholds - perhaps a result of their welcoming immigration policies since the 1970s.
        </p>
        <p>
            In contrast, the heyday of the provincial New Democrats in the 1970s and 1980s was quite geographically contained. It was popular in immigrant dense ridings along the western edge of inner-city Toronto - around the Humber River from Parkdale to Davenport to Black Creek - succeeded with certain kinds of immigrants. But it’s also a failure to make inroads into more typically non-white suburban immigrants. Save fleeting success in Brampton over the 2010s, they've had little luck since.
        </p>
        <p>
            And it's in these suburban, non-white, and immigrant-heavy ridings, that the provincial Conservatives have seen their greatest successes. Some of the biggest gains in 2018 were in Markham and North Scarborough, which they've maintained since. These ridings are home to mostly East Asian visible minorities, which the provincial Conservatives made a <a href='https://briarpatchmagazine.com/articles/view/organizing-the-suburbs' target='_blank'>concerted effort to organize</a> through ethnic churches, media, and socially conservative issues. 
        </p>
        <p>
            Moreover, while they failed to sweep Brampton and North Mississauga in 2018, both elections since in 2022 and 2025 have seen increasing gains. This reflects growing inroads with South Asian visible minorities who dominate the region.
        </p>
    </div>

    <div class="text">
        <h2>Do parties over-perform in the most immigrant ridings?</h2>

        <p>
            Correlation and geography shed a lot of light on what is happening and where. As a kind of safety check, we can also ask: how much better or worse do parties perform in the most immigrant-heavy ridings, compared to in general? Basically, when most people are immigrants in ridings, do we see similar patterns?
        </p>
    </div>

    <!-- View trend line mean vote share (choose party) for high immigrant ridings -->
    <div class="container">
        <VoteShareCompare />
    </div>

    <div class="text">
        <p>
            More or less, the answer is yes - it's the same. The federal Liberals still have the greatest leads, the provincial New Democrats still made inroads in the 1970s and 1980s, and the rise of the Conservatives - especially at the provincial level - is without dispute.
        </p>
        <p>
            But it's between the cracks of these big conclusions that we get the nuances of what is happening, when, and how much. Even by 2014, ahead of their breakthrough, provincial Conservatives had begun  doing better in immigrant-heavy ridings compared to the rest of the GTA, indicating that the foundation had already been laid.
        </p>
        <p>
            Likewise, the federal Liberals not only won over immigrants, but in the most immigrant ridings have consistently done better than their national vote share by 20% or 30% - showing just how deep immigrant loyalties lie - while the New Democrats decline may trace back as far as the 1980s.
        </p>
        <p>
            It also tells us what we don't know. We've looked at immigrants as a whole, but not really how different kinds of immigrants - varying by ethnicity, class, geography, and so on - participate. And equally, how they do not or cannot participate electorally - either through turnout, or voting restrictions.
        </p>
        <p>
            We could go on, but the point is the same. At about half of the population of the region, and a quarter of the country, immigrants are a major political constituency and a key part of the path to power for political parties. They form and lose loyalties to different parties at different times, and while these changes may feel like sudden shocks in the moment, by taking a step back we see competing long-term trends and political battles playing out over many years. For, just like any other group, immigrants are hardly a monolith.
        </p>
    </div>

    <div class="text">
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
