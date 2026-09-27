---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology extends the primary regulatory agencies ontology in FBC with additional regulators that are specific
      to the United States and augments certain U.S. financial services entities based on who regulates them.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2015-2025 Object Management Group,\
      \ Inc.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\
      \ documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the\
      \ rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit\
      \ persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice\
      \ and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE\
      \ IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\
      \ OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\
      \ HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\
      \ ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\t\
      See https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: US Regulatory Agencies Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/20230301/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of the ontology was modified to eliminate deprecations that are more than 6 months old, primarily related to
      name changes to better map to the legislation that defines the concepts.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20150801/FunctionalEntities/USJurisdiction/USRegulatoryAgencies.rdf
      version of this ontology was modified per the issue resolutions identified in the FIBO FBC 1.0 FTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20160801/FunctionalEntities/USJurisdiction/USRegulatoryAgencies.rdf
      version of this ontology was modified per the FIBO 2.0 RFC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/FunctionalEntities/USJurisdiction/USRegulatoryAgencies.rdf
      version of this ontology was modified to integrate a financial services provider identifier for certain banking identifiers,
      add a property for secondary federal regulator, add individual registration schemes for state-specific business registries,
      improve on some definitions, normalize some of the labels, eliminate duplication of concepts in LCC, to simplify addresses,
      merge countries with locations in FND, eliminte the redundant notion of an InstitutionType, which can be determined
      using a SPARQL query or classification and results in a very large disjunction, and correct a couple of improperly defined
      annotations.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200401/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of this ontology was revised to replace uses of hasTag in Relations with hasTag from LCC, as the more complex
      union of datatypes in the Relations concept is not needed here.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200701/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of this ontology was revised to add tax identification number, employer identification number, federal government
      entity and state government entity.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20201201/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of this ontology was revised to eliminate references to external dictionary sites that no longer resolve and
      clean up circular and ambiguous definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210101/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of this ontology was revised to add a restriction on PrimaryFederalRegulator to say that it must be a government
      body.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210401/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of this ontology was revised to reflect the move of certain organization-specific concepts from BE to FND.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20211001/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of this ontology was revised to correct a restriction defining state government entities and to make federal
      reserve district identifier a subclass of geographic region identifier and fix spelling errors.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20211201/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of this ontology was revised to eliminate dead links and address text formatting issues identified by hygiene
      testing.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than
      the OMG's Specification Metadata vocabulary and augmented to support better mapping to the NIC repository.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages,
      Countries and Codes (LCC), to eliminate redundancies in FIBO, and to augment the number and nature of financial institution
      entity types to cover more of the National Information Center (NIC) repository managed by the FFIEC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231101/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons)
      v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology
      Library (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of the ontology was modified to further reflect changes made in Commons v1.2 (FBC-338) and eliminate unused
      references and streamline representation (SEC-205).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251001/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of the ontology was modified to merge details from the old corporations ontology into corporate bodies for consistency
      and useability (BE-259).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251002/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of the ontology was modified to improve clarity, eliminate circularity due to migration of the original US Financial
      Services Entities Individuals to Commercial Registration Authorities, and for better alignment with the GLEIF LEI repository
      for broader FIBO usage (FND-407).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20260202/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
      version of the ontology was modified to eliminate the use of duplicate properties now available in Commons (FND-412).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2020-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2020-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/
  - concept: /concepts/fibo/BE/LegalEntities/LEIEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/20260701/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Parties/Parties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/
  - concept: /concepts/fibo/FND/Places/Addresses.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Locations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: US Regulatory Agencies Ontology
type: Ontology Definition
---

# US Regulatory Agencies Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/>

## Relationships

- **Related to**: [GovernmentEntities](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities.md)
- **Related to**: [USGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [CorporateBodies](/concepts/fibo/BE/LegalEntities/CorporateBodies.md)
- **Related to**: [FormalBusinessOrganizations](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md)
- **Related to**: [LEIEntities](/concepts/fibo/BE/LegalEntities/LEIEntities.md)
- **Related to**: [Executives](/concepts/fibo/BE/OwnershipAndControl/Executives.md)
- **Related to**: [BusinessCentersIndividuals](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals.md)
- **Related to**: [BusinessRegistries](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries.md)
- **Related to**: [CommercialRegistrationAuthorities](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.md)
- **Related to**: [FinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md)
- **Related to**: [USFinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [Parties](/concepts/fibo/FND/Parties/Parties.md)
- **Related to**: [Addresses](/concepts/fibo/FND/Places/Addresses.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Locations](<https://www.omg.org/spec/Commons/Locations/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [RegistrationAuthorities](<https://www.omg.org/spec/Commons/RegistrationAuthorities/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [ISO3166-1-CountryCodes](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-US](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/>)
- **Related to**: [USRegulatoryAgencies](<https://spec.edmcouncil.org/fibo/ontology/FBC/20260701/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology extends the primary regulatory agencies ontology in FBC with additional regulators that are specific to the United States and augments certain U.S. financial services entities based on who regulates them.
- **license**: Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2015-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: US Regulatory Agencies Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/20230301/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old, primarily related to name changes to better map to the legislation that defines the concepts.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20150801/FunctionalEntities/USJurisdiction/USRegulatoryAgencies.rdf version of this ontology was modified per the issue resolutions identified in the FIBO FBC 1.0 FTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20160801/FunctionalEntities/USJurisdiction/USRegulatoryAgencies.rdf version of this ontology was modified per the FIBO 2.0 RFC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/FunctionalEntities/USJurisdiction/USRegulatoryAgencies.rdf version of this ontology was modified to integrate a financial services provider identifier for certain banking identifiers, add a property for secondary federal regulator, add individual registration schemes for state-specific business registries, improve on some definitions, normalize some of the labels, eliminate duplication of concepts in LCC, to simplify addresses, merge countries with locations in FND, eliminte the redundant notion of an InstitutionType, which can be determined using a SPARQL query or classification and results in a very large disjunction, and correct a couple of improperly defined annotations.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200401/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of this ontology was revised to replace uses of hasTag in Relations with hasTag from LCC, as the more complex union of datatypes in the Relations concept is not needed here.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200701/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of this ontology was revised to add tax identification number, employer identification number, federal government entity and state government entity.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20201201/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of this ontology was revised to eliminate references to external dictionary sites that no longer resolve and clean up circular and ambiguous definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210101/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of this ontology was revised to add a restriction on PrimaryFederalRegulator to say that it must be a government body.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210401/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of this ontology was revised to reflect the move of certain organization-specific concepts from BE to FND.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20211001/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of this ontology was revised to correct a restriction defining state government entities and to make federal reserve district identifier a subclass of geographic region identifier and fix spelling errors.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20211201/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of this ontology was revised to eliminate dead links and address text formatting issues identified by hygiene testing.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary and augmented to support better mapping to the NIC repository.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), to eliminate redundancies in FIBO, and to augment the number and nature of financial institution entity types to cover more of the National Information Center (NIC) repository managed by the FFIEC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231101/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of the ontology was modified to further reflect changes made in Commons v1.2 (FBC-338) and eliminate unused references and streamline representation (SEC-205).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251001/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of the ontology was modified to merge details from the old corporations ontology into corporate bodies for consistency and useability (BE-259).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251002/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of the ontology was modified to improve clarity, eliminate circularity due to migration of the original US Financial Services Entities Individuals to Commercial Registration Authorities, and for better alignment with the GLEIF LEI repository for broader FIBO usage (FND-407).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20260202/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf version of the ontology was modified to eliminate the use of duplicate properties now available in Commons (FND-412).
- **copyright**: Copyright (c) 2020-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2020-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
