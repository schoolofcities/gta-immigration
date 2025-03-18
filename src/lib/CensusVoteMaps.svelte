<script>
    import { onMount } from "svelte";
    import maplibregl from "maplibre-gl";
    import "maplibre-gl/dist/maplibre-gl.css";
    import { FELXN_YEARS, ONTELXN_YEARS } from "../lib/constants.js";

    let map1, map2;
    const defaultCenter = [-79.3832, 43.6532];
    const defaultZoom = 9;
    const defaultMinZoom = 8;
    const defaultMaxZoom = 11;
    const maxBounds = [
        [-81.0, 42.5],  // Southwest corner (near London, ON)
        [-78.0, 45.0]   // Northeast corner (north of Peterborough)
    ];

    // Prevent infinite update loops
    let syncing = false;

    let curRegion = $state("fed");
    let curYear = $state(2021);
    let years = $state(FELXN_YEARS);
    let geoJsonData = $state(null);

    let parties = $state([]);
    let censusVariables = $state([]);

    let curParty = $state("lib_pct");
    let curCensusVariable = $state("pct_imm");

    const partyColors = {
        lib_pct: ["#f5c3c5", "#f1a6a9", "#ec888c", "#e76a6f", "#e34d53", "#de2f36", "#da121a", "#be0f16"],
        cons1_pct: ["#c4c9d2", "#a7aebb", "#8a93a5", "#6c788f", "#4f5d78", "#324262", "#15284c", "#122342"],
        ndp_pct: ["#fbdebf", "#f9cd9f", "#f7bd7f", "#f5ad5f", "#f39c3f", "#f18c1f", "#f07c00", "#d26c00"],
        cons2_pct: ["#caecda", "#b0e3c7", "#96dab5", "#7bd0a2", "#61c790", "#47be7d", "#2db56b", "#279e5d"]
    };

    const censusColors = {
        pct_imm: ["#dfe7e2", "#bfd0c6", "#9fb8a9", "#7fa18d", "#5f8a70", "#3f7254", "#1f5b37", "#00441b"], // Darker green
        avg_hou_inc: ["#ffffcc", "#ffeda0", "#fed976", "#feb24c", "#fd8d3c", "#f03b20", "#d95f0e"] // Not very dark yellow
    };

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

    function updateSelectOptions() {
        if (geoJsonData && geoJsonData.features.length > 0) {
            const properties = geoJsonData.features[0].properties;

            parties = [];
            if (properties.lib_pct !== null) parties.push({ name: "Liberals", property: "lib_pct" });
            if (properties.cons1_pct !== null) parties.push({ name: "Conservatives", property: "cons1_pct" });
            if (properties.ndp_pct !== null) parties.push({ name: "New Democrats", property: "ndp_pct" });
            if (properties.cons2_pct !== null) parties.push({ name: "Reform/Alliance", property: "cons2_pct" });

            censusVariables = [];
            if (properties.pct_imm !== null) censusVariables.push({ name: "Percent immigrants", property: "pct_imm" });
            if (properties.avg_hou_inc !== null) censusVariables.push({ name: "Average Household Income", property: "avg_hou_inc" });

            // Ensure curParty and curCensusVariable are valid
            if (!parties.some(p => p.property === curParty)) {
                curParty = parties.length > 0 ? parties[0].property : null;
            }
            if (!censusVariables.some(v => v.property === curCensusVariable)) {
                curCensusVariable = censusVariables.length > 0 ? censusVariables[0].property : null;
            }
        }
    }

    function loadGeoJson() {
        const filePath = `/data/elections/${curRegion}_stats_${curYear}.geojson`;
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

    function handleRegionChange(event) {
        curRegion = event.target.value;
        years = curRegion === "fed" ? FELXN_YEARS : ONTELXN_YEARS;
        curYear = years[years.length - 1];
        loadGeoJson();
    }

    function handleYearChange(event) {
        curYear = event.target.value;
        loadGeoJson();
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

        map1.addLayer({
            id: "party-vote-share",
            type: "fill",
            source: "party-vote-share",
            paint: {
                "fill-color": [
                    "step",
                    ["get", curParty],
                    partyColors[curParty][0], 0,
                    partyColors[curParty][1], 10,
                    partyColors[curParty][2], 20,
                    partyColors[curParty][3], 30,
                    partyColors[curParty][4], 40,
                    partyColors[curParty][5], 50,
                    partyColors[curParty][6], 60,
                    partyColors[curParty][7] // above 60
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
                censusColors.pct_imm[0], 0,
                censusColors.pct_imm[1], 0.1,
                censusColors.pct_imm[2], 0.2,
                censusColors.pct_imm[3], 0.3,
                censusColors.pct_imm[4], 0.4,
                censusColors.pct_imm[5], 0.5,
                censusColors.pct_imm[6], 0.6,
                censusColors.pct_imm[7], 0.7,
                censusColors.pct_imm[7] // above 0.7
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
                min, censusColors.avg_hou_inc[0],
                min + step, censusColors.avg_hou_inc[1],
                min + 2 * step, censusColors.avg_hou_inc[2],
                min + 3 * step, censusColors.avg_hou_inc[3],
                min + 4 * step, censusColors.avg_hou_inc[4],
                min + 5 * step, censusColors.avg_hou_inc[5],
                max, censusColors.avg_hou_inc[6]
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

    function handlePartyChange(event) {
        curParty = event.target.value;
        updatePartyMapLayer();
    }

    function handleCensusVariableChange(event) {
        curCensusVariable = event.target.value;
        updateCensusMapLayer();
    }

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

<div class="controls">
    <select onchange={handleRegionChange}>
        <option value="fed" selected>Federal</option>
        <option value="ont-ed">Ontario</option>
    </select>
    <select onchange={handleYearChange}>
        {#each years as y}
            <option value={y} selected={y === curYear}>{y}</option>
        {/each}
    </select>
</div>

<div class="map-container">
    <div class="map-section">
        <div class="map-controls">
            <select onchange={handlePartyChange}>
                {#each parties as party}
                    <option value={party.property}>{party.name}</option>
                {/each}
            </select>
        </div>
        <div id="map1" class="map"></div>
    </div>
    <div class="map-section">
        <div class="map-controls">
            <select onchange={handleCensusVariableChange}>
                {#each censusVariables as variable}
                    <option value={variable.property}>{variable.name}</option>
                {/each}
            </select>
        </div>
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
    .map-controls {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }
    .map-section {
        display: flex;
        flex-direction: column;
        width: 50%;
    }
</style>