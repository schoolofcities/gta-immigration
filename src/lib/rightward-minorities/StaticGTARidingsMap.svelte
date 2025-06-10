<script>
    import { geoPath, geoMercator } from "d3";
    import { onMount } from "svelte";

    // Props
    let {
        mapData = [],
        mapConfig,
        dataKey,
        year,
    } = $props();

    // State variables
    let divWidth = $state(null);
    let innerWidth = $derived(divWidth);
    let height = $derived(innerWidth / 1.4); 

    let projection = $derived(
        geoMercator()
            .center([-79.38, 43.68]) 
            .scale([innerWidth * 32]) 
            .translate([innerWidth / 2.3, height / 1.4]) 
            .angle([-25]) 
    );

    let path = $derived(geoPath(projection));

    function getColour(value) {
        if (value === null || value === undefined) {
            return "url(#diagonalHatch)";
        }
        
        const breaks = mapConfig.breaks;
        const colours = mapConfig.colours;
        
        if (value < breaks[0]) return colours[0];
        for (let i = 0; i < breaks.length - 1; i++) {
            if (value >= breaks[i] && value < breaks[i + 1]) {
                return colours[i + 1];
            }
        }
        return colours[colours.length - 1];
    }

    // Calculate Brampton West position
    let bramptonWestFeature = $derived(mapData.find(f => f.properties.geoname === 'Brampton West'));
    let bramptonWestCentroid = $derived(bramptonWestFeature ? path.centroid(bramptonWestFeature) : null);
</script>

<div class="map-inner-container" bind:offsetWidth={divWidth}>
    {#if mapData.length > 0}
        <svg width={innerWidth} {height} id={year}>
            <defs>
                <pattern id="diagonalHatch" patternUnits="userSpaceOnUse" width="4" height="4">
                    <path d="M-1,1 l2,-2 M0,4 l4,-4 M3,5 l2,-2" 
                          stroke="#cccccc" 
                          stroke-width="1" />
                </pattern>
            </defs>

            <text class="label" x="5" y="22">{mapConfig.name}</text>

            {#each mapData as feature}
                <path 
                    class="riding" 
                    stroke-width={feature.properties.geoname === 'Brampton West'? 1 : 0.3}
                    d={path(feature)} 
                    fill={getColour(feature.properties[dataKey])}
                />
            {/each}

            {#each mapConfig.colours as colour, i}
                <rect 
                    class="box" 
                    width="40" 
                    height="12" 
                    x={5 + (i * 40)} 
                    y="30" 
                    style="fill:{colour}; stroke: white;"
                />
            {/each}

            <!-- Brampton West Label - positioned relative to centroid -->
            {#if bramptonWestCentroid}
                <line 
                    x1={bramptonWestCentroid[0] - 20} 
                    y1={bramptonWestCentroid[1] - 55} 
                    x2={bramptonWestCentroid[0]} 
                    y2={bramptonWestCentroid[1]} 
                    stroke="black" 
                    stroke-width="1"
                />
                <text 
                    class="riding-label" 
                    x={bramptonWestCentroid[0] - 35} 
                    y={bramptonWestCentroid[1] - 60} 
                >
                    Brampton West
                </text>
            {/if}

            {#if dataKey === 'cons_pct_change'}
                <!-- Add line and text at 7.6% mark (second rectangle) -->
                <line 
                    x1={5 + 40 + 20} 
                    y1="30" 
                    x2={5 + 40 + 20} 
                    y2="60" 
                    stroke="var(--brandDarkBlue)" 
                    stroke-width="1"
                    stroke-dasharray="4,3"
                />
                <text 
                    class="legend-note" 
                    x={5 + 40 + 20} 
                    y="70" 
                    text-anchor="middle"
                >
                    Cons. gained 7.6% nationally
                </text>
            {/if}

            {#each mapConfig.breaks as breakNum, i}
                <text 
                    class="label legend" 
                    x={5 + ((i + 1) * 40)} 
                    y="55" 
                    text-anchor="middle"
                >
                    {mapConfig.breakPrefix}{breakNum}{mapConfig.breakSuffix}
                </text>
            {/each}
        </svg>
    {/if}
</div>

<style>
    .map-inner-container {
        width: 100%;
        max-width: 600px;
        min-width: 400px;
    }

    .riding {
        stroke: white;
        /* stroke-width: 0.5px; */
        opacity: 1;
    }

    .box {
        opacity: 1;
    }

    .label {
        font-size: 15px;
        font-weight: 600;
        fill: var(--brandDarkBlue);
    }

    .riding-label {
        font-size: 10px;
        font-weight: 600;
        fill: var(--brandDarkBlue);
    }

    .legend {
        font-size: 13px;
        font-weight: 400;
    }

    .legend-note {
        font-size: 10px;
        fill: var(--brandDarkBlue);
    }
</style>