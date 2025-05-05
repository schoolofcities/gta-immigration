<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import { PARTY_COLOURS, PARTIES_INFO } from "../constants.js";
    import SmallScatterPlot from '../SmallScatterPlot.svelte';

    // Configuration
    const elections = [
        // { year: 1963, region: "ontario" },
        // { year: 1967, region: "ontario" },
        // { year: 1971, region: "ontario" },
        // { year: 1975, region: "ontario" },
        // { year: 1977, region: "ontario" },
        // { year: 1981, region: "ontario" },
        { year: 1985, region: "ontario" },
        { year: 1987, region: "ontario" },
        { year: 1990, region: "ontario" },
        { year: 1995, region: "ontario" },
        { year: 1999, region: "ontario" },
        { year: 2003, region: "ontario" },
        { year: 2007, region: "ontario" },
        { year: 2011, region: "ontario" },
        { year: 2014, region: "ontario" },
        { year: 2018, region: "ontario" },
        { year: 2022, region: "ontario" },
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

<div class="plots-title">
    <h4>
        Ridings with more immigrants are increasingly voting Conservative
    </h4>
    <p>
        Correlation between immigrants (as % of population) and voting Conservative in Ontario provincial elections
    </p>
</div>
<div class="plots-container">
    {#each electionData as data, index}
        <SmallScatterPlot 
            points={data.points} 
            correlation={data.correlation} 
            year={data.year} 
            showArrows={false}
        />
    {/each}
</div>
  
<style>

    .plots-title {
        max-width: 700px;
        margin: 0 auto;
    }

    .plots-title p {
        margin-top: -25px;
        margin-bottom: -15px;
        font-family: RobotoRegular;
        font-size: 14.5px;
        line-height: 20px;
    }

    .plots-container {
        max-width: 701px;
        display: grid;
        grid-template-columns: repeat(6, 1fr);  /* 6 columns by default */
        gap: 17px;
        margin: 0 auto;
        margin-top: 24px;
    }

    @media (max-width: 700px) {
        .plots-title {
            margin-left: 15px;
            margin-right: 15px;
        }
        .plots-container {
            max-width: 340px;
            grid-template-columns: repeat(3, 1fr);  /* 3 columns when the screen is less than 700px */
        }
    }

</style>