<script>
    import { onMount } from "svelte";
    import StaticGTARidingsMap from "./StaticGTARidingsMap.svelte";
    import { CENSUS_SHADES, PARTY_SHADES, OTHER_SHADES } from "../constants";

    // State variables
    let electionData = $state(null);

    const mapConfigs = {
        'VM': {
            breaks: [10, 20, 30, 40, 50, 60],
            breakPrefix: '',
            breakSuffix: '%',
            name: 'Visible Minority (% of population)',
            colours: CENSUS_SHADES.pct_vm,
        },
        'VoteShare': {
            breaks: [10, 20, 30, 40, 50, 60],
            breakPrefix: '',
            breakSuffix: '%',
            name: 'Conservative Vote Share (%)',
            colours: PARTY_SHADES.cons1,
        },
        'VoteShareChange': {
            breaks: [5, 10, 15, 20],
            breakPrefix: '+',
            breakSuffix: '%',
            name: 'Change in Conservative Vote Share, 2021-2025 (%)',
            colours: OTHER_SHADES.cons_change,
        }
    }

    onMount(async () => {
        try {
            const response = await fetch('/gta-immigration/data/elections/fed_stats_2025.geojson');
            if (!response.ok) throw new Error('Failed to load data');
            
            const geoJsonData = await response.json();
            electionData = geoJsonData.features;
        } catch (err) {
            console.log(err.message);
        }
    });
</script>

<div class="panel-container">
    {#if electionData}
        <div class="container plots-title">
            <h4>
                Conservatives made major gains in the visible minority-heavy GTA suburbs
            </h4>
            <p>
                Many ridings saw gains far in excess of their national vote share change of 7.6%. In Brampton West, a riding where 88% of the population are visible minorities, the Conservatives gained 22% and flipped the seat - their 4th largest gain in the country.
            </p>
        </div>
        <div class="maps-container">
            <div class="map-section">
                <StaticGTARidingsMap 
                    mapData={electionData} 
                    mapConfig={mapConfigs.VM} 
                    dataKey="pct_vm" 
                    year="2025" 
                />
            </div>
            <div class="map-section">
                <StaticGTARidingsMap 
                    mapData={electionData} 
                    mapConfig={mapConfigs.VoteShareChange} 
                    dataKey="cons_pct_change" 
                    year="2025" 
                />
            </div>
        </div>
    {/if}
</div>

<style>
    .panel-container {
        width: 100%;
    }

    .maps-container {
        max-width: 1200px;
        display: flex;
        gap: 20px;
        margin: 0 auto;
        width: calc(100% - 20px);
        margin-top: 25px;
    }

    .map-section {
        flex: 1;
        min-width: 0;
    }

    @media (max-width: 900px) {
        .maps-container {
            flex-direction: column;
            gap: 20px;
            margin: 10px;
            width: calc(100% - 20px);
        }

        .map-section {
            width: 100%;
        }
    }

    .error {
        color: red;
    }
</style>