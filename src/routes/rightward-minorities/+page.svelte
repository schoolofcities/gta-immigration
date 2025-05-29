<script>
    import TopSofC from '$lib/TopSofC.svelte';
    import VMCorrelationDisplay from '$lib/rightward-minorities/VMCorrelationDisplay.svelte';
    import VMVoteSharePanel from '$lib/rightward-minorities/StaticVMVoteSharePanel.svelte';
    import Gen2ProfilesPanel from '$lib/rightward-minorities/Gen2ProfilesPanel.svelte';
    import EthnicityVoteChartMultiples from '$lib/rightward-minorities/EthnicityVoteChartMultiples.svelte';

    import '../../assets/global-styles.css';

    import Footnote from '$lib/Footnote.svelte';
    import Footnotes from '$lib/Footnotes.svelte';
    import { createFootnoteStore } from '$lib/footnoteUtils';

    const footnoteStore = createFootnoteStore();
    const { footnotes, addFootnote } = footnoteStore;

    const fns = [
        `hello *world*`
    ]
</script>

<svelte:head>
	<meta
		name="viewport"
		content="width=device-width, initial-scale=1, minimum-scale=1"
	/>

	<title>Rightward shifts amongst visible minorities in the Greater Toronto Area | School of Cities</title>

	<meta name="description" content="">
	<meta name="author" content="Emine Fidan Elcioglu">
    
	<meta property="og:title" content="Rightward shifts amongst visible minorities in the Greater Toronto Area" />
	<meta property="og:description" content="Visible minorities in the GTA have been shifting to the Conservatives" />
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://schoolofcities.github.io/gta-immigration/rightward-minorities" />
	<!-- <meta property="og:image" content="https://schoolofcities.github.io/gta-immigration/web-card-rightward-minorities.png" /> -->
	<meta property="og:locale" content="en_CA">

	<!-- <meta name="twitter:card" content="summary_large_image" /> -->
	<meta name="twitter:site" content="https://schoolofcities.github.io/gta-immigration/rightward-minorities" />
	<meta name="twitter:creator" content="@UofTCities" />
	<meta name="twitter:title" content="Rightward shifts amongst visible minorities in the Greater Toronto Area" />
	<meta name="twitter:description" content="Visible minorities in the GTA have been shifting to the Conservatives" />
	<!-- <meta name="twitter:image" content="https://schoolofcities.github.io/gta-immigration/web-card-rightward-minorities.png" />  -->
    
</svelte:head>

<main>
    <TopSofC/>

    <div class="title">
        <h1>Rightward shifts amongst visible minorities in the Greater Toronto Area</h1>
        <p>
            Writing & Research: 
            <a href='https://fidanelcioglu.com/' target='_blank'>Emine Fidan Elcioglu</a>
        </p>
        <p>
            Maps & Graphics:
            <a href='https://www.linkedin.com/in/aniket-k-8a8b9921b/' target='_blank'>Aniket Kali</a>,
            <a href='https://jamaps.github.io/' target='_blank'>Jeff Allen</a>
        </p>
        <p>
            Editing: 
            Felicity Heyworth, Aniket Kali
        </p>
        <p>
            June 2025
        </p>
    </div>

    <div class="text">
        <p>
            Lorem ipsum, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.<Footnote id={addFootnote(fns[0])} /> 
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
            title='Conservatives now do better in South Asian-heavy ridings'
            subtitle="Conservative vote share (%) and South Asian (% of population) in the GTA's five most South Asian ridings"
            subtitleGroup="South Asian"
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
            subtitleGroup="Chinese"
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
        <Footnotes footnotes={footnotes} />
    </div>
</main>

<style>

</style>
