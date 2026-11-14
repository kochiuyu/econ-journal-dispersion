/* Journal images are matched by complete title, never by publisher alone. */
(function () {
  "use strict";
  var images = {"accountingorganizationsandsociety":"aos.webp","americaneconomicreview":"aer.webp","harvardbusinessreview":"hbr.webp","journalofaccountingandeconomics":"jae.webp","journalofbusinessventuring":"jbv.webp","journaloffinancialandquantitativeanalysis":"jfqa.webp","journaloffinancialeconomics":"jfe.webp","journalofinternationalbusinessstudies":"jibs.webp","journaloftheacademyofmarketingscience":"jams.webp","organizationalbehaviorandhumandecisionprocesses":"obhdp.webp","researchpolicy":"rp.webp","reviewofaccountingstudies":"rast.webp","reviewofeconomicstudies":"restud.svg","contemporaryaccountingresearch":"car.webp","econometrica":"econometrica.webp","humanresourcemanagement":"hrm.webp","journalofaccountingresearch":"jar.webp","journalofconsumerpsychology":"jcp.webp","journaloffinance":"jf.webp","journalofmanagementstudies":"jms.webp","journalofoperationsmanagement":"joom.webp","strategicentrepreneurshipjournal":"sej.webp","americansociologicalreview":"asr.webp","journalofmanagementinformationsystems":"jmis.webp","strategicmanagementjournal":"smj.webp","administrativesciencequarterly":"asq.webp","entrepreneurshiptheoryandpractice":"etp.webp","psychologicalscience":"psych_sci.webp","journalofmarketingresearch":"jmr.webp","journalofmanagement":"jom.webp","productionandoperationsmanagement":"pom.webp","journalofmarketing":"jm.webp","informationsystemsresearch":"isr.webp","managementscience":"ms.webp","marketingscience":"mktg_sci.webp","manufacturingandserviceoperationsmanagement":"msom.webp","operationsresearch":"or.webp","organizationscience":"orgsci.webp","accountingreview":"tar.webp","misquarterly":"misq.webp","reviewoffinancialstudies":"rfs.webp","mitsloanmanagementreview":"sloan_mr.webp","reviewoffinance":"rof.webp","academyofmanagementannals":"aom_annals.webp","academyofmanagementjournal":"amj.webp","academyofmanagementreview":"amr.webp","journalofpoliticaleconomy":"jpe.webp","journalofbusinessresearch":"journal_business_research.webp","decisionsciences":"decision_sciences.webp","journalofbusinessandpsychology":"journal_business_psychology.webp","industrialmarketingmanagement":"industrial_marketing_management.webp","journalofcomputerinformationsystems":"journal_computer_information_systems.webp","internationaljournalofadvertising":"international_journal_advertising.webp","cognitivescience":"cognitive_science.webp","journalofsupplychainmanagement":"journal_supply_chain_management.webp","internationaljournalofresearchinmarketing":"international_journal_research_marketing.webp","eventmanagement":"event_management.webp","journaloforganizationalbehavior":"journal_organizational_behavior.webp","groupandorganizationmanagement":"group_organization_management.webp","journalofbusinessethics":"journal_business_ethics.webp","organizationstudies":"organization_studies.webp","transportationresearchrecord":"transportation_research_record.webp","personnelpsychology":"personnel_psychology.webp","journalofbusinesslogistics":"journal_business_logistics.webp","internationaljournalofinformationmanagement":"international_journal_information_management.webp","journalofretailing":"journal_retailing.webp","journalofadvertisingresearch":"journal_advertising_research.webp","asiapacificjournalofmanagement":"asia_pacific_journal_management.webp","humanrelations":"human_relations.webp","journaloftheamericanstatisticalassociation":"journal_american_statistical_association.webp","journalofworldbusiness":"journal_world_business.webp","healthcommunication":"health_communication.webp","managementandorganizationreview":"management_organization_review.webp","internationaljournalofconsumerstudies":"international_journal_consumer_studies.webp","managementcommunicationquarterly":"management_communication_quarterly.webp","journalofinnovationandknowledge":"journal_innovation_knowledge.webp","journalofadvertising":"journal_advertising.webp","smallbusinesseconomics":"small_business_economics.webp","corporategovernanceaninternationalreview":"corporate_governance_international_review.webp","appliedpsychologyaninternationalreview":"applied_psychology_international_review.webp","journalofconsumerbehaviour":"journal_consumer_behaviour.webp","journalofglobalsportmanagement":"journal_global_sport_management.webp","journalofhospitalityandtourismresearch":"journal_hospitality_tourism_research.webp","socialscienceandmedicine":"social_science_medicine.webp","appliedenergy":"applied_energy.webp","journalofserviceresearch":"journal_service_research.webp","europeanjournalofinternationalmanagement":"european_journal_international_management.webp","annalsoftourismresearch":"annals_tourism_research.webp","organization":"organization.webp","accountingforum":"accounting_forum.webp","businessandsociety":"business_society.webp","longrangeplanning":"long_range_planning.webp","journalofvocationalbehavior":"journal_vocational_behavior.webp","cogentbusinessandmanagement":"cogent_business_management.webp","journaloftravelresearch":"journal_travel_research.webp","journalofpublicpolicyandmarketing":"journal_public_policy_marketing.webp","strategicorganization":"strategic_organization.webp"};
  var failed = new Set();

  function key(name) {
    return String(name || "").normalize("NFKC").toLowerCase()
      .replace(/^the\s+/, "").replace(/&/g, "and")
      .replace(/[^\p{L}\p{N}]+/gu, "");
  }
  function initials(name) {
    var words = String(name || "").match(/[\p{L}\p{N}]+/gu) || [];
    words = words.filter(function (word) { return !/^(the|a|an|and|of|for|in|on|at|to)$/i.test(word); });
    return words.slice(0, 3).map(function (word) { return Array.from(word)[0]; }).join("").toUpperCase() || "J";
  }
  function prepend(cell, name) {
    if (!name || cell.querySelector(".journal-identity")) return;
    var identity = document.createElement("span");
    identity.className = "journal-identity";
    var label = document.createElement("span");
    label.className = "journal-label";
    while (cell.firstChild) label.appendChild(cell.firstChild);
    var mark = document.createElement("span");
    mark.className = "journal-mark";
    mark.setAttribute("aria-hidden", "true");
    mark.textContent = initials(name);
    var asset = images[key(name)];
    if (asset && !failed.has(asset)) {
      var img = document.createElement("img");
      img.src = "assets/journals/" + asset;
      img.alt = "";
      img.width = 24;
      img.height = 30;
      img.loading = "lazy";
      img.decoding = "async";
      img.setAttribute("fetchpriority", "low");
      img.addEventListener("error", function () { failed.add(asset); img.remove(); });
      mark.appendChild(img);
    }
    identity.append(mark, label);
    cell.appendChild(identity);
  }
  window.journalIcons = { prepend: prepend };
})();
