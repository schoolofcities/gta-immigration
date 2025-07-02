<script>
    import ImmigrationMap from '$lib/suburbanization/ImmigrationMap.svelte';
</script>

<div class="container plots-title">
    <h4>
        Downtown Toronto used to be the hub of the region's immigrants, but now, it's the suburbs
    </h4>
    <p>
        Percentage of population that are immigrants per census tract in 20-year intervals
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

<style>
    /* Default styles for the container and divs */
    .map-grid {
        margin: 0 auto;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        max-width: 1200px;
        gap: 20px;
        margin-top: 25px;
    }

    .map-outer-container {
        width: 100%; /* Default to 100% width on mobile */
        box-sizing: border-box;
    }

    /* Media query for larger screens */
    @media (min-width: 768px) {
        .map-outer-container {
            width: calc(50% - 10px); /* Two per row with gap */
        }
    }
</style>