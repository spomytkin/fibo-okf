---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines concepts for derivative contracts, including forwards and futures, representing a commitment
      to sell or purchase the underlier at a defined price at a given time in the future.
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
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\nSee https://opensource.org/licenses/MIT."
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Futures and Forwards Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20210301/DerivativesContracts/FuturesAndForwards.rdf version
      of this ontology was modified to eliminate references to hasContractSize, clean up unnecessary restrictions on Future
      and Forward, and eliminate the redundant listing class.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20210601/DerivativesContracts/FuturesAndForwards.rdf version
      of this ontology was modified to move designated contract market to the markets ontology in FBC and revise the definition
      of a CurrencyFuture to eliminate an unnecessary superclass and restriction due to the release of CurrencyContracts and
      to revise the definition of a dividend future to reference the listed share that it tracks rather than the dividend
      itself.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20210701/DerivativesContracts/FuturesAndForwards.rdf version
      of this ontology was modified to incorporate the concepts that were originally in a separate, very small equity forwards
      ontology.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20220901/DerivativesContracts/FuturesAndForwards.rdf version
      of this ontology was modified to better integrate adjustment method.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20221001/DerivativesContracts/FuturesAndForwards.rdf version
      of this ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary, and to move the definition of an underlier and the related property, has underlier,
      to financial instruments so that these concepts are also available for use in relation to pool-backed securities.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20230201/DerivativesContracts/FuturesAndForwards.rdf version
      of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20230301/DerivativesContracts/FuturesAndForwards.rdf version
      of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC), eliminating redundancies in FIBO as appropriate and to replace content that is now available in the
      OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20231201/DerivativesContracts/FuturesAndForwards.rdf version
      of this ontology was modified to support details of ISO 4914, Financial services - Unique Product Identifier (UPI),
      (DER-146).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20250201/DerivativesContracts/FuturesAndForwards.rdf version
      of this ontology was modified to simplify and refine definitions related to underliers (DER-112).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20250301/DerivativesContracts/FuturesAndForwards.rdf version
      of this ontology was modified to clarify the distinction between a future and a forward (DER-148).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/20250701/DerivativesContracts/FuturesAndForwards/
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/
  - concept: /concepts/fibo/DER/DerivativesContracts/Options.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/
  - concept: /concepts/fibo/IND/MarketIndices/BasketIndices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/
  - concept: /concepts/fibo/SEC/Debt/Bonds.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/
  - concept: /concepts/fibo/SEC/Debt/TradedShortTermDebt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/
  - concept: /concepts/fibo/SEC/Securities/Baskets.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/
sources:
- id: fibo-source-4932191e9c
  resource: references/fibo/DER/DerivativesContracts/FuturesAndForwards.rdf
  sha256: 4932191e9cdfb6ce62af4c9077f0e5e184cf60c8a969d4a7166b65bf658bce7f
  title: FIBO source DER/DerivativesContracts/FuturesAndForwards.rdf
title: Futures and Forwards Ontology
type: Ontology Definition
---

# Futures and Forwards Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/>

## Relationships

- **Related to**: [Publishers](/concepts/fibo/BE/FunctionalEntities/Publishers.md)
- **Related to**: [DerivativesBasics](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics.md)
- **Related to**: [Options](/concepts/fibo/DER/DerivativesContracts/Options.md)
- **Related to**: [Swaps](/concepts/fibo/DER/DerivativesContracts/Swaps.md)
- **Related to**: [SecurityBasedDerivatives](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [InstrumentPricing](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing.md)
- **Related to**: [Markets](/concepts/fibo/FBC/FunctionalEntities/Markets.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [Objectives](/concepts/fibo/FND/GoalsAndObjectives/Objectives.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [EconomicIndicators](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators.md)
- **Related to**: [BasketIndices](/concepts/fibo/IND/MarketIndices/BasketIndices.md)
- **Related to**: [Bonds](/concepts/fibo/SEC/Debt/Bonds.md)
- **Related to**: [DebtInstruments](/concepts/fibo/SEC/Debt/DebtInstruments.md)
- **Related to**: [TradedShortTermDebt](/concepts/fibo/SEC/Debt/TradedShortTermDebt.md)
- **Related to**: [EquityInstruments](/concepts/fibo/SEC/Equities/EquityInstruments.md)
- **Related to**: [Baskets](/concepts/fibo/SEC/Securities/Baskets.md)
- **Related to**: [SecuritiesListings](/concepts/fibo/SEC/Securities/SecuritiesListings.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [FuturesAndForwards](<https://spec.edmcouncil.org/fibo/ontology/DER/20250701/DerivativesContracts/FuturesAndForwards/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines concepts for derivative contracts, including forwards and futures, representing a commitment to sell or purchase the underlier at a defined price at a given time in the future.
- **license**: Copyright (c) 2015-2025 EDM Council, Inc. Copyright (c) 2015-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 See https://opensource.org/licenses/MIT.
- **label** (en): Futures and Forwards Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20210301/DerivativesContracts/FuturesAndForwards.rdf version of this ontology was modified to eliminate references to hasContractSize, clean up unnecessary restrictions on Future and Forward, and eliminate the redundant listing class.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20210601/DerivativesContracts/FuturesAndForwards.rdf version of this ontology was modified to move designated contract market to the markets ontology in FBC and revise the definition of a CurrencyFuture to eliminate an unnecessary superclass and restriction due to the release of CurrencyContracts and to revise the definition of a dividend future to reference the listed share that it tracks rather than the dividend itself.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20210701/DerivativesContracts/FuturesAndForwards.rdf version of this ontology was modified to incorporate the concepts that were originally in a separate, very small equity forwards ontology.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20220901/DerivativesContracts/FuturesAndForwards.rdf version of this ontology was modified to better integrate adjustment method.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20221001/DerivativesContracts/FuturesAndForwards.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary, and to move the definition of an underlier and the related property, has underlier, to financial instruments so that these concepts are also available for use in relation to pool-backed securities.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20230201/DerivativesContracts/FuturesAndForwards.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20230301/DerivativesContracts/FuturesAndForwards.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate and to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20231201/DerivativesContracts/FuturesAndForwards.rdf version of this ontology was modified to support details of ISO 4914, Financial services - Unique Product Identifier (UPI), (DER-146).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20250201/DerivativesContracts/FuturesAndForwards.rdf version of this ontology was modified to simplify and refine definitions related to underliers (DER-112).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20250301/DerivativesContracts/FuturesAndForwards.rdf version of this ontology was modified to clarify the distinction between a future and a forward (DER-148).
- **copyright**: Copyright (c) 2015-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2015-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
