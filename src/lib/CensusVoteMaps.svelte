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

    let region = $state("fed");
    let year = $state(2021);
    let years = $state(FELXN_YEARS);
    let geoJsonData = $state(null);

    let parties = $state([]);
    let censusVariables = $state([]);

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
            if (properties.lib_pct !== null) parties.push("Liberals");
            if (properties.cons1_pct !== null) parties.push("Conservatives");
            if (properties.ndp_pct !== null) parties.push("New Democrats");
            if (properties.cons2_pct !== null) parties.push("Reform/Alliance");

            censusVariables = [];
            if (properties.pct_imm !== null) censusVariables.push("Percent immigrants");
            if (properties.avg_hou_inc !== null) censusVariables.push("Average Household Income");
        }
    }

    function loadGeoJson() {
        const filePath = `/data/elections/${region}_stats_${year}.geojson`;
        fetch(filePath)
            .then(response => response.json())
            .then(data => {
                geoJsonData = data;
                console.log($state.snapshot(geoJsonData));
                updateSelectOptions();
            });
    }

    function handleRegionChange(event) {
        region = event.target.value;
        years = region === "fed" ? FELXN_YEARS : ONTELXN_YEARS;
        year = years[years.length - 1];
        loadGeoJson();
    }

    function handleYearChange(event) {
        year = event.target.value;
        loadGeoJson();
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
            <option value={y} selected={y === year}>{y}</option>
        {/each}
    </select>
</div>

<div class="map-container">
    <div class="map-section">
        <div class="map-controls">
            <select>
                {#each parties as party}
                    <option value={party}>{party}</option>
                {/each}
            </select>
        </div>
        <div id="map1" class="map"></div>
    </div>
    <div class="map-section">
        <div class="map-controls">
            <select>
                {#each censusVariables as variable}
                    <option value={variable}>{variable}</option>
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