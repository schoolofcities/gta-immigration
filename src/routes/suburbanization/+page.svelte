<script>
    import TopSofC from '$lib/TopSofC.svelte';
    import ImmigrationMapContainer from '$lib/suburbanization/ImmigrationMapContainer.svelte';
    import LineGraphTime from '$lib/suburbanization/LineGraphTime.svelte';
    import StepGraphContainer from '$lib/suburbanization/StepGraphContainer.svelte';

    import mapLegend from './assets/map-legend.svg?raw';
    import map1961 from './assets/map-1961.svg?raw';
    import map1981 from './assets/map-1981.svg?raw';
    import map2001 from './assets/map-2001.svg?raw';
    import map2021 from './assets/map-2021.svg?raw';

    import '../../assets/global-styles.css';

    import Footnote from '$lib/Footnote.svelte';
    import Footnotes from '$lib/Footnotes.svelte';
    import { createFootnoteStore } from '$lib/footnoteUtils';

    const footnoteStore = createFootnoteStore();
    const { footnotes, addFootnote } = footnoteStore;

    const fns = [
        `[Immigrants make up the largest share of the population in over 150 years and continue to shape who we are as Canadians](https://www150.statcan.gc.ca/n1/daily-quotidien/221026/dq221026a-eng.htm)`,

        `Terminology from Mireille Vézina and René Houle, "[Settlement patterns and social integration of the population with an immigrant background in the Montréal, Toronto and Vancouver metropolitan areas](https://www150.statcan.gc.ca/n1/pub/89-657-x/89-657-x2016002-eng.htm)", Statistics Canada Ethnicity, Language and Immigration Thematic Series (2017), Catalogue no. 89-657-X2016002`,

        `Michael Lewyn, “[How Suburbia Happened in Toronto](https://digitalcommons.tourolaw.edu/cgi/viewcontent.cgi?article=1550&context=scholarlyworks),” *Fla. A & M UL Rev.* 6 (2010): 299-311.`,

        `Sandeep Kumar and Bonica Leung, “Formation of an Ethnic Enclave: Process and Motivations,” *Plan Canada*, 45:2 (2005), 43-45.`,

        `Citizenship and Immigration Canada, “New federal Immigrant Investor Program will bring to Canada more resources to fund economic development and job creation initiatives” (November 10, 2010.) Archived at [https://web.archive.org/web/20101115061929/http://www.cic.gc.ca/english/department/media/backgrounders/2010/2010-11-10a.asp](https://web.archive.org/web/20101115061929/http://www.cic.gc.ca/english/department/media/backgrounders/2010/2010-11-10a.asp)`,

        `Shuguang Wang and Jason Zhong, "Delineating Ethnoburbs in Metropolitan Toronto", CERIS Working Paper No. 100 (2013)`,

        `Jeff Allen, Steven Farber, and Ignacio Tiznado-Aitken, “Pathways to suburban poverty in nine Canadian metropolitan areas”, *Cities* 147, (2024), 104848, [https://doi.org/10.1016/j.cities.2024.104848](https://doi.org/10.1016/j.cities.2024.104848)`,

        `Sutama Ghosh, “Everyday Lives in Vertical Neighbourhoods: Exploring Bangladeshi Residential Spaces in Toronto's Inner Suburbs”, *International Journal of Urban and Regional Research* 38, no. 6 (2014): 2008–24. [https://doi.org/10.1111/1468-2427.12170](https://doi.org/10.1111/1468-2427.12170); and Robert A. Murdie, Carlos Teixeira, Michael Lanphier, and Paul Anisef, “Towards a Comfortable Neighbourhood and Appropriate Housing: Immigrant Experiences in Toronto”, in *The World in a City*, (University of Toronto Press, 2003), 132.`,
    ]
</script>

<svelte:head>
	<meta
		name="viewport"
		content="width=device-width, initial-scale=1, minimum-scale=1"
	/>

	<title>The Suburbanization of Immigrants in the Greater Toronto Area | School of Cities</title>

	<meta name="description" content="">
	<meta name="author" content="Aniket Kali, Serene Tan, & Jeff Allen">
    
	<meta property="og:title" content="The Suburbanization of Immigrants in the Greater Toronto Area" />
	<meta property="og:description" content="Immigrants have increasingly moved to the suburbs over the years" />
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://schoolofcities.github.io/gta-immigration/suburbanization" />
	<meta property="og:image" content="https://schoolofcities.github.io/gta-immigration/web-card-suburbanization.png" />
	<meta property="og:locale" content="en_CA">

	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:site" content="https://schoolofcities.github.io/gta-immigration/suburbanization" />
	<meta name="twitter:creator" content="@UofTCities" />
	<meta name="twitter:title" content="The Suburbanization of Immigrants in the Greater Toronto Area" />
	<meta name="twitter:description" content="Immigrants have increasingly moved to the suburbs over the years" />
	<meta name="twitter:image" content="https://schoolofcities.github.io/gta-immigration/web-card-suburbanization.png" /> 
    
