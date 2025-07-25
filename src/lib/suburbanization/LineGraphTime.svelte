<script>
    import { CENSUS_COLOURS } from '$lib/constants';
    import { scaleLinear, scaleTime, line } from 'd3';
    import { onMount } from 'svelte';

    let containerWidth = 600;
    const containerHeight = 300;
    const margin = { top: 30, right: 30, bottom: 50, left: 50 };

    $: innerWidth = containerWidth - margin.left - margin.right;
    $: innerHeight = containerHeight - margin.top - margin.bottom;

    let data = [];

    onMount(async () => {
        const response = await fetch('/gta-immigration/data/immigration_analysis/pop_dists.csv');
        const csvText = await response.text();
        
        // Parse CSV data
        const rows = csvText.split('\n').slice(1); // Skip header
        data = rows.filter(row => row.trim() !== '').map(row => {
            const [year, imm, not_imm, pop, imm_new, vm, imm_2nd] = row.split(',');
            return {
                year: +year,
                imm: +imm,
                not_imm: +not_imm,
                pop: +pop,
                imm_new: imm_new ? +imm_new : null,
                vm: vm ? +vm : null,
                imm_2nd: imm_2nd ? +imm_2nd : null
            };
        });
    });

    $: xScale = scaleTime()
        .domain([new Date(Math.min(...data.map(d => d.year))), new Date(Math.max(...data.map(d => d.year)))])
        .range([0, innerWidth]);

    $: yScale = scaleLinear()
        .domain([0, 40])
        .range([innerHeight, 0]);

    $: lineGenerator = line()
        .x(d => xScale(new Date(d.year)))
        .y(d => yScale(d.value));

    $: immLineData = data.map(d => ({ year: d.year, value: d.imm }));
    $: notImmLineData = data.map(d => ({ year: d.year, value: d.not_imm }));
    $: newImmLineData3 = data.map(d => ({ year: d.year, value: d.imm_new })).filter(d => (d.value !== null && d.year <= 1996));
    $: newImmLineData5 = data.map(d => ({ year: d.year, value: d.imm_new })).filter(d => (d.value !== null && d.year >= 1996));

</script>


<div class="container plots-title">
    <h4>
        Immigrants new and old are moving to the suburbs
    </h4>
    <p>
        Average distance in kilometres that residents in the Greater Toronto Area live from Toronto's city centre among <span id="non-imm">non-immigrants</span>, <span id="imm">all immigrants</span>, and <span id="new-imm">new immigrants</span>.
    </p>
</div>

