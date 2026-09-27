---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology provides examples of how to represent common equity indices as identified in the IND-EFT-DEV use
      case.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2020-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2020-2025 Object Management Group,\
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
    value: Equity Index Example Individuals Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20210901/MarketIndices/EquityIndexExampleIndividuals.rdf version
      of this ontology was modified to reflect the move of market data provider from interest rates in IND to publishers in
      BE.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20221001/MarketIndices/EquityIndexExampleIndividuals.rdf version
      of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20230201/MarketIndices/EquityIndexExampleIndividuals.rdf version
      of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20230301/MarketIndices/EquityIndexExampleIndividuals.rdf version
      of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons)
      v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20240101/MarketIndices/EquityIndexExampleIndividuals.rdf version
      of this ontology was modified to eliminate implicit punning and revise properties that are now deprecated (moved to
      Commons).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20240901/MarketIndices/EquityIndexExampleIndividuals.rdf version
      of this ontology was modified to revise a remaining property that moved to Commons.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20241101/MarketIndices/EquityIndexExampleIndividuals.rdf version
      of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library
      (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20250301/MarketIndices/EquityIndexExampleIndividuals.rdf version
      of the ontology was modified to move examples to a separate domain area for clarification for FIBO users (FND-407).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2020-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2020-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/
  - concept: /concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/20260601/Securities/EquityIndexExamples/
  - concept: /concepts/fibo/EXMP/Securities/EquitiesExamples.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/Analytics.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - concept: /concepts/fibo/IND/Indicators/Indicators.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/
  - concept: /concepts/fibo/IND/MarketIndices/BasketIndices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/
  - concept: /concepts/fibo/SEC/Securities/Baskets.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesClassification.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/
sources:
- id: fibo-source-c9fb5c672c
  resource: references/fibo/EXMP/Securities/EquityIndexExamples.rdf
  sha256: c9fb5c672cbb6dc4ba551074dd33b7e27294259b5a24a6064670bc5c0205149d
  title: FIBO source EXMP/Securities/EquityIndexExamples.rdf
title: Equity Index Example Individuals Ontology
type: Ontology Definition
---

# Equity Index Example Individuals Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/>

## Relationships

- **Related to**: [Publishers](/concepts/fibo/BE/FunctionalEntities/Publishers.md)
- **Related to**: [FormalBusinessOrganizations](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md)
- **Related to**: [ControlParties](/concepts/fibo/BE/OwnershipAndControl/ControlParties.md)
- **Related to**: [PrivateLimitedCompanies](/concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.md)
- **Related to**: [EquitiesExamples](/concepts/fibo/EXMP/Securities/EquitiesExamples.md)
- **Related to**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [BusinessRegistries](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries.md)
- **Related to**: [CommercialRegistrationAuthorities](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.md)
- **Related to**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [Analytics](/concepts/fibo/FND/Utilities/Analytics.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [Indicators](/concepts/fibo/IND/Indicators/Indicators.md)
- **Related to**: [BasketIndices](/concepts/fibo/IND/MarketIndices/BasketIndices.md)
- **Related to**: [Baskets](/concepts/fibo/SEC/Securities/Baskets.md)
- **Related to**: [SecuritiesClassification](/concepts/fibo/SEC/Securities/SecuritiesClassification.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [EquityIndexExamples](<https://spec.edmcouncil.org/fibo/ontology/EXMP/20260601/Securities/EquityIndexExamples/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology provides examples of how to represent common equity indices as identified in the IND-EFT-DEV use case.
- **license**: Copyright (c) 2020-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2020-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Equity Index Example Individuals Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20210901/MarketIndices/EquityIndexExampleIndividuals.rdf version of this ontology was modified to reflect the move of market data provider from interest rates in IND to publishers in BE.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20221001/MarketIndices/EquityIndexExampleIndividuals.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20230201/MarketIndices/EquityIndexExampleIndividuals.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20230301/MarketIndices/EquityIndexExampleIndividuals.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20240101/MarketIndices/EquityIndexExampleIndividuals.rdf version of this ontology was modified to eliminate implicit punning and revise properties that are now deprecated (moved to Commons).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20240901/MarketIndices/EquityIndexExampleIndividuals.rdf version of this ontology was modified to revise a remaining property that moved to Commons.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20241101/MarketIndices/EquityIndexExampleIndividuals.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20250301/MarketIndices/EquityIndexExampleIndividuals.rdf version of the ontology was modified to move examples to a separate domain area for clarification for FIBO users (FND-407).
- **copyright**: Copyright (c) 2020-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2020-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
