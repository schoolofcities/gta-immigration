<script>
    import { CENSUS_COLOURS } from '$lib/constants';
    import { scaleLinear, line, curveStepBefore } from 'd3';
    import { onMount } from 'svelte';

    export let year;
    export let showYAxisLabel = false;
    export let showXAxisLabel = false;
    export let showXAxisTicks = false;
    export let showLocationLabels = false;

    let containerWidth = 600;
    $: isMobile = containerWidth <= 600;

    const baseHeight = 125;
    const extraBottomSpace = 20; // For x-axis label
    $: extraTopSpace = isMobile ? 40 : 20
    
    // Base margins (used for all graphs)
    const baseMargin = { top: 20, right: 30, bottom: 20, left: 50 };
    
    // Calculate actual height and margin based on what we need to show
    $: containerHeight = (showXAxisLabel ? baseHeight + extraBottomSpace : baseHeight) + 
                         (showLocationLabels ? extraTopSpace : 0);
    $: margin = {
        ...baseMargin,
        top: showLocationLabels ? baseMargin.top + extraTopSpace : baseMargin.top,
        bottom: showXAxisLabel ? baseMargin.bottom + extraBottomSpace : baseMargin.bottom
    };

    $: innerWidth = containerWidth - margin.left - margin.right;
    $: innerHeight = containerHeight - margin.top - margin.bottom;

    let data = [];

    // Location markers data
    const locationMarkers = [
        { start: 0, end: 10, label: "Old Toronto" },
        { start: 10, end: 20, label: "Inner Suburbs" },
        { start: 20, end: 30, label: "Outer Suburbs" },
        { start: 30, end: 50, label: "Exurbs" }
    ];

    function getLabelParts(label) {
        if (!isMobile || label === "Exurbs") return [label];
        return label.split(' ');
    }

    function getLabelY(label, i) {
        if (!isMobile) return -9;
        else if (label === "Exurbs") return -19;
        else if (i === 0) return -25;
        else return -13;
    }

    onMount(async () => {
        const response = await fetch(`/gta-immigration/data/immigration_analysis/imm_dist_${year}.csv`);
        const csvText = await response.text();
        
        // Parse CSV data and add (0,0) point
        const rows = csvText.split('\n').slice(1); // Skip header
        const parsedData = rows.filter(row => row.trim() !== '').map(row => {
            const [dist_km, num_pop_tot, num_not_imm_tot, num_imm_tot, num_imm_new] = row.split(',');
            return {
                dist_km: +dist_km,
                num_not_imm_tot: +num_not_imm_tot,
                num_imm_tot: +num_imm_tot,
                num_imm_new: +num_imm_new,
            };
        });

        // Setting initial value to 0 does not lead to a complementary value at the end easily
        data = [
            { 
                dist_km: 0, 
                num_not_imm_tot: parsedData[0].num_not_imm_tot, 
                num_imm_tot: parsedData[0].num_imm_tot,
                num_imm_new: parsedData[0].num_imm_new,
            }, 
            ...parsedData
        ];
    });

    const ySteps = [0, 40000, 80000];

    $: xScale = scaleLinear()
        .domain([0, 50])
        .range([0, innerWidth]);

    $: yScale = scaleLinear()
        .domain([0, ySteps[2]])
        .range([innerHeight, 0]);

    // Line generator for step lines
    $: lineGenerator = line()
        .x(d => xScale(d.dist_km))
        .y(d => yScale(d.num_not_imm_tot))
        .curve(curveStepBefore);

    $: immLineGenerator = line()
        .x(d => xScale(d.dist_km))
        .y(d => yScale(d.num_imm_tot))
        .curve(curveStepBefore);

    $: newImmLineGenerator = line()
        .x(d => xScale(d.dist_km))
        .y(d => yScale(d.num_imm_new))
        .curve(curveStepBefore);
</script>

