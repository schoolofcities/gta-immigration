<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import { PARTY_COLOURS, PARTIES_INFO } from "./constants.js";
    import SmallScatterPlot from './SmallScatterPlot.svelte';

    // Configuration
    const elections = [
        { year: 1999, region: "ontario" },
        { year: 2014, region: "ontario" },
        { year: 2025, region: "ontario" }
    ];
    const party = "cons1";
    const partyPropertyTag = PARTIES_INFO.find(p => p.tag === party).propertyTag;

    // Data storage
    let electionData = $state([]);

    onMount(() => {
        loadElectionData();
    });

    function loadElectionData() {
        const promises = elections.map(election => {
            return Promise.all([
                d3.json(`/gta-immigration/data/elections/ont-ed_stats_${election.year}.geojson`),
                d3.csv(`/gta-immigration/data/elections_analysis/ed_corrs.csv`)
            ]).then(([geoJsonData, corrData]) => {
                const row = corrData.find(d => 
                    d.year === election.year.toString() && d.region === election.region
                );
                
                const points = geoJsonData.features.map(d => ({
                    x: d.properties.pct_imm,
                    y: d.properties[partyPropertyTag],
                    geoname: d.properties.geoname
                }));

                return {
                    year: election.year,
                    points,
                    correlation: row ? parseFloat(row[`corr_pct_imm_${party}`]) : 0,
                };
            });
        });

        Promise.all(promises).then(results => {
            electionData = results.sort((a, b) => a.year - b.year);
        }).catch(error => {
            console.error("Error loading data:", error);
        });
    }
</script>

<div class="plots-container">
    {#each electionData as data, index}
        <SmallScatterPlot 
            points={data.points} 
            correlation={data.correlation} 
            year={data.year} 
            showArrows={index === 0}
        />
    {/each}
</div>
  
<style>
    .plots-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        max-width: 960px;
        margin: 0 auto;
        margin-top: 24px;
    }   
  
    @media (max-width: 980px) {
        .plots-container {
            flex-direction: column;
            align-items: center;
        }
    }
</style>