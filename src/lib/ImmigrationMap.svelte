<script>
    // import ctData from "../assets/ctData.geo.json"; 
    // import rinks from "../assets/toronto-rinks.geo.json";
    // import border from "../assets/toronto-former-municipal-boundaries.geo.json"
    // import municipalPoints from '../assets/toronto-former-municipal-points.geo.json';
    // var ledColours = ["#ede9fe", "#dad9f9", "#aaacd4", "#6e6d9f", "#383669"] 
    // export let demoGP;
    
    import { onMount } from "svelte";
    import { geoPath, geoMercator, scaleThreshold } from "d3"; 
    import { CENSUS_SHADES } from "./constants";

    // Props
    let { curYear } = $props();
    
    const colours = CENSUS_SHADES['pct_imm'].concat(['#002b36']);
    const mapConfig = {
        1961: {
            'breaks': [10, 20, 30, 40, 50, 60, 70],
            'breakSuffix': '%',
            'name': `Immigrant (% of population) in ${curYear}`,
            'immDist': 0.0,
            'notImmDist': 0.0,
            'popDist': 0.0,
        },
        1981: {
            'breaks': [10, 20, 30, 40, 50, 60, 70],
            'breakSuffix': '%',
            'name': `Immigrant (% of population) in ${curYear}`,
            'immDist': 0.0,
            'notImmDist': 0.0,
            'popDist': 0.0,
        },
        2001: {
            'breaks': [10, 20, 30, 40, 50, 60, 70],
            'breakSuffix': '%',
            'name': `Immigrant (% of population) in ${curYear}`,
            'immDist': 0.0,
            'notImmDist': 0.0,
            'popDist': 0.0,
        },
        2021: {
            'breaks': [10, 20, 30, 40, 50, 60, 70],
            'breakSuffix': '%',
            'name': `Immigrant (% of population) in ${curYear}`,
            'immDist': 0.0,
            'notImmDist': 0.0,
            'popDist': 0.0,
        },
    }

    // State variables
    let immData = $state.raw(null);  

    let divWidth = $state(null);
    let innerWidth = $derived(divWidth);
    let height = $derived(innerWidth / 1.55);

    let projection = $derived(
        geoMercator()
            .center([-79.188 + 0.24 * ((600 - innerWidth) / 200), 43.727 - 0.02 * ((600 - innerWidth) / 200) ])
            .scale([62000 * innerWidth / 600])
            .angle([-17])
    );

    // let projection = $derived(
    //     geoMercator()
    //         .center([-79.4, 43.8]) // shifted west and slightly north
    //         .scale([62000 * innerWidth / 3200]) // reduced from 62000 to 25000
    //         .angle([-12]) // adjusted from -17 to -12 for GTA orientation
    // );
    let path = $derived(geoPath(projection));

    // Other variables
    var color = scaleThreshold()
        .domain(mapConfig[curYear]["breaks"])
        .range(colours);

    // Functions
    function getColour(percentage) {
        // TODO: Add support for nan!!
        if (percentage < 10) return colours[0];
        else if (percentage < 20) return colours[1];
        else if (percentage < 30) return colours[2];
        else if (percentage < 40) return colours[3];
        else if (percentage < 50) return colours[4];
        else if (percentage < 60) return colours[5];
        else if (percentage < 70) return colours[6];
        else return colours[7];
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
                    return feature
                })

                immData = data.features;
            });
    }

    $effect(() => {
        console.log(immData);
    });
    
    onMount(() => {
        loadGeoJson();
    });

    // let toRinks = rinks.features;
    // let ct = ctData.features;

    // ct.map((item =>{
    //     item.properties[demoGP]
    //     ?(item.properties["color_"+demoGP] = color(item.properties[demoGP]))
    //     :(item.properties["color_"+demoGP] = "white");
    // }))

    // const demoGPs = {
    //     "PopDen":{
    //         "breaks":[2500,5000,7500],
    //         "name":"Population Density (# of people per sq.km)",
    //         "breakSuffix": "",
    //         "barChartText": "overall population",
    //         "walkTime": 34.3,
    //         "transitTime": 23.4
    //     },
    //     "Immi%":{
    //         "breaks":[30,45,60],
    //         "name": "Immigrant (% of population)",
    //         "breakSuffix": "%",
    //         "barChartText": "immigrant population",
    //         "walkTime": 37,
    //         "transitTime": 24.5
    //     },
    //     "VM%":{
    //         "breaks":[30,45,60],
    //         "name": "Visible Minority (% of population)",
    //         "breakSuffix": "%",
    //         "barChartText": "visible minorities",
    //         "walkTime": 39.7,
    //         "transitTime": 25.4
    //     },
    //     "LIn%":{
    //         "breaks":[5,10,15],
    //         "name":"Low Income (% of population)",
    //         "breakSuffix": "%",
    //         "barChartText": "low-income residents",
    //         "walkTime": 33.5,
    //         "transitTime": 22.7
    //     }
    // }