<div class="chart-container" bind:clientWidth={containerWidth}>
    {#if data.length > 0}
        <svg width={containerWidth} height={containerHeight}>
            <g transform={`translate(${margin.left},${margin.top})`}>
                <!-- Location labels at top (if enabled) -->
                {#if showLocationLabels}
                    <g class="location-labels">
                        <!-- Vertical lines (5px to 20px from top) -->
                        {#each [10, 20, 30] as tick}
                            <line
                                x1={xScale(tick)}
                                y1={-5}  
                                x2={xScale(tick)}
                                y2={isMobile ? -40 : -20}  
                                stroke="#e0e0e0"
                                stroke-width="1"
                            />
                        {/each}

                        <!-- Location labels -->
                        {#each locationMarkers as loc}
                            {@const labelParts = getLabelParts(loc.label)}
                            {#each labelParts as part, i}
                                <text
                                    x={xScale((loc.start + loc.end) / 2)}
                                    y={getLabelY(part, i)} 
                                    text-anchor="middle"
                                    font-size="12"
                                >
                                    {part}
                                </text>
                            {/each}
                        {/each}
                    </g>
                {/if}

                <!-- Y-axis grid lines (horizontal) -->
                {#each ySteps as tick}
                    <line
                        x1={0}
                        y1={yScale(tick)}
                        x2={innerWidth}
                        y2={yScale(tick)}
                        stroke="#e0e0e0"
                        stroke-width="1"
                    />
                {/each}

                <!-- X-axis grid lines (vertical) -->
                {#each [10, 20, 30, 40] as tick}
                    <line
                        x1={xScale(tick)}
                        y1={5}
                        x2={xScale(tick)}
                        y2={innerHeight - 5}
                        stroke="#e0e0e0"
                        stroke-width="1"
                    />
                {/each}

                <!-- X-axis ticks and labels -->
                {#if showXAxisTicks}
                    <g transform={`translate(0,${innerHeight})`}>
                        {#each [0, 10, 20, 30, 40, 50] as tick}
                            <text
                                class="tick-label"
                                x={xScale(tick)}
                                y={15}  
                                text-anchor="middle"
                                font-size="12"
                            >
                                {tick}
                            </text>
                        {/each}
                    </g>
                {/if}

                <!-- Y-axis ticks and labels -->
                <g>
                    {#each ySteps as tick}
                        <text
                            class="tick-label"
                            x={-10}  
                            y={yScale(tick)}
                            text-anchor="end"
                            dominant-baseline="middle"
                            font-size="12"
                        >
                            {tick === 0 ? '0' : tick/1000 + 'K'}
                        </text>
                    {/each}
                </g>

                <!-- Y-axis label (conditional) -->
                {#if showYAxisLabel}
                    <text
                        class="axis-label"
                        x={-40}  
                        y={innerHeight / 2}
                        text-anchor="middle"
                        transform="rotate(-90, -40, {innerHeight / 2})"
                        font-size="12"
                    >
                        Population
                    </text>
                {/if}

                <!-- X-axis label (conditional) -->
                {#if showXAxisLabel}
                    <text
                        class="axis-label"
                        x={innerWidth / 2}
                        y={innerHeight + 35}  
                        text-anchor="middle"
                        font-size="12"
                    >
                        Distance (km)
                    </text>
                {/if}

                <!-- Step lines -->
                <path
                    d={lineGenerator(data)}
                    fill="none"
                    stroke={CENSUS_COLOURS.not_imm}
                    stroke-width="2"
                />

                <path
                    d={immLineGenerator(data)}
                    fill="none"
                    stroke={CENSUS_COLOURS.imm}
                    stroke-width="2"
                />

                <path
                    d={newImmLineGenerator(data)}
                    fill="none"
                    stroke={CENSUS_COLOURS.new_imm}
                    stroke-width="2"
                />
            </g>
        </svg>
    {/if}
</div>

<style>
    .chart-container {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
    }

    .tick-label {
        fill: #000;
        font-size: 12px;
    }

    .axis-label {
        fill: #000;
    }
</style>