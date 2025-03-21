<script>
    import TopSofC from '$lib/TopSofC.svelte';
    import CensusVoteMaps from '$lib/CensusVoteMaps.svelte';
    import CorrelationDisplay from '$lib/CorrelationDisplay.svelte';
    import CorrelationTimeline from '$lib/CorrelationTimeline.svelte';
    import VoteShareCompare from '$lib/VoteShareCompare.svelte';
</script>

<main>

    <TopSofC/>
    <div class="title">
        <!-- <h1>Immigrant Political Shifts</h1> -->
        <h1>Changes in immigrant voting patterns in the Greater Toronto Area</h1>
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
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
            At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. 
        </p>
    </div>

    <div class="text">
        <h2>How do ridings compare?</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>
    <!-- Dual panel of constituency maps: vote share & immigrant percent -->
    <CensusVoteMaps />

    <br/>
    <br/>

    <div class="text">
        <h2>Does party vote share correspond to where immigrants live?</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>
    
    <!-- View graph of all data points and correlation year (choose party+year) -->
    <div class="container">
        <CorrelationDisplay />
    </div>

    <div class="text">
        <p>tLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>

    <!-- View trend line of correlation (choose party) -->
    <div class="container">
        <CorrelationTimeline />
    </div>

    <div class="text">
        <h2>How does party vote compare in immigrant dominated ridings?</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>

    <!-- View trend line mean vote share (choose party) for high immigrant ridings -->
    <div class="container">
        <VoteShareCompare />
    </div>

    <div class="text">
        <h2>Data & Methods</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>
</main>

<style>
</style>
