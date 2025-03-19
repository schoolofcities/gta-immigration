import { PARTIES_INFO } from "./constants";

export function getRegionTag(region) {
    return region == "federal" ? "fed" : "ont-ed"
}

export function updatePartyOptions(geoJsonData) {
    if (geoJsonData && geoJsonData.features.length > 0) {
        const properties = geoJsonData.features[0].properties;
        
        let parties = [];
        if (properties.lib_pct !== null) parties.push(PARTIES_INFO[0]);
        if (properties.cons1_pct !== null) parties.push(PARTIES_INFO[1]);
        if (properties.cons2_pct !== null) parties.push(PARTIES_INFO[2]);
        if (properties.ndp_pct !== null) parties.push(PARTIES_INFO[3]);

        return parties;
    }
}

export function updateCensusVarOptions(geoJsonData) {
    if (geoJsonData && geoJsonData.features.length > 0) {
        const properties = geoJsonData.features[0].properties;
        
        let censusVars = [];
        if (properties.pct_imm !== null) censusVars.push({ name: "Percent immigrants", propertyTag: "pct_imm" });
        if (properties.avg_hou_inc !== null) censusVars.push({ name: "Average Household Income", propertyTag: "avg_hou_inc" });

        return censusVars;
    }
}