</script>



<div id="container" bind:offsetWidth={divWidth}>

	<svg width={innerWidth} {height} id={curYear}>

        <text class="label" x="5" y="22">{mapConfig[curYear].name}</text>
        
        <!-- {#each border.features as data}
            <path d={path(data)} stroke="#1E3765" stroke-width=1 fill=none opacity=0.23/>
        {/each} -->

        {#each immData as data}
            <path class="ct" d={path(data)} fill={data.properties.colour}/>
        {/each}

        <!-- {#each border.features as data}
            <path d={path(data)} stroke="#1E3765" stroke-width=1 fill=none opacity=0.8/>
        {/each} -->

        <!-- {#each toRinks as data}
            <circle
            class="rink"
            cx={projection(data.geometry.coordinates)[0]}
            cy={projection(data.geometry.coordinates)[1]}
            r="4"
            stroke="white"
            stroke-width="2"
            fill="black"/>
        {/each} -->

        <!-- {#each municipalPoints.features as data}
			<text
				class="legend"
				x={projection(data.geometry.coordinates)[0]}
				y={projection(data.geometry.coordinates)[1]}
				text-anchor="middle"
				stroke="white"
				stroke-width=2.5
				font-size=12
				opacity=0.7
				>{data.properties.AREA_NAME}
			</text>
			<text
				class="legend"
				x={projection(data.geometry.coordinates)[0]}
				y={projection(data.geometry.coordinates)[1]}
				text-anchor="middle"
				font-size=12
				>{data.properties.AREA_NAME}
			</text>
		{/each} -->

        <!-- <rect class="box" width="40" height = "12" x="125" y="30" style="fill:{ledColours[3]}; stroke: white;"></rect>
        <rect class="box" width="40" height = "12" x="85" y="30" style="fill:{ledColours[2]}; stroke: white;"></rect>
		<rect class="box" width="40" height = "12" x="45" y="30" style="fill:{ledColours[1]}; stroke: white;"></rect>
		<rect class="box" width="40" height = "12" x="5" y="30" style="fill:{ledColours[0]}; stroke: white;"></rect> -->

        <!-- <text class="label legend" x="125" y="55" text-anchor="middle">{demoGPs[demoGP]["breaks"][2]+ demoGPs[demoGP].breakSuffix}</text>
		<text class="label legend" x="85" y="55" text-anchor="middle">{demoGPs[demoGP]["breaks"][1]+ demoGPs[demoGP].breakSuffix}</text>
		<text class="label legend" x="45" y="55" text-anchor="middle">{demoGPs[demoGP]["breaks"][0]+ demoGPs[demoGP].breakSuffix}</text> -->
        
    </svg>

    <!-- <svg width={innerWidth} height="60">

        <text class="label" x="5" y="{12}" text-anchor="start">Average travel time to nearest rink ({demoGPs[demoGP]["barChartText"]}):</text>

        <text class="label legend" x="46" y="{30}" text-anchor="end">Walk</text>
        <rect class="bar" width="{250 * demoGPs[demoGP]["walkTime"] / 40}" height = "8" x="50" y="{22}" style="fill: #6D247A; stroke: white;"></rect>
        <text class="label legend" x="{53 + 250 * demoGPs[demoGP]["walkTime"] / 40}" y="{30}" text-anchor="start">{demoGPs[demoGP]["walkTime"]} minutes</text>

        <text class="label legend" x="46" y="{48}" text-anchor="end">Transit</text>
        <rect class="bar" width="{250 * demoGPs[demoGP]["transitTime"] / 40}" height = "8" x="50" y="{40}" style="fill: #6D247A; stroke: white;"></rect>
        <text class="label legend" x="{53 + 250 * demoGPs[demoGP]["transitTime"] / 40}" y="{48}" text-anchor="start">{demoGPs[demoGP]["transitTime"]} minutes</text>
        
    </svg> -->

</div>



<style>
    #container {
        width: 100%;
        max-width: 600px;
        min-width: 400px;
    }
    .rink{
        stroke: var(--brandWhite);
        stroke-width: 1px;
        fill: var(--brandGray90)
    }
    .ct {
        stroke: var(--brandWhite);
        stroke-width: 0.1px;
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