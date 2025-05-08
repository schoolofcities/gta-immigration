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

            {#each mapConfig.breaks as breakNum, i}
                <text 
                    class="label legend" 
                    x={5 + ((i + 1) * 40)} 
                    y="55" 
                    text-anchor="middle"
                >
                    {breakNum}{mapConfig.breakSuffix}
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
        stroke-width: 0.05px;
        opacity: 0.75;
    }
    .box {
        opacity: 0.75;
    }
    .label {
        font-size: 15px;
        font-weight: 600;
        fill: var(--brandDarkBlue);
    }
    .legend {
        font-size: 13px;
        font-weight: 400;
    }
</style>