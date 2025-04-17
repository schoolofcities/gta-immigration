<script>
    import { onMount } from "svelte";
    import maplibregl from "maplibre-gl";
    import "maplibre-gl/dist/maplibre-gl.css";
    import { FELXN_YEARS, ONTELXN_YEARS, PARTY_SHADES, CENSUS_SHADES, PARTIES_INFO } from "../lib/constants.js";
    import { getRegionTag, updateCensusVarOptions, updatePartyOptions } from "./utils.js";
    import Legend from './Legend.svelte';
    import PlaceLabels from '../assets/municipality-place-labels.geo.json';

    let map1, map2;

    // Map config objects
    const mapConfig = {
        style: {
            version: 8, 
            sources: {}, 
            glyphs: "https://schoolofcities.github.io/fonts/fonts/{fontstack}/{range}.pbf",
            layers: [
                {
                    id: 'background', 
                    type: 'background', 
                    paint: {
                        'background-color': '#fcfcfc' 
                    }
                }
            ] // empty layers
        },
        // style: "https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",
        center: [-79.386, 43.702],
        zoom: 9,
        maxZoom: 11,
        minZoom: 8,
        maxBounds: [
            [-81.0, 42.5], // Southwest corner (near London, ON)
            [-78.0, 45.0] // Northeast corner (north of Peterborough)
        ],
        bearing: -17.2,
        dragRotate: false,
        pitchWithRotate: false,
        touchZoomRotate: true,
        attributionControl: false,
        scrollZoom: false
    };

    const navControlConfig = {
        showCompass: true,
        visualizePitch: false
    };

    const scaleControlConfig = {
        maxWidth: 100,
        unit: 'metric'
    };

    // State variables
    let curRegion = $state("ontario");
    let curRegionTag = $derived(getRegionTag(curRegion));

    let curYear = $state(2025);
    let years = $state(ONTELXN_YEARS);

    let geoJsonData = $state(null);

    let curParties = $derived(updatePartyOptions(geoJsonData));
    let curParty = $state("cons1");

    let curCensusVars = $derived(updateCensusVarOptions(geoJsonData));
    let curCensusVariable = $state("pct_imm");

    // State for hovered/tapped riding
    let hoveredRidingId = $state(null);
    let hoveredRidingData = $state(null);

    // Generate census variable labels based on the current variable
    let censusLabels = $derived(
        curCensusVariable === 'pct_imm' ? generateLabels(0, 60, 7) : // if 
        curCensusVariable === 'pct_vm' ? generateLabels(0, 90, 7) : // else if 
        (geoJsonData ? generateHouseholdIncomeLabels() : []) // else 
    );
    
    // Generate party vote share labels (0-60%)
    const partyLabels = generateLabels(0, 60, 7);

    // Prevent infinite update loops
    let syncing = false;
    function syncMaps(movingMap, targetMap) {
        movingMap.on("move", () => {
            if (!syncing) {
                syncing = true;
                targetMap.jumpTo({
                    center: movingMap.getCenter(),
                    zoom: movingMap.getZoom()
                });
                syncing = false;
            }
        });
    }

    // Consolidated function to add labels to a map
    function addLabelsToMap(map, loadDataCallback = null) {
        map.addSource('labels-source', {
            type: 'geojson',
            data: PlaceLabels 
        });
        map.addLayer({
            id: 'labels-layer',
            type: 'symbol',
            source: 'labels-source',
            layout: {
                'text-field': ['get', 'name'], 
                'text-size': 12, 
                'text-offset': [0, 0], 
                'text-anchor': 'top', 
                'text-allow-overlap': false, 
                'text-font': ['TradeGothic LT Bold'] 
            },
            paint: {
                'text-color': '#1E3765', 
                'text-halo-color': '#FFFFFF', 
                'text-halo-width': 1,
                'text-opacity': 0.7
            }
        });
        
        if (loadDataCallback) {
            loadDataCallback();
        }
    }

    function loadGeoJson() {
        const filePath = `/gta-immigration/data/elections/${curRegionTag}_stats_${curYear}.geojson`;
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
                geoJsonData = data;
                updateSelectOptions();
                
                // Update layers only if labels exist
                if (map1 && map1.getLayer('labels-layer')) updatePartyMapLayer();
                if (map2 && map2.getLayer('labels-layer')) updateCensusMapLayer();
            });
    }

    function updateSelectOptions() {
        if (geoJsonData && geoJsonData.features.length > 0) {
            // Ensure curParty and curCensusVariable are valid
            if (!curParties.some(p => p.tag === curParty)) {
                curParty = curParties.length > 0 ? curParties[0].tag : null;
            }
            if (!curCensusVars.some(v => v.propertyTag === curCensusVariable)) {
                curCensusVariable = curCensusVars.length > 0 ? curCensusVars[0].propertyTag : null;
            }
        }
    }

    // Helper function to generate legend labels
    function generateLabels(min, max, steps) {
        const stepSize = (max - min) / (steps - 1);
        return Array.from({length: steps}, (_, i) => 
            i === steps - 1 ? `${min + (i * stepSize)}%+` : `${min + (i * stepSize)}%`
        );
    }
    
    function generateHouseholdIncomeLabels() {
        const values = geoJsonData.features.map(f => f.properties.avg_hou_inc);
        const min = Math.min(...values);
        const max = Math.max(...values);
        const step = (max - min) / 6;
        return Array.from({length: 7}, (_, i) => 
            i === 6 ? `$${Math.round((min + (i * step)) / 1000)}K` 
                   : `$${Math.round((min + (i * step)) / 1000)}K`
        );
    }

    function handleRegionChange(event) {
        curRegion = event.target.value;
        years = curRegion === "federal" ? FELXN_YEARS : ONTELXN_YEARS;
        curYear = years[years.length - 1];
        loadGeoJson();
    }

    function handleYearChange(event) {
        curYear = event.target.value;
        loadGeoJson();
    }

    function handlePartyChange(event) {
        curParty = event.target.value;
        updatePartyMapLayer();
    }

    function handleCensusVariableChange(event) {
        curCensusVariable = event.target.value;
        updateCensusMapLayer();
    }

    function updatePartyMapLayer() {
        if (map1.getLayer("party-vote-share-boundary")) {
            map1.removeLayer("party-vote-share-boundary");
        }
        if (map1.getLayer("party-vote-share")) {
            map1.removeLayer("party-vote-share");
        }
        if (map1.getSource("party-vote-share")) {
            map1.removeSource("party-vote-share");
        }

        map1.addSource("party-vote-share", {
            type: "geojson",
            data: geoJsonData
        });

        const partyPropertyTag = PARTIES_INFO.find(party => party.tag === curParty).propertyTag;

        map1.addLayer({
            id: "party-vote-share",
            type: "fill",
            source: "party-vote-share",
            paint: {
                "fill-color": [
                    "step",
                    ["get", partyPropertyTag],
                    PARTY_SHADES[curParty][0], // 0-10%
                    10, PARTY_SHADES[curParty][1], // 10-20%
                    20, PARTY_SHADES[curParty][2], // 20-30%
                    30, PARTY_SHADES[curParty][3], // 30-40%
                    40, PARTY_SHADES[curParty][4], // 40-50%
                    50, PARTY_SHADES[curParty][5], // 50-60%
                    60, PARTY_SHADES[curParty][6] // 60%+
                ],
                "fill-opacity": 0.9
            }
        }, 'labels-layer');

        map1.addLayer({
            id: "party-vote-share-boundary",
            type: "line",
            source: "party-vote-share",
            paint: {
                "line-color": "#fff",
                "line-width": [
                    "case",
                    ["boolean", ["feature-state", "hover"], false],
                    3, // Highlighted line width
                    0.5 // Default line width
                ]
            }
        }, 'labels-layer');
    }

    function updateCensusMapLayer() {
        if (map2.getLayer("census-variable-boundary")) {
            map2.removeLayer("census-variable-boundary");
        }
        if (map2.getLayer("census-variable")) {
            map2.removeLayer("census-variable");
        }
        if (map2.getSource("census-variable")) {
            map2.removeSource("census-variable");
        }

        map2.addSource("census-variable", {
            type: "geojson",
            data: geoJsonData
        });

        let paintConfig;
        if (curCensusVariable === "pct_imm") {
            paintConfig = [
                "step",
                ["get", curCensusVariable],
                CENSUS_SHADES.pct_imm[0], // 0-10%
                10, CENSUS_SHADES.pct_imm[1], // 10-20%
                20, CENSUS_SHADES.pct_imm[2], // 20-30%
                30, CENSUS_SHADES.pct_imm[3], // 30-40%
                40, CENSUS_SHADES.pct_imm[4], // 40-50%
                50, CENSUS_SHADES.pct_imm[5], // 50-60%
                60, CENSUS_SHADES.pct_imm[6], // 60%+
            ];
        } else if (curCensusVariable === "pct_vm") {
            paintConfig = [
                "step",
                ["get", curCensusVariable],
                CENSUS_SHADES.pct_vm[0], // 0-15%
                15, CENSUS_SHADES.pct_vm[1], // 15-30%
                30, CENSUS_SHADES.pct_vm[2], // 30-45%
                45, CENSUS_SHADES.pct_vm[3], // 45-60%
                60, CENSUS_SHADES.pct_vm[4], // 60-75%
                75, CENSUS_SHADES.pct_vm[5], // 75-90%
                90, CENSUS_SHADES.pct_vm[6], // 90%+
            ];
        }
        else if (curCensusVariable === "avg_hou_inc") {
            const values = geoJsonData.features.map(f => f.properties.avg_hou_inc);
            const min = Math.min(...values);
            const max = Math.max(...values);
            const step = (max - min) / 6;

            paintConfig = [
                "interpolate",
                ["linear"],
                ["get", curCensusVariable],
                min, CENSUS_SHADES.avg_hou_inc[0],
                min + step, CENSUS_SHADES.avg_hou_inc[1],
                min + 2 * step, CENSUS_SHADES.avg_hou_inc[2],
                min + 3 * step, CENSUS_SHADES.avg_hou_inc[3],
                min + 4 * step, CENSUS_SHADES.avg_hou_inc[4],
                min + 5 * step, CENSUS_SHADES.avg_hou_inc[5],
                max, CENSUS_SHADES.avg_hou_inc[6]
            ];
        }

        map2.addLayer({
            id: "census-variable",
            type: "fill",
            source: "census-variable",
            paint: {
                "fill-color": paintConfig,
                "fill-opacity": 0.9
            }
        }, 'labels-layer');

        map2.addLayer({
            id: "census-variable-boundary",
            type: "line",
            source: "census-variable",
            paint: {
                "line-color": "#ffffff",
                "line-width": [
                    "case",
                    ["boolean", ["feature-state", "hover"], false],
                    3, // Highlighted line width
                    0.5 // Default line width
                ]
            }
        }, 'labels-layer');
    }

    // Function to handle hover and click events
    function handleRidingInteraction(map, event) {
        const layersToQuery = map === map1 ? ["party-vote-share"] : ["census-variable"];
        const existingLayers = layersToQuery.filter(layer => map.getLayer(layer));

        if (existingLayers.length === 0) return;

        const features = map.queryRenderedFeatures(event.point, {
            layers: existingLayers
        });

        // Reset the hover state for the previously highlighted riding
        if (hoveredRidingId !== null) {
            if (map1.getLayer("party-vote-share")) {
                map1.setFeatureState(
                    { source: "party-vote-share", id: hoveredRidingId },
                    { hover: false }
                );
            }
            if (map2.getLayer("census-variable")) {
                map2.setFeatureState(
                    { source: "census-variable", id: hoveredRidingId },
                    { hover: false }
                );
            }
        }

        if (features.length > 0) {
            const feature = features[0];
            hoveredRidingId = feature.id; // Use feature.id
            hoveredRidingData = feature.properties;

            // Ensure the name property is correctly accessed
            hoveredRidingData.name = feature.properties.geoname || "Unknown Riding";

            // Highlight the riding on both maps
            if (map1.getLayer("party-vote-share")) {
                map1.setFeatureState(
                    { source: "party-vote-share", id: hoveredRidingId },
                    { hover: true }
                );
            }
            if (map2.getLayer("census-variable")) {
                map2.setFeatureState(
                    { source: "census-variable", id: hoveredRidingId },
                    { hover: true }
                );
            }
        } else {
            // If no riding is hovered, reset the hover state
            hoveredRidingId = null;
            hoveredRidingData = null;
        }
    }

    $effect(() => {
        if (geoJsonData) {
            updatePartyMapLayer();
            updateCensusMapLayer();

            // Add hover and click event listeners to both maps
            map1.on("mousemove", (e) => handleRidingInteraction(map1, e));
            map1.on("mouseleave", () => {
                if (hoveredRidingId !== null) {
                    if (map1.getLayer("party-vote-share")) {
                        map1.setFeatureState(
                            { source: "party-vote-share", id: hoveredRidingId },
                            { hover: false }
                        );
                    }
                    if (map2.getLayer("census-variable")) {
                        map2.setFeatureState(
                            { source: "census-variable", id: hoveredRidingId },
                            { hover: false }
                        );
                    }
                    hoveredRidingId = null;
                    hoveredRidingData = null;
                }
            });
            map1.on("click", (e) => handleRidingInteraction(map1, e));

            map2.on("mousemove", (e) => handleRidingInteraction(map2, e));
            map2.on("mouseleave", () => {
                if (hoveredRidingId !== null) {
                    if (map1.getLayer("party-vote-share")) {
                        map1.setFeatureState(
                            { source: "party-vote-share", id: hoveredRidingId },
                            { hover: false }
                        );
                    }
                    if (map2.getLayer("census-variable")) {
                        map2.setFeatureState(
                            { source: "census-variable", id: hoveredRidingId },
                            { hover: false }
                        );
                    }
                    hoveredRidingId = null;
                    hoveredRidingData = null;
                }
            });
            map2.on("click", (e) => handleRidingInteraction(map2, e));
        }
    });

    onMount(() => {
        map1 = new maplibregl.Map({
            container: "map1",
            ...mapConfig
        });

        map1.addControl(new maplibregl.NavigationControl(navControlConfig), 'top-right');
        map1.addControl(new maplibregl.ScaleControl(scaleControlConfig), 'bottom-left');

        map2 = new maplibregl.Map({
            container: "map2",
            ...mapConfig
        });

        map2.addControl(new maplibregl.NavigationControl(navControlConfig), 'top-right');
        map2.addControl(new maplibregl.ScaleControl(scaleControlConfig), 'bottom-left');

        // Sync both maps
        syncMaps(map1, map2);
        syncMaps(map2, map1);

        // Use the consolidated function to add labels
        map1.on('load', () => {
            addLabelsToMap(map1, loadGeoJson);
        });

        map2.on('load', () => {
            addLabelsToMap(map2);
        });
    });
