---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: sequence of characters representing some currency
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Codes for the representation of currencies and funds, ISO 4217, Eighth edition, 2015-08-01, section 3.2
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The first (left-most) two characters of the ISO 4217 3-letter currency identifier relate to the currency authority
      that issues the currency, and is, in most cases the ISO 3166-1 alpha 2 code for the geopolitical entity whose central
      bank is the issuer. The third (right-most) character of the identifier (alphabetic code) is an indicator derived from
      the name of the major currency unit or fund. If the currency is not associated with a single geographical entity as
      described in ISO 3166-1, typically a specially allocated identifier (alpha-2 code) is used to describe the currency
      authority. This code has been allocated by the Maintenance Agency from within the user-assigned range of codes XA to
      XZ specified in 8.1.3 of ISO 3166-1:2013. The character following X will be a mnemonic, where possible, derived from
      the name of the geographical area concerned.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/CurrencyIdentifier
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: currency identifier
type: Ontology Class
---

# currency identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/CurrencyIdentifier>

## Definition

sequence of characters representing some currency

## Relationships

- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)
- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: some values from of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)

## Annotations

- **label**: currency identifier
- **definition**: sequence of characters representing some currency
- **adaptedFrom**: Codes for the representation of currencies and funds, ISO 4217, Eighth edition, 2015-08-01, section 3.2
- **explanatoryNote**: The first (left-most) two characters of the ISO 4217 3-letter currency identifier relate to the currency authority that issues the currency, and is, in most cases the ISO 3166-1 alpha 2 code for the geopolitical entity whose central bank is the issuer. The third (right-most) character of the identifier (alphabetic code) is an indicator derived from the name of the major currency unit or fund. If the currency is not associated with a single geographical entity as described in ISO 3166-1, typically a specially allocated identifier (alpha-2 code) is used to describe the currency authority. This code has been allocated by the Maintenance Agency from within the user-assigned range of codes XA to XZ specified in 8.1.3 of ISO 3166-1:2013. The character following X will be a mnemonic, where possible, derived from the name of the geographical area concerned.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
