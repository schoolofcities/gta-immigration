<script>
    import TopSofC from '$lib/TopSofC.svelte';
    import ImmigrationMap from '$lib/ImmigrationMap.svelte';
</script>

<main>
    <TopSofC/>
    <div class="title">
        <h1>Changes in Immigrant Settlement Patterns in the Greater Toronto Area</h1>
        <p>
            Aniket Kali,
            Serene Tan,
            Jeff Allen
            <br />
            <br />
            April 2025
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

    <!-- LINE GRAPH -->

    <div class="text">
        <p>explanation...</p>
        <p>conclusion...</p>
    </div>

    <div class="text">
        <h2>Data & Methods</h2>
        <p>information...</p>
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
        margin-top: 10px;
        margin-bottom: 20px;
    }

    /* Media query for larger screens */
    @media (min-width: 768px) {
        .map-outer-container {
            width: calc(50% - 10px); /* Two per row with gap */
        }
    }
</style>
