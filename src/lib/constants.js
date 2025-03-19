export const FELXN_YEARS = [
    1962, 1963, 1965, 1968, 1972, 1974, 1979, 1980, 1984, 1988, 
    1993, 1997, 2000, 2004, 2006, 2008, 2011, 2015, 2019, 2021
];

export const ONTELXN_YEARS = [
    1963, 1967, 1971, 1975, 1977, 1981, 1985, 1987, 1990, 1995, 
    1999, 2003, 2007, 2011, 2014, 2018, 2022, 2025
];

export const PARTIES_INFO = [
    {"name": "Liberals", "tag": "lib", "propertyTag": "lib_pct"},
    {"name": "Conservatives", "tag": "cons1", "propertyTag": "cons1_pct"},
    {"name": "Reform/Alliance", "tag": "cons2", "propertyTag": "cons2_pct"},
    {"name": "New Democrats", "tag": "ndp", "propertyTag": "ndp_pct"},
]

export const PARTY_TAG_MAP = {
    "Liberals": "lib_pct",
    "Conservatives": "cons1_pct",
    "New Democrats": "ndp_pct"
};

export const PARTY_COLOURS = {
    lib_pct: "#da121a",
    cons1_pct: "#15284c", 
    ndp_pct: "#f07c00", 
    cons2_pct: "#2db56b", 
};

export const PARTY_SHADES = {
    lib: ["#f5c3c5", "#f1a6a9", "#ec888c", "#e76a6f", "#e34d53", "#de2f36", "#da121a", "#be0f16"],
    cons1: ["#c4c9d2", "#a7aebb", "#8a93a5", "#6c788f", "#4f5d78", "#324262", "#15284c", "#122342"],
    ndp: ["#fbdebf", "#f9cd9f", "#f7bd7f", "#f5ad5f", "#f39c3f", "#f18c1f", "#f07c00", "#d26c00"],
    cons2: ["#caecda", "#b0e3c7", "#96dab5", "#7bd0a2", "#61c790", "#47be7d", "#2db56b", "#279e5d"]
};

export const CENSUS_SHADES = {
    pct_imm: ["#dfe7e2", "#bfd0c6", "#9fb8a9", "#7fa18d", "#5f8a70", "#3f7254", "#1f5b37", "#00441b"], // Darker green
    avg_hou_inc: ["#ffffcc", "#ffeda0", "#fed976", "#feb24c", "#fd8d3c", "#f03b20", "#d95f0e"] // Not very dark yellow
};