</svelte:head>

<main>
    <TopSofC/>
    <div class="title">
        <h1>The Suburbanization of Immigrants in the Greater Toronto Area</h1>
        <p>
            <a href='https://www.linkedin.com/in/aniket-k-8a8b9921b/' target='_blank'>Aniket Kali</a>,
            <a href='https://www.linkedin.com/in/serene-tan-530239113' target='_blank'>Serene Tan</a>,
            <a href='https://jamaps.github.io/' target='_blank'>Jeff Allen</a>
            |
            July 2025
        </p>
    </div>

    <div class="text">

        {@html mapLegend}
        
    </div>

    <div class="map-container">

        <!-- copy this into the .svg to scale by aspect ratio for small screens, preserveAspectRatio="xMidYMid meet" -->

        <div class="map">
            {@html map1961}
        </div>

        <div class="map">
            {@html map1981}
        </div>

        <div class="map">
            {@html map2001}
        </div>

        <div class="map">
            {@html map2021}
        </div>

    </div>

    <!-- <ImmigrationMapContainer /> -->
    
    <div class="text">
        <p>
            It's said that Canada is a nation of immigrants, and nowhere has that been more evident than the Greater Toronto Area, with about one-third of all new immigrants choosing the region in 2021.<Footnote id={addFootnote(fns[0])} /> This isn't too surprising – Toronto has long been the immigrant hub of the country, with its foreign-born population exceeding the national average consistently. It's where they've ended up that's really changed: before, it was the downtown, and now, it's the suburbs. 
        </p>

        <p>
            As postwar immigration boomed, many immigrants chose downtown Toronto as their new home, with some neighbourhoods home to a majority of immigrants. Over time however, immigrants dispersed: first into the inner suburbs like North York and Scarborough, and later into the outer suburbs and beyond, like Brampton and Markham. 
        </p>
        <p>
            Since the early 2000s especially, immigrants have been more likely to settle in these peripheral municipalities.<Footnote id={addFootnote(fns[1])} />
        </p>
        <p>
            It's not just newcomers, though. Whether it's Italian immigrants moving to Vaughan, or Portuguese immigrants moving to North York, once settled, older immigrants have also chosen to leave the downtown for the suburbs.
        </p>
        <h2>
            Why the move to the suburbs?
        </h2>
        <p>
            In the early and mid 20th century, it was commonplace for immigrants across North America to settle in downtown neighbourhoods. Many new immigrants were working-class, and the downtown provided opportunities to make a living: a short commute to work and jobs, cheap and easy access to housing, and social support through nearby family and ethnic communities. 
        </p>
        <p>
            As early as the 1940s, Toronto's planners actively paved the path toward suburban growth. New highways were built to make it easier to live in the suburbs, and density was far lower than in the downtown.<Footnote id={addFootnote(fns[2])} /> Unlike the downtown – the densest and <a href='https://schoolofcities.github.io/neighbourhood-income-toronto-2020/' target="_blank">poorest</a> part of the city – the suburbs appealed to those who could afford it as roomier, home to better services and schools, and an easy commute to downtown Toronto. 
        </p>
    </div>

    <LineGraphTime />

    <div class="text">
        <p>
            In 1967, Canada ended race and nationality quotas for immigration in favour of a points-based system, focused on likelihood of integration. The program favoured younger people with higher educational attainment, work experience, and English or French language abilities. Increasingly, new immigrants arrived with professional qualifications and the means to eventually afford the spaciousness of a suburban home, and did not have to remain in the smaller and tenanted housing of downtown areas. With the growing development of industrial and business parks in the peripheral municipalities, there were also desirable jobs in the suburbs.<Footnote id={addFootnote(fns[3])} />
        </p>
        <p>
            The Canadian immigrant investor program (1986-2014) also contributed to this trend. This program required applicants to invest a minimum of $800,000 in the country and have a minimum of $1,600,000 net worth to qualify for immigration.<Footnote id={addFootnote(fns[4])} />
        </p>
        <p>
            As immigrants from the world over have settled across the GTA, they've created new cultural hubs and moved cultural services along with them – most notably with South Asian Canadians in Brampton, and Chinese Canadians in Markham.<Footnote id={addFootnote(fns[5])} /> These, too, attract immigrants to settle in target suburbs, where their old home may not feel as far away. 
        </p>
    </div>  

    <StepGraphContainer />
    
    <div class="text">
        <p>
            No doubt the appeal of the suburbs and ethnic communities form a strong part of the story, but it would be a mistake to leave it there. While it's true that the downtown was once poorer, recent decades have seen a switch: a <a href="https://schoolofcities.github.io/neighbourhood-income-toronto-2020/" target="_blank">wealthier</a> and <a href="https://www.theguardian.com/cities/2020/jan/14/my-parkdale-is-gone-how-gentrification-reached-the-one-place-that-seemed-immune" target="_blank">gentrifying</a> downtown against rising suburban poverty.<Footnote id={addFootnote(fns[6])} /> Immigrants remain amongst the most likely victims to become part of the suburban poor, amidst a cost-of-living crisis, a lack of affordable housing, and “<a href="https://www.thestar.com/news/canada/immigrants-to-canada-have-long-found-their-qualifications-questioned-and-careers-crushed-things-were-supposed/article_c3ed7483-40f0-4acc-9e76-c8036f8f3270.html" target="_blank">deskilling</a>” where exactly those qualifications that gave them the points to immigrate are seen as invalid and inferior to Canadian credentials. 
        </p>
        <p>
            In that context, wealthier immigrants can afford spacious suburban homes, yes, but working-class immigrants are more often limited to low-cost rental units in high-rise apartments in the inner suburbs.<Footnote id={addFootnote(fns[7])} />
        </p>
        <p>
            At the end of the day, the immigrant story of settlement isn't all that different in the larger tale of suburbanization: immigrants settled in and moved to suburban areas of large Canadian cities for the same reasons that non-immigrants had. Some considered them to be better places with larger homes and better schools, others sought out their own communities, and many went where their wallet would let them. 
        </p>
    </div>

    <div class="text">
        <br>
        <br>

        <div class="footnotes">
            <h3>Data & Methods</h3>
            <p>
                We used census data published through <a href="https://observatory.uwo.ca/unicen/index.html" target="_blank">UNI-CEN</a> from 1961 onwards for this project. Our analysis considers census data that falls within the Greater Toronto Area (GTA). Specifically, we collected census tract (CT) and census subdivision (CSD) level data, where 50% and 25% of the geometry was within the GTA respectively. We only used CSD data to cover regions where CT data was missing, and weighted CSD data proportionately to the cut used, using <a href="https://github.com/schoolofcities/gta-immigration/blob/main/analysis/join_ct_csd_imm_stats_gta.ipynb" target="_blank">this script</a>. In 1961 and 1971, parts of the GTA had no CSD data available, so we used placeholder geometry with null values. 
            </p>
            <p>
                Our main object of interest was immigration data: the total number of immigrants as well as the number of new immigrants. The precise census codes can be <a href="https://github.com/schoolofcities/gta-immigration/blob/main/analysis/constants.py" target="_blank">found here</a>. We took “new immigrants” to mean “immigrated in the last 5 years”, as is conventional in most census data. Due to irregularities in the census, we sometimes had to define this as the last 3 years (1981, 1986, 1991) or were unable to retrieve the data (1971). 
            </p>
            <p>
                In order to measure distance, we computed the distance from the centroid of a given CT or CSD to Nathan Philipps Square. For mean distance in a year, we weighted them by the normalized number of immigrants, and for 1km-bands, we classified them within 1km buckets, using <a href="https://github.com/schoolofcities/gta-immigration/blob/main/analysis/analyze_imm_stats.ipynb" target="_blank">this script</a>.
            </p>
            <p>
                The final dataset is <a href="https://github.com/schoolofcities/gta-immigration/tree/main/static/data" target="_blank">available here</a>, and all code for this project is in the <a href="https://github.com/schoolofcities/gta-immigration" target="_blank">GitHub repository</a>.
            </p>
        </div>
    </div>

    <div class="text">
        <Footnotes footnotes={footnotes} />
        
    </div>
</main>

<style>

    .map-container {
        margin: 0 auto;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        max-width: 1400px;
        gap: 20px;
        margin-top: 25px;
    }

    .map {
        width: 100%;
        box-sizing: border-box;
        max-width: 700px;
        margin: 0 auto;
        position: relative;
        padding-left: 5px;
        padding-right: 5px;
        padding-top: 5px;
        padding-bottom: 5px;
        border: solid 1px #e9e9e9;
    }

    @media (min-width: 1200px) {
        .map {
            width: calc(50% - 10px); /* Two per row with gap */
        }
    }

    .map svg {
        width: 30px;
        height: auto;
        display: block;
    }

</style>
