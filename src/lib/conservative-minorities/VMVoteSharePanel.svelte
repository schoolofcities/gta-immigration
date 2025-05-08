<script>
    import { onMount } from "svelte";
    import StaticGTARidingsMap from "./StaticGTARidingsMap.svelte";
    import { CENSUS_SHADES, PARTY_SHADES } from "../constants";

    // State variables
    let electionData = $state(null);
    let loading = $state(true);
    let error = $state(null);

    const mapConfigs = {
        'VM': {
            breaks: [10, 20, 30, 40, 50, 60],
            breakSuffix: '%',
            name: 'Visible Minority (% of population)',
            colours: CENSUS_SHADES.pct_vm,
        },
        'VoteShare': {
            breaks: [10, 20, 30, 40, 50, 60],
            breakSuffix: '%',
            name: 'Conservative Vote Share (%)',
            colours: PARTY_SHADES.cons1,
        },
    }

    onMount(async () => {
        try {
            const response = await fetch('/gta-immigration/data/elections/fed_stats_2025.geojson');
            if (!response.ok) throw new Error('Failed to load data');
            
            const geoJsonData = await response.json();
            electionData = geoJsonData.features;
            loading = false;
        } catch (err) {
            error = err.message;
            loading = false;
        }
    });
</script>

<div class="panel-container">
    {#if loading}
        <p>Loading data...</p>
    {:else if error}
        <p class="error">Error: {error}</p>
    {:else if electionData}
        <div class="maps-container">
            <StaticGTARidingsMap 
                mapData={electionData} 
                mapConfig={mapConfigs.VM} 
                dataKey="pct_vm" 
                year="2025" 
            />
            <StaticGTARidingsMap 
                mapData={electionData} 
                mapConfig={mapConfigs.VoteShare} 
                dataKey="cons1_pct" 
                year="2025" 
            />
        </div>
    {/if}
</div>

<style>
    .panel-container {
        width: 100%;
        display: flex;
        flex-direction: column;
    }
    .maps-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: center;
    }
    .error {
        color: red;
    }
</style>