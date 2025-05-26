<script>
    import TopSofC from '$lib/TopSofC.svelte';
    import VMCorrelationDisplay from '$lib/rightward-minorities/VMCorrelationDisplay.svelte';
    import VMVoteSharePanel from '$lib/rightward-minorities/StaticVMVoteSharePanel.svelte';
    import Gen2ProfilesPanel from '$lib/rightward-minorities/Gen2ProfilesPanel.svelte';
    import EthnicityVoteChartMultiples from '$lib/rightward-minorities/EthnicityVoteChartMultiples.svelte';

    import '../../assets/global-styles.css';
</script>

<svelte:head>
	<meta
		name="viewport"
		content="width=device-width, initial-scale=1, minimum-scale=1"
	/>

	<title>Rightward shifts amongst visible minorities in the Greater Toronto Area | School of Cities</title>

	<meta name="description" content="">
	<meta name="author" content="Emine Fidan Elcioglu, Aniket Kali, Serene Tan, & Jeff Allen">
    
	<meta property="og:title" content="Rightward shifts amongst visible minorities in the Greater Toronto Area" />
	<meta property="og:description" content="Visible minorities in the GTA have begun to shift to the Conservatives" />
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://schoolofcities.github.io/gta-immigration/rightward-minorities" />
	<!-- <meta property="og:image" content="https://schoolofcities.github.io/gta-immigration/web-card-rightward-minorities.png" /> -->
	<meta property="og:locale" content="en_CA">

	<!-- <meta name="twitter:card" content="summary_large_image" /> -->
	<meta name="twitter:site" content="https://schoolofcities.github.io/gta-immigration/rightward-minorities" />
	<meta name="twitter:creator" content="@UofTCities" />
	<meta name="twitter:title" content="Rightward shifts amongst visible minorities in the Greater Toronto Area" />
	<meta name="twitter:description" content="Visible minorities in the GTA have begun to shift to the Conservatives" />
	<!-- <meta name="twitter:image" content="https://schoolofcities.github.io/gta-immigration/web-card-rightward-minorities.png" />  -->
    
</svelte:head>

<main>
    <TopSofC/>

    <div class="title">
        <h1>Rightward shifts amongst visible minorities in the Greater Toronto Area</h1>
        <p>
            <a href='https://fidanelcioglu.com/' target='_blank'>Emine Fidan Elcioglu</a>,
            <a href='https://www.linkedin.com/in/aniket-k-8a8b9921b/' target='_blank'>Aniket Kali</a>,
            <a href='https://www.linkedin.com/in/serene-tan-530239113' target='_blank'>Serene Tan</a>,
            <a href='https://jamaps.github.io/' target='_blank'>Jeff Allen</a>
            |
            May 2025
        </p>
    </div>

    <div class="text">
        <p>
            Lorem ipsum, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
    </div>

    <div class="container">
        <VMCorrelationDisplay />
    </div>

    <div class="text">
        <p>
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </div>

    <div class="text">
        <h2>What is happening?</h2>
        <p>
            Lorem ipsum, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
        <p>
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </div>

    <div>
        <VMVoteSharePanel />
    </div>

    <div class="text">
        <p>
            Lorem ipsum, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
        <p>
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </div>

    <div class="text">
        <h2>2nd Generation Immigrants</h2>
        <p>
            Discussion of 2nd gen visible minorities shifting right - introduce the main study, qualitative data, etc.
        </p>
        <p>
            Lorem ipsum, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
        <p>
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </div>

    <div class="container">
        <Gen2ProfilesPanel />
    </div>

    <div class="text">
        <p>
            Lorem ipsum, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
        <p>
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </div>

    <div class="text">
        <h2>South Asian Canadians and Chinese Canadians</h2>
        <p>
            Lorem ipsum, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
        <p>
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </div>

    <div class="container">
        <EthnicityVoteChartMultiples
            ethnicType='sa'
            title='Conservatives now do better in South Asian-heavy ridings versus in general'
            subtitle="Conservative vote share (%) and South Asian (% of population) in the GTA's five most South Asian ridings"
        />
    </div>

    <div class="text">
        <p>
            Lorem ipsum, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
        <p>
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </div>

    <div class="container">
        <EthnicityVoteChartMultiples
            ethnicType='chn'
            title='Conservatives also do better in Chinese-heavy ridings, but more in Ontario'
            subtitle="Conservative vote share (%) and Chinese (% of population) in the GTA's five most Chinese ridings"
        />
    </div>

    <div class="text">
        <p>
            Lorem ipsum, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
        <p>
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
            Conservative shifts within South Asian and Chinese minorities – highlighting 2nd gen, but then broader discussion on why these communities are shifting right/who in them (from research + prior reporting). Note Mainstreet Research polling.
        </p>
    </div>

    <div class="text">
        <h2>Conclusion</h2>
        <p>
            Discuss key factors we didn’t go into as much: income, turnout, disenfranchised
        </p>

        <p>
            Conclusion: why is this happening, what does it mean?
        </p>
    </div>

    <div class="text">
        <br>
        <br>

        <div class="footnotes">
            <h3>Data & Methods</h3>
        </div>
    </div>

    <div class="text">
        <div class="footnotes">
            <h3>Footnotes</h3>
        </div>
    </div>
</main>

<style>

</style>
