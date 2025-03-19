<script>
    import CensusVoteMaps from '$lib/CensusVoteMaps.svelte';
    import CorrelationDisplay from '$lib/CorrelationDisplay.svelte';
    import CorrelationTimeline from '$lib/CorrelationTimeline.svelte';
    import VoteShareCompare from '$lib/VoteShareCompare.svelte';
</script>

<main>
    <div class="title">
        <h1>Immigrant Political Shifts</h1>
        <h2>Changes in immigrant vote patterns in the GTA</h2>
        <p>
            Aniket Kali,
            Serene Tan,
            Jeff Allen
            <br />
            <br />
            March 2025
        </p>
    </div>

    <div class="text">
        <h2>How do ridings compare?</h2>
        <p>text here</p>
    </div>
    <!-- Dual panel of constituency maps: vote share & immigrant percent -->
    <CensusVoteMaps />

    <div class="text">
        <h2>Does party vote share correspond to where immigrants live?</h2>
        <p>text here</p>
    </div>
    
    <!-- View graph of all data points and correlation year (choose party+year) -->
    <div class="container">
        <CorrelationDisplay />
    </div>

    <div class="text">
        <p>text here</p>
    </div>

    <!-- View trend line of correlation (choose party) -->
    <div class="container">
        <CorrelationTimeline />
    </div>

    <div class="text">
        <h2>How does party vote compare in immigrant dominated ridings?</h2>
        <p>text here</p>
    </div>

    <!-- View trend line mean vote share (choose party) for high immigrant ridings -->
    <div class="container">
        <VoteShareCompare />
    </div>

    <div class="text">
        <h2>Data & Methods</h2>
        <p>text here</p>
    </div>
</main>

<style>
</style>
