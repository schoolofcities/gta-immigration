<script>
    import { onMount } from "svelte";
    import { PARTY_COLOURS, PARTY_TAG_MAP } from "../lib/constants.js";
    import * as d3 from 'd3';

    const parties = [
        { name: "Liberals", tag: "lib" },
        { name: "Conservatives", tag: "cons1" },
        { name: "New Democrats", tag: "ndp" },
    ];

    // State variables
    let curRegion = $state("federal");
    let curParty = $state("lib");
    let curScope = $state("gta");
    let curVoteShares = $state([]); // To store the processed data

    // Function to handle curRegion change
    function handleRegionChange(event) {
        curRegion = event.target.value;
    }

    // Function to handle curParty change
    function handlePartyChange(event) {
        curParty = event.target.value;
    }

    // Function to handle curScope change
    function handleScopeChange(event) {
        curScope = event.target.value;
    }

    // Function to load and process the CSV
    function loadVoteShares() {
        const csvPath = "/data/elections_analysis/ed_top_5_imm_results.csv"; // Static path to the CSV file

        d3.csv(csvPath)
            .then((data) => {
                // Filter rows based on curRegion and curParty
                const filteredData = data.filter(
                    (row) => row.region === curRegion && row.party === curParty
                );

                // Group by year and extract the required columns
                const result = [];
                const years = new Set(filteredData.map((row) => row.year));

                years.forEach((year) => {
                    const yearData = filteredData.filter((row) => row.year === year);
                    yearData.forEach((row) => {
                        const firstElement = parseFloat(row.top_5_imm_pct); // Convert to number
                        const secondElement = curScope === 'gta' 
                            ? parseFloat(row.gta_pct) 
                            : parseFloat(row.full_pct); // Convert to number
                        if (!isNaN(firstElement) && !isNaN(secondElement)) {
                            result.push([parseFloat(year), firstElement, secondElement]);
                        }
                    });
                });

                // Save the result to curVoteShares 
                curVoteShares = result;
                // console.log($state.snapshot(curVoteShares));
            })
            .catch((error) => {
                console.error('Error parsing CSV:', error);
            });
    }

    // Function to draw the graph
    function drawGraph() {
        const svg = d3.select("#vote-share-graph");
        svg.selectAll("*").remove(); // Clear previous content

        const margin = { top: 20, right: 30, bottom: 50, left: 60 };
        const width = svg.node().getBoundingClientRect().width - margin.left - margin.right;
        const height = +svg.attr("height") - margin.top - margin.bottom;
        const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

        const x = d3.scalePoint()
            .domain(curVoteShares.map(d => d[0]))
            .range([0, width]);

        const y = d3.scaleLinear()
            .domain([-25, 35])
            .range([height, 0]);

        g.append("g")
            .attr("transform", `translate(0,${height})`)
            .call(d3.axisBottom(x).tickFormat(d3.format("d")))
            .append("text")
            .attr("fill", "#000")
            .attr("x", width / 2)
            .attr("y", 40)
            .attr("text-anchor", "middle")
            .text("Election year");

        g.append("g")
            .call(d3.axisLeft(y))
            .append("text")
            .attr("fill", "#000")
            .attr("transform", "rotate(-90)")
            .attr("y", -50)
            .attr("x", -height / 2)
            .attr("dy", "0.71em")
            .attr("text-anchor", "middle")
            .text("Vote share difference");

        // Add dotted black line at y = 0
        g.append("line")
            .attr("x1", 0)
            .attr("x2", width)
            .attr("y1", y(0))
            .attr("y2", y(0))
            .attr("stroke", "black")
            .attr("stroke-width", 1)
            .attr("stroke-dasharray", "4,4");

        const line = d3.line()
            .x(d => x(d[0]))
            .y(d => y(d[1] - d[2]))
            .curve(d3.curveMonotoneX);

        g.append("path")
            .datum(curVoteShares)
            .attr("fill", "none")
            .attr("stroke", PARTY_COLOURS[`${curParty}_pct`])
            .attr("stroke-width", 1.5)
            .attr("stroke-dasharray", "3,3")
            .attr("d", line);

        g.selectAll("dot")
            .data(curVoteShares)
            .enter().append("circle")
            .attr("r", 3.5)
            .attr("cx", d => x(d[0]))
            .attr("cy", d => y(d[1] - d[2]))
            .attr("fill", PARTY_COLOURS[`${curParty}_pct`]);
    }

    // Load the CSV when the component mounts or when state variables change
    $effect(() => {
        curRegion;
        curParty;
        curScope;

        // Call the function
        loadVoteShares();
    });

    // Redraw the graph whenever curVoteShares is updated
    $effect(() => {
        curVoteShares;
        drawGraph();
    });
</script>

<div>
    <select onchange={handleRegionChange}>
        <option value="federal" selected>Federal</option>
        <option value="ontario">Ontario</option>
    </select>

    <select onchange={handlePartyChange}>
        {#each parties as party}
            <option value={party.tag}>{party.name}</option>
        {/each}
    </select>

    <select onchange={handleScopeChange}>
        <option value="gta" selected>GTA</option>
        <option value="full">Full</option>
    </select>
</div>

<!-- {#if curVoteShares.length > 0}
    <div>
        <pre>{JSON.stringify(curVoteShares, null, 2)}</pre>
    </div>
{/if} -->

<!-- SVG container for the graph -->
<svg id="vote-share-graph" width="100%" height="400"></svg>

<style>
    select {
        width: 100%;
        margin-bottom: 10px;
    }
</style>