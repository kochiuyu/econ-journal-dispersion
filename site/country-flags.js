/* Decorative flags for country and territory labels. SVGs are served by https://flagcdn.com/. */
(function () {
  "use strict";

  var codes = (
    "AD AE AF AG AI AL AM AO AQ AR AS AT AU AW AX AZ BA BB BD BE BF BG BH BI BJ BL BM BN BO BQ BR BS BT BV BW BY BZ " +
    "CA CC CD CF CG CH CI CK CL CM CN CO CR CU CV CW CX CY CZ DE DJ DK DM DO DZ EC EE EG EH ER ES ET FI FJ FK FM FO FR " +
    "GA GB GD GE GF GG GH GI GL GM GN GP GQ GR GS GT GU GW GY HK HM HN HR HT HU ID IE IL IM IN IO IQ IR IS IT JE JM JO JP " +
    "KE KG KH KI KM KN KP KR KW KY KZ LA LB LC LI LK LR LS LT LU LV LY MA MC MD ME MF MG MH MK ML MM MN MO MP MQ MR MS " +
    "MT MU MV MW MX MY MZ NA NC NE NF NG NI NL NO NP NR NU NZ OM PA PE PF PG PH PK PL PM PN PR PS PT PW PY QA RE RO RS " +
    "RU RW SA SB SC SD SE SG SH SI SJ SK SL SM SN SO SR SS ST SV SX SY SZ TC TD TF TG TH TJ TK TL TM TN TO TR TT TV TW " +
    "TZ UA UG UM US UY UZ VA VC VE VG VI VN VU WF WS XK YE YT ZA ZM ZW"
  ).split(" ");
  var byName = new Map();

  function key(name) {
    return name.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[^a-z0-9]/g, "");
  }

  codes.forEach(function (code) { byName.set(key(code), code); });
  if (typeof Intl.DisplayNames === "function") {
    ["long", "short"].forEach(function (style) {
      var names = new Intl.DisplayNames("en", { type: "region", style: style, fallback: "none" });
      codes.forEach(function (code) {
        var name = names.of(code);
        if (name) byName.set(key(name), code);
      });
    });
  }

  var aliases = {
    "Bosnia and Herzegovina": "BA",
    "Czech Republic": "CZ",
    "Hong Kong SAR China": "HK",
    "Iran (Islamic Republic of)": "IR",
    "Korea, Republic of": "KR",
    "Lao People's Democratic Republic": "LA",
    "Macao SAR China": "MO",
    "Macau": "MO",
    "Republic of Korea": "KR",
    "Russian Federation": "RU",
    "State of Palestine": "PS",
    "Taiwan, Province of China": "TW",
    "Türkiye": "TR",
    "Turkey": "TR",
    "UK": "GB",
    "United States of America": "US",
    "USA": "US",
    "Viet Nam": "VN"
  };
  Object.keys(aliases).forEach(function (name) { byName.set(key(name), aliases[name]); });

  function update(container, country) {
    if (!container) return;
    var code = byName.get(key(country || ""));
    var existing = container.querySelector(".country-flag");
    if (existing && existing.dataset.code === code) return;
    if (existing) existing.remove();
    if (!code) return;

    var flag = document.createElement("img");
    flag.className = "country-flag";
    flag.dataset.code = code;
    flag.alt = "";
    flag.width = 18;
    flag.height = 12;
    flag.loading = "lazy";
    flag.referrerPolicy = "no-referrer";
    flag.addEventListener("error", function () { flag.hidden = true; });
    flag.src = "https://flagcdn.com/" + code.toLowerCase() + ".svg";
    container.prepend(flag);
  }

  window.updateCountryFlag = update;
})();
