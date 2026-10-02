---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: The financial business and commerce domain covers business concepts that are common to common to a number of finance
      areas, such as loans, securities, and corporate actions, including products and services, financial intermediaries,
      registrars and regulators, and financial instruments and products.
  - predicate: http://purl.org/dc/terms/contributor
    value: Adaptive Analytics, Inc.
  - predicate: http://purl.org/dc/terms/contributor
    value: Bloomberg LP
  - predicate: http://purl.org/dc/terms/contributor
    value: Capacity Post, Inc.
  - predicate: http://purl.org/dc/terms/contributor
    value: Citigroup
  - predicate: http://purl.org/dc/terms/contributor
    value: Credit Suisse
  - predicate: http://purl.org/dc/terms/contributor
    value: Dassault Systemes / No Magic
  - predicate: http://purl.org/dc/terms/contributor
    value: Deutsche Bank
  - predicate: http://purl.org/dc/terms/contributor
    value: Exprentis
  - predicate: http://purl.org/dc/terms/contributor
    value: Federated Knowledge, LLC
  - predicate: http://purl.org/dc/terms/contributor
    value: John F. Gemski
  - predicate: http://purl.org/dc/terms/contributor
    value: Nordea Bank AB
  - predicate: http://purl.org/dc/terms/contributor
    value: Office of Financial Research (US Dept of the Treasury)
  - predicate: http://purl.org/dc/terms/contributor
    value: Pinnacle Bank (Morgan Hill, California)
  - predicate: http://purl.org/dc/terms/contributor
    value: Probanker Simulations, LLC
  - predicate: http://purl.org/dc/terms/contributor
    value: Quarule
  - predicate: http://purl.org/dc/terms/contributor
    value: State Street Bank and Trust
  - predicate: http://purl.org/dc/terms/contributor
    value: Statistics Canada
  - predicate: http://purl.org/dc/terms/contributor
    value: Tahoe Blue Ltd
  - predicate: http://purl.org/dc/terms/contributor
    value: Thematix Partners LLC
  - predicate: http://purl.org/dc/terms/contributor
    value: Wells Fargo
  - predicate: http://purl.org/dc/terms/contributor
    value: agnos.ai UK Ltd.
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/issued
    value: '2015-08-13T18:00:00'
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2015-2025 EDM Council, Inc.\nCopyright (c) 2015-2025 Object Management Group, Inc.\n\nPermission\
      \ is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files\
      \ (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy,\
      \ modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom\
      \ the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission\
      \ notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS',\
      \ WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/modified
    value: '2025-10-6T18:00:00'
  - predicate: http://purl.org/dc/terms/title
    value: EDMA Financial Industry Business Ontology (FIBO) Financial Business and Commerce (FBC) Domain
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Financial Business and Commerce Domain
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The 'all' ontology for FBC is provided for convenience for FIBO users. This ontology does not add new assertions,
      but imports most of the Production (Released) ontologies that comprise the FIBO Foundations (FND), Business Entities
      (BE) and Financial Business and Commerce (FBC) domains, excluding individuals for governments and jurisdictions, financial
      services and most regulatory organizations and related registries, as well as the LCC region-specific ontologies.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/AllBE.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/AllBE/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/20251001/AllFBC/
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/
  - concept: /concepts/fibo/FBC/FinancialInstruments/Settlement.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCenters.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCenters/
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/
  - concept: /concepts/fibo/FBC/FunctionalEntities/RegulatoryAgencies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://spec.edmcouncil.org/fibo/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/AllFBC/
sources:
- id: fibo-source-e3532d6612
  resource: references/fibo/FBC/AllFBC.rdf
  sha256: e3532d66123e9323c4f9f08c2531780cbfb75d1b1c439f47f5f88c0708a6fcd1
  title: FIBO source FBC/AllFBC.rdf
title: Financial Business and Commerce Domain
type: Ontology Definition
---

# Financial Business and Commerce Domain

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/AllFBC/>

## Relationships

- **Related to**: [AllBE](/concepts/fibo/BE/AllBE.md)
- **Related to**: [CreditEvents](/concepts/fibo/FBC/DebtAndEquities/CreditEvents.md)
- **Related to**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Related to**: [Guaranty](/concepts/fibo/FBC/DebtAndEquities/Guaranty.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [InstrumentPricing](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing.md)
- **Related to**: [Settlement](/concepts/fibo/FBC/FinancialInstruments/Settlement.md)
- **Related to**: [BusinessCenters](/concepts/fibo/FBC/FunctionalEntities/BusinessCenters.md)
- **Related to**: [BusinessRegistries](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries.md)
- **Related to**: [FinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md)
- **Related to**: [Markets](/concepts/fibo/FBC/FunctionalEntities/Markets.md)
- **Related to**: [RegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/RegulatoryAgencies.md)
- **Related to**: [ClientsAndAccounts](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [AllFBC](<https://spec.edmcouncil.org/fibo/ontology/FBC/20251001/AllFBC/>)
- **See also**: [fibo](<https://spec.edmcouncil.org/fibo/>)

## Annotations

- **abstract**: The financial business and commerce domain covers business concepts that are common to common to a number of finance areas, such as loans, securities, and corporate actions, including products and services, financial intermediaries, registrars and regulators, and financial instruments and products.
- **contributor**: Adaptive Analytics, Inc.
- **contributor**: Bloomberg LP
- **contributor**: Capacity Post, Inc.
- **contributor**: Citigroup
- **contributor**: Credit Suisse
- **contributor**: Dassault Systemes / No Magic
- **contributor**: Deutsche Bank
- **contributor**: Exprentis
- **contributor**: Federated Knowledge, LLC
- **contributor**: John F. Gemski
- **contributor**: Nordea Bank AB
- **contributor**: Office of Financial Research (US Dept of the Treasury)
- **contributor**: Pinnacle Bank (Morgan Hill, California)
- **contributor**: Probanker Simulations, LLC
- **contributor**: Quarule
- **contributor**: State Street Bank and Trust
- **contributor**: Statistics Canada
- **contributor**: Tahoe Blue Ltd
- **contributor**: Thematix Partners LLC
- **contributor**: Wells Fargo
- **contributor**: agnos.ai UK Ltd.
- **issued**: 2015-08-13T18:00:00
- **license**: Copyright (c) 2015-2025 EDM Council, Inc. Copyright (c) 2015-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **modified**: 2025-10-6T18:00:00
- **title**: EDMA Financial Industry Business Ontology (FIBO) Financial Business and Commerce (FBC) Domain
- **label**: Financial Business and Commerce Domain
- **copyright**: Copyright (c) 2015-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2015-2025 Object Management Group, Inc.
- **explanatoryNote**: The 'all' ontology for FBC is provided for convenience for FIBO users. This ontology does not add new assertions, but imports most of the Production (Released) ontologies that comprise the FIBO Foundations (FND), Business Entities (BE) and Financial Business and Commerce (FBC) domains, excluding individuals for governments and jurisdictions, financial services and most regulatory organizations and related registries, as well as the LCC region-specific ontologies.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
