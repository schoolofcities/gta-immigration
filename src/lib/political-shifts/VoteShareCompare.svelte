<script>
    import { PARTIES_INFO, PARTY_COLOURS } from "../constants.js";
    import * as d3 from 'd3';

    const parties = PARTIES_INFO.filter(party => party.name !== 'Reform/Alliance');

    // State variables
    let curRegion = $state("ontario");
    let curScope = $state("full");
    let curVoteShares = $state({
        "Liberals": [],
        "Conservatives": [],
        "New Democrats": []
    });
    let windowWidth = $state(400);
    

    function handleRegionChange(event) {
        curRegion = event.target.value;
    }

    function handleScopeChange(event) {
        curScope = event.target.value;
    }

    function setLabelPos(partyName, region) {
        let dx;
        let dy;
        let textAnchor = "start";

        if (region === 'ontario') {
            if (partyName === "Liberals") {
                dx = 5; // to the right
                dy = 5; // slightly below
            } else if (partyName === "New Democrats") {
                dx = 5; // to the right
                dy = 5; // slightly below
            } else if (partyName === "Conservatives") {
                dx = 5; // to the right
                dy = 10; // slightly below
            }
        } else { // federal
            if (partyName === "Liberals") {
                dx = 5; // to the right
                dy = 10; // slightly below
            } else if (partyName === "New Democrats") {
                dx = 5; // to the right
                dy = -5; // slightly above
            } else if (partyName === "Conservatives") {
                dx = 5; // to the right
                dy = 10; // slightly below
            }
        }

        return { dx, dy, textAnchor };
    }

    // Function to load and process the CSV
    function loadVoteShares() {
        const csvPath = "/gta-immigration/data/elections_analysis/ed_top_5_imm_results.csv";

        d3.csv(csvPath)
            .then((data) => {
                const newVoteShares = {
                    "Liberals": [],
                    "Conservatives": [],
                    "New Democrats": []
                };

                parties.forEach(party => {
                    const filteredData = data.filter(
                        (row) => row.region === curRegion && row.party === party.tag
                    );

                    const result = [];
                    const years = new Set(filteredData.map((row) => row.year));

                    years.forEach((year) => {
                        const yearData = filteredData.filter((row) => row.year === year);
                        yearData.forEach((row) => {
                            const firstElement = parseFloat(row.top_5_imm_pct);
                            const secondElement = curScope === 'gta' 
                                ? parseFloat(row.gta_pct) 
                                : parseFloat(row.full_pct);
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
            right: containerWidth <= 700 ? 40 : 30,
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

        const xScale = d3.scalePoint()
            .domain(allYears)
            .range([0, width]);

        const yScale = d3.scaleLinear()
            .domain([-30, 33])
            .range([height, 0]);

        // Add x-axis grid lines
        g.selectAll(".x-grid-line")
            .data(allYears)
            .enter()
            .append("line")
            .attr("class", "x-grid-line")
            .attr("x1", d => xScale(d))
            .attr("x2", d => xScale(d))
            .attr("y1", 0)
            .attr("y2", height)
            .attr("stroke", "#d3d3d3")
            .attr("stroke-width", 0.5);

        // Add y-axis grid lines
        g.selectAll(".y-grid-line")
            .data(d3.range(-30, 31, 10))
            .enter()
            .append("line")
            .attr("class", "y-grid-line")
            .attr("x1", 0)
            .attr("x2", width)
            .attr("y1", d => yScale(d))
            .attr("y2", d => yScale(d))
            .attr("stroke", "#d3d3d3")
            .attr("stroke-width", 0.5);

        // Modified x-axis with proper mobile rotation and alignment
        const xAxis = g.append("g")
            .attr("transform", `translate(0,${height})`)
            .call(d3.axisBottom(xScale)
                .tickFormat(d3.format("d"))
                .tickSize(0)); // Keep tick lines invisible
        
        xAxis.select(".domain").remove();
        
        // Add subtle tick marks that match grid lines (only on mobile)
        if (containerWidth <= 700) {
            xAxis.selectAll(".tick")
                .append("line")
                .attr("class", "x-tick-line")
                .attr("x1", 0)
                .attr("x2", 0)
                .attr("y1", 0)
                .attr("y2", 6) // Short tick length
                .attr("stroke", "#d3d3d3") // Same as grid lines
                .attr("stroke-width", 0.5);
        }

        // Style x-axis labels with adjusted positioning
        xAxis.selectAll("text")
            .style("font-size", "11px")
            .style("font-family", "RobotoRegular")
            .style("text-anchor", containerWidth <= 700 ? "end" : "middle")
            .attr("dx", containerWidth <= 700 ? "-0.5em" : "0") // Reduced from -0.8em
            .attr("dy", containerWidth <= 700 ? "1.2em" : "0.71em") // Adjusted vertical position
            .attr("transform", containerWidth <= 700 ? "rotate(-45)" : "rotate(0)");

        // Modified y-axis
        const yAxis = g.append("g")
            .attr("transform", "translate(-5,0)") 
            .call(d3.axisLeft(yScale)
                .ticks(6)
                .tickFormat(d => d + "%")
                .tickSize(0))
            .select(".domain").remove();

        // Style y-axis tick labels
        yAxis.selectAll("text")
            .attr("fill", "#666")
            .style("font-size", "11px")
            .style("font-family", "RobotoRegular");

        // Add y-axis label
        g.append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", -50)
            .attr("x", -height / 2)
            .attr("dy", "0.71em")
            .attr("text-anchor", "middle")
            .style("font-size", "13px")
            .style("font-family", "RobotoRegular")
            .text("Vote share difference");

        // Add dotted black line at y = 0
        g.append("line")
            .attr("x1", 0)
            .attr("x2", width)
            .attr("y1", yScale(0))
            .attr("y2", yScale(0))
            .attr("stroke", "#D0D1C9")
            .attr("stroke-width", 2);

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
        const lineHeight = 15;
        const textOffset = 8;

        // Add up arrow (Overperforming)
        g.append("line")
            .attr("x1", arrowX)
            .attr("x2", arrowX)
            .attr("y1", yScale(5))
            .attr("y2", yScale(30))
            .attr("stroke", "black")
            .attr("stroke-width", 1)
            .attr("marker-end", "url(#arrowhead)");

        // Overperforming label - line 1
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", yScale(28))
            .attr("dy", "0")
            .style("font-size", "14px")
            .style("font-family", "RobotoRegular")
            .text("Overperforming in");
        
        // Overperforming label - line 2
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", yScale(28))
            .attr("dy", lineHeight + "px")
            .style("font-size", "14px")
            .style("font-family", "RobotoRegular")
            .text("high-immigrant ridings");

        // Add down arrow (Underperforming)
        g.append("line")
            .attr("x1", arrowX)
            .attr("x2", arrowX)
            .attr("y1", yScale(-5))
            .attr("y2", yScale(-27))
            .attr("stroke", "black")
            .attr("stroke-width", 1)
            .attr("marker-end", "url(#arrowhead)");

        // Underperforming label - line 1
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", yScale(-24))
            .attr("dy", "0")
            .style("font-size", "14px")
            .style("font-family", "RobotoRegular")
            .text("Underperforming in");
        
        // Underperforming label - line 2
        g.append("text")
            .attr("x", arrowX + textOffset)
            .attr("y", yScale(-24))
            .attr("dy", lineHeight + "px")
            .style("font-size", "14px")
            .style("font-family", "RobotoRegular")
            .text("high-immigrant ridings");

        const line = d3.line()
            .x(d => xScale(d[0]))
            .y(d => yScale(d[1] - d[2]))
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
                .attr("stroke-dasharray", "5,1")
                .attr("d", line);

            g.selectAll(`vote-share-compare-dot-${party.tag}`)
                .data(partyData)
                .enter().append("circle")
                .attr("class", `vote-share-compare-dot-${party.tag}`)
                .attr("r", 3.5)
                .attr("cx", d => xScale(d[0]))
                .attr("cy", d => yScale(d[1] - d[2]))
                .attr("fill", PARTY_COLOURS[party.tag]);

            // Add party labels based on the requirements
            const labelIndex = curRegion === 'ontario' ? 9 : 9;
            if (partyData.length > labelIndex) {
                const labelData = partyData[labelIndex];
                const xPos = xScale(labelData[0]);
                const yPos = yScale(labelData[1] - labelData[2]);
                
                const { dx, dy, textAnchor } = setLabelPos(party.name, curRegion);

                g.append("text")
                    .attr("x", xPos)
                    .attr("y", yPos)
                    .attr("dx", dx)
                    .attr("dy", dy)
                    .attr("text-anchor", textAnchor)
                    .style("font-size", "14px")
                    .style("font-family", "RobotoRegular")
                    .style("fill", PARTY_COLOURS[party.tag])
                    .style("stroke", "white")
                    .style("stroke-width", "4px")
                    .text(party.name);

                g.append("text")
                    .attr("x", xPos)
                    .attr("y", yPos)
                    .attr("dx", dx)
                    .attr("dy", dy)
                    .attr("text-anchor", textAnchor)
                    .style("font-size", "14px")
                    .style("font-family", "RobotoRegular")
                    .style("fill", PARTY_COLOURS[party.tag])
                    .text(party.name);
            }
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


<div style="margin-bottom: -20px; margin-top: -25px;" bind:clientWidth={windowWidth}>

    <div class="sentence-controls">
        <p>
            Show how the major parties perform in the top 5 most immigrant ridings over time for 
            <select onchange={handleRegionChange} class="inline-select">
                <option value="federal">federal</option>
                <option value="ontario" selected>Ontario</option>
            </select>
            elections, compared to their performance in the 
            <select onchange={handleScopeChange} class="inline-select">
                <option value="gta">GTA</option>
                <option value="full" selected>full</option>
            </select>
            {curScope === 'gta' ? 'alone' : 'election'}.
        </p>
    </div>

    <svg id="vote-share-graph" height="400"></svg>

</div>

<style>
    svg {
        max-width: 100%;
    }
</style>