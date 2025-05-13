<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import { PARTY_COLOURS, PARTIES_INFO } from "../constants.js";
    import SmallScatterPlot from '../SmallScatterPlot.svelte';

    // Configuration
    const ontElections = [
        { year: 1999, region: "ontario" },
        { year: 2003, region: "ontario" },
        { year: 2007, region: "ontario" },
        { year: 2011, region: "ontario" },
        { year: 2014, region: "ontario" },
        { year: 2018, region: "ontario" },
        { year: 2022, region: "ontario" },
        { year: 2025, region: "ontario" },
    ]

    const fedElections = [
        // { year: 1997, region: "federal" },
        // { year: 2000, region: "federal" },
        { year: 2004, region: "federal" },
        { year: 2006, region: "federal" },
        { year: 2008, region: "federal" },
        { year: 2011, region: "federal" },
        { year: 2015, region: "federal" },
        { year: 2019, region: "federal" },
        { year: 2021, region: "federal" },
        { year: 2025, region: "federal" },
    ]

    const party = "cons1";
    const partyPropertyTag = PARTIES_INFO.find(p => p.tag === party).propertyTag;

    const height = 75;
    const plotWidth = 75;
    const colorStart = -0.3;
    const colorEnd = 0.15;

    // State variables
    let ontElectionData = $state([]);
    let fedElectionData = $state([]);

    onMount(() => {
        loadElectionData(ontElections, 'ontario');
        loadElectionData(fedElections, 'federal');
    });

    // $effect(() => {
    //     console.log($state.snapshot(ontElectionData));
    //     console.log($state.snapshot(fedElectionData));
    // })

    function loadElectionData(elections, region) {
        const promises = elections.map(election => {
            const dataPath = region === 'ontario' ? `/gta-immigration/data/elections/ont-ed_stats_${election.year}.geojson` : `/gta-immigration/data/elections/fed_stats_${election.year}.geojson`

            return Promise.all([
                d3.json(dataPath),
                d3.csv(`/gta-immigration/data/elections_analysis/ed_corrs_vm.csv`)
            ]).then(([geoJsonData, corrData]) => {
                const row = corrData.find(d => 
                    d.year === election.year.toString() && d.region === election.region
                );
                
                const points = geoJsonData.features.map(d => ({
                    x: d.properties.pct_vm,
                    y: d.properties[partyPropertyTag],
                    geoname: d.properties.geoname
                }));

                return {
                    year: election.year,
                    points,
                    correlation: row ? parseFloat(row[`corr_pct_vm_${party}`]) : 0,
                };
            });
        });

        Promise.all(promises).then(results => {
            if (region === 'ontario') {
                ontElectionData = results.sort((a, b) => a.year - b.year);
            } else {
                fedElectionData = results.sort((a, b) => a.year - b.year);
            }
        }).catch(error => {
            console.error("Error loading data:", error);
        });
    }
</script>

<div class="plots-title">
    <h4>
        Ridings with more visible minorities are increasingly voting Conservative
    </h4>
    <p>
        Correlation between visible minorities (as % of population) and voting Conservative in Ontario elections
    </p>
</div>
<div class="plots-container">
    {#each ontElectionData as data, index}
        <SmallScatterPlot 
            points={data.points} 
            correlation={data.correlation} 
            year={data.year} 
            xEnd={100}
            height={height}
            plotWidth={plotWidth}
            colorStart={colorStart}
            colorEnd={colorEnd}
        />
    {/each}
</div>
<div class="plots-title">
    <h4></h4>
    <p>
        Correlation between visible minorities (as % of population) and voting Conservative in federal elections
    </p>
</div>
<div class="plots-container">
    {#each fedElectionData as data, index}
        <SmallScatterPlot 
            points={data.points} 
            correlation={data.correlation} 
            year={data.year} 
            xEnd={100}
            height={height}
            plotWidth={plotWidth}
            colorStart={colorStart}
            colorEnd={colorEnd}
        />
    {/each}
</div>

<style>
    .plots-container {
        max-width: 701px;
        display: grid;
        grid-template-columns: repeat(8, 1fr);  /* 6 columns by default */
        gap: 12px;
        margin: 0 auto;
        margin-top: 24px;
    }

    @media (max-width: 700px) {
        .plots-container {
            max-width: 340px;
            grid-template-columns: repeat(4, 1fr);  /* 3 columns when the screen is less than 700px */
        }
    }

</style>