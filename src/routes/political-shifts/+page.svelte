<script>
    import TopSofC from '$lib/TopSofC.svelte';
    import StaticCorrelationDisplay from '$lib/StaticCorrelationDisplay.svelte';
    import CensusVoteMaps from '$lib/CensusVoteMaps.svelte';
    import CorrelationDisplay from '$lib/CorrelationDisplay.svelte';
    import CorrelationTimeline from '$lib/CorrelationTimeline.svelte';
    import VoteShareCompare from '$lib/VoteShareCompare.svelte';
    import '../../assets/global-styles.css';

    import Footnote from '$lib/Footnote.svelte';

    function parseMarkdown(text) {
        return text
            .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')       // bold
            .replace(/\*(?!\*)(.+?)\*/g, '<em>$1</em>')              // italics
            .replace(/\[([^\]]+)]\(([^)]+)\)/g, '<a href="$2">$1</a>'); // links
    }

    let footnotes = [];
    function addFootnote(text) {
        const id = footnotes.length + 1;
        const parsed = parseMarkdown(text);
        footnotes.push({ id, text: parsed });
        return id;
    }

    const fns = [
        `See, for example, Brian K. Ray, Greg Halseth, and Benjamin Johnson, "The Changing 'Face' of the Suburbs: Issues of Ethnicity and Residential Change in Suburban Vancouver", *International Journal of Urban and Regional Research* 21, no. 1 (1997), 75-99, [https://doi.org/10.1111/1468-2427.00059](https://doi.org/10.1111/1468-2427.00059); Harald Bauder and Bob Sharpe, "Residential segregation of visible minorities in Canada's gateway cities", *The Canadian Geographer* 46, no. 3 (2002), 204-222, [https://doi.org/10.1111/j.1541-0064.2002.tb00741.x](https://doi.org/10.1111/j.1541-0064.2002.tb00741.x); Robert Murdie and Carlos Teixeira, "Towards a Comfortable Neighbourhood and Appropriate Housing: Immigrant Experiences in Toronto", ed. Paul Anisef and Michael Lanphier (eds.) *The World in a City* (University of Toronto Press, 2003); Virpal Kataure and Margaret Walton-Roberts "The housing preferences and location choices of second-generation South Asians living in ethnic enclaves", *South Asian Diaspora* 5, no. 1 (2013), 57-76, [https://doi.org/10.1080/19438192.2013.722385](https://doi.org/10.1080/19438192.2013.722385); Shuguang Wang and Jason Zhong, "Delineating Ethnoburbs in Metropolitan Toronto", CERIS Working Paper No. 100 (2013); Mireille Vézina and René Houle, "Settlement patterns and social integration of the population with an immigrant background in the Montréal, Toronto and Vancouver metropolitan areas", Statistics Canada Ethnicity, Language and Immigration Thematic Series (2017), Catalogue no. 89-657-X2016002`,

        `Lucia Lo, Amer Shalaby, and Baha Alshalalfah, "Relationship between Immigrant Settlement Patterns and Transit Use in the Greater Toronto Area", *Journal of Urban Planning and Development*, 137, no. 4 (2011), 470-476, [https://doi.org/10.1061/(ASCE)UP.1943-5444.0000080](https://doi.org/10.1061/(ASCE)UP.1943-5444.0000080)`,

        `Triadafilos Triadafilopoulos, "Dismantling White Canada: Race, Rights, and the Origins of the Points System", in Wanted and Welcome? *Policies for Highly Skilled Immigrants in Comparative Perspective*, ed. Triadafilos Triadafilopoulos (Springer, 2013), 15-37`,

        `See Erin Tolley, "Political Players or Partisan Pawns? Immigrants, Minorities, and Conservatives in Canada", in *The Blueprint: Conservative parties and their impact on Canadian politics*, ed. J.P. Lewis and Joanna Everitt (University of Toronto Press, 2017), 101; and Zack Taylor, "The Political Geography of Immigration: Party Competition for Immigrants' Votes in Canada, 1997–2019", *American Review of Canadian Studies* 51 no. 1(2021), 18-40, [https://doi.org/10.1080/02722011.2021.1874732](https://doi.org/10.1080/02722011.2021.1874732); Tolley, 2017`,

        `Fidan Elcioglu, "I Began to Think More Like a Canadian: How Second-Generation South Asian and Chinese Canadians Confront Racism by Becoming Conservative Voters," *Ethnic and Racial Studies* (2025): 1–20, [https://doi.org/10.1080/01419870.2025.2474628](https://doi.org/10.1080/01419870.2025.2474628)`,
    ]
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
	<meta property="og:description" content="Immigrants in the GTA have had many political shifts across time and geography" />
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://schoolofcities.github.io/gta-immigration/political-shifts" />
	<meta property="og:image" content="https://schoolofcities.github.io/gta-immigration/web-card-political-shifts.png" />
	<meta property="og:locale" content="en_CA">

	<!-- <meta name="twitter:card" content="summary_large_image" /> -->
	<meta name="twitter:site" content="https://schoolofcities.github.io/gta-immigration/political-shifts" />
	<meta name="twitter:creator" content="@UofTCities" />
	<meta name="twitter:title" content="Changes in immigrant voting patterns in the Greater Toronto Area" />
	<meta name="twitter:description" content="Immigrants in the GTA have had many political shifts across time and geography" />
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
        <p>
            Immigrant-heavy ridings across the Greater Toronto Area (GTA) have swung from being decisively against to decisively for the provincial Conservatives over these last 30 years. It's part of the trend we're seeing across North America where <a href='https://www.ft.com/content/a7607626-5491-48bd-aa56-5a10cbeeb768' target='_blank'>immigrants</a> and <a href='https://theconversation.com/why-are-so-many-second-generation-south-asian-and-chinese-canadians-planning-to-vote-conservative-253820' target='_blank'>minorities</a> are swinging to the political right; and it's also a story of how one of the GTA's largest constituencies is much more dynamic than we often realize.
        </p>
    </div>

    <StaticCorrelationDisplay />

    <div class="text">
        <p>
            Since the late twentieth century, researchers have noted the changing demographics in Canada's suburbs, particularly in terms of ethnicity and immigrant status.<Footnote id={addFootnote(fns[0])} /> 
            In the Greater Toronto Area, the share of immigrants in the inner suburbs (Etobicoke, North York, Scarborough) has grown since the 1970s, and in the outer suburbs (Halton, Peel, York, and Durham) since the 1990s, while declining in the inner city region (City of Toronto) at the same time.<Footnote id={addFootnote(fns[1])} /> 
            Additionally, since <a href='https://www.justice.gc.ca/eng/rp-pr/csj-sjc/jsp-sjp/rp02_8-dr02_8/p3.html' target="_blank">immigration reform in 1967</a> – which abolished race and nationality quotas in favour of a point-based system – immigrants have increasingly been visible minorities.<Footnote id={addFootnote(fns[2])} /> 
        </p>

        <p>
            How has this changing composition played out in the political and electoral landscape of the GTA?
        </p>
    </div>

    <div class="text">
        <h2>Does party vote share correspond to where immigrants live?</h2>
        <p>
            In 2018, the provincial Conservatives pulled off a historic feat: immigrant-heavy ridings were more likely than not to vote for them. Neither the provincial nor federal Conservatives had pulled this off in the time we reviewed in this study – looking at census data since 1961 – and certainly not since the official end of race-based immigration quotas in 1967.
        </p>
    </div>

    <!-- View trend line of correlation (choose party) -->
    <div class="container">
        <CorrelationTimeline />
    </div>

    <div class="text">
        <p>
            The fact is that as immigrants have begun to grow as a political constituency, political parties have made a concerted effort to win them over for about the past 40 years.<Footnote id={addFootnote(fns[3])} /> 
            In ridings dominated by specific immigrant and ethnic groups, it can be a political strategy to actively target messages at ethno-religious communities, run candidates who represent specific ethnic groups, and use ethnic media outlets to reach groups of people through their collective identities.
        </p>
        <p>
            These efforts are a competition, and we see that in how different parties have risen and fallen in their popularity in immigrant-heavy ridings.
        </p>

        <h4>Federal</h4>
        
        <p>
            In 1971, the federal Liberals, under Prime Minister Pierre Elliott Trudeau, announced multiculturalism as official Canadian policy. While the federal Liberals had always performed well in immigrant-heavy ridings, their popularity rose steeply from the 1972 election onwards, to reach all-time highs for four decades before starting to fall in the 2010s. 
        </p>
        <p>
            While the Liberals still reigned supreme federally, the federal Conservatives became much more competitive in immigrant-heavy ridings beginning in the early 2000s. This may coincide with federal Conservative leader and Prime Minister Stephen Harper's <a href='https://www.cicnews.com/2006/05/primeminister-stephen-harper-reaching-canadian-immigrants-0597.html#gs.l52rih' target='_blank'>immigrant-friendly policies</a>.
        </p>
        <p>
            More recently, in a study funded by the School of Cities<Footnote id={addFootnote(fns[4])} />, Professor Emine Fidan Elcioglu found many second generation immigrants had started voting Conservative as a way of assimilating – following years of outreach by the federal Conservatives into suburban and minority communities. 
        </p>
        <p>
            The left-leaning New Democrats have, in contrast, seen a steep fall in popularity since 2004. The party has yet to recover and continues to decline in immigrant-heavy ridings.
        </p>

        <h4>Provincial</h4>

        <p>
            While Conservatives at both levels have seen rising support in recent decades in the ridings where immigrants live, there's one major difference: since 2018, Ontario's Conservatives have become the party of immigrants in the GTA. Unlike their federal counterpart, who has made gains but is still outcompeted by the Liberals, they have ranked or tied for first place in immigrant-heavy ridings in each election since. 
        </p>
        <p>
            This is a remarkable shift from decades past, when more immigrants meant fewer votes for the Conservatives – reaching an all-time low as recently as 1995.
        </p>
        <p>
            Equally unlike the federal level, it was Ontario's New Democrats who were most popular in immigrant-heavy ridings throughout the 1970s and 80s, largely during the leaderships of Stephen Lewis and Bob Rae. They would be overshadowed by the provincial Liberals in 1987 (who, in turn, would dominate until 2018), but remained competitive in immigrant-heavy ridings until the early 2000s. Since then, they've seen a decline similar to their federal counterpart.
        </p>
        <p>
            Nonetheless, all the trends we see are in the big picture, and there are exceptions. The plots below show the fine details of the relationship between percent immigrants and party vote share for individual GTA ridings in each election: points further to the right indicate a higher percentage of immigrants in the riding, and points higher on the plot indicate a larger party vote share.
        </p>
    </div>

    <!-- View graph of all data points and correlation year (choose party+year) -->
    <div class="container">
        <CorrelationDisplay />
    </div>

    <div class="text">
        <h2>How do different ridings compare geographically?</h2>
        <p>
            Toronto's suburbs have become the heart of immigration in the region - in Scarborough since the 1980s, and then later in Brampton, Markham, and Mississauga. By looking at how voting patterns have changed in these regions, we can understand these trends in detail.
        </p>
        <p>
            The maps below show (by riding) party vote share on the left, and census data on the right. Moving through the years, we can see the changes in where immigrants are and how that has played out geographically in their voting patterns.
        </p>
    </div>

    <!-- Dual panel of constituency maps: vote share & immigrant percent -->
    <CensusVoteMaps />

    <div class="text">
        <p>
            The federal Liberals have seen their greatest successes in Scarborough, Mississauga, and North Etobicoke – corresponding to the shift of immigrants into Toronto's inner, and then outer, suburbs from the 1980s onward. This shift suggests the development of suburban immigrant strongholds – perhaps a result of the Liberals’ welcoming immigration policies since the 1970s.
        </p>
        <p>
            In contrast, the heyday of the provincial New Democrats in the 1970s and 80s was quite geographically contained. They were popular in immigrant-heavy ridings along the western edge of inner-city Toronto – around the Humber River, from Parkdale to Davenport to Black Creek – where they succeeded with certain kinds of immigrants. But they failed to make inroads into more typically non-white suburban immigrant communities. Save fleeting success in Brampton in the 2010s, they've had little luck.
        </p>
        <p>
            And it's in these suburban, non-white, and immigrant-heavy ridings that the provincial Conservatives have seen their greatest successes. Some of the biggest gains in 2018 were in Markham and North Scarborough, which they've maintained since. These ridings are home to mostly East Asian visible minorities, who the provincial Conservatives made a <a href='https://briarpatchmagazine.com/articles/view/organizing-the-suburbs' target='_blank'>concerted effort to</a> access through ethnic churches, media, and socially conservative issues
        <p>
            Moreover, while they failed to sweep Brampton and North Mississauga in 2018, both elections since – in 2022 and 2025 – saw the Conservatives flip these ridings and continue to grow their margins. This suggests growing inroads with South Asian visible minorities, who dominate the region.
        </p>
    </div>

    <div class="text">
        <h2>Do parties over-perform in the most immigrant ridings?</h2>

        <p>
            Correlation and geography shed a lot of light on what is happening, and where. How much better or worse do parties perform in the most immigrant-heavy ridings, compared to elsewhere? Basically, when most people in a riding are immigrants, do we see the same trends and political preferences?
        </p>
    </div>

    <!-- View trend line mean vote share (choose party) for high immigrant ridings -->
    <div class="container">
        <VoteShareCompare />
    </div>

    <div class="text">
        <p>
            More or less, the answer is yes – we see the same broad trends. The federal Liberals still have the greatest leads, the provincial New Democrats still made inroads in the 1970s and 1980s before declining in recent years, and the rise of the Conservatives in the last decade - especially at the provincial level - is without dispute.
        </p>
        <p>
            But it's between the cracks of these big conclusions that we get the nuances of what is happening, when, and how much. Even by 2014, ahead of their breakthrough, provincial Conservatives had begun doing better in immigrant-heavy ridings compared to the rest of the GTA, indicating that a foundation had already been laid.
        </p>
        <p>
            Likewise, the federal Liberals not only continue to win over immigrants but in the most immigrant-heavy ridings, have consistently done better than their national vote share by 20% or 30% – showing just how deep immigrant loyalties lie – while the New Democrats’ decline may trace back as far as the 1980s.
        </p>
        <p>
            It also tells us what we don't know. We've looked at immigrants as a whole, but not at how different kinds of immigrants – varying by ethnicity, class, geography, and so on – participate (or do not or cannot participate electorally, either through turnout or voting restrictions).
        </p>
        <p>
            At about half of the population of the region, and a quarter of the country, immigrants are a major political constituency and a key part of the path to power for political parties. They form and lose loyalties to different parties at different times, and while these changes may feel like sudden shocks in the moment, by taking a step back we see competing long-term trends and political battles playing out over many years – just like any other group, immigrants are not a monolith.
        </p>
    </div>

    <div class="text">
        <br>
        <br>

        <div class="footnotes">
            <h3>Data & Methods</h3>
            
            <p>We obtained federal election results from <a href='https://github.com/Lucas-Czarnecki/Canadian-Federal-Elections/tree/main' target='_blank'>Lucas Czarnecki's database</a>, sourced from Canada's Library of Parliament (LoP), and Ontario election results from <a href='https://www.elections.on.ca/en/resource-centre/elections-results.html' target='_blank'>Elections Ontario</a>.</p>

            <p>For consistency, we focused on the three major parties in Anglo-Canada – the <a href='https://en.wikipedia.org/wiki/Liberal_Party_of_Canada' target='_blank'>Liberals</a>, <a href='https://en.wikipedia.org/wiki/New_Democratic_Party' target='_blank'>New Democrats</a>, and Conservatives – while grouping all other parties under "Other". The label "Conservatives" refers to the dominant center-right/right-wing party in each context: the <a href='https://en.wikipedia.org/wiki/Progressive_Conservative_Party_of_Ontario' target='_blank'>Progressive Conservatives in Ontario</a>, the <a href='https://en.wikipedia.org/wiki/Progressive_Conservative_Party_of_Canada' target='_blank'>federal Progressive Conservatives</a> (until 2004), and the <a href='https://en.wikipedia.org/wiki/Conservative_Party_of_Canada' target='_blank'>Conservative Party of Canada</a> (from 2004 onward). The only exception was including the <a href='https://en.wikipedia.org/wiki/Reform_Party_of_Canada' target='_blank'>Reform</a>/<a href='https://en.wikipedia.org/wiki/Canadian_Alliance' target='_blank'>Alliance</a> parties in the three federal elections they contested (1993, 1997, and 2000).<Footnote id={addFootnote('They would go on to merge with the federal Progressive Conservative party to form the Conservative Party of Canada in 2003.')} /></p>

            <p>Census data was drawn from <a href='https://observatory.uwo.ca/unicen/index.html' target='_blank'>UNI-CEN</a>, where we used census tract-level statistics starting in 1961. Immigration data is available from 1961 onward, household income from 1971 onward, and visible minority demographics from 2001 onward.</p>

            <p>Because historical electoral ridings lack direct census data, we estimated statistics using areal interpolation. We calculated relevant statistics by aggregating all census tracts fully or partially within each riding (using these <a href='https://github.com/schoolofcities/gta-immigration/blob/main/analysis/get_ed_ct_coverage_gta.ipynb' target='_blank'>two</a> <a href='https://github.com/schoolofcities/gta-immigration/blob/main/analysis/get_ed_ct_stats_gta.ipynb' target='_blank'>scripts</a>), weighting partial overlaps by their proportional area.</p>

            <p>The maps displayed and used for interpolation came from <a href='https://observatory.uwo.ca/unicen/index.html' target='_blank'>UNI-CEN</a> (federal ridings and census tracts) and <a href='http://election-atlas.ca' target='_blank'>election-atlas.ca</a> (Ontario ridings). We included only ridings where at least 75% of the area was covered by census tracts and 50% fell within the Greater Toronto Area.</p>

            <p>The final dataset is <a href='https://github.com/schoolofcities/gta-immigration/tree/main/static/data/elections' target='_blank'>available here</a>, and all code for this project is in the <a href='https://github.com/schoolofcities/gta-immigration/tree/main' target='_blank'>GitHub repository</a>.</p>
        </div>
    </div>

    <div class="text">
        <div class="footnotes">
            <h3>Footnotes</h3>
            {#each footnotes as footnote (footnote.id)}
                <div id={`footnote-${footnote.id}`} class="footnote-item">
                    <sup>{footnote.id}</sup>
                    <p style="display:inline">{@html footnote.text}</p>

                    <a href={`#footnote-ref-${footnote.id}`} class="backlink" on:click|preventDefault={() => {
                        const element = document.getElementById(`footnote-ref-${footnote.id}`);
                        const yOffset = -100;
                        if (element) {
                            const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
                            window.scrollTo({ top: y, behavior: 'auto' });
                        }
                    }}>
                        ↩
                    </a>
                </div>
            {/each}
        </div>
    </div>
</main>

<style>
    .footnote-item {
        margin-bottom: 0.5em;
        line-height: 1.4;
        position: relative;
        padding-left: 1.5em;
    }

    .footnote-item sup {
        position: absolute;
        left: 0;
    }

    .backlink {
        margin-left: 0.5em;
        text-decoration: none;
        color: #007FA3;
    }
</style>
