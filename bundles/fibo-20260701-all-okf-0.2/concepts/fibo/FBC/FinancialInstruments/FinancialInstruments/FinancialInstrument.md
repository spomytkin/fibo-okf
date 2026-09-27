---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial instrument
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: written contract that gives rise to both a financial asset of one entity and a financial liability of another entity
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'Examples of financial instruments include: cash, evidence of an ownership interest in an entity, or a contractual
      right to receive (or deliver) cash, or another financial instrument.'
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2021/issued/part-a/ias-32-financial-instruments-presentation.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A financial instrument can be thought of as a template that defines an arrangement structure that remains to be
      fleshed out with terms and parameters in order to establish a specific instance of the contract.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasNominalValue
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isDenominatedIn
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isNegotiable
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Issuer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/FinancialInstrumentShortName
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasFinancialInstrumentShortName
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/hasRestriction
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
- id: fibo-source-6fed3fa3dd
  resource: references/fibo/SEC/Securities/SecuritiesClassification.rdf
  sha256: 6fed3fa3ddd850e875bf020fa5eb79e1d90023fb74888e9c1856e32882bc8f76
  title: FIBO source SEC/Securities/SecuritiesClassification.rdf
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
- id: fibo-source-241669b0c1
  resource: references/fibo/SEC/Securities/SecuritiesRestrictions.rdf
  sha256: 241669b0c114de2a69849d3c5ae0b04d6c14efbda13080a5a41e98a49ceef1f2
  title: FIBO source SEC/Securities/SecuritiesRestrictions.rdf
title: financial instrument
type: Ontology Class
---

# financial instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument>

## Definition

written contract that gives rise to both a financial asset of one entity and a financial liability of another entity

## Relationships

- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Constraints

- **[hasNominalValue](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasNominalValue.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[isDenominatedIn](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/isDenominatedIn.md)**: some values from of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[isLegallyRecordedIn](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn.md)**: min qualified cardinality 0 of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)
- **[isNegotiable](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/isNegotiable.md)**: exact qualified cardinality 1 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from of type [Issuer](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Issuer.md)
- **[hasFinancialInstrumentShortName](/concepts/fibo/SEC/Securities/SecuritiesIssuance/hasFinancialInstrumentShortName.md)**: min qualified cardinality 0 of type [FinancialInstrumentShortName](/concepts/fibo/SEC/Securities/SecuritiesIssuance/FinancialInstrumentShortName.md)
- **[hasRestriction](/concepts/fibo/SEC/Securities/SecuritiesRestrictions/hasRestriction.md)**: min qualified cardinality 0 of type [SecuritiesRestriction](/concepts/fibo/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: min qualified cardinality 0 of type [IndustrySectorClassifier](/concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: min qualified cardinality 0 of type [FinancialInstrumentClassifier](/concepts/fibo/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: min qualified cardinality 0 of type [FinancialInstrumentIdentifier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md)

## Annotations

- **label**: financial instrument
- **definition**: written contract that gives rise to both a financial asset of one entity and a financial liability of another entity
- **example**: Examples of financial instruments include: cash, evidence of an ownership interest in an entity, or a contractual right to receive (or deliver) cash, or another financial instrument.
- **adaptedFrom**: https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2021/issued/part-a/ias-32-financial-instruments-presentation.pdf
- **explanatoryNote**: A financial instrument can be thought of as a template that defines an arrangement structure that remains to be fleshed out with terms and parameters in order to establish a specific instance of the contract.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
