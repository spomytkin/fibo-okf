---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology provides examples of how to represent simple equities.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2019-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2019-2025 Object Management Group,\
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
    value: Equities Example Individuals Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200301/Equities/EquitiesExampleIndividuals.rdf version of this
      ontology was modified to add CFI codes to the example equity instruments.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200501/Equities/EquitiesExampleIndividuals.rdf version of this
      ontology was revised to replace uses of hasTag in Relations with hasTag from LCC, as the more complex union of datatypes
      in the Relations concept is not needed here.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200701/Equities/EquitiesExampleIndividuals.rdf version of this
      ontology was revised to add the share class to some of the examples, replace registered form with book entry (registered)
      form, and add detail to the common share and listing individuals.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20201201/Equities/EquitiesExampleIndividuals.rdf version of this
      ontology was revised to replace equity issuer with share issuer.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210301/Equities/EquitiesExampleIndividuals.rdf version of this
      ontology was revised to address changes to the markets individuals ontology.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20221201/Equities/EquitiesExampleIndividuals.rdf version of the
      ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Equities/EquitiesExampleIndividuals.rdf version of this
      ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes
      (LCC) and to eliminate redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Equities/EquitiesExampleIndividuals.rdf version of this
      ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240101/Equities/EquitiesExampleIndividuals.rdf version of the
      ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20250301/Equities/EquitiesExampleIndividuals.rdf version of the
      ontology was modified to integrate migration of individuals to Commercial Registration Authorities (FND-407).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20260601/Equities/EquitiesExampleIndividuals.rdf version of the
      ontology was modified to replace references to the now deprecated hasTag property in Relations with its equivalent in
      OMG Commons (FND-412).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2019-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2019-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/20260701/Securities/EquitiesExamples/
  - concept: /concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/
  - concept: /concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Classifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/
sources:
- id: fibo-source-67472951ed
  resource: references/fibo/EXMP/Securities/EquitiesExamples.rdf
  sha256: 67472951eda4ab333ca860aff880574f4629454478bbf8d10154cde935dfb619
  title: FIBO source EXMP/Securities/EquitiesExamples.rdf
title: Equities Example Individuals Ontology
type: Ontology Definition
---

# Equities Example Individuals Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/>

## Relationships

- **Related to**: [USGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [DowJonesIndustrialAverageCompanies](/concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies.md)
- **Related to**: [FinancialInstitutionExamples](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.md)
- **Related to**: [MarketsAndExchangesExamples](/concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [MarketsIndividuals](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals.md)
- **Related to**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [ISO4217-CurrencyCodes](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [EquityInstruments](/concepts/fibo/SEC/Equities/EquityInstruments.md)
- **Related to**: [SecuritiesIdentification](/concepts/fibo/SEC/Securities/SecuritiesIdentification.md)
- **Related to**: [SecuritiesIdentificationIndividuals](/concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.md)
- **Related to**: [SecuritiesIssuance](/concepts/fibo/SEC/Securities/SecuritiesIssuance.md)
- **Related to**: [SecuritiesListings](/concepts/fibo/SEC/Securities/SecuritiesListings.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [RegistrationAuthorities](<https://www.omg.org/spec/Commons/RegistrationAuthorities/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [EquitiesExamples](<https://spec.edmcouncil.org/fibo/ontology/EXMP/20260701/Securities/EquitiesExamples/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology provides examples of how to represent simple equities.
- **license**: Copyright (c) 2019-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2019-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Equities Example Individuals Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200301/Equities/EquitiesExampleIndividuals.rdf version of this ontology was modified to add CFI codes to the example equity instruments.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200501/Equities/EquitiesExampleIndividuals.rdf version of this ontology was revised to replace uses of hasTag in Relations with hasTag from LCC, as the more complex union of datatypes in the Relations concept is not needed here.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200701/Equities/EquitiesExampleIndividuals.rdf version of this ontology was revised to add the share class to some of the examples, replace registered form with book entry (registered) form, and add detail to the common share and listing individuals.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20201201/Equities/EquitiesExampleIndividuals.rdf version of this ontology was revised to replace equity issuer with share issuer.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210301/Equities/EquitiesExampleIndividuals.rdf version of this ontology was revised to address changes to the markets individuals ontology.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20221201/Equities/EquitiesExampleIndividuals.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Equities/EquitiesExampleIndividuals.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Equities/EquitiesExampleIndividuals.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240101/Equities/EquitiesExampleIndividuals.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20250301/Equities/EquitiesExampleIndividuals.rdf version of the ontology was modified to integrate migration of individuals to Commercial Registration Authorities (FND-407).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20260601/Equities/EquitiesExampleIndividuals.rdf version of the ontology was modified to replace references to the now deprecated hasTag property in Relations with its equivalent in OMG Commons (FND-412).
- **copyright**: Copyright (c) 2019-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2019-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
