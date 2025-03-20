<script>
    import { onMount } from "svelte";
    import maplibregl from "maplibre-gl";
    import "maplibre-gl/dist/maplibre-gl.css";
    import { FELXN_YEARS, ONTELXN_YEARS, PARTY_SHADES, CENSUS_SHADES, PARTIES_INFO } from "../lib/constants.js";
    import { getRegionTag, updateCensusVarOptions, updatePartyOptions } from "./utils.js";

    let map1, map2;
    const defaultCenter = [-79.3832, 43.6532];
    const defaultZoom = 9;
    const defaultMinZoom = 8;
    const defaultMaxZoom = 11;
    const maxBounds = [
        [-81.0, 42.5],  // Southwest corner (near London, ON)
        [-78.0, 45.0]   // Northeast corner (north of Peterborough)
    ];

    let curRegion = $state("federal");
    let curRegionTag = $derived(getRegionTag(curRegion));

    let curYear = $state(2021);
    let years = $state(FELXN_YEARS);

    let geoJsonData = $state(null);

    let curParties = $derived(updatePartyOptions(geoJsonData));
    let curParty = $state("lib");

    let curCensusVars = $derived(updateCensusVarOptions(geoJsonData));
    let curCensusVariable = $state("pct_imm");

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

    function loadGeoJson() {
        const filePath = `/data/elections/${curRegionTag}_stats_${curYear}.geojson`;
        fetch(filePath)
            .then(response => response.json())
            .then(data => {
                geoJsonData = data;
                // console.log($state.snapshot(geoJsonData));
                updateSelectOptions();
                updatePartyMapLayer();
                updateCensusMapLayer();
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
                    PARTY_SHADES[curParty][0], 0,
                    PARTY_SHADES[curParty][1], 10,
                    PARTY_SHADES[curParty][2], 20,
                    PARTY_SHADES[curParty][3], 30,
                    PARTY_SHADES[curParty][4], 40,
                    PARTY_SHADES[curParty][5], 50,
                    PARTY_SHADES[curParty][6], 60,
                    PARTY_SHADES[curParty][7] // above 60
                ],
                "fill-opacity": 0.75
            }
        });

        map1.addLayer({
            id: "party-vote-share-boundary",
            type: "line",
            source: "party-vote-share",
            paint: {
                "line-color": "#000000",
                "line-width": 0.5
            }
        });
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
                CENSUS_SHADES.pct_imm[0], 0,
                CENSUS_SHADES.pct_imm[1], 10,
                CENSUS_SHADES.pct_imm[2], 20,
                CENSUS_SHADES.pct_imm[3], 30,
                CENSUS_SHADES.pct_imm[4], 40,
                CENSUS_SHADES.pct_imm[5], 50,
                CENSUS_SHADES.pct_imm[6], 60,
                CENSUS_SHADES.pct_imm[7], 70,
                CENSUS_SHADES.pct_imm[7] // above 70
            ];
        } else if (curCensusVariable === "avg_hou_inc") {
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
                "fill-opacity": 0.75
            }
        });

        map2.addLayer({
            id: "census-variable-boundary",
            type: "line",
            source: "census-variable",
            paint: {
                "line-color": "#000000",
                "line-width": 0.5
            }
        });
    }

    $effect(() => {
        if (geoJsonData) {
            updatePartyMapLayer();
            updateCensusMapLayer();
        }
    });

    onMount(() => {
        map1 = new maplibregl.Map({
            container: "map1",
            style: "https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",
            center: defaultCenter, // Example: Toronto
            zoom: defaultZoom,
            maxZoom: defaultMaxZoom,
            minZoom: defaultMinZoom,
            maxBounds: maxBounds,
        });

        map2 = new maplibregl.Map({
            container: "map2",
            style: "https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",
            center: defaultCenter, // Same starting position
            zoom: defaultZoom,
            maxZoom: defaultMaxZoom,
            minZoom: defaultMinZoom,
            maxBounds: maxBounds,
        });

        // Sync both maps
        syncMaps(map1, map2);
        syncMaps(map2, map1);

        loadGeoJson();
    });
</script>

<div class="container">
    <div class="controls">
        <div class="control-row">
            <select onchange={handleRegionChange}>
                <option value="federal" selected>Federal</option>
                <option value="ontario">Ontario</option>
            </select>
            <select onchange={handleYearChange}>
                {#each years as y}
                    <option value={y} selected={y === curYear}>{y}</option>
                {/each}
            </select>
        </div>
        <div class="control-row">
            <select onchange={handlePartyChange}>
                {#each curParties as party}
                    <option value={party.tag}>{party.name}</option>
                {/each}
            </select>
            <select onchange={handleCensusVariableChange}>
                {#each curCensusVars as variable}
                    <option value={variable.propertyTag}>{variable.name}</option>
                {/each}
            </select>
        </div>
    </div>
</div>

<div class="map-container">
    <div class="map-section">
        <div id="map1" class="map"></div>
    </div>
    <div class="map-section">
        <div id="map2" class="map"></div>
    </div>
</div>

<style>
    .map-container {
        display: flex;
        gap: 10px;
    }
    .map {
        width: 100%;
        height: 500px;
    }
    .controls {
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-bottom: 10px;
    }
    .control-row {
        display: flex;
        gap: 10px;
        justify-content: space-between;
    }
    .control-row select {
        width: 48%;
    }
    .map-section {
        display: flex;
        flex-direction: column;
        width: 50%;
    }

    @media (max-width: 700px) {
        .map-container {
            flex-direction: column;
        }
        .map-section {
            width: 100%;
        }
    }
</style>