</script>

<div class="container">
    <div class="sentence-controls">
        <p>
            I want to see data for the 
            <select onchange={handleYearChange} class="inline-select">
                {#each years as y}
                    <option value={y} selected={y === curYear}>{y}</option>
                {/each}
            </select>
            <select onchange={handleRegionChange} class="inline-select">
                <option value="federal">federal</option>
                <option value="ontario" selected>Ontario</option>
            </select>
            election.
            Show me the party vote share for the
            <select onchange={handlePartyChange} class="inline-select">
                {#each curParties as party}
                    <option value={party.tag} selected={party.tag === curParty}>{party.name}</option>
                {/each}
            </select>
            with the census data for
            <select onchange={handleCensusVariableChange} class="inline-select">
                {#each curCensusVars as variable}
                    <option value={variable.propertyTag}>{variable.name.toLowerCase()}</option>
                {/each}
            </select>.
        </p>
    </div>
</div>

<div class="map-container">
    <div class="map-section">
        <Legend 
            title="% Party Vote" 
            colors={PARTY_SHADES[curParty]} 
            labels={partyLabels}
        />
        <div id="map1" class="map"></div>
    </div>
    <div class="map-section">
        <Legend 
            title={(
                curCensusVariable === 'pct_imm' ? '% Immigrants' : // if 
                curCensusVariable === 'pct_vm' ? "% Visible Minorities" : // else if 
                curCensusVariable === 'avg_hou_inc' ? 'Avg. Household Income' : // else if 
                null // else 
            )}
            colors={CENSUS_SHADES[curCensusVariable]} 
            labels={censusLabels}
        />
        <div id="map2" class="map"></div>
    </div>
</div>

<div class="container">
    <!-- First Row: Riding Name -->
    <div class="info-row">
        {#if hoveredRidingData}
            <p><b>{hoveredRidingData.name}</b></p>
        {:else}
            <p><i>Hover/click on a riding</i></p>
        {/if}
    </div>

    <!-- Second Row: Party Vote -->
    <div class="info-row">
        {#if PARTIES_INFO}
            {#if hoveredRidingData}
                {@const party = PARTIES_INFO.find(p => p.tag === curParty)}
                {#if hoveredRidingData[party.propertyTag] !== undefined}
                    <p>Vote share = <b>{(hoveredRidingData[party.propertyTag]).toFixed(1)}%</b></p>
                {:else}
                    <p>Vote share = <b>N/A</b></p>
                {/if}
            {:else}
                <p>Vote share = <b>N/A</b></p>
            {/if}
        {/if}
    </div>

    <!-- Third Row: Census Variable -->
    <div class="info-row">
        {#if curCensusVars}
            {#if hoveredRidingData}
                {@const censusVar = curCensusVars.find(v => v.propertyTag === curCensusVariable)}
                {#if hoveredRidingData[curCensusVariable] !== undefined}
                    {@const censusVal = hoveredRidingData[curCensusVariable]}
                    {#if curCensusVariable === 'pct_imm'}
                        <p>{censusVar.name} = <b>{censusVal.toFixed(1)}%</b></p>
                    {:else if curCensusVariable === 'avg_hou_inc'}
                        <p>{censusVar.name} = <b>${Math.round(censusVal / 1000)}K</b></p>
                    {:else if curCensusVariable === 'pct_vm'}
                        <p>{censusVar.name} = <b>{censusVal.toFixed(1)}%</b></p>
                    {:else}
                        <p>{censusVar.name} = <b>N/A</b></p>
                    {/if}
                {:else}
                    <p>{censusVar.name} = <b>N/A</b></p>
                {/if}
            {:else}
                {@const censusVar = curCensusVars.find(v => v.propertyTag === curCensusVariable)}
                <p>{censusVar.name} = <b>N/A</b></p>
            {/if}
        {/if}
    </div>
</div>

<style>
    .map-container {
        max-width: 1600px;
        display: flex;
        gap: 10px;
        margin: 0 auto;
        width: calc(100% - 20px);
    }

    .map-section {
        flex: 1;
        min-width: 0;
    }

    .map {
        width: 100%;
        height: 500px;
        border: solid 1px var(--brandGray);
    }

    @media (max-width: 700px) {
        .map-container {
            flex-direction: column;
            gap: 10px;
            margin: 10px;
            width: calc(100% - 20px);
        }

        .map-section {
            width: 100%;
        }
    }
</style>