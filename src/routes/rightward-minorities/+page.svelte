<script>
    import TopSofC from '$lib/TopSofC.svelte';
    import VMCorrelationDisplay from '$lib/rightward-minorities/VMCorrelationDisplay.svelte';
    import VMVoteSharePanel from '$lib/rightward-minorities/VMVoteSharePanel.svelte';
    import Gen2ProfilesPanel from '$lib/rightward-minorities/Gen2ProfilesPanel.svelte';
    import EthnicityVoteChartMultiples from '$lib/rightward-minorities/EthnicityVoteChartMultiples.svelte';

    import '../../assets/global-styles.css';
</script>

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
            Introduction
        </p>
    </div>

    <div class="container">
        <VMCorrelationDisplay />
    </div>

    <div class="text">
        <p>
            Continued introduction
        </p>
    </div>

    <div class="text">
        <h2>What is happening?</h2>
        <p>
            Background, historical context, summary of what is driving these changes now
        </p>
    </div>

    <div>
        <VMVoteSharePanel />
    </div>

    <div class="text">
        <p>
            Tie in to recent elections
        </p>
    </div>

    <div class="text">
        <h2>2nd Generation Immigrants</h2>
        <p>
            Discussion of 2nd gen visible minorities shifting right - introduce the main study, qualitative data, etc.
        </p>
    </div>

    <div class="container">
        <Gen2ProfilesPanel />
    </div>

    <div class="text">
        <p>
            Summarize key conclusions on 2nd gens
        </p>
    </div>

    <div class="text">
        <h2>South Asian Canadians and Chinese Canadians</h2>
        <p>
            Summary of these groups in particular
        </p>
    </div>

    <div class="container">
        <EthnicityVoteChartMultiples />
    </div>

    <div class="text">
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
