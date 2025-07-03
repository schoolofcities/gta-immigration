<script>
    import TopSofC from '$lib/TopSofC.svelte';
    import ImmigrationMapContainer from '$lib/suburbanization/ImmigrationMapContainer.svelte';
    import LineGraphTime from '$lib/suburbanization/LineGraphTime.svelte';
    import StepGraphContainer from '$lib/suburbanization/StepGraphContainer.svelte';

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
            June 2025
        </p>
    </div>

    <div class="text">
        <p>
            introduction...
        </p>
    </div>

    <ImmigrationMapContainer />
    
    <div class="text">
        <h2>Why the move to the suburbs?</h2>
        <p>information...</p>
    </div>

    <LineGraphTime />

    <StepGraphContainer />
    
    <div class="text">
        <p>explanation...</p>
        <p>conclusion...</p>
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
