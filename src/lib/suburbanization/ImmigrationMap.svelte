<script>
    // import border from "../assets/toronto-former-municipal-boundaries.geo.json"
    // import municipalPoints from '../assets/toronto-former-municipal-points.geo.json';
    
    import { onMount } from "svelte";
    import { geoPath, geoMercator, scaleThreshold } from "d3"; 
    import { CENSUS_SHADES } from "../constants";

    // Props
    let { curYear } = $props();
    
    const colours = [
        CENSUS_SHADES['pct_imm'][0], 
        CENSUS_SHADES['pct_imm'][2], 
        CENSUS_SHADES['pct_imm'][4], 
        CENSUS_SHADES['pct_imm'][6], 
        "#4b0f5c"
    ];
    const mapConfig = {
        1961: {
            'breaks': [15, 30, 45, 60],
            'breakSuffix': '%',
            'name': `Immigrant (% of population) in ${curYear}`,
            'immDist': 14.85,
            'notImmDist': 19.51,
            'popDist': 17.98,
        },
        1981: {
            'breaks': [15, 30, 45, 60],
            'breakSuffix': '%',
            'name': `Immigrant (% of population) in ${curYear}`,
            'immDist': 23.62,
            'notImmDist': 31.35,
            'popDist': 28.61,
        },
        2001: {
            'breaks': [15, 30, 45, 60],
            'breakSuffix': '%',
            'name': `Immigrant (% of population) in ${curYear}`,
            'immDist': 26.68,
            'notImmDist': 35.81,
            'popDist': 32.01,
        },
        2021: {
            'breaks': [15, 30, 45, 60],
            'breakSuffix': '%',
            'name': `Immigrant (% of population) in ${curYear}`,
            'immDist': 31.58,
            'notImmDist': 36.18,
            'popDist': 34.15,
        },
    }

    // State variables
    let immData = $state.raw(null);  

    let divWidth = $state(null);
    let innerWidth = $derived(divWidth);
    let height = $derived(innerWidth / 1.55);

    let scaleFactor = $derived(innerWidth <= 500 ? 25 : 30);
    let heightOffset = $derived(innerWidth <= 500 ? 85 : 100)

    let projection = $derived(
        geoMercator()
            .center([-79.4, 43.7])
            .scale([innerWidth * scaleFactor])
            .translate([(innerWidth / 2) - 50, (height / 2) + heightOffset])
            .angle([-30])
    );
    let path = $derived(geoPath(projection));

    // Other variables
    var color = scaleThreshold()
        .domain(mapConfig[curYear]["breaks"])
        .range(colours);

    // Functions
    function getColour(percentage) {
        if (percentage === null) {
            return "url(#diagonalHatch)"; // For diagonal lines
            // return "#cccccc"; // for simple light gray
        }
        else if (percentage < 15) return colours[0];
        else if (percentage < 30) return colours[1];
        else if (percentage < 45) return colours[2];
        else if (percentage < 60) return colours[3];
        else return colours[4];
    }

    function loadGeoJson() {
        const filePath = `/gta-immigration/data/immigration/imm_stats_${curYear}.geojson`;
        fetch(filePath)
            .then(response => response.json())
            .then(data => {
                // Add an id to each feature if it doesn't already have one
                data.features = data.features.map((feature, index) => {
                    if (!feature.id) {
                        feature.id = index; // Use index as a fallback ID
                    }
                    return feature;
                });
                
                // Set the appropriate colour
                data.features = data.features.map((feature) => {
                    feature.properties.colour = getColour(feature.properties.pct_imm);
                    return feature;
                });

                immData = data.features;
            });
    }

    onMount(() => {
        loadGeoJson();
    });
</script>

<div class="map-inner-container" bind:offsetWidth={divWidth}>
	<svg width={innerWidth} {height} id={curYear}>
        <defs>
            <pattern id="diagonalHatch" patternUnits="userSpaceOnUse" width="4" height="4">
                <path d="M-1,1 l2,-2 M0,4 l4,-4 M3,5 l2,-2" 
                      stroke="#cccccc" 
                      stroke-width="1" />
            </pattern>
        </defs>

        <text class="label" x="5" y="22">{mapConfig[curYear].name}</text>
        
        <!-- {#each border.features as data}
            <path d={path(data)} stroke="#1E3765" stroke-width=1 fill=none opacity=0.23/>
        {/each} -->

        {#each immData as data}
            <path 
                class="ct" 
                d={path(data)} 
                fill={data.properties.colour} 
                stroke={data.properties.colour} 
            />
        {/each}

        {#each colours as colour, i} 
            <rect class="box" width="50" height="12" x={5 + (i * 50)} y="30" style="fill:{colours[i]}; stroke: white;"></rect>
        {/each}

        {#each mapConfig[curYear].breaks as breakNum, i}
            <text class="label legend" x={5 + ((i + 1) * 50)} y="55" text-anchor="middle">{mapConfig[curYear]["breaks"][i]+ mapConfig[curYear].breakSuffix}</text>
        {/each}
    </svg>
</div>

<style>
    .map-inner-container {
        width: 100%;
        max-width: 600px;
        min-width: 400px;
    }

    .ct {
        stroke-width: 0.4;
    }

    .box {
        /* opacity: 0.75; */
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