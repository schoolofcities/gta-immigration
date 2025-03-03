<script>
    import { onMount } from "svelte";
    import maplibregl from "maplibre-gl";
    import "maplibre-gl/dist/maplibre-gl.css";

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
    });
</script>

<style>
    .map-container {
        display: flex;
        gap: 10px;
    }
    .map {
        width: 50%;
        height: 500px;
    }
</style>

<div class="map-container">
    <div id="map1" class="map"></div>
    <div id="map2" class="map"></div>
</div>
