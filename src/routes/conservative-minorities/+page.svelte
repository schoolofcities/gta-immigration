<script>
    import TopSofC from '$lib/TopSofC.svelte';
    import VMCorrelationDisplay from '$lib/conservative-minorities/VMCorrelationDisplay.svelte';
    import VMVoteSharePanel from '$lib/conservative-minorities/VMVoteSharePanel.svelte';
    import Gen2ProfilesPanel from '$lib/conservative-minorities/Gen2ProfilesPanel.svelte';

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
        <p>
            VIS: Correlation between %VM and %Cons over time, Ontario (1999-2025) and federal (1997-2025), showing a clear trend
        </p>

        <VMCorrelationDisplay />
    </div>

    <div class="text">
        <p>
            Background, historical context, summary of what is driving these changes now
        </p>
    </div>

    <div>
        <p>
            VIS: Map of %Cons vote share change in the last (federal) election in GTA ridings
        </p>
        <p>
            VIS: Map of %VM in GTA ridings
        </p>

        <VMVoteSharePanel />
    </div>

    <div class="text">
        <p>
            Discussion of 2nd gen visible minorities shifting right
        </p>
    </div>

    <div class="container">
        <p>
            VIS*4: Riding, %VM, %Cons (federal and Ontario) – 2-3 sentence quote from qualitative data
        </p>

        <Gen2ProfilesPanel />
    </div>

    <div class="text">
        <p>
            Summarize key conclusions on 2nd gens
        </p>
    </div>

    <div class="container">
        <p>
            VIS: %Cons (federal and Ontario) ranked by %VM South Asian (maybe vs. ~2000)
        </p>
        <p>
            VIS: %Cons (federal and Ontario) ranked by %VM Chinese (maybe vs. ~2000)
        </p>
    </div>

    <div class="text">
        <p>
            Conservative shifts within South Asian and Chinese minorities – highlighting 2nd gen, but then broader discussion on why these communities are shifting right/who in them (from research + prior reporting). Note Mainstreet Research polling.
        </p>

        <p>
            Discuss key factors we didn’t go into as much: income, turnout, disenfranchised
        </p>

        <p>
            Conclusion: why is this happening, what does it mean?
        </p>
    </div>
</main>

<style>

</style>
