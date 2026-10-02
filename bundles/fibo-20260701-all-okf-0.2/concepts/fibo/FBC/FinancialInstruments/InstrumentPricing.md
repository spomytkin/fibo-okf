---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology provides a basic set of definitions related to pricing, yield, and spread that are extended in other
      instrument-specific ontologies.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Instrument Pricing Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200601/FinancialInstruments/InstrumentPricing.rdf version of
      this ontology was modified to reflect the move of dated collection from arrangements to financial dates.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200701/FinancialInstruments/InstrumentPricing.rdf version of
      this ontology was modified to add trading day and trading session, to address ambiguity in some definitions, to add
      adjusted price and to create a more general hasLotSize property that can be used in various contexts.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20201201/FinancialInstruments/InstrumentPricing.rdf version of
      this ontology was modified to replace a redundant concept, calculation formula with formula, add a general price determination
      class needed for options, add a restriction on SecurityPrice to point to the security, and add hasRoundLotSize.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210301/FinancialInstruments/InstrumentPricing.rdf version of
      this ontology was modified to change one of the subclasses of price determination method to a named individual and correct
      the definition of mean price determination. Note that there may be multiple individuals of type 'closing price determination
      method', depending on the exchange and other factors. Also revised the lot size properties to have a range of xsd:decimal
      to allow for fractional shares or number of elements, revised the explanatory note, and added examples.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210601/FinancialInstruments/InstrumentPricing.rdf version of
      this ontology was modified to address text formatting issues uncovered by hygiene testing.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/FinancialInstruments/InstrumentPricing.rdf version of
      this ontology was modified to eliminate a redundant restriction on CollectionOfSecurityPrices, better integrate pricing
      methods, loosen the domain restriction on hasPricingSource and add dealer to the set of possible sources for prices.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20221201/FinancialInstruments/InstrumentPricing.rdf version of
      the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/FinancialInstruments/InstrumentPricing.rdf version of
      this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/FinancialInstruments/InstrumentPricing.rdf version of
      this ontology was modified to move the nominal for auction market from CDS to the pricing ontology (its IRI was that
      of this instrument pricing ontology but it was mistakenly in the CDS ontology) and simplify the definition (DER-140),
      and to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231201/FinancialInstruments/InstrumentPricing.rdf version of
      this ontology was enhanced to incorporate additional definitions for pricing terminology (SEC-185).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/FBC/20240701/FinancialInstruments/InstrumentPricing.rdf version
      of the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2020-2024 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2020-2024 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/20250701/FinancialInstruments/InstrumentPricing/
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/
  - concept: /concepts/fibo/FND/Utilities/Analytics.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/
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
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: Instrument Pricing Ontology
type: Ontology Definition
---

# Instrument Pricing Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/>

## Relationships

- **Related to**: [Publishers](/concepts/fibo/BE/FunctionalEntities/Publishers.md)
- **Related to**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [Markets](/concepts/fibo/FBC/FunctionalEntities/Markets.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Objectives](/concepts/fibo/FND/GoalsAndObjectives/Objectives.md)
- **Related to**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership.md)
- **Related to**: [Analytics](/concepts/fibo/FND/Utilities/Analytics.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [InstrumentPricing](<https://spec.edmcouncil.org/fibo/ontology/FBC/20250701/FinancialInstruments/InstrumentPricing/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology provides a basic set of definitions related to pricing, yield, and spread that are extended in other instrument-specific ontologies.
- **license**: https://opensource.org/licenses/MIT
- **label** (en): Instrument Pricing Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200601/FinancialInstruments/InstrumentPricing.rdf version of this ontology was modified to reflect the move of dated collection from arrangements to financial dates.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200701/FinancialInstruments/InstrumentPricing.rdf version of this ontology was modified to add trading day and trading session, to address ambiguity in some definitions, to add adjusted price and to create a more general hasLotSize property that can be used in various contexts.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20201201/FinancialInstruments/InstrumentPricing.rdf version of this ontology was modified to replace a redundant concept, calculation formula with formula, add a general price determination class needed for options, add a restriction on SecurityPrice to point to the security, and add hasRoundLotSize.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210301/FinancialInstruments/InstrumentPricing.rdf version of this ontology was modified to change one of the subclasses of price determination method to a named individual and correct the definition of mean price determination. Note that there may be multiple individuals of type 'closing price determination method', depending on the exchange and other factors. Also revised the lot size properties to have a range of xsd:decimal to allow for fractional shares or number of elements, revised the explanatory note, and added examples.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210601/FinancialInstruments/InstrumentPricing.rdf version of this ontology was modified to address text formatting issues uncovered by hygiene testing.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/FinancialInstruments/InstrumentPricing.rdf version of this ontology was modified to eliminate a redundant restriction on CollectionOfSecurityPrices, better integrate pricing methods, loosen the domain restriction on hasPricingSource and add dealer to the set of possible sources for prices.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20221201/FinancialInstruments/InstrumentPricing.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/FinancialInstruments/InstrumentPricing.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/FinancialInstruments/InstrumentPricing.rdf version of this ontology was modified to move the nominal for auction market from CDS to the pricing ontology (its IRI was that of this instrument pricing ontology but it was mistakenly in the CDS ontology) and simplify the definition (DER-140), and to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231201/FinancialInstruments/InstrumentPricing.rdf version of this ontology was enhanced to incorporate additional definitions for pricing terminology (SEC-185).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/FBC/20240701/FinancialInstruments/InstrumentPricing.rdf version of the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
- **copyright**: Copyright (c) 2020-2024 EDM Council, Inc.
- **copyright**: Copyright (c) 2020-2024 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