<div class="chart-container" bind:clientWidth={containerWidth}>
    {#if data.length > 0}
        <svg width={containerWidth} height={containerHeight}>
            <g transform={`translate(${margin.left},${margin.top})`}>
                <!-- Y-axis grid lines -->
                {#each [0, 10, 20, 30, 40] as tick}
                    <line
                        x1={0}
                        y1={yScale(tick)}
                        x2={innerWidth}
                        y2={yScale(tick)}
                        stroke="#e0e0e0"
                        stroke-width="1"
                    />
                {/each}

                <!-- X-axis ticks and labels (every 10 years) -->
                <g transform={`translate(0,${innerHeight})`}>
                    {#each data.filter(d => d.year % 10 === 1) as d}
                        <text
                            class="tick-label"
                            x={xScale(new Date(d.year))}
                            y={20}
                            text-anchor="middle"
                            font-size="12"
                        >
                            {d.year}
                        </text>
                    {/each}
                </g>

                <!-- Y-axis ticks and labels -->
                <g>
                    {#each [0, 10, 20, 30, 40] as tick}
                        <text
                            class="tick-label"
                            x={-10}
                            y={yScale(tick)}
                            text-anchor="end"
                            dominant-baseline="middle"
                            font-size="12"
                        >
                            {tick} km
                        </text>
                    {/each}
                </g>

                <!-- Y-axis label -->
                <!-- <text
                    class="axis-label"
                    x={-30}
                    y={innerHeight / 2}
                    text-anchor="middle"
                    transform="rotate(-90, -30, {innerHeight / 2})"
                    font-size="12"
                >
                    Average distance (km)
                </text> -->



                <!-- Lines -->
                <path
                    d={lineGenerator(immLineData)}
                    fill="none"
                    stroke={CENSUS_COLOURS.imm}
                    stroke-width="3"
                />

                {#each immLineData as d}
                    <circle
                        cx={xScale(new Date(d.year))}
                        cy={yScale(d.value)}
                        r="4"
                        fill={CENSUS_COLOURS.imm}
                        stroke="white"
                        stroke-width="1"
                    />
                {/each}

                <path
                    d={lineGenerator(notImmLineData)}
                    fill="none"
                    stroke={CENSUS_COLOURS.not_imm}
                    stroke-width="3"
                />

                {#each notImmLineData as d}
                    <circle
                        cx={xScale(new Date(d.year))}
                        cy={yScale(d.value)}
                        r="4"
                        fill={CENSUS_COLOURS.not_imm}
                        stroke="white"
                        stroke-width="1"
                    />
                {/each}

                <path
                    d={lineGenerator(newImmLineData3)}
                    fill="none"
                    stroke={CENSUS_COLOURS.new_imm}
                    stroke-width="3"
                    stroke-dasharray="4,2"
                />

                {#each newImmLineData3 as d}
                    <circle
                        cx={xScale(new Date(d.year))}
                        cy={yScale(d.value)}
                        r="4"
                        fill={CENSUS_COLOURS.new_imm}
                        stroke="white"
                        stroke-width="1"
                    />
                {/each}

                <path
                    d={lineGenerator(newImmLineData5)}
                    fill="none"
                    stroke={CENSUS_COLOURS.new_imm}
                    stroke-width="3"
                />

                {#each newImmLineData5 as d}
                    <circle
                        cx={xScale(new Date(d.year))}
                        cy={yScale(d.value)}
                        r="4"
                        fill={CENSUS_COLOURS.new_imm}
                        stroke="white"
                        stroke-width="1"
                    />
                {/each}

                <!-- Line labels -->
                <text
                    class="line-label"
                    x={xScale(new Date(1991))}
                    y={yScale(27)}
                    fill={CENSUS_COLOURS.imm}
                    text-anchor="middle"
                    font-size="12"
                >
                    All immigrants
                </text>

                <text
                    class="line-label"
                    x={xScale(new Date(1981))}
                    y={yScale(34)}
                    fill={CENSUS_COLOURS.not_imm}
                    text-anchor="middle"
                    font-size="12"
                >
                    Non-immigrants
                </text>

                <text
                    class="line-label"
                    x={xScale(new Date(2001))}
                    y={yScale(19)}
                    fill={CENSUS_COLOURS.new_imm}
                    text-anchor="middle"
                    font-size="12"
                >
                    New immigrants
                </text>
            </g>
        </svg>
    {/if}
</div>

<div class="container plots-title">
    <p style="color: var(--brandGray80); font-size: 12px;">
        Data are from the Canadian census. A new immigrant is defined as arriving in the 3 years prior to the census for 1981, 1986, and 1991 and in the 5 years prior to the census for 1996 to 2021. New immigrants are part of the “all immigrants” category.
    </p>
</div>

<style>
    .chart-container {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
    }

    .tick-label {
        fill: var(--brandGray80);
        font-size: 12px;
    }

    .axis-label {
        fill: var(--brandGray90);
    }

    .line-label {
        font-family: RobotoRegular, sans-serif;
    }

    .line-label {
        font-weight: bold;
    }

    #non-imm {
        /* background-color: var(--brandYellow); */
        border-bottom: solid 2px var(--brandLightGreen);
    }

    #imm {
        /* color: #ffffff; */
        /* background-color: var(--brandPurple); */
        border-bottom: solid 2px var(--brandPurple);
    }

    #new-imm {
        /* background-color: #d5a4b2; */
        border-bottom: solid 2px var(--brandPink);
    }
</style>