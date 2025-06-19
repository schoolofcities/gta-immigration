<script>
    import TopSofC from '$lib/TopSofC.svelte';
    import ImmigrationMap from '$lib/suburbanization/ImmigrationMap.svelte';
    import LineGraphTime from '$lib/suburbanization/LineGraphTime.svelte';

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
        <h1>The Suburbanization of Immigration in the Greater Toronto Area</h1>
        <p>
            Aniket Kali,
            Serene Tan,
            Jeff Allen
            |
            June 2025
        </p>
    </div>

    <div class="text">
        <p>
            introduction...
        </p>
    </div>

    <div class="map-grid">
        <div class="map-outer-container">
            <ImmigrationMap curYear={1961} />
        </div>
        <div class="map-outer-container">
            <ImmigrationMap curYear={1981} />
        </div>
        <div class="map-outer-container">
            <ImmigrationMap curYear={2001} />
        </div>
        <div class="map-outer-container">
            <ImmigrationMap curYear={2021} />
        </div>
    </div>

    <div class="text">
        <h2>How do immigrants compare to the general population?</h2>
        <p>information...</p>
    </div>

    <LineGraphTime />

    <!-- Chart multiples comparing distribution of immigrants/non-immigrants -->
    
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
    /* Default styles for the container and divs */
    .map-grid {
        margin: 0 auto;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        max-width: 1200px;
        gap: 20px;
    }

    .map-outer-container {
        width: 100%; /* Default to 100% width on mobile */
        box-sizing: border-box;
        margin-top: 0px;
        margin-bottom: 0px;
    }

    /* Media query for larger screens */
    @media (min-width: 768px) {
        .map-outer-container {
            width: calc(50% - 10px); /* Two per row with gap */
        }
    }
</style>
