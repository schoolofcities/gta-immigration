<script>
    import { PARTIES_INFO, PARTY_COLOURS } from "../lib/constants.js";
    import * as d3 from 'd3';

    const parties = PARTIES_INFO.filter(party => party.name !== 'Reform/Alliance');

    // State variables
    let curRegion = $state("federal");
    let curScope = $state("gta");

    let curVoteShares = $state({
        "Liberals": [],
        "Conservatives": [],
        "New Democrats": []
    });
    let windowWidth = $state(window.innerWidth);
    
    window.addEventListener('resize', () => windowWidth = window.innerWidth);

    function handleRegionChange(event) {
        curRegion = event.target.value;
    }

    function handleScopeChange(event) {
        curScope = event.target.value;
    }

    // Function to load and process the CSV
    function loadVoteShares() {
        const csvPath = "/gta-immigration/data/elections_analysis/ed_top_5_imm_results.csv"; // Static path to the CSV file

        d3.csv(csvPath)
            .then((data) => {
                const newVoteShares = {
                    "Liberals": [],
                    "Conservatives": [],
                    "New Democrats": []
                };

                parties.forEach(party => {
                    // Filter rows based on curRegion and current party
                    const filteredData = data.filter(
                        (row) => row.region === curRegion && row.party === party.tag
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

                    newVoteShares[party.name] = result;
                });

                curVoteShares = newVoteShares;
            })
            .catch((error) => {
                console.error('Error parsing CSV:', error);
            });
    }

    function drawGraph() {
        const svg = d3.select("#vote-share-graph");
        svg.selectAll("*").remove();

        const containerWidth = svg.node().parentElement.getBoundingClientRect().width || 700;
        const margin = { 
            top: 20, 
            right: containerWidth <= 700 ? 40 : 30, // Increase right margin for smaller screens
            bottom: 50, 
            left: 60 
        };
        const width = Math.min(containerWidth, 700) - margin.left - margin.right;
        const height = 400 - margin.top - margin.bottom;

        svg.attr("width", width + margin.left + margin.right)
           .attr("height", height + margin.top + margin.bottom);

        const g = svg.append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        // Get all years from all parties' data
        const allYears = [];
        Object.values(curVoteShares).forEach(partyData => {
            partyData.forEach(item => {
                if (!allYears.includes(item[0])) {
                    allYears.push(item[0]);
                }
            });
        });
        allYears.sort();

        const x = d3.scalePoint()
            .domain(allYears)
            .range([0, width]);

        const y = d3.scaleLinear()
            .domain([-25, 35])
            .range([height, 0]);

        // Modified x-axis
        g.append("g")
            .attr("transform", `translate(0,${height})`)
            .call(d3.axisBottom(x).tickFormat(d3.format("d")))
            .selectAll("text")
            .style("text-anchor", containerWidth <= 700 ? "end" : "middle")
            .attr("dx", containerWidth <= 700 ? "-0.8em" : "0")
            .attr("dy", containerWidth <= 700 ? "0.15em" : "0.71em")
            .attr("transform", containerWidth <= 700 ? "rotate(-45)" : "rotate(0)");

        // Year label
        g.append("text")
            .attr("fill", "#000")
            .attr("x", width / 2)
            .attr("y", height + (containerWidth <= 700 ? 45 : 40))
            .attr("text-anchor", "middle")
            .style("font-size", "11px")
            .text("Election year");

        // Modified y-axis with ticks every 10 units
        g.append("g")
            .call(d3.axisLeft(y).ticks(6)) // This will create ticks at -20, -10, 0, 10, 20, 30
            .append("text")
            .attr("fill", "#000")
            .attr("transform", "rotate(-90)")
            .attr("y", -50)
            .attr("x", -height / 2)
            .attr("dy", "0.71em")
            .attr("text-anchor", "middle")
            .style("font-size", "11px")
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

        // Add arrowhead definition
        svg.append("defs").append("marker")
            .attr("id", "arrowhead")
            .attr("viewBox", "0 -5 10 10")
            .attr("refX", 5)
            .attr("refY", 0)
            .attr("markerWidth", 6)
            .attr("markerHeight", 6)
            .attr("orient", "auto")
            .append("path")
            .attr("d", "M0,-5L10,0L0,5")
            .attr("fill", "black");

        // Position arrows based on screen width
        const arrowX = windowWidth <= 700 ? 10 : 20;
        const lineHeight = 12; // Height between text lines
        const textOffset = windowWidth <= 700 ? 3 : 5; // Smaller offset on mobile

        // Add up arrow (Overperforming)
        g.append("line")
            .attr("x1", arrowX)
            .attr("x2", arrowX)
            .attr("y1", y(5))
            .attr("y2", y(30))
            .attr("stroke", "black")
            .attr("stroke-width", 1)
            .attr("marker-end", "url(#arrowhead)");

        // Overperforming label - line 1
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", y(28))
            .attr("dy", "0")
            .style("font-size", "10px")
            .text("More votes in");
        
        // Overperforming label - line 2
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", y(28))
            .attr("dy", lineHeight + "px")
            .style("font-size", "10px")
            .text("high-immigrant ridings");

        // Add down arrow (Underperforming)
        g.append("line")
            .attr("x1", arrowX)
            .attr("x2", arrowX)
            .attr("y1", y(-5))
            .attr("y2", y(-20))
            .attr("stroke", "black")
            .attr("stroke-width", 1)
            .attr("marker-end", "url(#arrowhead)");

        // Underperforming label - line 1
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", y(-18))
            .attr("dy", "0")
            .style("font-size", "10px")
            .text("Less votes in");
        
        // Underperforming label - line 2
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", y(-18))
            .attr("dy", lineHeight + "px")
            .style("font-size", "10px")
            .text("high-immigrant ridings");

        const line = d3.line()
            .x(d => x(d[0]))
            .y(d => y(d[1] - d[2]))
            .curve(d3.curveMonotoneX);

        // Draw lines and dots for each party
        parties.forEach(party => {
            const partyData = curVoteShares[party.name];
            if (!partyData || partyData.length === 0) return;

            g.append("path")
                .datum(partyData)
                .attr("fill", "none")
                .attr("stroke", PARTY_COLOURS[party.tag])
                .attr("stroke-width", 1.5)
                .attr("stroke-dasharray", "3,3")
                .attr("d", line);

            g.selectAll(`dot-${party.tag}`)
                .data(partyData)
                .enter().append("circle")
                .attr("r", 3.5)
                .attr("cx", d => x(d[0]))
                .attr("cy", d => y(d[1] - d[2]))
                .attr("fill", PARTY_COLOURS[party.tag]);
        });
    }

    $effect(() => {
        curVoteShares;
        windowWidth;
        drawGraph();
    });

    $effect(() => {
        curRegion;
        curScope;
        loadVoteShares();
    });
</script>

<div class="sentence-controls">
    <p>
        I want to see vote share difference for
        <select onchange={handleRegionChange} class="inline-select">
            <option value="federal" selected>federal</option>
            <option value="ontario">ontario</option>
        </select>
        elections in the
        <select onchange={handleScopeChange} class="inline-select">
            <option value="gta" selected>GTA</option>
            <option value="full">full</option>
        </select>
        {curScope === 'gta' ? 'only' : 'results'}.
    </p>
</div>

<svg id="vote-share-graph" height="400"></svg>

<style>
    svg {
        max-width: 100%;
    }
</style>