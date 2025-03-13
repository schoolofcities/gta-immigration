<script>
    import { onMount } from "svelte";
    import { PARTY_COLOURS } from "../lib/constants.js";
    import * as d3 from 'd3';

    const partyTagMap = {
        "Liberals": "lib_pct",
        "Conservatives": "cons1_pct",
        "New Democrats": "ndp_pct"
    };
    const parties = ["Liberals", "Conservatives", "New Democrats"];

    let region = $state("fed");
    let curParties = $state([]);
    let curCorrs = $state({
        "Liberals": [],  // contains elements of the form [year, corr]
        "Conservatives": [],
        "New Democrats": [],
    });

    let svg; // Reference to the SVG element

    // Function to handle region change
    function handleRegionChange(event) {
        region = event.target.value;
        updateCorrelations();
    }

    // Function to toggle a party on/off
    function toggleParty(party) {
        if (curParties.includes(party)) {
            curParties = curParties.filter(p => p !== party);
        } else {
            curParties = [...curParties, party];
        }
        drawGraph(); // Redraw the graph when parties change
    }

    // Function to update correlations based on the selected region
    function updateCorrelations() {
        d3.csv('/data/elections_analysis/ed_corrs.csv').then(data => {
            const regionFilter = region === 'fed' ? 'federal' : 'ontario';
            const filteredData = data.filter(row => row.region === regionFilter);

            // Update the curCorrs state variable
            curCorrs = {
                "Liberals": filteredData.map(row => [parseInt(row.year), parseFloat(row.corr_pct_imm_lib)]),
                "Conservatives": filteredData.map(row => [parseInt(row.year), parseFloat(row.corr_pct_imm_cons1)]),
                "New Democrats": filteredData.map(row => [parseInt(row.year), parseFloat(row.corr_pct_imm_ndp)]),
            };
            drawGraph(); // Redraw the graph with the new data
        }).catch(error => {
            console.error('Error loading or processing CSV data:', error);
        });
    }

    // Function to draw the line graph
    function drawGraph() {
        // Clear the existing SVG content
        d3.select("#graph").selectAll("*").remove();

        // Set up SVG dimensions
        const width = 600;
        const height = 400;
        const margin = { top: 20, right: 30, bottom: 30, left: 40 };

        // Create the SVG container
        svg = d3.select("#graph")
            .attr("width", width)
            .attr("height", height);

        // Get all unique years from curCorrs
        const allYears = [...new Set(Object.values(curCorrs).flatMap(data => data.map(d => d[0])))];

        // Create scales
        const xScale = d3.scalePoint()
            .domain(allYears) // Use all available years
            .range([margin.left, width - margin.right]);

        const yScale = d3.scaleLinear()
            .domain([-1, 1]) // Correlation ranges from -1 to 1
            .range([height - margin.bottom, margin.top]);

        // Create axes
        const xAxis = d3.axisBottom(xScale).tickFormat(d3.format("d")); // Format years as integers
        const yAxis = d3.axisLeft(yScale);

        svg.append("g")
            .attr("transform", `translate(0,${height - margin.bottom})`)
            .call(xAxis);

        svg.append("g")
            .attr("transform", `translate(${margin.left},0)`)
            .call(yAxis);

        // Define a line generator
        const line = d3.line()
            .x(d => xScale(d[0]))
            .y(d => yScale(d[1]));

        // Draw lines and dots for each selected party
        curParties.forEach(party => {
            const data = curCorrs[party];
            if (!data) return;

            // Draw the line
            svg.append("path")
                .datum(data)
                .attr("fill", "none")
                .attr("stroke", PARTY_COLOURS[partyTagMap[party]] || "black") // Fallback to black if color is missing
                .attr("stroke-width", 2)
                .attr("d", line);

            // Draw dots for each data point
            svg.selectAll(`.dot-${party}`)
                .data(data)
                .enter()
                .append("circle")
                .attr("class", `dot-${party}`)
                .attr("cx", d => xScale(d[0]))
                .attr("cy", d => yScale(d[1]))
                .attr("r", 4)
                .attr("fill", PARTY_COLOURS[partyTagMap[party]] || "black"); // Fallback to black if color is missing
        });
    }

    // Initialize the graph on mount
    onMount(() => {
        updateCorrelations();
    });
</script>

<div>
    <select onchange={handleRegionChange}>
        <option value="fed" selected>Federal</option>
        <option value="ont-ed">Ontario</option>
    </select>
    {#each parties as party}
        <button 
            onclick={() => toggleParty(party)} 
            class:active={curParties.includes(party)}
        >
            {party}
        </button>
    {/each}
</div>

<!-- SVG container for the graph -->
<svg id="graph"></svg>

<style>
    select {
        width: 100%;
        margin-bottom: 10px;
    }

    button {
        background-color: gray;
        color: white;
        margin-right: 10px;
        padding: 10px;
        border: none;
        cursor: pointer;
    }
    button.active {
        background-color: blue;
    }
</style>