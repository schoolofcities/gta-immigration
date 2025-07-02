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
        <h2>How do immigrants compare to the general population?</h2>
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
