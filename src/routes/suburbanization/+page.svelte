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

    <!-- <ImmigrationMap curYear={1961} /> -->
    <!-- <ImmigrationMap curYear={1981} /> -->
    <!-- <ImmigrationMap curYear={2001} /> -->
    <ImmigrationMap curYear={2021} />

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
</style>
