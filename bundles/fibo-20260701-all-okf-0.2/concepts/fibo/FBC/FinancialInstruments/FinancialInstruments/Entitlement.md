---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: entitlement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial instrument that provides the holder an interest in, or the privilege to subscribe to, or to receive specific
      assets under terms specified
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth
      edition, 2019-10.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that certain fund units, including but not limited to units in pension funds and other non-public investment
      structures may be considered entitlements but not securities. They may or may not be identified using traditional financial
      instrument identifiers. Some entitlements, such as warrants, whose value changes based on the value of some underlier,
      are considered derivative instruments.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: right
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityForm
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isIssuedInForm
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Entitlement
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: entitlement
type: Ontology Class
---

# entitlement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Entitlement>

## Definition

financial instrument that provides the holder an interest in, or the privilege to subscribe to, or to receive specific assets under terms specified

## Relationships

- **Subclass of**: [FinancialInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)

## Constraints

- **[isIssuedInForm](/concepts/fibo/SEC/Securities/SecuritiesIssuance/isIssuedInForm.md)**: min qualified cardinality 0 of type [SecurityForm](/concepts/fibo/SEC/Securities/SecuritiesIssuance/SecurityForm.md)

## Annotations

- **label**: entitlement
- **definition**: financial instrument that provides the holder an interest in, or the privilege to subscribe to, or to receive specific assets under terms specified
- **adaptedFrom**: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth edition, 2019-10.
- **explanatoryNote**: Note that certain fund units, including but not limited to units in pension funds and other non-public investment structures may be considered entitlements but not securities. They may or may not be identified using traditional financial instrument identifiers. Some entitlements, such as warrants, whose value changes based on the value of some underlier, are considered derivative instruments.
- **synonym**: right

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
